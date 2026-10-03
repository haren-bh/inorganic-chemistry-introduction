/**
 * AP Chemistry Practice & Exam Quiz Controller
 * Supports:
 *  - All 9 official College Board AP Chemistry Units (Fall 2024 CED); question counts per unit come from the payload
 *  - Mode 1 ("batch"): Do 10 questions at a time, score at the end, and reveal all correct answers + explanations
 *  - Mode 2 ("single"): Do 1 question at a time with immediate Correct/Incorrect feedback and detailed explanation
 *  - Per-Unit and Per-Mode Retakes with live elapsed timers
 *  - Persistent Attempt History & Past Performance Dashboard in localStorage
 */

(function () {
  "use strict";

  const payloadEl = document.getElementById("quiz-payload-json");
  if (!payloadEl) return;

  const PAYLOAD = JSON.parse(payloadEl.textContent);
  const UNITS = PAYLOAD.units || [];
  const ALL_QUESTIONS = PAYLOAD.questions || [];
  const UNIT_BY_ID = new Map(UNITS.map((u) => [u.id, u]));
  const Q_BY_ID = new Map(ALL_QUESTIONS.map((q) => [q.id, q]));
  const Q_BY_UID = new Map(ALL_QUESTIONS.map((q) => [q.uid, q]));
  const LETTERS = ["A", "B", "C", "D"];

  // Storage keys (scoped dynamically to the active username via window.InorganicUserSync)
  const STORAGE_KEY = "inorganic_chem_ap_quiz_v2";
  const ATTEMPTS_STORAGE_KEY = "inorganic_chem_ap_quiz_attempts_v1";
  const SESSIONS_STORAGE_KEY = "inorganic_chem_ap_quiz_sessions_v1";
  const LEGACY_STORAGE_KEYS = ["inorganic_chem_ap_quiz_v1"];

  function activeHistoryKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getHistoryStorageKey === "function") {
      return window.InorganicUserSync.getHistoryStorageKey();
    }
    return STORAGE_KEY;
  }

  function activeAttemptsKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getAttemptsStorageKey === "function") {
      return window.InorganicUserSync.getAttemptsStorageKey();
    }
    return ATTEMPTS_STORAGE_KEY;
  }

  function activeSessionsKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getSessionsStorageKey === "function") {
      return window.InorganicUserSync.getSessionsStorageKey();
    }
    return SESSIONS_STORAGE_KEY;
  }

  function notifyCloudSync(immediate = false) {
    if (!window.InorganicUserSync) return;
    if (immediate && typeof window.InorganicUserSync.pushNow === "function") {
      window.InorganicUserSync.pushNow({ merge: true });
    } else if (typeof window.InorganicUserSync.schedulePush === "function") {
      window.InorganicUserSync.schedulePush({ merge: true });
    }
  }

  // =========================================================================
  // LocalStorage Persistence: Lifetime Mastery, Attempts & Active Sessions
  // =========================================================================

  function loadHistory() {
    try {
      LEGACY_STORAGE_KEYS.forEach((k) => localStorage.removeItem(k));
      const raw = localStorage.getItem(activeHistoryKey());
      if (!raw) return {};
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return {};
      const hist = {};
      Object.keys(parsed).forEach((uid) => {
        const entry = parsed[uid];
        const q = Q_BY_UID.get(uid);
        if (!q || !entry || typeof entry.selected !== "number" || entry.rev !== q.rev) return;
        hist[q.id] = { selected: entry.selected, correct: entry.selected === q.correct_index };
      });
      return hist;
    } catch (_) {
      return {};
    }
  }

  function saveHistory(hist, syncCloud = true) {
    try {
      const out = {};
      Object.keys(hist).forEach((qIdStr) => {
        const q = Q_BY_ID.get(Number(qIdStr));
        const entry = hist[qIdStr];
        if (q && entry) out[q.uid] = { selected: entry.selected, correct: entry.correct, rev: q.rev };
      });
      localStorage.setItem(activeHistoryKey(), JSON.stringify(out));
      if (syncCloud) notifyCloudSync(false);
    } catch (_) {
      // Ignore storage quota errors
    }
  }

  function loadAttempts() {
    try {
      const raw = localStorage.getItem(activeAttemptsKey());
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return [];
      return parsed.filter(
        (a) =>
          a &&
          typeof a.unitId === "number" &&
          (a.mode === "batch" || a.mode === "single") &&
          typeof a.correct === "number" &&
          typeof a.total === "number"
      );
    } catch (_) {
      return [];
    }
  }

  function saveAttempts(attempts, syncCloud = true) {
    try {
      localStorage.setItem(activeAttemptsKey(), JSON.stringify(attempts));
      if (syncCloud) notifyCloudSync(true);
    } catch (_) {
      // Ignore storage quota errors
    }
  }

  function serializeAnswersMap(ansByQId) {
    const out = {};
    if (!ansByQId || typeof ansByQId !== "object") return out;
    Object.keys(ansByQId).forEach((qIdStr) => {
      const q = Q_BY_ID.get(Number(qIdStr));
      const sel = ansByQId[qIdStr];
      if (q && typeof sel === "number") {
        out[q.uid] = { selected: sel, rev: q.rev };
      }
    });
    return out;
  }

  function deserializeAnswersMap(rawByUid) {
    const out = {};
    if (!rawByUid || typeof rawByUid !== "object") return out;
    Object.keys(rawByUid).forEach((uid) => {
      const entry = rawByUid[uid];
      const q = Q_BY_UID.get(uid);
      if (q && entry && typeof entry.selected === "number" && entry.rev === q.rev) {
        out[q.id] = entry.selected;
      }
    });
    return out;
  }

  function loadSessions() {
    const empty = { batchByUnitSet: {}, singleByUnit: {}, lastLocation: null };
    try {
      const raw = localStorage.getItem(activeSessionsKey());
      if (!raw) return empty;
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return empty;

      const batchByUnitSet = {};
      if (parsed.batchByUnitSet && typeof parsed.batchByUnitSet === "object") {
        Object.keys(parsed.batchByUnitSet).forEach((key) => {
          const item = parsed.batchByUnitSet[key];
          if (!item || typeof item !== "object") return;
          let customQuestions = null;
          if (Array.isArray(item.customUids)) {
            const resolved = item.customUids.map((uid) => Q_BY_UID.get(uid)).filter(Boolean);
            if (resolved.length > 0) customQuestions = resolved;
          }
          const answers = deserializeAnswersMap(item.answers);
          const submitted = Boolean(item.submitted);
          const elapsedSec = Math.max(0, Number(item.elapsedSec) || 0);
          const hasProgress = elapsedSec > 0 || Object.keys(answers).length > 0;
          // Never auto-start timer on page load: restore in-progress sessions as "paused"
          const timerState = submitted ? "completed" : hasProgress ? "paused" : "not_started";

          batchByUnitSet[key] = {
            answers,
            submitted,
            elapsedSec,
            timerState,
            updatedAt: item.updatedAt || null,
            lastAttempt: item.lastAttempt || null,
            customQuestions,
          };
        });
      }

      const singleByUnit = {};
      if (parsed.singleByUnit && typeof parsed.singleByUnit === "object") {
        Object.keys(parsed.singleByUnit).forEach((uKey) => {
          const item = parsed.singleByUnit[uKey];
          if (!item || typeof item !== "object") return;
          const answers = deserializeAnswersMap(item.answers);
          const elapsedSec = Math.max(0, Number(item.elapsedSec) || 0);
          const ansCount = Object.keys(answers).length;
          const uTotal = unitQuestionCount(Number(uKey));
          const isDone = uTotal > 0 && ansCount >= uTotal;
          const hasProgress = elapsedSec > 0 || ansCount > 0;
          const timerState = isDone ? "completed" : hasProgress ? "paused" : "not_started";

          singleByUnit[uKey] = {
            answers,
            elapsedSec,
            timerState,
            updatedAt: item.updatedAt || null,
            singleIndex: Math.max(0, Number(item.singleIndex) || 0),
            lastLoggedSignature: String(item.lastLoggedSignature || ""),
          };
        });
      }

      const lastLocation =
        parsed.lastLocation && typeof parsed.lastLocation === "object" ? parsed.lastLocation : null;

      return { batchByUnitSet, singleByUnit, lastLocation };
    } catch (_) {
      return empty;
    }
  }

  function saveSessions(syncCloud = true) {
    try {
      const batchOut = {};
      Object.keys(state.sessions.batchByUnitSet).forEach((key) => {
        const s = state.sessions.batchByUnitSet[key];
        if (!s) return;
        const ansMap = serializeAnswersMap(s.answers);
        const elapsed = Math.max(0, Math.round(s.elapsedSec || 0));
        const hasProg = elapsed > 0 || Object.keys(ansMap).length > 0;
        const persistedTimerState = s.submitted
          ? "completed"
          : s.timerState === "running" || s.timerState === "paused" || hasProg
          ? "paused"
          : "not_started";
        batchOut[key] = {
          answers: ansMap,
          submitted: Boolean(s.submitted),
          elapsedSec: elapsed,
          timerState: persistedTimerState,
          updatedAt: s.updatedAt || null,
          lastAttempt: s.lastAttempt || null,
          customUids: Array.isArray(s.customQuestions) ? s.customQuestions.map((q) => q.uid) : null,
        };
      });

      const singleOut = {};
      Object.keys(state.sessions.singleByUnit).forEach((uKey) => {
        const s = state.sessions.singleByUnit[uKey];
        if (!s) return;
        const ansMap = serializeAnswersMap(s.answers);
        const elapsed = Math.max(0, Math.round(s.elapsedSec || 0));
        const hasProg = elapsed > 0 || Object.keys(ansMap).length > 0;
        const persistedTimerState =
          s.timerState === "completed"
            ? "completed"
            : s.timerState === "running" || s.timerState === "paused" || hasProg
            ? "paused"
            : "not_started";
        singleOut[uKey] = {
          answers: ansMap,
          elapsedSec: elapsed,
          timerState: persistedTimerState,
          updatedAt: s.updatedAt || null,
          singleIndex: Math.max(0, Number(s.singleIndex) || 0),
          lastLoggedSignature: String(s.lastLoggedSignature || ""),
        };
      });

      const lastLocation = {
        mode: state.mode,
        unitId: state.unitId,
        batchSetIndex: state.batchSetIndex,
        updatedAt: new Date().toISOString(),
      };
      state.sessions.lastLocation = lastLocation;

      localStorage.setItem(
        activeSessionsKey(),
        JSON.stringify({
          batchByUnitSet: batchOut,
          singleByUnit: singleOut,
          lastLocation,
        })
      );
      if (syncCloud) notifyCloudSync(false);
    } catch (_) {
      // Ignore storage quota errors
    }
  }

  function unitQuestionCount(unitId) {
    const u = UNIT_BY_ID.get(unitId);
    return u ? u.question_count : 0;
  }

  // Application State
  const state = {
    mode: "single", // "single" (Instant Feedback Mode, default) | "batch" (Timed Mode: 10 questions at a time)
    unitId: 1,
    topicFilter: "all",
    difficultyFilter: "all",
    searchQuery: "",

    // Mode 1 active set index for the current unit (0..N-1 or -1 for random 10)
    batchSetIndex: 0,

    // Mode 2 question grid visibility
    showQGrid: true,

    // Persistent data
    history: loadHistory(),
    attempts: loadAttempts(),
    sessions: loadSessions(),
  };

  // =========================================================================
  // Session Accessors per (Unit, Mode, Set)
  // =========================================================================

  function batchSessionKey(unitId = state.unitId, setIdx = state.batchSetIndex) {
    return `${unitId}:${setIdx}`;
  }

  function getBatchSession(unitId = state.unitId, setIdx = state.batchSetIndex) {
    const key = batchSessionKey(unitId, setIdx);
    if (!state.sessions.batchByUnitSet[key]) {
      state.sessions.batchByUnitSet[key] = {
        answers: {},
        submitted: false,
        elapsedSec: 0,
        timerState: "not_started",
        updatedAt: null,
        lastAttempt: null,
        customQuestions: null,
      };
    }
    return state.sessions.batchByUnitSet[key];
  }

  function getSingleSession(unitId = state.unitId) {
    const key = String(unitId);
    if (!state.sessions.singleByUnit[key]) {
      state.sessions.singleByUnit[key] = {
        answers: {},
        elapsedSec: 0,
        timerState: "not_started",
        updatedAt: null,
        singleIndex: 0,
        lastLoggedSignature: "",
      };
    }
    return state.sessions.singleByUnit[key];
  }

  function getActiveSession() {
    return state.mode === "batch" ? getBatchSession() : getSingleSession();
  }

  function getEffectiveTimerState(sess, mode = state.mode, unitId = state.unitId) {
    if (!sess) return "not_started";
    if (mode === "batch") {
      if (sess.submitted) return "completed";
    } else {
      const unitQs = getQuestionsForUnit(unitId);
      const ansCount = unitQs.filter((q) => typeof sess.answers[q.id] === "number").length;
      if (unitQs.length > 0 && ansCount >= unitQs.length) return "completed";
    }
    if (sess.timerState === "running") return "running";
    const hasProgress =
      (Number(sess.elapsedSec) || 0) > 0 || Object.keys(sess.answers || {}).length > 0;
    if (sess.timerState === "paused" || hasProgress) return "paused";
    return "not_started";
  }

  function pauseAllRunningSessions(save = false) {
    let changed = false;
    Object.values(state.sessions.batchByUnitSet).forEach((s) => {
      if (s && s.timerState === "running") {
        s.timerState = "paused";
        s.updatedAt = new Date().toISOString();
        changed = true;
      }
    });
    Object.values(state.sessions.singleByUnit).forEach((s) => {
      if (s && s.timerState === "running") {
        s.timerState = "paused";
        s.updatedAt = new Date().toISOString();
        changed = true;
      }
    });
    if (changed && save) {
      saveSessions(true);
    }
    return changed;
  }

  function startOrResumeActiveTimer() {
    pauseAllRunningSessions(false);
    const sess = getActiveSession();
    const curState = getEffectiveTimerState(sess);
    if (curState === "completed") return;
    sess.timerState = "running";
    sess.updatedAt = new Date().toISOString();
    saveSessions(false);
    if (state.mode === "batch") {
      renderBatchMode();
    } else {
      renderSingleMode();
    }
  }

  function pauseActiveTimer() {
    const sess = getActiveSession();
    if (!sess || sess.timerState !== "running") return;
    sess.timerState = "paused";
    sess.updatedAt = new Date().toISOString();
    saveSessions(true);
    if (state.mode === "batch") {
      renderBatchMode();
    } else {
      renderSingleMode();
    }
  }

  function computeSingleSignature(ansMap) {
    const keys = Object.keys(ansMap || {}).sort((a, b) => Number(a) - Number(b));
    if (keys.length === 0) return "";
    return keys.map((k) => `${k}=${ansMap[k]}`).join("&");
  }

  // =========================================================================
  // Formatting, Time & KaTeX Helpers
  // =========================================================================

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatMMSS(sec) {
    const s = Math.max(0, Math.round(Number(sec) || 0));
    const mins = Math.floor(s / 60);
    const rem = s % 60;
    return `${String(mins).padStart(2, "0")}:${String(rem).padStart(2, "0")}`;
  }

  function formatDurationHuman(sec) {
    const s = Math.max(0, Math.round(Number(sec) || 0));
    if (s < 60) return `${s}s`;
    const mins = Math.floor(s / 60);
    const rem = s % 60;
    if (mins < 60) return rem > 0 ? `${mins}m ${rem}s` : `${mins}m`;
    const hrs = Math.floor(mins / 60);
    const remMins = mins % 60;
    return `${hrs}h ${remMins}m`;
  }

  function formatDateTime(isoStr) {
    try {
      const d = new Date(isoStr);
      if (Number.isNaN(d.getTime())) return String(isoStr || "");
      return d.toLocaleString(undefined, {
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
      });
    } catch (_) {
      return String(isoStr || "");
    }
  }

  function renderMathInContainer(container) {
    if (!container) return;

    if (window.katex) {
      const explicitNodes = container.querySelectorAll(".katex-inline[data-tex]");
      explicitNodes.forEach((node) => {
        if (node.dataset.rendered === "1") return;
        const tex = node.getAttribute("data-tex") || "";
        try {
          window.katex.render(tex, node, {
            throwOnError: false,
            displayMode: false,
          });
          node.dataset.rendered = "1";
        } catch (_) {
          node.textContent = tex;
        }
      });
    }

    if (window.renderMathInElement) {
      try {
        window.renderMathInElement(container, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false },
            { left: "\\(", right: "\\)", display: false },
            { left: "\\[", right: "\\]", display: true },
          ],
          throwOnError: false,
        });
      } catch (_) {
        // Ignore KaTeX parse edge cases
      }
    }
  }

  // =========================================================================
  // Live Elapsed Timer Engine (Only Ticks After User Clicks Start / Resume)
  // =========================================================================

  function updateTimerBadgesUI() {
    // Mode 1 (Batch) Timer Badge & Buttons
    const bSess = getBatchSession();
    const bState = getEffectiveTimerState(bSess, "batch", state.unitId);
    const batchValEl = document.getElementById("batch-timer-val");
    const batchBadgeEl = document.getElementById("batch-timer-badge");
    const batchTagEl = document.getElementById("batch-timer-state-tag");
    const btnBatchStart = document.getElementById("btn-batch-timer-start");
    const btnBatchPause = document.getElementById("btn-batch-timer-pause");
    const btnBatchResume = document.getElementById("btn-batch-timer-resume");

    if (batchValEl) batchValEl.textContent = formatMMSS(bSess.elapsedSec);
    if (batchBadgeEl) batchBadgeEl.setAttribute("data-timer-state", bState);
    if (batchTagEl) {
      batchTagEl.textContent =
        bState === "running"
          ? "Running"
          : bState === "paused"
          ? "Paused"
          : bState === "completed"
          ? "Completed"
          : "Ready";
    }
    if (btnBatchStart) btnBatchStart.hidden = bState !== "not_started";
    if (btnBatchPause) btnBatchPause.hidden = bState !== "running";
    if (btnBatchResume) btnBatchResume.hidden = bState !== "paused";

    // Mode 2 (Single) Timer Badge & Buttons
    const sSess = getSingleSession();
    const sState = getEffectiveTimerState(sSess, "single", state.unitId);
    const singleValEl = document.getElementById("single-timer-val");
    const singleBadgeEl = document.getElementById("single-timer-badge");
    const singleTagEl = document.getElementById("single-timer-state-tag");
    const btnSingleStart = document.getElementById("btn-single-timer-start");
    const btnSinglePause = document.getElementById("btn-single-timer-pause");
    const btnSingleResume = document.getElementById("btn-single-timer-resume");

    if (singleValEl) singleValEl.textContent = formatMMSS(sSess.elapsedSec);
    if (singleBadgeEl) singleBadgeEl.setAttribute("data-timer-state", sState);
    if (singleTagEl) {
      singleTagEl.textContent =
        sState === "running"
          ? "Running"
          : sState === "paused"
          ? "Paused"
          : sState === "completed"
          ? "Completed"
          : "Ready";
    }
    if (btnSingleStart) btnSingleStart.hidden = sState !== "not_started";
    if (btnSinglePause) btnSinglePause.hidden = sState !== "running";
    if (btnSingleResume) btnSingleResume.hidden = sState !== "paused";

    renderTimerGateBanner();
  }

  function renderTimerGateBanner() {
    const gateEl = document.getElementById("quiz-timer-gate-banner");
    if (!gateEl) return;

    const isBatch = state.mode === "batch";
    const sess = isBatch ? getBatchSession() : getSingleSession();
    const tState = getEffectiveTimerState(sess, state.mode, state.unitId);
    const questions = isBatch ? getCurrentBatchQuestions() : getFilteredQuestions();

    if (questions.length === 0 || tState === "completed") {
      gateEl.hidden = true;
      return;
    }

    const answeredCount = questions.filter((q) => typeof sess.answers[q.id] === "number").length;
    const totalCount = questions.length;
    const scopeTitle = isBatch
      ? state.batchSetIndex === -1
        ? "Random 10-Question Set"
        : `Set ${state.batchSetIndex + 1} (Q${questions[0].unit_q_num}–Q${questions[totalCount - 1].unit_q_num})`
      : `Unit ${state.unitId} (Question ${(sess.singleIndex || 0) + 1} of ${totalCount})`;

    gateEl.hidden = false;
    gateEl.setAttribute("data-gate-state", tState);

    if (tState === "not_started") {
      gateEl.innerHTML = `
        <div class="gate-banner-inner">
          <div class="gate-banner-copy">
            <span class="gate-status-pill is-ready">⏱ Timer Ready · 00:00</span>
            <div>
              <strong>Ready to begin ${escapeHtml(scopeTitle)}?</strong>
              <p>The timer will only start after you click <strong>Start Quiz</strong>. You can pause at any time or leave the page and resume later.</p>
            </div>
          </div>
          <div class="gate-banner-actions">
            <button type="button" class="btn btn-primary" data-gate-action="start">
              ▶ Start Quiz &amp; Timer
            </button>
          </div>
        </div>
      `;
    } else if (tState === "paused") {
      gateEl.innerHTML = `
        <div class="gate-banner-inner">
          <div class="gate-banner-copy">
            <span class="gate-status-pill is-paused">⏸ Paused · <span data-gate-elapsed>${formatMMSS(sess.elapsedSec)}</span></span>
            <div>
              <strong>Session Paused — ${escapeHtml(scopeTitle)} (${answeredCount} of ${totalCount} answered)</strong>
              <p>Your progress and elapsed time are saved. Click <strong>Resume Quiz</strong> to continue from where you left off.</p>
            </div>
          </div>
          <div class="gate-banner-actions">
            <button type="button" class="btn btn-primary" data-gate-action="resume">
              ▶ Resume Quiz (<span data-gate-elapsed>${formatMMSS(sess.elapsedSec)}</span>)
            </button>
            <button type="button" class="btn btn-secondary btn-sm" data-gate-action="retake">
              ↺ Restart Fresh
            </button>
          </div>
        </div>
      `;
    } else {
      gateEl.innerHTML = `
        <div class="gate-banner-inner is-compact">
          <div class="gate-banner-copy">
            <span class="gate-status-pill is-running">● Timer Running · <span data-gate-elapsed>${formatMMSS(sess.elapsedSec)}</span></span>
            <span><strong>${escapeHtml(scopeTitle)}</strong> · ${answeredCount} of ${totalCount} answered (progress auto-saves if you leave)</span>
          </div>
          <div class="gate-banner-actions">
            <button type="button" class="btn btn-secondary btn-sm" data-gate-action="pause">
              ⏸ Pause Quiz
            </button>
          </div>
        </div>
      `;
    }
  }

  setInterval(() => {
    if (document.hidden) return;
    if (state.mode === "batch") {
      const bSess = getBatchSession();
      const activeQs = getCurrentBatchQuestions();
      if (bSess.timerState === "running" && !bSess.submitted && activeQs.length > 0) {
        bSess.elapsedSec = (bSess.elapsedSec || 0) + 1;
        bSess.updatedAt = new Date().toISOString();
        const batchValEl = document.getElementById("batch-timer-val");
        if (batchValEl) batchValEl.textContent = formatMMSS(bSess.elapsedSec);
        document.querySelectorAll("[data-gate-elapsed]").forEach((el) => {
          el.textContent = formatMMSS(bSess.elapsedSec);
        });
        if (bSess.elapsedSec % 5 === 0) saveSessions(false);
      }
    } else {
      const sSess = getSingleSession();
      const unitQs = getQuestionsForUnit(state.unitId);
      const answeredCount = unitQs.filter((q) => typeof sSess.answers[q.id] === "number").length;
      if (sSess.timerState === "running" && unitQs.length > 0 && answeredCount < unitQs.length) {
        sSess.elapsedSec = (sSess.elapsedSec || 0) + 1;
        sSess.updatedAt = new Date().toISOString();
        const singleValEl = document.getElementById("single-timer-val");
        if (singleValEl) singleValEl.textContent = formatMMSS(sSess.elapsedSec);
        document.querySelectorAll("[data-gate-elapsed]").forEach((el) => {
          el.textContent = formatMMSS(sSess.elapsedSec);
        });
        if (sSess.elapsedSec % 5 === 0) saveSessions(false);
      }
    }
  }, 1000);

  // Auto-pause and persist when user leaves or hides the page
  window.addEventListener("pagehide", () => {
    pauseAllRunningSessions(true);
  });
  window.addEventListener("beforeunload", () => {
    pauseAllRunningSessions(true);
  });
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) {
      if (pauseAllRunningSessions(true)) {
        updateTimerBadgesUI();
      }
    }
  });

  // =========================================================================
  // Attempt Recording Engine
  // =========================================================================

  function recordAttempt({
    unitId,
    mode,
    setIndex = null,
    scopeKey,
    scopeLabel,
    correct,
    answered,
    total,
    durationSec,
  }) {
    const unit = UNIT_BY_ID.get(unitId) || { id: unitId, title: `Unit ${unitId}` };
    const priorSameScope = state.attempts.filter(
      (a) => a.unitId === unitId && a.mode === mode && a.scopeKey === scopeKey
    ).length;
    const attemptNumber = priorSameScope + 1;
    const denominator = mode === "batch" ? Math.max(1, total) : Math.max(1, answered);
    const pct = Math.round((correct / denominator) * 100);

    const attempt = {
      id: `att_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`,
      timestamp: new Date().toISOString(),
      unitId,
      unitTitle: unit.title,
      mode,
      setIndex,
      scopeKey,
      scopeLabel,
      correct,
      answered,
      total,
      pct,
      durationSec: Math.max(1, Math.round(Number(durationSec) || 1)),
      attemptNumber,
    };

    state.attempts.push(attempt);
    saveAttempts(state.attempts);
    return attempt;
  }

  function logSingleUnitAttemptIfNeeded(unitId = state.unitId, forceLog = false) {
    const sSess = getSingleSession(unitId);
    const unitQs = getQuestionsForUnit(unitId);
    let answered = 0;
    let correct = 0;
    unitQs.forEach((q) => {
      const sel = sSess.answers[q.id];
      if (typeof sel === "number") {
        answered += 1;
        if (sel === q.correct_index) correct += 1;
      }
    });

    if (answered === 0) return null;
    const sig = computeSingleSignature(sSess.answers);
    if (!forceLog && sig === sSess.lastLoggedSignature) {
      return null;
    }

    const att = recordAttempt({
      unitId,
      mode: "single",
      setIndex: null,
      scopeKey: `u${unitId}-single`,
      scopeLabel: `1-by-1 Practice (${answered}/${unitQs.length} Qs Answered)`,
      correct,
      answered,
      total: unitQs.length,
      durationSec: sSess.elapsedSec,
    });

    sSess.lastLoggedSignature = sig;
    saveSessions();
    return att;
  }

  // =========================================================================
  // Filtering & Question Pool Helpers
  // =========================================================================

  function getQuestionsForUnit(unitId) {
    return ALL_QUESTIONS.filter((q) => q.unit_id === unitId);
  }

  function getFilteredQuestions() {
    const unitQs = getQuestionsForUnit(state.unitId);
    const qLower = state.searchQuery.trim().toLowerCase();

    return unitQs.filter((q) => {
      if (state.topicFilter !== "all" && q.topic_code !== state.topicFilter) {
        return false;
      }
      if (state.difficultyFilter !== "all" && q.difficulty !== state.difficultyFilter) {
        return false;
      }
      if (qLower) {
        const hay = `${q.unit_q_num} ${q.topic_code} ${q.topic_title} ${q.question} ${q.options.join(" ")} ${q.explanation}`.toLowerCase();
        if (!hay.includes(qLower)) return false;
      }
      return true;
    });
  }

  function getBatchSets(filteredQs) {
    const sets = [];
    for (let i = 0; i < filteredQs.length; i += 10) {
      sets.push(filteredQs.slice(i, i + 10));
    }
    return sets;
  }

  function getCurrentBatchQuestions() {
    const bSess = getBatchSession();
    if (state.batchSetIndex === -1 && Array.isArray(bSess.customQuestions) && bSess.customQuestions.length > 0) {
      return bSess.customQuestions;
    }
    const filtered = getFilteredQuestions();
    const sets = getBatchSets(filtered);
    if (sets.length === 0) return [];
    const validIdx = Math.max(0, Math.min(state.batchSetIndex, sets.length - 1));
    return sets[validIdx] || [];
  }

  // =========================================================================
  // Progress, Sidebar & Active Unit Attempt Strip
  // =========================================================================

  function updateMasteryUI() {
    const totalAnswered = Object.keys(state.history).length;
    const totalCorrect = Object.values(state.history).filter((h) => h && h.correct).length;
    const totalAttempts = state.attempts.length;

    const overallTextEl = document.getElementById("overall-mastery-text");
    if (overallTextEl) {
      const pct = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
      overallTextEl.textContent =
        totalAnswered > 0
          ? `${totalAnswered} / ${ALL_QUESTIONS.length} Answered (${pct}% ✓) • ${totalAttempts} Attempt${totalAttempts === 1 ? "" : "s"}`
          : `0 / ${ALL_QUESTIONS.length} Answered • ${totalAttempts} Attempt${totalAttempts === 1 ? "" : "s"}`;
    }

    const navAttemptCountEl = document.getElementById("nav-attempt-count");
    if (navAttemptCountEl) {
      navAttemptCountEl.textContent = String(totalAttempts);
    }

    // Update per-unit sidebar badges and mini progress bars
    UNITS.forEach((u) => {
      const unitQs = getQuestionsForUnit(u.id);
      let answered = 0;
      let correct = 0;
      unitQs.forEach((q) => {
        const h = state.history[q.id];
        if (h) {
          answered += 1;
          if (h.correct) correct += 1;
        }
      });

      const unitAttempts = state.attempts.filter((a) => a.unitId === u.id).length;
      const statBadge = document.querySelector(`[data-unit-stat="${u.id}"]`);
      if (statBadge) {
        if (answered > 0) {
          statBadge.textContent = unitAttempts > 0 ? `${correct}/${answered} ✓ · ${unitAttempts} att` : `${correct}/${answered} ✓`;
        } else {
          statBadge.textContent = `${u.question_count} Qs`;
        }
      }
      const bar = document.querySelector(`[data-unit-bar="${u.id}"]`);
      if (bar) {
        const pct = Math.min(100, Math.round((answered / Math.max(1, u.question_count)) * 100));
        bar.style.width = `${pct}%`;
      }
    });
  }

  function renderUnitAttemptStrip() {
    const stripEl = document.getElementById("unit-attempt-strip");
    if (!stripEl) return;

    const unit = UNIT_BY_ID.get(state.unitId) || UNITS[0];
    const modeLabel = state.mode === "batch" ? "Mode 1 (10-Question Sets)" : "Mode 2 (1 Question at a Time)";
    const unitModeAttempts = state.attempts.filter(
      (a) => a.unitId === state.unitId && a.mode === state.mode
    );

    if (unitModeAttempts.length === 0) {
      stripEl.innerHTML = `
        <div class="unit-attempt-strip-left">
          <strong>Unit ${unit.id} · ${escapeHtml(modeLabel)}:</strong>
          <span>No saved attempts yet for this unit &amp; mode. Complete a set or click <em>Save Attempt / Retake</em> to log your performance.</span>
        </div>
        <div>
          <a href="/dashboard" class="strip-link-btn">Open Performance Dashboard →</a>
        </div>
      `;
      return;
    }

    const bestPct = Math.max(...unitModeAttempts.map((a) => a.pct));
    const avgPct = Math.round(
      unitModeAttempts.reduce((sum, a) => sum + a.pct, 0) / unitModeAttempts.length
    );
    const totalSec = unitModeAttempts.reduce((sum, a) => sum + (a.durationSec || 0), 0);
    const latest = unitModeAttempts[unitModeAttempts.length - 1];

    stripEl.innerHTML = `
      <div class="unit-attempt-strip-left">
        <strong>Unit ${unit.id} · ${escapeHtml(modeLabel)} History:</strong>
        <span class="strip-pill"><strong>${unitModeAttempts.length}</strong> Attempt${unitModeAttempts.length === 1 ? "" : "s"}</span>
        <span class="strip-pill">Best: <strong>${bestPct}%</strong></span>
        <span class="strip-pill">Avg: <strong>${avgPct}%</strong></span>
        <span class="strip-pill">Latest: <strong>${latest.correct}/${state.mode === "batch" ? latest.total : latest.answered} (${latest.pct}%)</strong> in <strong>${formatMMSS(latest.durationSec)}</strong></span>
        <span class="strip-pill">Total Time: <strong>${formatDurationHuman(totalSec)}</strong></span>
      </div>
      <div>
        <a href="/dashboard" class="strip-link-btn">Full Performance Dashboard →</a>
      </div>
    `;
  }

  // =========================================================================
  // Unit Header Banner, Topic Dropdown & Unit Pager
  // =========================================================================

  function renderUnitBanner() {
    const bannerEl = document.getElementById("quiz-unit-banner");
    const unit = UNIT_BY_ID.get(state.unitId) || UNITS[0];
    if (!bannerEl || !unit) return;

    const prevUnit = UNIT_BY_ID.get(unit.id - 1);
    const nextUnit = UNIT_BY_ID.get(unit.id + 1);

    bannerEl.style.setProperty("--cat-color", unit.color);
    bannerEl.innerHTML = `
      <div class="section-banner-num" aria-hidden="true">U${unit.id}</div>
      <div class="section-banner-body">
        <h2 class="section-banner-title" tabindex="-1">${escapeHtml(unit.title)}</h2>
      </div>
      <div class="section-banner-nav">
        <a
          href="${prevUnit ? `#/unit/${prevUnit.id}` : "#"}"
          class="section-nav-btn ${prevUnit ? "" : "is-disabled"}"
          ${prevUnit ? "" : 'aria-disabled="true" tabindex="-1"'}
        >← Unit ${prevUnit ? prevUnit.id : ""}</a>
        <a
          href="${nextUnit ? `#/unit/${nextUnit.id}` : "#"}"
          class="section-nav-btn ${nextUnit ? "" : "is-disabled"}"
          ${nextUnit ? "" : 'aria-disabled="true" tabindex="-1"'}
        >Unit ${nextUnit ? nextUnit.id : ""} →</a>
      </div>
    `;
  }

  function populateTopicDropdown() {
    const selectEl = document.getElementById("quiz-topic-select");
    const unit = UNIT_BY_ID.get(state.unitId);
    if (!selectEl || !unit) return;

    let html = `<option value="all">All Unit ${unit.id} CED Topics (${unit.question_count} Questions)</option>`;
    unit.topics.forEach((t) => {
      const selectedAttr = state.topicFilter === t.code ? "selected" : "";
      html += `<option value="${escapeHtml(t.code)}" ${selectedAttr}>Topic ${escapeHtml(t.code)}: ${escapeHtml(t.title)} (${t.count} Qs)</option>`;
    });
    selectEl.innerHTML = html;
  }

  function renderUnitPager() {
    const pagerEl = document.getElementById("quiz-unit-pager");
    if (!pagerEl) return;
    const prevUnit = UNIT_BY_ID.get(state.unitId - 1);
    const nextUnit = UNIT_BY_ID.get(state.unitId + 1);

    const prevHtml = prevUnit
      ? `<a href="#/unit/${prevUnit.id}" class="pager-card pager-prev" style="--cat-color: ${prevUnit.color}">
           <small>← Previous AP Chemistry Unit (Weight: ${escapeHtml(prevUnit.exam_weight)})</small>
           <strong>${escapeHtml(prevUnit.title)}</strong>
         </a>`
      : `<div></div>`;

    const nextHtml = nextUnit
      ? `<a href="#/unit/${nextUnit.id}" class="pager-card pager-next" style="--cat-color: ${nextUnit.color}">
           <small>Next AP Chemistry Unit (Weight: ${escapeHtml(nextUnit.exam_weight)}) →</small>
           <strong>${escapeHtml(nextUnit.title)}</strong>
         </a>`
      : `<div></div>`;

    pagerEl.innerHTML = prevHtml + nextHtml;
  }

  function syncSidebarActive() {
    document.querySelectorAll(".quiz-unit-btn").forEach((btn) => {
      const uid = Number(btn.getAttribute("data-unit"));
      btn.classList.toggle("active", uid === state.unitId);
    });
  }

  // =========================================================================
  // MODE 1: 10-Question Practice Set (Score at the End)
  // =========================================================================

  function renderBatchMode() {
    const filtered = getFilteredQuestions();
    const sets = getBatchSets(filtered);
    const pillsContainer = document.getElementById("batch-set-pills");
    const stageEl = document.getElementById("quiz-questions-stage");
    const bannerEl = document.getElementById("batch-score-banner");
    const bottomBarEl = document.getElementById("batch-bottom-bar");

    if (state.batchSetIndex !== -1 && state.batchSetIndex >= sets.length) {
      state.batchSetIndex = 0;
    }

    const bSess = getBatchSession();

    // 1. Render Set Selector Pills (Set 1: Q1–10, Set 2: Q11–20, etc.)
    if (pillsContainer) {
      if (sets.length === 0) {
        pillsContainer.innerHTML = `<span class="text-muted">No matching questions</span>`;
      } else {
        pillsContainer.innerHTML = sets
          .map((setQs, idx) => {
            const firstNum = setQs[0].unit_q_num;
            const lastNum = setQs[setQs.length - 1].unit_q_num;
            const isActive = state.batchSetIndex === idx;
            const setSess = getBatchSession(state.unitId, idx);
            const scopeKey = `u${state.unitId}-set${idx}`;
            const setAttempts = state.attempts.filter(
              (a) => a.unitId === state.unitId && a.mode === "batch" && a.scopeKey === scopeKey
            );
            const latestAtt = setAttempts.length > 0 ? setAttempts[setAttempts.length - 1] : setSess.lastAttempt;
            const answeredInSet = setQs.filter((q) => typeof setSess.answers[q.id] === "number").length;
            let statusBadge = "";
            if (latestAtt) {
              statusBadge = `<span class="set-pill-score">${latestAtt.correct}/${latestAtt.total}${setAttempts.length > 1 ? ` (×${setAttempts.length})` : ""}</span>`;
            } else if (!setSess.submitted && (answeredInSet > 0 || setSess.elapsedSec > 0)) {
              statusBadge = `<span class="set-pill-paused" title="Paused in-progress set">⏸ ${answeredInSet}/${setQs.length}</span>`;
            }
            return `
              <button
                type="button"
                class="set-pill-btn ${isActive ? "active" : ""}"
                data-set-idx="${idx}"
              >
                Set ${idx + 1} (Q${firstNum}–Q${lastNum}) ${statusBadge}
              </button>
            `;
          })
          .join("");
      }
    }

    const activeQs = getCurrentBatchQuestions();

    if (activeQs.length === 0) {
      if (bannerEl) bannerEl.hidden = true;
      if (bottomBarEl) bottomBarEl.hidden = true;
      stageEl.innerHTML = `
        <div class="empty-state">
          <h3>No questions match your current filter</h3>
          <p>Try resetting the CED Topic filter, Difficulty filter, or search box.</p>
        </div>
      `;
      updateBatchProgressStrip(activeQs);
      updateTimerBadgesUI();
      return;
    }

    if (bottomBarEl) bottomBarEl.hidden = false;

    // 2. Update Progress Strip, Timer & Question Dots
    updateBatchProgressStrip(activeQs);
    updateTimerBadgesUI();

    // 3. Render Score Banner if Set is Submitted
    if (bSess.submitted) {
      renderBatchScoreBanner(activeQs);
    } else if (bannerEl) {
      bannerEl.hidden = true;
    }

    // 4. Render All 10 Question Cards in the Active Set
    stageEl.innerHTML = activeQs
      .map((q, idxInSet) => buildQuestionCardHtml(q, idxInSet + 1, activeQs.length, "batch"))
      .join("");

    // 5. Update bottom bar button state
    const bottomSubmitBtn = document.getElementById("btn-bottom-submit");
    const topSubmitBtn = document.getElementById("btn-submit-batch");
    const bottomInfoEl = document.getElementById("batch-bottom-info");
    if (bSess.submitted) {
      if (bottomSubmitBtn) bottomSubmitBtn.textContent = "✓ Set Scored — Review Answers Above";
      if (topSubmitBtn) topSubmitBtn.textContent = "✓ Scored";
      if (bottomInfoEl) {
        bottomInfoEl.innerHTML =
          "<strong>Set Completed &amp; Saved to Attempts:</strong> Review the step-by-step explanations above, or click <em>↺ Retake This Set</em> to start a fresh attempt.";
      }
    } else {
      if (bottomSubmitBtn) bottomSubmitBtn.textContent = `✓ Submit ${activeQs.length}-Question Set & Show Answers`;
      if (topSubmitBtn) topSubmitBtn.textContent = `✓ Submit ${activeQs.length} Questions & Score`;
      if (bottomInfoEl) {
        const answeredCount = activeQs.filter((q) => typeof bSess.answers[q.id] === "number").length;
        bottomInfoEl.innerHTML = `You have answered <strong>${answeredCount} of ${activeQs.length}</strong> questions in this set. Submit when ready to record your attempt, time, and score.`;
      }
    }

    renderMathInContainer(stageEl);
    if (bSess.submitted && bannerEl) {
      renderMathInContainer(bannerEl);
    }
  }

  function updateBatchProgressStrip(activeQs) {
    const labelEl = document.getElementById("batch-progress-label");
    const progEl = document.getElementById("batch-progress-bar");
    const dotsEl = document.getElementById("batch-q-dots");
    const bSess = getBatchSession();

    const total = activeQs.length;
    const answered = activeQs.filter((q) => typeof bSess.answers[q.id] === "number").length;

    if (labelEl) {
      labelEl.innerHTML = `Answered <strong>${answered}</strong> of <strong>${total}</strong> questions`;
    }
    if (progEl) {
      progEl.max = Math.max(1, total);
      progEl.value = answered;
      progEl.textContent = `${Math.round((answered / Math.max(1, total)) * 100)}%`;
    }
    if (dotsEl) {
      dotsEl.innerHTML = activeQs
        .map((q, idx) => {
          const sel = bSess.answers[q.id];
          const hasAns = typeof sel === "number";
          let cls = "";
          if (bSess.submitted) {
            cls = hasAns && sel === q.correct_index ? "is-correct" : "is-wrong";
          } else if (hasAns) {
            cls = "is-answered";
          }
          return `
            <button
              type="button"
              class="q-dot-btn ${cls}"
              data-jump-card="q-card-${q.id}"
              title="Jump to Question ${idx + 1} (Unit Q#${q.unit_q_num})"
            >${idx + 1}</button>
          `;
        })
        .join("");
    }
  }

  function renderBatchScoreBanner(activeQs) {
    const bannerEl = document.getElementById("batch-score-banner");
    if (!bannerEl) return;

    const bSess = getBatchSession();
    const total = activeQs.length;
    let correctCount = 0;
    let wrongCount = 0;
    let unansweredCount = 0;

    activeQs.forEach((q) => {
      const sel = bSess.answers[q.id];
      if (typeof sel !== "number") {
        unansweredCount += 1;
      } else if (sel === q.correct_index) {
        correctCount += 1;
      } else {
        wrongCount += 1;
      }
    });

    const pct = total > 0 ? Math.round((correctCount / total) * 100) : 0;
    let circleClass = "score-high";
    let apFeedback = "Outstanding AP Level 5 Mastery! You demonstrated strong command of the concepts and calculations in this set.";
    if (pct < 60) {
      circleClass = "score-low";
      apFeedback = "Review the step-by-step explanations below carefully, focusing on the governing equations and conceptual distractors.";
    } else if (pct < 80) {
      circleClass = "score-mid";
      apFeedback = "Solid AP Exam performance (AP 3–4 range)! Review the missed questions below to sharpen your accuracy.";
    }

    const setTitle =
      state.batchSetIndex === -1
        ? "Random 10-Question Practice Set"
        : `Practice Set ${state.batchSetIndex + 1} (Questions ${activeQs[0].unit_q_num}–${activeQs[total - 1].unit_q_num})`;

    const filtered = getFilteredQuestions();
    const totalSets = getBatchSets(filtered).length;
    const hasNextSet = state.batchSetIndex >= 0 && state.batchSetIndex + 1 < totalSets;
    const durationSec = bSess.lastAttempt ? bSess.lastAttempt.durationSec : bSess.elapsedSec;
    const attemptNum = bSess.lastAttempt ? bSess.lastAttempt.attemptNumber : 1;

    bannerEl.hidden = false;
    bannerEl.innerHTML = `
      <div class="score-banner-grid">
        <div class="score-circle ${circleClass}">
          <span class="score-circle-num">${correctCount}/${total}</span>
          <span class="score-circle-pct">${pct}%</span>
        </div>
        <div class="score-details">
          <span class="section-eyebrow">ATTEMPT #${attemptNum} SAVED • UNIT ${state.unitId} • TIME: ${formatMMSS(durationSec)}</span>
          <h3>${escapeHtml(setTitle)} — Scored!</h3>
          <p>${escapeHtml(apFeedback)}</p>
          <div class="score-Chips-row">
            <span class="score-stat-pill pill-ok">✓ ${correctCount} Correct</span>
            <span class="score-stat-pill pill-err">✗ ${wrongCount} Incorrect</span>
            ${unansweredCount > 0 ? `<span class="score-stat-pill">— ${unansweredCount} Unanswered</span>` : ""}
            <span class="score-stat-pill">⏱ Time: ${formatDurationHuman(durationSec)}</span>
            <span class="score-stat-pill">Attempt #${attemptNum}</span>
          </div>
        </div>
        <div class="score-banner-actions">
          <button type="button" class="btn btn-accent" id="btn-banner-retry">
            ↺ Retake This Set
          </button>
          ${
            hasNextSet
              ? `<button type="button" class="btn btn-primary" id="btn-banner-next-set">
                   Next Set (Set ${state.batchSetIndex + 2}) →
                 </button>`
              : ""
          }
          <a href="/dashboard" class="btn btn-secondary">
            📊 View Dashboard
          </a>
        </div>
      </div>
    `;
  }

  // =========================================================================
  // MODE 2: 1 Question at a Time (Instant Feedback & Explanation)
  // =========================================================================

  function renderSingleMode() {
    const filtered = getFilteredQuestions();
    const stageEl = document.getElementById("quiz-questions-stage");
    const bannerEl = document.getElementById("batch-score-banner");
    const bottomBarEl = document.getElementById("batch-bottom-bar");
    const jumpSelect = document.getElementById("single-jump-select");
    const qgridEl = document.getElementById("single-qgrid");
    const unitScoreEl = document.getElementById("single-unit-score");

    if (bannerEl) bannerEl.hidden = true;
    if (bottomBarEl) bottomBarEl.hidden = true;

    const sSess = getSingleSession();
    updateTimerBadgesUI();

    if (filtered.length === 0) {
      stageEl.innerHTML = `
        <div class="empty-state">
          <h3>No questions match your current filter</h3>
          <p>Try resetting the CED Topic filter, Difficulty filter, or search box.</p>
        </div>
      `;
      if (jumpSelect) jumpSelect.innerHTML = `<option>No questions</option>`;
      if (qgridEl) qgridEl.innerHTML = "";
      return;
    }

    if (sSess.singleIndex >= filtered.length) {
      sSess.singleIndex = 0;
    }
    if (sSess.singleIndex < 0) {
      sSess.singleIndex = filtered.length - 1;
    }

    const currentQ = filtered[sSess.singleIndex];

    // 1. Populate Jump Select Dropdown
    if (jumpSelect) {
      jumpSelect.innerHTML = filtered
        .map((q, idx) => {
          const sel = sSess.answers[q.id];
          const hasAns = typeof sel === "number";
          const mark = hasAns ? (sel === q.correct_index ? " ✓" : " ✗") : "";
          const selectedAttr = idx === sSess.singleIndex ? "selected" : "";
          return `<option value="${idx}" ${selectedAttr}>Question ${q.unit_q_num} of ${unitQuestionCount(q.unit_id)} • Topic ${escapeHtml(q.topic_code)}${mark}</option>`;
        })
        .join("");
    }

    // 2. Update Unit Score in Mode 2 Toolbar
    if (unitScoreEl) {
      let answered = 0;
      let correct = 0;
      filtered.forEach((q) => {
        const sel = sSess.answers[q.id];
        if (typeof sel === "number") {
          answered += 1;
          if (sel === q.correct_index) correct += 1;
        }
      });
      const pct = answered > 0 ? ` (${Math.round((correct / answered) * 100)}%)` : "";
      unitScoreEl.innerHTML = `Mode 2 Score: <strong>${correct} / ${answered}</strong>${pct}`;
    }

    // 3. Render the unit's Question Map Grid (1..question_count)
    const qgridRangeEl = document.getElementById("qgrid-range");
    if (qgridRangeEl) qgridRangeEl.textContent = `(1–${unitQuestionCount(state.unitId)})`;
    if (qgridEl) {
      qgridEl.hidden = !state.showQGrid;
      qgridEl.innerHTML = filtered
        .map((q, idx) => {
          const sel = sSess.answers[q.id];
          const hasAns = typeof sel === "number";
          let statusCls = "";
          if (hasAns) {
            statusCls = sel === q.correct_index ? "is-correct" : "is-wrong";
          }
          const curCls = idx === sSess.singleIndex ? "is-current" : "";
          return `
            <button
              type="button"
              class="qgrid-btn ${statusCls} ${curCls}"
              data-single-idx="${idx}"
              title="Question ${q.unit_q_num}: Topic ${escapeHtml(q.topic_code)}"
            >${q.unit_q_num}</button>
          `;
        })
        .join("");
    }

    // 4. Prev / Next button states
    const prevBtn = document.getElementById("btn-single-prev");
    const nextBtn = document.getElementById("btn-single-next");
    if (prevBtn) prevBtn.disabled = sSess.singleIndex <= 0;
    if (nextBtn) nextBtn.disabled = sSess.singleIndex >= filtered.length - 1;

    // 5. Render the Focused Single Question Card
    stageEl.innerHTML = buildQuestionCardHtml(currentQ, sSess.singleIndex + 1, filtered.length, "single");
    renderMathInContainer(stageEl);
  }

  // =========================================================================
  // Shared Question Card HTML Builder (Mode 1 & Mode 2)
  // =========================================================================

  function buildQuestionCardHtml(q, posInView, totalInView, mode) {
    const isBatch = mode === "batch";
    const bSess = isBatch ? getBatchSession() : null;
    const sSess = !isBatch ? getSingleSession() : null;
    const activeSess = isBatch ? bSess : sSess;
    const effTimerState = getEffectiveTimerState(activeSess);
    const selectedIdx = isBatch ? bSess.answers[q.id] : sSess.answers[q.id];
    const hasSelected = typeof selectedIdx === "number";
    const isRevealed = isBatch ? bSess.submitted : hasSelected;
    const isCorrect = hasSelected && selectedIdx === q.correct_index;
    const isTimerLocked = !isRevealed && effTimerState !== "running";

    let cardStateClass = "";
    let statusPillHtml = "";

    if (isRevealed) {
      if (!hasSelected) {
        cardStateClass = "card-unanswered-review";
        statusPillHtml = `<span class="q-status-pill status-unanswered">— Unanswered • Correct Answer: ${q.correct_letter}</span>`;
      } else if (isCorrect) {
        cardStateClass = "card-correct";
        statusPillHtml = `<span class="q-status-pill status-correct">✓ Correct (${q.correct_letter})</span>`;
      } else {
        cardStateClass = "card-wrong";
        statusPillHtml = `<span class="q-status-pill status-wrong">✗ Incorrect (Your Answer: ${LETTERS[selectedIdx]} • Correct: ${q.correct_letter})</span>`;
      }
    } else if (isTimerLocked) {
      cardStateClass = "card-timer-locked";
      const lockLabel = effTimerState === "paused" ? "⏸ Timer Paused" : "⏱ Click Start Quiz to Answer";
      statusPillHtml = `<button type="button" class="q-status-pill status-locked-btn" data-card-timer-start="1">${lockLabel}</button>`;
    }

    const diffClass = q.difficulty === "Challenging" ? "diff-challenging" : "";
    const headerNumLabel = isBatch
      ? `Set Q${posInView} of ${totalInView} · Unit ${q.unit_id} #${q.unit_q_num}`
      : `Question ${q.unit_q_num} of ${unitQuestionCount(q.unit_id)} (Unit ${q.unit_id})`;

    const stimulusHtml = q.stimulus
      ? `<div class="q-stimulus-box">${q.stimulus}</div>`
      : "";

    const optionsHtml = q.options
      .map((optText, optIdx) => {
        const letter = LETTERS[optIdx];
        const isThisSelected = hasSelected && selectedIdx === optIdx;
        const isThisCorrect = optIdx === q.correct_index;

        let optClass = "";
        let tagHtml = "";

        if (isRevealed) {
          if (isThisCorrect) {
            optClass = "opt-correct-answer";
            tagHtml = `<span class="q-option-tag">${isThisSelected ? "✓ Your Answer (Correct)" : "✓ Correct Answer"}</span>`;
          } else if (isThisSelected) {
            optClass = "opt-wrong-selected";
            tagHtml = `<span class="q-option-tag">✗ Your Choice</span>`;
          }
        } else if (isThisSelected) {
          optClass = "is-selected";
          tagHtml = `<span class="q-option-tag">Selected</span>`;
        }

        if (isTimerLocked) {
          optClass += " is-timer-locked";
        }

        const disabledAttr = isRevealed ? "disabled" : "";

        return `
          <button
            type="button"
            class="q-option-btn ${optClass.trim()}"
            data-q-id="${q.id}"
            data-opt-idx="${optIdx}"
            ${isTimerLocked ? 'data-timer-locked="1"' : ""}
            ${disabledAttr}
          >
            <span class="q-option-letter">${letter}</span>
            <span class="q-option-text">${optText}</span>
            ${tagHtml}
          </button>
        `;
      })
      .join("");

    let explanationHtml = "";
    if (isRevealed) {
      const expBoxClass = isCorrect ? "exp-correct" : "exp-wrong";
      const expHeadline = !hasSelected
        ? `Unanswered — The Correct Answer is ${q.correct_letter}`
        : isCorrect
        ? `✓ Correct! Option ${q.correct_letter} is the right answer.`
        : `✗ Incorrect — You selected ${LETTERS[selectedIdx]}, but the correct answer is ${q.correct_letter}.`;

      explanationHtml = `
        <div class="q-explanation-box ${expBoxClass}">
          <div class="exp-header">
            <span class="exp-title">${escapeHtml(expHeadline)}</span>
            <span class="q-topic-pill">CED Topic ${escapeHtml(q.topic_code)}</span>
          </div>
          <p class="exp-body"><strong>Explanation:</strong> ${q.explanation}</p>
        </div>
      `;
    }

    let singleFooterHtml = "";
    if (!isBatch) {
      singleFooterHtml = `
        <div class="single-card-footer">
          <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; align-items: center;">
            ${
              hasSelected
                ? `<button type="button" class="btn btn-secondary btn-sm" data-retry-single="${q.id}">
                     ↺ Redo This Question
                   </button>`
                : isTimerLocked
                ? `<span class="text-muted" style="font-size: 0.84rem;">Click <strong>▶ ${effTimerState === "paused" ? "Resume Quiz" : "Start Quiz"}</strong> above to start the timer and select your answer.</span>`
                : `<span class="text-muted" style="font-size: 0.84rem;">Select an option above (A–D) to immediately check your answer and view the explanation.</span>`
            }
          </div>
          <div style="display: flex; gap: 0.5rem;">
            ${
              sSess.singleIndex > 0
                ? `<button type="button" class="btn btn-secondary btn-sm" id="btn-card-prev">← Previous</button>`
                : ""
            }
            ${
              sSess.singleIndex < totalInView - 1
                ? `<button type="button" class="btn btn-primary btn-sm" id="btn-card-next">Next Question →</button>`
                : ""
            }
          </div>
        </div>
      `;
    }

    return `
      <article class="quiz-q-card ${cardStateClass}" id="q-card-${q.id}">
        <div class="q-card-header">
          <div class="q-meta-left">
            <span class="q-num-badge">${escapeHtml(headerNumLabel)}</span>
            <span class="q-topic-pill">Topic ${escapeHtml(q.topic_code)} · ${escapeHtml(q.topic_title)}</span>
            <span class="q-diff-pill ${diffClass}">${escapeHtml(q.difficulty)}</span>
          </div>
          ${statusPillHtml}
        </div>
        ${stimulusHtml}
        <div class="q-stem">${q.question}</div>
        <div class="q-options-list" role="group" aria-label="Answer choices for question ${q.unit_q_num}">
          ${optionsHtml}
        </div>
        ${explanationHtml}
        ${singleFooterHtml}
      </article>
    `;
  }

  // =========================================================================
  // Master View Renderer & Mode Switcher
  // =========================================================================

  function renderAll() {
    syncSidebarActive();
    renderUnitBanner();
    populateTopicDropdown();
    renderUnitPager();
    updateMasteryUI();
    renderUnitAttemptStrip();

    const batchPanel = document.getElementById("batch-controls-panel");
    const singlePanel = document.getElementById("single-controls-panel");
    const btnModeBatch = document.getElementById("btn-mode-batch");
    const btnModeSingle = document.getElementById("btn-mode-single");
    const btnToggleTimed = document.getElementById("btn-toggle-timed-mode");

    const isBatch = state.mode === "batch";
    if (batchPanel) batchPanel.hidden = !isBatch;
    if (singlePanel) singlePanel.hidden = isBatch;

    if (btnToggleTimed) {
      btnToggleTimed.setAttribute("data-current-mode", state.mode);
      btnToggleTimed.classList.toggle("is-timed-active", isBatch);
      if (isBatch) {
        btnToggleTimed.textContent = "← Instant Feedback Mode";
        btnToggleTimed.title = "Revert back to Instant Feedback Mode (1 Question at a Time)";
      } else {
        btnToggleTimed.textContent = "⏱ Timed Mode";
        btnToggleTimed.title = "Switch to Timed 10-Question Batch Quiz Mode";
      }
    }

    if (btnModeBatch) {
      btnModeBatch.classList.toggle("active", isBatch);
      btnModeBatch.setAttribute("aria-selected", String(isBatch));
    }
    if (btnModeSingle) {
      btnModeSingle.classList.toggle("active", !isBatch);
      btnModeSingle.setAttribute("aria-selected", String(!isBatch));
    }

    if (isBatch) {
      renderBatchMode();
    } else {
      renderSingleMode();
    }
  }

  function selectUnit(unitId, resetFilters = true) {
    pauseAllRunningSessions(false);
    const validId = UNIT_BY_ID.has(unitId) ? unitId : 1;
    state.unitId = validId;
    if (resetFilters) {
      state.topicFilter = "all";
      state.difficultyFilter = "all";
      state.searchQuery = "";
      state.batchSetIndex = 0;

      const diffSelect = document.getElementById("quiz-difficulty-select");
      if (diffSelect) diffSelect.value = "all";
      const searchInput = document.getElementById("quiz-search-input");
      if (searchInput) searchInput.value = "";
    }
    saveSessions(false);

    const doUpdate = () => {
      renderAll();
      window.scrollTo({ top: 0, behavior: "smooth" });
    };

    if (document.startViewTransition) {
      document.startViewTransition(doUpdate);
    } else {
      doUpdate();
    }
  }

  // =========================================================================
  // Batch Set & Unit Retake Actions
  // =========================================================================

  function drawRandomBatchSet() {
    pauseAllRunningSessions(false);
    const pool = getFilteredQuestions();
    if (pool.length === 0) return;
    const copy = pool.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = copy[i];
      copy[i] = copy[j];
      copy[j] = tmp;
    }
    state.batchSetIndex = -1;
    const bSess = getBatchSession(state.unitId, -1);
    bSess.customQuestions = copy.slice(0, Math.min(10, copy.length));
    bSess.answers = {};
    bSess.submitted = false;
    bSess.elapsedSec = 0;
    bSess.timerState = "not_started";
    bSess.updatedAt = new Date().toISOString();
    bSess.lastAttempt = null;
    saveSessions();
    renderBatchMode();
  }

  function submitCurrentBatchSet() {
    const activeQs = getCurrentBatchQuestions();
    if (activeQs.length === 0) return;

    const bSess = getBatchSession();
    if (bSess.submitted) return;

    bSess.submitted = true;
    bSess.timerState = "completed";
    bSess.updatedAt = new Date().toISOString();
    let correctCount = 0;
    let answeredCount = 0;

    activeQs.forEach((q) => {
      const sel = bSess.answers[q.id];
      if (typeof sel === "number") {
        answeredCount += 1;
        const isOk = sel === q.correct_index;
        if (isOk) correctCount += 1;
        state.history[q.id] = { selected: sel, correct: isOk };
      }
    });

    const scopeKey =
      state.batchSetIndex === -1
        ? `u${state.unitId}-random`
        : `u${state.unitId}-set${state.batchSetIndex}`;
    const scopeLabel =
      state.batchSetIndex === -1
        ? "Random 10-Question Set"
        : `Set ${state.batchSetIndex + 1} (Q${activeQs[0].unit_q_num}–Q${activeQs[activeQs.length - 1].unit_q_num})`;

    const attempt = recordAttempt({
      unitId: state.unitId,
      mode: "batch",
      setIndex: state.batchSetIndex,
      scopeKey,
      scopeLabel,
      correct: correctCount,
      answered: answeredCount,
      total: activeQs.length,
      durationSec: bSess.elapsedSec,
    });

    bSess.lastAttempt = attempt;

    saveHistory(state.history);
    saveSessions();
    updateMasteryUI();
    renderUnitAttemptStrip();
    renderBatchMode();

    const bannerEl = document.getElementById("batch-score-banner");
    if (bannerEl) {
      bannerEl.scrollIntoView({ behavior: "smooth", block: "nearest" });
    }
  }

  function retakeCurrentBatchSet() {
    const activeQs = getCurrentBatchQuestions();
    const bSess = getBatchSession();

    // If the student answered questions in this set and hadn't submitted yet, log the partial attempt before clearing
    if (!bSess.submitted && activeQs.length > 0) {
      let answeredCount = 0;
      let correctCount = 0;
      activeQs.forEach((q) => {
        const sel = bSess.answers[q.id];
        if (typeof sel === "number") {
          answeredCount += 1;
          if (sel === q.correct_index) correctCount += 1;
        }
      });
      if (answeredCount > 0) {
        const scopeKey =
          state.batchSetIndex === -1
            ? `u${state.unitId}-random`
            : `u${state.unitId}-set${state.batchSetIndex}`;
        const scopeLabel =
          state.batchSetIndex === -1
            ? "Random 10-Question Set"
            : `Set ${state.batchSetIndex + 1} (Q${activeQs[0].unit_q_num}–Q${activeQs[activeQs.length - 1].unit_q_num})`;
        recordAttempt({
          unitId: state.unitId,
          mode: "batch",
          setIndex: state.batchSetIndex,
          scopeKey,
          scopeLabel,
          correct: correctCount,
          answered: answeredCount,
          total: activeQs.length,
          durationSec: bSess.elapsedSec,
        });
      }
    }

    bSess.answers = {};
    bSess.submitted = false;
    bSess.elapsedSec = 0;
    bSess.timerState = "not_started";
    bSess.updatedAt = new Date().toISOString();
    saveSessions();
    updateMasteryUI();
    renderUnitAttemptStrip();
    renderBatchMode();
  }

  function retakeUnitInMode(unitId, targetMode, optionalSetIndex = null) {
    pauseAllRunningSessions(false);
    const validUnitId = UNIT_BY_ID.has(unitId) ? unitId : state.unitId;

    if (targetMode === "batch") {
      const unitQs = getQuestionsForUnit(validUnitId);
      const sets = getBatchSets(unitQs);

      if (typeof optionalSetIndex === "number") {
        // Retake a specific set in Mode 1
        state.unitId = validUnitId;
        state.mode = "batch";
        state.batchSetIndex = optionalSetIndex;
        if (optionalSetIndex === -1) {
          drawRandomBatchSet();
        } else {
          retakeCurrentBatchSet();
        }
      } else {
        // Retake all Mode 1 sets in this unit
        sets.forEach((setQs, idx) => {
          const s = getBatchSession(validUnitId, idx);
          if (!s.submitted) {
            let ansCount = 0;
            let corrCount = 0;
            setQs.forEach((q) => {
              const sel = s.answers[q.id];
              if (typeof sel === "number") {
                ansCount += 1;
                if (sel === q.correct_index) corrCount += 1;
              }
            });
            if (ansCount > 0) {
              recordAttempt({
                unitId: validUnitId,
                mode: "batch",
                setIndex: idx,
                scopeKey: `u${validUnitId}-set${idx}`,
                scopeLabel: `Set ${idx + 1} (Q${setQs[0].unit_q_num}–Q${setQs[setQs.length - 1].unit_q_num})`,
                correct: corrCount,
                answered: ansCount,
                total: setQs.length,
                durationSec: s.elapsedSec,
              });
            }
          }
          s.answers = {};
          s.submitted = false;
          s.elapsedSec = 0;
          s.timerState = "not_started";
          s.updatedAt = new Date().toISOString();
        });

        const randSess = getBatchSession(validUnitId, -1);
        randSess.answers = {};
        randSess.submitted = false;
        randSess.elapsedSec = 0;
        randSess.timerState = "not_started";
        randSess.updatedAt = new Date().toISOString();

        state.unitId = validUnitId;
        state.mode = "batch";
        state.batchSetIndex = 0;
      }
    } else {
      // Mode 2 ("single"): Save any unlogged progress as an attempt, then reset Mode 2 for this unit
      logSingleUnitAttemptIfNeeded(validUnitId, false);
      const sSess = getSingleSession(validUnitId);
      sSess.answers = {};
      sSess.elapsedSec = 0;
      sSess.singleIndex = 0;
      sSess.timerState = "not_started";
      sSess.updatedAt = new Date().toISOString();
      sSess.lastLoggedSignature = "";

      state.unitId = validUnitId;
      state.mode = "single";
    }

    if (window.location.hash !== `#/unit/${validUnitId}`) {
      history.replaceState(null, "", `#/unit/${validUnitId}`);
    }
    saveSessions();
    renderAll();
    const workspaceEl = document.getElementById("quiz-unit-banner");
    if (workspaceEl) {
      workspaceEl.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  // =========================================================================
  // Event Listeners, Deep-Link Query Params & Leave-and-Resume Routing
  // =========================================================================

  function parseHashRoute() {
    const hash = window.location.hash || "";
    const m = hash.match(/^#\/unit\/(\d+)/);
    if (m) {
      const uid = Number(m[1]);
      if (UNIT_BY_ID.has(uid)) return uid;
    }
    return null;
  }

  function findMostRecentResumableLocation() {
    if (state.sessions && state.sessions.lastLocation) {
      const loc = state.sessions.lastLocation;
      if (UNIT_BY_ID.has(Number(loc.unitId))) {
        return {
          unitId: Number(loc.unitId),
          mode: loc.mode === "single" ? "single" : "batch",
          batchSetIndex: typeof loc.batchSetIndex === "number" ? loc.batchSetIndex : 0,
        };
      }
    }
    // Fallback: scan batch and single sessions for any paused / in-progress session
    let bestCand = null;
    let bestTime = "";
    Object.entries((state.sessions && state.sessions.batchByUnitSet) || {}).forEach(([k, s]) => {
      if (!s || s.submitted) return;
      const ansCount = Object.keys(s.answers || {}).length;
      if (ansCount > 0 || (s.elapsedSec || 0) > 0) {
        const m = k.match(/^(\d+):(-?\d+)$/);
        if (m && UNIT_BY_ID.has(Number(m[1]))) {
          const t = String(s.updatedAt || "");
          if (!bestCand || t >= bestTime) {
            bestTime = t;
            bestCand = {
              unitId: Number(m[1]),
              mode: "batch",
              batchSetIndex: Number(m[2]),
            };
          }
        }
      }
    });
    Object.entries((state.sessions && state.sessions.singleByUnit) || {}).forEach(([k, s]) => {
      if (!s) return;
      const ansCount = Object.keys(s.answers || {}).length;
      const uId = Number(k);
      if (UNIT_BY_ID.has(uId) && (ansCount > 0 || (s.elapsedSec || 0) > 0)) {
        const t = String(s.updatedAt || "");
        if (!bestCand || t >= bestTime) {
          bestTime = t;
          bestCand = {
            unitId: uId,
            mode: "single",
            batchSetIndex: 0,
          };
        }
      }
    });
    return bestCand;
  }

  function applyInitialRouteAndResume() {
    const params = new URLSearchParams(window.location.search);
    const paramUnit = params.get("unit") ? Number(params.get("unit")) : null;
    const paramMode = params.get("mode");
    const paramSet = params.get("set") !== null && params.get("set") !== "" ? Number(params.get("set")) : null;
    const paramAction = params.get("action");

    if (paramUnit && UNIT_BY_ID.has(paramUnit)) {
      state.unitId = paramUnit;
      state.mode = paramMode === "batch" ? "batch" : "single";
      if (typeof paramSet === "number" && !Number.isNaN(paramSet)) {
        state.batchSetIndex = paramSet;
      }
      // Clean URL query params so refreshing doesn't re-trigger destructive actions
      history.replaceState(null, "", `${window.location.pathname}#/unit/${state.unitId}`);

      if (paramAction === "retake") {
        retakeUnitInMode(state.unitId, state.mode, paramSet);
        return;
      }
      if (paramAction === "resume") {
        saveSessions(false);
        renderAll();
        return;
      }
      saveSessions(false);
      renderAll();
      return;
    }

    const explicitHashUnit = parseHashRoute();
    const savedLoc = findMostRecentResumableLocation();

    state.mode = "single";
    if (explicitHashUnit) {
      state.unitId = explicitHashUnit;
      if (savedLoc && savedLoc.unitId === explicitHashUnit) {
        state.batchSetIndex = savedLoc.batchSetIndex;
      }
    } else if (savedLoc) {
      state.unitId = savedLoc.unitId;
      state.batchSetIndex = savedLoc.batchSetIndex;
      history.replaceState(null, "", `#/unit/${state.unitId}`);
    } else {
      state.unitId = 1;
    }

    renderAll();
  }

  window.addEventListener("hashchange", () => {
    const targetUnit = parseHashRoute();
    if (targetUnit && targetUnit !== state.unitId) {
      selectUnit(targetUnit, true);
    }
  });

  // Sidebar AP Chemistry Units Submenu Click Handler
  const quizUnitSidebarEl = document.getElementById("quiz-unit-sidebar");
  if (quizUnitSidebarEl) {
    quizUnitSidebarEl.addEventListener("click", (e) => {
      const unitBtn = e.target.closest("[data-unit]");
      if (!unitBtn) return;
      const targetUnit = Number(unitBtn.getAttribute("data-unit"));
      if (UNIT_BY_ID.has(targetUnit)) {
        e.preventDefault();
        if (window.location.hash !== `#/unit/${targetUnit}`) {
          history.pushState(null, "", `#/unit/${targetUnit}`);
        }
        selectUnit(targetUnit, true);
      }
    });
  }

  // Timed Mode / Instant Feedback Mode Toggle Buttons
  const btnToggleTimedMode = document.getElementById("btn-toggle-timed-mode");
  if (btnToggleTimedMode) {
    btnToggleTimedMode.addEventListener("click", () => {
      pauseAllRunningSessions(false);
      state.mode = state.mode === "single" ? "batch" : "single";
      saveSessions();
      renderAll();
    });
  }

  const btnRevertInstantMode = document.getElementById("btn-revert-instant-mode");
  if (btnRevertInstantMode) {
    btnRevertInstantMode.addEventListener("click", () => {
      if (state.mode !== "single") {
        pauseAllRunningSessions(false);
        state.mode = "single";
        saveSessions();
        renderAll();
      }
    });
  }

  // Mode Switch Buttons (legacy fallback if present)
  document.querySelectorAll(".mode-switch-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const newMode = btn.getAttribute("data-mode");
      if (newMode && newMode !== state.mode) {
        pauseAllRunningSessions(false);
        state.mode = newMode;
        saveSessions();
        renderAll();
      }
    });
  });

  // Timer Start / Pause / Resume Buttons in Mode 1 & Mode 2 Toolbars
  ["btn-batch-timer-start", "btn-batch-timer-resume", "btn-single-timer-start", "btn-single-timer-resume"].forEach(
    (id) => {
      const btn = document.getElementById(id);
      if (btn) {
        btn.addEventListener("click", () => {
          startOrResumeActiveTimer();
        });
      }
    }
  );

  ["btn-batch-timer-pause", "btn-single-timer-pause"].forEach((id) => {
    const btn = document.getElementById(id);
    if (btn) {
      btn.addEventListener("click", () => {
        pauseActiveTimer();
      });
    }
  });

  // Timer Gate Banner Delegated Click
  const timerGateEl = document.getElementById("quiz-timer-gate-banner");
  if (timerGateEl) {
    timerGateEl.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-gate-action]");
      if (!btn) return;
      const action = btn.getAttribute("data-gate-action");
      if (action === "start" || action === "resume") {
        startOrResumeActiveTimer();
      } else if (action === "pause") {
        pauseActiveTimer();
      } else if (action === "retake") {
        if (state.mode === "batch") {
          retakeCurrentBatchSet();
        } else {
          retakeUnitInMode(state.unitId, "single");
        }
      }
    });
  }

  // AP Reference Sheet Drawer Toggle
  const btnToggleRef = document.getElementById("btn-toggle-ref");
  const btnCloseRef = document.getElementById("btn-close-ref");
  const refDrawer = document.getElementById("ap-ref-drawer");
  if (btnToggleRef && refDrawer) {
    btnToggleRef.addEventListener("click", () => {
      const isHidden = refDrawer.hidden;
      refDrawer.hidden = !isHidden;
      btnToggleRef.setAttribute("aria-expanded", String(isHidden));
      if (isHidden) {
        renderMathInContainer(refDrawer);
      }
    });
  }
  if (btnCloseRef && refDrawer && btnToggleRef) {
    btnCloseRef.addEventListener("click", () => {
      refDrawer.hidden = true;
      btnToggleRef.setAttribute("aria-expanded", "false");
    });
  }

  // Filters: Topic, Difficulty, Search
  const topicSelect = document.getElementById("quiz-topic-select");
  if (topicSelect) {
    topicSelect.addEventListener("change", () => {
      pauseAllRunningSessions(false);
      state.topicFilter = topicSelect.value;
      state.batchSetIndex = 0;
      getSingleSession().singleIndex = 0;
      saveSessions(false);
      renderAll();
    });
  }

  const diffSelect = document.getElementById("quiz-difficulty-select");
  if (diffSelect) {
    diffSelect.addEventListener("change", () => {
      pauseAllRunningSessions(false);
      state.difficultyFilter = diffSelect.value;
      state.batchSetIndex = 0;
      getSingleSession().singleIndex = 0;
      saveSessions(false);
      renderAll();
    });
  }

  const searchInput = document.getElementById("quiz-search-input");
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      pauseAllRunningSessions(false);
      state.searchQuery = searchInput.value;
      state.batchSetIndex = 0;
      getSingleSession().singleIndex = 0;
      saveSessions(false);
      renderAll();
    });
  }

  // Mode 1 Controls (Set pills, Random 10, Retake Set, Retake Unit, Submit)
  const batchPillsEl = document.getElementById("batch-set-pills");
  if (batchPillsEl) {
    batchPillsEl.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-set-idx]");
      if (!btn) return;
      const idx = Number(btn.getAttribute("data-set-idx"));
      if (idx !== state.batchSetIndex) {
        pauseAllRunningSessions(false);
        state.batchSetIndex = idx;
        saveSessions();
        renderBatchMode();
      }
    });
  }

  const btnRandomBatch = document.getElementById("btn-random-batch");
  if (btnRandomBatch) {
    btnRandomBatch.addEventListener("click", drawRandomBatchSet);
  }

  const btnRetakeUnitBatch = document.getElementById("btn-retake-unit-batch");
  if (btnRetakeUnitBatch) {
    btnRetakeUnitBatch.addEventListener("click", () => {
      retakeUnitInMode(state.unitId, "batch");
    });
  }

  const btnClearBatch = document.getElementById("btn-clear-batch");
  if (btnClearBatch) btnClearBatch.addEventListener("click", retakeCurrentBatchSet);

  const btnBottomClear = document.getElementById("btn-bottom-clear");
  if (btnBottomClear) btnBottomClear.addEventListener("click", retakeCurrentBatchSet);

  const btnSubmitBatch = document.getElementById("btn-submit-batch");
  if (btnSubmitBatch) btnSubmitBatch.addEventListener("click", submitCurrentBatchSet);

  const btnBottomSubmit = document.getElementById("btn-bottom-submit");
  if (btnBottomSubmit) btnBottomSubmit.addEventListener("click", submitCurrentBatchSet);

  // Quick-jump dots in Mode 1
  const batchDotsEl = document.getElementById("batch-q-dots");
  if (batchDotsEl) {
    batchDotsEl.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-jump-card]");
      if (!btn) return;
      const cardId = btn.getAttribute("data-jump-card");
      const targetCard = document.getElementById(cardId);
      if (targetCard) {
        targetCard.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    });
  }

  // Score Banner Action Buttons (Retake Set, Next Set)
  const scoreBannerEl = document.getElementById("batch-score-banner");
  if (scoreBannerEl) {
    scoreBannerEl.addEventListener("click", (e) => {
      if (e.target.closest("#btn-banner-retry")) {
        retakeCurrentBatchSet();
      } else if (e.target.closest("#btn-banner-next-set")) {
        pauseAllRunningSessions(false);
        state.batchSetIndex += 1;
        saveSessions();
        renderBatchMode();
        window.scrollTo({ top: 0, behavior: "smooth" });
      }
    });
  }

  // Mode 2 Controls (Prev, Next, Jump Select, Random, Save Attempt, Retake Unit, Q-Grid)
  const btnSinglePrev = document.getElementById("btn-single-prev");
  if (btnSinglePrev) {
    btnSinglePrev.addEventListener("click", () => {
      const sSess = getSingleSession();
      if (sSess.singleIndex > 0) {
        sSess.singleIndex -= 1;
        saveSessions();
        renderSingleMode();
      }
    });
  }

  const btnSingleNext = document.getElementById("btn-single-next");
  if (btnSingleNext) {
    btnSingleNext.addEventListener("click", () => {
      const filtered = getFilteredQuestions();
      const sSess = getSingleSession();
      if (sSess.singleIndex < filtered.length - 1) {
        sSess.singleIndex += 1;
        saveSessions();
        renderSingleMode();
      }
    });
  }

  const singleJumpSelect = document.getElementById("single-jump-select");
  if (singleJumpSelect) {
    singleJumpSelect.addEventListener("change", () => {
      const sSess = getSingleSession();
      sSess.singleIndex = Number(singleJumpSelect.value) || 0;
      saveSessions();
      renderSingleMode();
    });
  }

  const btnSingleRandom = document.getElementById("btn-single-random");
  if (btnSingleRandom) {
    btnSingleRandom.addEventListener("click", () => {
      const filtered = getFilteredQuestions();
      if (filtered.length <= 1) return;
      const sSess = getSingleSession();
      let nextIdx = sSess.singleIndex;
      while (nextIdx === sSess.singleIndex) {
        nextIdx = Math.floor(Math.random() * filtered.length);
      }
      sSess.singleIndex = nextIdx;
      saveSessions();
      renderSingleMode();
    });
  }

  const btnSaveSingleAttempt = document.getElementById("btn-save-single-attempt");
  if (btnSaveSingleAttempt) {
    btnSaveSingleAttempt.addEventListener("click", () => {
      const att = logSingleUnitAttemptIfNeeded(state.unitId, true);
      if (att) {
        updateMasteryUI();
        renderUnitAttemptStrip();
      }
    });
  }

  const btnRetakeUnitSingle = document.getElementById("btn-retake-unit-single");
  if (btnRetakeUnitSingle) {
    btnRetakeUnitSingle.addEventListener("click", () => {
      retakeUnitInMode(state.unitId, "single");
    });
  }

  const btnToggleQGrid = document.getElementById("btn-toggle-qgrid");
  if (btnToggleQGrid) {
    btnToggleQGrid.addEventListener("click", () => {
      state.showQGrid = !state.showQGrid;
      btnToggleQGrid.setAttribute("aria-expanded", String(state.showQGrid));
      const qgridEl = document.getElementById("single-qgrid");
      if (qgridEl) qgridEl.hidden = !state.showQGrid;
    });
  }

  const singleQGridEl = document.getElementById("single-qgrid");
  if (singleQGridEl) {
    singleQGridEl.addEventListener("click", (e) => {
      const btn = e.target.closest("[data-single-idx]");
      if (!btn) return;
      const sSess = getSingleSession();
      sSess.singleIndex = Number(btn.getAttribute("data-single-idx")) || 0;
      saveSessions();
      renderSingleMode();
    });
  }

  function highlightTimerGateBanner() {
    const gateEl = document.getElementById("quiz-timer-gate-banner");
    if (!gateEl) return;
    gateEl.scrollIntoView({ behavior: "smooth", block: "center" });
    gateEl.classList.remove("is-pulsing");
    void gateEl.offsetWidth;
    gateEl.classList.add("is-pulsing");
    const primaryBtn = gateEl.querySelector("[data-gate-action='start'], [data-gate-action='resume']");
    if (primaryBtn) primaryBtn.focus({ preventScroll: true });
  }

  // Question Stage Delegated Click Handler (Selecting Options in Mode 1 & Mode 2)
  const stageEl = document.getElementById("quiz-questions-stage");
  if (stageEl) {
    stageEl.addEventListener("click", (e) => {
      if (e.target.closest("[data-card-timer-start]")) {
        startOrResumeActiveTimer();
        return;
      }

      const optBtn = e.target.closest(".q-option-btn");
      if (optBtn && !optBtn.disabled) {
        if (optBtn.getAttribute("data-timer-locked") === "1") {
          highlightTimerGateBanner();
          return;
        }

        const qId = Number(optBtn.getAttribute("data-q-id"));
        const optIdx = Number(optBtn.getAttribute("data-opt-idx"));

        if (state.mode === "batch") {
          const bSess = getBatchSession();
          if (bSess.submitted) return;
          bSess.answers[qId] = optIdx;
          bSess.updatedAt = new Date().toISOString();
          saveSessions();
          renderBatchMode();
        } else {
          // Mode 2: Immediately evaluate, show Correct/Incorrect status and detailed explanation
          const sSess = getSingleSession();
          sSess.answers[qId] = optIdx;
          sSess.updatedAt = new Date().toISOString();
          const qObj = Q_BY_ID.get(qId);
          if (qObj) {
            state.history[qId] = {
              selected: optIdx,
              correct: optIdx === qObj.correct_index,
            };
            saveHistory(state.history);
          }

          // Auto-record attempt if all questions in the unit have now been answered in Mode 2
          const unitQs = getQuestionsForUnit(state.unitId);
          const answeredCount = unitQs.filter((q) => typeof sSess.answers[q.id] === "number").length;
          if (unitQs.length > 0 && answeredCount === unitQs.length) {
            sSess.timerState = "completed";
            logSingleUnitAttemptIfNeeded(state.unitId, false);
          }

          saveSessions();
          updateMasteryUI();
          renderUnitAttemptStrip();
          renderSingleMode();
        }
        return;
      }

      // Mode 2: "Redo This Question" button
      const retryBtn = e.target.closest("[data-retry-single]");
      if (retryBtn) {
        const qId = Number(retryBtn.getAttribute("data-retry-single"));
        const sSess = getSingleSession();
        delete sSess.answers[qId];
        sSess.updatedAt = new Date().toISOString();
        saveSessions();
        renderSingleMode();
        return;
      }

      // Mode 2: Card footer Prev / Next buttons
      if (e.target.closest("#btn-card-prev")) {
        const sSess = getSingleSession();
        if (sSess.singleIndex > 0) {
          sSess.singleIndex -= 1;
          saveSessions();
          renderSingleMode();
        }
      } else if (e.target.closest("#btn-card-next")) {
        const filtered = getFilteredQuestions();
        const sSess = getSingleSession();
        if (sSess.singleIndex < filtered.length - 1) {
          sSess.singleIndex += 1;
          saveSessions();
          renderSingleMode();
        }
      }
    });
  }

  // Listen for user login / profile switch / Cloud Storage sync events
  window.addEventListener("inorganic-user-synced", (e) => {
    const detail = (e && e.detail) || {};
    if (detail.silentQuizReload) {
      updateMasteryUI();
      renderUnitAttemptStrip();
      return;
    }
    state.history = loadHistory();
    state.attempts = loadAttempts();
    state.sessions = loadSessions();
    applyInitialRouteAndResume();
  });

  // Initial Boot
  applyInitialRouteAndResume();

  // Re-run KaTeX once deferred CDN scripts finish loading
  window.addEventListener("load", () => {
    renderMathInContainer(document.body);
  });
})();
