/**
 * AP Chemistry Dedicated Performance & Analytics Dashboard (dashboard_app.js)
 * ---------------------------------------------------------------------------
 * Renders interactive SVG charts, graphs, and structured analytics tables:
 *   1. 5 KPI Summary Cards (Attempts, Accuracy & AP Band, Bank Coverage, Time/Pace, Paused Sessions)
 *   2. Active & Paused Sessions Table ("Resume Where You Left Off")
 *   3. SVG Line & Area Chart: Accuracy & AP Score Progression Over Attempts
 *   4. SVG Donut Chart + Breakdown Table: 570-Question Bank Mastery Distribution
 *   5. SVG Grouped Bar Chart: Unit 1–9 Mode 1 Best vs. Mode 2 Best vs. Bank Mastery
 *   6. SVG Horizontal Bar Chart: Average Time Pace (s/Q) by Unit vs. 90s AP Target
 *   7. Structured Table: Complete Units 1–9 & Mode Analytics Summary Table
 *   8. Structured Table: Chronological Attempt History Log
 */

(function () {
  "use strict";

  const payloadEl = document.getElementById("quiz-payload");
  if (!payloadEl) return;

  let PAYLOAD;
  try {
    PAYLOAD = JSON.parse(payloadEl.textContent);
  } catch (err) {
    console.error("Failed to parse dashboard quiz payload:", err);
    return;
  }

  const UNITS = PAYLOAD.units || [];
  const ALL_QUESTIONS = PAYLOAD.questions || [];
  const UNIT_BY_ID = new Map(UNITS.map((u) => [u.id, u]));
  const Q_BY_UID = new Map(ALL_QUESTIONS.map((q) => [q.uid, q]));

  const BASE_HISTORY_KEY = "inorganic_chem_ap_quiz_v2";
  const BASE_ATTEMPTS_KEY = "inorganic_chem_ap_quiz_attempts_v1";
  const BASE_SESSIONS_KEY = "inorganic_chem_ap_quiz_sessions_v1";

  function activeHistoryKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getHistoryStorageKey === "function") {
      return window.InorganicUserSync.getHistoryStorageKey();
    }
    return BASE_HISTORY_KEY;
  }

  function activeAttemptsKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getAttemptsStorageKey === "function") {
      return window.InorganicUserSync.getAttemptsStorageKey();
    }
    return BASE_ATTEMPTS_KEY;
  }

  function activeSessionsKey() {
    if (window.InorganicUserSync && typeof window.InorganicUserSync.getSessionsStorageKey === "function") {
      return window.InorganicUserSync.getSessionsStorageKey();
    }
    return BASE_SESSIONS_KEY;
  }

  function escapeHtml(str) {
    return String(str ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatMMSS(totalSec) {
    const sec = Math.max(0, Math.floor(Number(totalSec) || 0));
    const hrs = Math.floor(sec / 3600);
    const mins = Math.floor((sec % 3600) / 60);
    const rem = sec % 60;
    if (hrs > 0) {
      return `${hrs}:${mins < 10 ? "0" : ""}${mins}:${rem < 10 ? "0" : ""}${rem}`;
    }
    return `${mins < 10 ? "0" : ""}${mins}:${rem < 10 ? "0" : ""}${rem}`;
  }

  function formatDurationHuman(totalSec) {
    const sec = Math.max(0, Math.floor(Number(totalSec) || 0));
    if (sec === 0) return "0s";
    const hrs = Math.floor(sec / 3600);
    const mins = Math.floor((sec % 3600) / 60);
    const rem = sec % 60;
    if (hrs > 0) return `${hrs}h ${mins}m`;
    if (mins > 0) return `${mins}m ${rem}s`;
    return `${rem}s`;
  }

  function formatDateTime(isoString) {
    if (!isoString) return "—";
    try {
      const d = new Date(isoString);
      if (Number.isNaN(d.getTime())) return String(isoString);
      return d.toLocaleString(undefined, {
        month: "short",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
      });
    } catch (_e) {
      return String(isoString);
    }
  }

  function deserializeAnswersMap(rawByUid) {
    const out = {};
    if (!rawByUid || typeof rawByUid !== "object") return out;
    Object.keys(rawByUid).forEach((uid) => {
      const entry = rawByUid[uid];
      const q = Q_BY_UID.get(uid);
      if (q && entry && typeof entry.selected === "number" && entry.rev === q.rev) {
        out[q.id] = entry.selected;
      } else if (typeof entry === "number") {
        const qNum = Number(uid);
        if (!Number.isNaN(qNum)) out[qNum] = entry;
      }
    });
    return out;
  }

  function loadHistory() {
    try {
      const raw = localStorage.getItem(activeHistoryKey());
      if (!raw) return {};
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return {};
      const hist = {};
      Object.keys(parsed).forEach((uid) => {
        const entry = parsed[uid];
        const q = Q_BY_UID.get(uid);
        if (q && entry && typeof entry.selected === "number" && entry.rev === q.rev) {
          hist[q.id] = { selected: entry.selected, correct: entry.selected === q.correct_index };
        }
      });
      return hist;
    } catch (_e) {
      return {};
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
    } catch (_e) {
      return [];
    }
  }

  function loadSessions() {
    const empty = { batch: {}, single: {}, lastLocation: null };
    try {
      const raw = localStorage.getItem(activeSessionsKey());
      if (!raw) return empty;
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return empty;

      const batch = {};
      const rawBatch = parsed.batchByUnitSet || parsed.batch || {};
      Object.keys(rawBatch).forEach((key) => {
        const item = rawBatch[key];
        if (!item || typeof item !== "object") return;
        let customQuestions = null;
        if (Array.isArray(item.customUids)) {
          const resolved = item.customUids.map((uid) => Q_BY_UID.get(uid)).filter(Boolean);
          if (resolved.length > 0) customQuestions = resolved;
        }
        batch[key] = {
          answers: deserializeAnswersMap(item.answers),
          submitted: Boolean(item.submitted),
          elapsedSec: Math.max(0, Number(item.elapsedSec) || 0),
          timerState: item.timerState || "paused",
          updatedAt: item.updatedAt || "",
          customQuestions,
        };
      });

      const single = {};
      const rawSingle = parsed.singleByUnit || parsed.single || {};
      Object.keys(rawSingle).forEach((uKey) => {
        const item = rawSingle[uKey];
        if (!item || typeof item !== "object") return;
        single[uKey] = {
          answers: deserializeAnswersMap(item.answers),
          elapsedSec: Math.max(0, Number(item.elapsedSec) || 0),
          timerState: item.timerState || "paused",
          updatedAt: item.updatedAt || "",
          singleIndex: Math.max(0, Number(item.singleIndex) || 0),
        };
      });

      return {
        batch,
        single,
        lastLocation:
          parsed.lastLocation && typeof parsed.lastLocation === "object" ? parsed.lastLocation : null,
      };
    } catch (_e) {
      return empty;
    }
  }

  function getQuestionsForUnit(unitId) {
    return ALL_QUESTIONS.filter((q) => q.unit_id === unitId);
  }

  function getBatchSetsForUnit(unitId) {
    const unitQs = getQuestionsForUnit(unitId);
    const sets = [];
    for (let i = 0; i < unitQs.length; i += 10) {
      sets.push(unitQs.slice(i, i + 10));
    }
    return sets;
  }

  const state = {
    unitFilter: "all",
    modeFilter: "all",
    history: loadHistory(),
    attempts: loadAttempts(),
    sessions: loadSessions(),
  };

  function getFilteredAttempts() {
    return state.attempts.filter((a) => {
      if (state.unitFilter !== "all" && a.unitId !== Number(state.unitFilter)) return false;
      if (state.modeFilter !== "all" && a.mode !== state.modeFilter) return false;
      return true;
    });
  }

  function getApBandInfo(pct, hasData = true) {
    if (!hasData) {
      return { band: "—", label: "No Attempts Yet", cls: "badge-neutral" };
    }
    if (pct >= 75) {
      return { band: "AP 5", label: "AP 5 · Extremely Well Qualified", cls: "badge-high" };
    }
    if (pct >= 60) {
      return { band: "AP 4", label: "AP 4 · Well Qualified", cls: "badge-high" };
    }
    if (pct >= 45) {
      return { band: "AP 3", label: "AP 3 · Qualified", cls: "badge-mid" };
    }
    return { band: "AP 1–2", label: "Developing (<45%)", cls: "badge-low" };
  }

  // =========================================================================
  // Collect Active / Paused Resumable Sessions
  // =========================================================================

  function collectPausedSessions() {
    const items = [];
    const lastLoc = state.sessions.lastLocation;

    // 1. Scan Mode 1 (Batch) sessions
    Object.entries(state.sessions.batch || {}).forEach(([key, sess]) => {
      if (!sess || sess.submitted) return;
      const m = key.match(/^(\d+):(-?\d+)$/);
      if (!m) return;
      const unitId = Number(m[1]);
      const setIdx = Number(m[2]);
      const unit = UNIT_BY_ID.get(unitId);
      if (!unit) return;

      const sets = getBatchSetsForUnit(unitId);
      const setQs =
        setIdx === -1
          ? Array.isArray(sess.customQuestions)
            ? sess.customQuestions
            : []
          : sets[setIdx] || [];
      const totalQs = setQs.length || 10;
      const answeredCount =
        setQs.length > 0
          ? setQs.filter((q) => typeof (sess.answers || {})[q.id] === "number").length
          : Object.keys(sess.answers || {}).length;
      const elapsedSec = Math.max(0, Math.floor(Number(sess.elapsedSec) || 0));

      if (answeredCount > 0 || elapsedSec > 0) {
        const isLastActive =
          lastLoc &&
          lastLoc.mode === "batch" &&
          Number(lastLoc.unitId) === unitId &&
          Number(lastLoc.batchSetIndex) === setIdx;

        const scopeLabel =
          setIdx === -1
            ? "Random 10-Question Set"
            : setQs.length > 0
            ? `Set ${setIdx + 1} (Q${setQs[0].unit_q_num}–Q${setQs[setQs.length - 1].unit_q_num})`
            : `Set ${setIdx + 1}`;

        items.push({
          unitId,
          unitTitle: unit.title,
          mode: "batch",
          modeLabel: "Mode 1 · 10-Q Set",
          setIdx,
          scopeLabel,
          answeredCount,
          totalQs,
          elapsedSec,
          updatedAt: sess.updatedAt || "",
          isLastActive: Boolean(isLastActive),
          resumeUrl: `/quiz?unit=${unitId}&mode=batch&set=${setIdx}&action=resume`,
          retakeUrl: `/quiz?unit=${unitId}&mode=batch&set=${setIdx}&action=retake`,
        });
      }
    });

    // 2. Scan Mode 2 (Single) sessions
    Object.entries(state.sessions.single || {}).forEach(([key, sess]) => {
      if (!sess) return;
      const unitId = Number(key);
      const unit = UNIT_BY_ID.get(unitId);
      if (!unit) return;

      const unitQs = getQuestionsForUnit(unitId);
      const answeredCount = unitQs.filter((q) => typeof (sess.answers || {})[q.id] === "number").length;
      const elapsedSec = Math.max(0, Math.floor(Number(sess.elapsedSec) || 0));
      const singleIdx = Math.max(0, Number(sess.singleIndex) || 0);

      if ((answeredCount > 0 && answeredCount < unitQs.length) || elapsedSec > 0) {
        const isLastActive =
          lastLoc && lastLoc.mode === "single" && Number(lastLoc.unitId) === unitId;

        items.push({
          unitId,
          unitTitle: unit.title,
          mode: "single",
          modeLabel: "Mode 2 · 1-by-1",
          setIdx: null,
          scopeLabel: `Currently on Question #${Math.min(singleIdx + 1, unitQs.length)} of ${unitQs.length}`,
          answeredCount,
          totalQs: unitQs.length,
          elapsedSec,
          updatedAt: sess.updatedAt || "",
          isLastActive: Boolean(isLastActive),
          resumeUrl: `/quiz?unit=${unitId}&mode=single&action=resume`,
          retakeUrl: `/quiz?unit=${unitId}&mode=single&action=retake`,
        });
      }
    });

    items.sort((a, b) => {
      if (a.isLastActive !== b.isLastActive) return a.isLastActive ? -1 : 1;
      return String(b.updatedAt).localeCompare(String(a.updatedAt));
    });

    return items;
  }

  // =========================================================================
  // 1. Update User Header & Top Resume CTA
  // =========================================================================

  function renderHeaderStatus(pausedSessions) {
    const eyebrowEl = document.getElementById("dash-user-eyebrow");
    if (eyebrowEl && window.InorganicUserSync) {
      const uName = window.InorganicUserSync.getDisplayName();
      const sStat = window.InorganicUserSync.getSyncStatus();
      const syncTag =
        sStat && sStat.state === "synced"
          ? `SYNCED TO CLOUD STORAGE (${sStat.bucket || "haren-agent-storage"})`
          : sStat && sStat.state === "syncing"
          ? "SYNCING WITH HAREN-AGENT-STORAGE…"
          : "SAVED IN LOCAL & SERVER STORAGE • HAREN-AGENT-STORAGE";
      eyebrowEl.textContent = `STUDENT: ${uName.toUpperCase()} • ${syncTag}`;
    }

    const resumeBtn = document.getElementById("btn-dash-resume-primary");
    if (!resumeBtn) return;
    if (pausedSessions.length > 0) {
      const topSess = pausedSessions[0];
      resumeBtn.href = topSess.resumeUrl;
      resumeBtn.textContent = `▶ Resume Unit ${topSess.unitId} (${formatMMSS(topSess.elapsedSec)})`;
    } else if (state.sessions.lastLocation && UNIT_BY_ID.has(Number(state.sessions.lastLocation.unitId))) {
      const loc = state.sessions.lastLocation;
      resumeBtn.href = `/quiz?unit=${loc.unitId}&mode=${loc.mode || "batch"}&set=${loc.batchSetIndex ?? 0}&action=resume`;
      resumeBtn.textContent = `▶ Continue Unit ${loc.unitId} Quiz`;
    } else {
      resumeBtn.href = "/quiz";
      resumeBtn.textContent = "▶ Go to AP Practice Quiz";
    }
  }

  // =========================================================================
  // 2. Render 5 KPI Summary Cards
  // =========================================================================

  function renderKpiCards(pausedSessions) {
    const kpiGridEl = document.getElementById("dash-kpi-grid");
    if (!kpiGridEl) return;

    const filteredAttempts = getFilteredAttempts();
    const totalAttempts = filteredAttempts.length;
    const batchCount = filteredAttempts.filter((a) => a.mode === "batch").length;
    const singleCount = filteredAttempts.filter((a) => a.mode === "single").length;

    const totalCorrect = filteredAttempts.reduce((s, a) => s + (a.correct || 0), 0);
    const totalDenom = filteredAttempts.reduce(
      (s, a) => s + (a.mode === "batch" ? a.total || 0 : a.answered || 0),
      0
    );
    const overallPct = totalDenom > 0 ? Math.round((totalCorrect / totalDenom) * 100) : 0;
    const apInfo = getApBandInfo(overallPct, totalDenom > 0);

    // Bank coverage (filtered by unit if unit filter is active)
    const poolQs =
      state.unitFilter === "all"
        ? ALL_QUESTIONS
        : getQuestionsForUnit(Number(state.unitFilter));
    let bankAnswered = 0;
    let bankCorrect = 0;
    poolQs.forEach((q) => {
      const h = state.history[q.id];
      if (h) {
        bankAnswered += 1;
        if (h.correct) bankCorrect += 1;
      }
    });
    const bankCoveragePct = poolQs.length > 0 ? Math.round((bankAnswered / poolQs.length) * 100) : 0;

    const totalDurationSec = filteredAttempts.reduce((s, a) => s + (a.durationSec || 0), 0);
    const pausedSec = pausedSessions.reduce((s, p) => s + (p.elapsedSec || 0), 0);
    const avgSecPerQ = totalDenom > 0 ? Math.round(totalDurationSec / totalDenom) : 0;

    kpiGridEl.innerHTML = `
      <div class="dash-kpi-card">
        <span class="dash-kpi-label">Saved Quiz Attempts</span>
        <strong class="dash-kpi-val">${totalAttempts}</strong>
        <span class="dash-kpi-sub">${batchCount} Mode 1 (10-Q Sets) • ${singleCount} Mode 2 (1-by-1)</span>
      </div>
      <div class="dash-kpi-card">
        <span class="dash-kpi-label">Cumulative Accuracy</span>
        <strong class="dash-kpi-val">${totalDenom > 0 ? `${overallPct}%` : "—"}</strong>
        <span class="dash-kpi-sub">${totalCorrect}/${totalDenom} Correct • <strong>${escapeHtml(apInfo.label)}</strong></span>
      </div>
      <div class="dash-kpi-card">
        <span class="dash-kpi-label">Question Bank Mastery</span>
        <strong class="dash-kpi-val">${bankAnswered} / ${poolQs.length}</strong>
        <span class="dash-kpi-sub">${bankCoveragePct}% of bank answered (${bankCorrect} mastered ✓)</span>
      </div>
      <div class="dash-kpi-card">
        <span class="dash-kpi-label">Active Study Time &amp; Pace</span>
        <strong class="dash-kpi-val">${formatDurationHuman(totalDurationSec + pausedSec)}</strong>
        <span class="dash-kpi-sub">${
          totalDenom > 0
            ? `Avg Pace: ${avgSecPerQ}s / Q (AP Target ≤ 90s)`
            : pausedSec > 0
            ? `${formatDurationHuman(pausedSec)} in paused sessions`
            : "Manual Start/Pause timer tracking"
        }</span>
      </div>
      <div class="dash-kpi-card">
        <span class="dash-kpi-label">Paused / Resumable Sessions</span>
        <strong class="dash-kpi-val">${pausedSessions.length}</strong>
        <span class="dash-kpi-sub">${
          pausedSessions.length > 0
            ? `Last active: U${pausedSessions[0].unitId} (${formatMMSS(pausedSessions[0].elapsedSec)})`
            : "All started sets are completed"
        }</span>
      </div>
    `;
  }

  // =========================================================================
  // 3. Render Active & Paused Sessions Table ("Resume Where You Left Off")
  // =========================================================================

  function renderPausedSessionsTable(pausedSessions) {
    const wrapEl = document.getElementById("dash-paused-table-wrap");
    const metaEl = document.getElementById("dash-paused-meta");
    if (!wrapEl) return;

    if (metaEl) {
      metaEl.textContent =
        pausedSessions.length > 0
          ? `${pausedSessions.length} paused session${pausedSessions.length === 1 ? "" : "s"} ready to resume`
          : "No paused sessions currently in progress";
    }

    if (pausedSessions.length === 0) {
      wrapEl.innerHTML = `
        <div class="dash-empty-state">
          <strong>No paused quiz sessions right now.</strong> Whenever you start a quiz timer and pause or leave the page, your exact question progress and elapsed time appear here so you can resume with one click.
        </div>
      `;
      return;
    }

    const rowsHtml = pausedSessions
      .map((item) => {
        const pctDone = item.totalQs > 0 ? Math.round((item.answeredCount / item.totalQs) * 100) : 0;
        return `
          <tr class="${item.isLastActive ? "is-highlighted-row" : ""}">
            <td>
              <span class="unit-tag-badge">U${item.unitId}</span>
              <strong>${escapeHtml(item.unitTitle)}</strong>
            </td>
            <td>
              <strong>${escapeHtml(item.modeLabel)}</strong>
              <div style="font-size: 0.76rem; color: #4b5563;">${escapeHtml(item.scopeLabel)}</div>
            </td>
            <td>
              <strong>${item.answeredCount} / ${item.totalQs} Answered (${pctDone}%)</strong>
              <div class="table-mini-bar-wrap">
                <div class="table-mini-bar-fill" style="width: ${pctDone}%"></div>
              </div>
            </td>
            <td>
              <strong>⏱ ${formatMMSS(item.elapsedSec)}</strong>
            </td>
            <td>
              <span class="status-badge badge-paused">
                ⏸ Paused${item.isLastActive ? " · Last Active" : ""}
              </span>
            </td>
            <td>
              <div class="table-actions-cell">
                <a href="${item.resumeUrl}" class="dash-action-link is-primary">
                  ▶ Resume Quiz (${formatMMSS(item.elapsedSec)})
                </a>
                <a href="${item.retakeUrl}" class="dash-action-link">
                  ↺ Restart Fresh
                </a>
              </div>
            </td>
          </tr>
        `;
      })
      .join("");

    wrapEl.innerHTML = `
      <table class="dash-data-table">
        <thead>
          <tr>
            <th>Unit</th>
            <th>Practice Mode &amp; Scope</th>
            <th>Saved Progress</th>
            <th>Elapsed Time</th>
            <th>Session Status</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  // =========================================================================
  // 4. SVG Chart 1: Accuracy & Score Progression Over Attempts (Line & Area)
  // =========================================================================

  function renderAccuracyTrendChart() {
    const stageEl = document.getElementById("chart-accuracy-trend");
    if (!stageEl) return;

    const attempts = getFilteredAttempts();
    if (attempts.length === 0) {
      stageEl.innerHTML = `
        <div class="dash-empty-state">
          <strong>No attempt data to plot yet.</strong> Complete a 10-question set in Mode 1 or save an attempt in Mode 2 on the <a href="/quiz">AP Practice Quiz</a> page to generate your chronological accuracy trend line and AP score band curve.
        </div>
      `;
      return;
    }

    const recent = attempts.slice(-20);
    const W = 720;
    const H = 260;
    const padL = 46;
    const padR = 24;
    const padT = 22;
    const padB = 42;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const xAt = (idx) => {
      if (recent.length === 1) return padL + plotW / 2;
      return padL + (idx / (recent.length - 1)) * plotW;
    };
    const yAt = (pct) => padT + plotH - (Math.max(0, Math.min(100, pct)) / 100) * plotH;

    // Horizontal grid lines & AP score threshold lines
    const yTicks = [0, 25, 45, 60, 75, 100];
    const gridHtml = yTicks
      .map((val) => {
        const y = yAt(val).toFixed(1);
        const isAp5 = val === 75;
        const isAp4 = val === 60;
        const stroke = isAp5 ? "#10b981" : isAp4 ? "#9ca3af" : "#e5e7eb";
        const dash = isAp5 || isAp4 ? 'stroke-dasharray="4 4"' : "";
        return `
          <line x1="${padL}" y1="${y}" x2="${W - padR}" y2="${y}" stroke="${stroke}" stroke-width="1" ${dash} />
          <text x="${padL - 8}" y="${Number(y) + 4}" text-anchor="end" font-size="11" fill="#6b7280" font-family="Inter, sans-serif">${val}%</text>
        `;
      })
      .join("");

    // Primary line & shaded area
    const pts = recent.map((a, idx) => ({
      x: xAt(idx),
      y: yAt(a.pct),
      attempt: a,
      idx,
    }));

    const linePath = pts
      .map((p, i) => `${i === 0 ? "M" : "L"} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`)
      .join(" ");

    const areaPath =
      pts.length > 1
        ? `${linePath} L ${pts[pts.length - 1].x.toFixed(1)} ${(padT + plotH).toFixed(1)} L ${pts[0].x.toFixed(1)} ${(padT + plotH).toFixed(1)} Z`
        : "";

    // 3-Attempt Rolling Average Line
    const rollingPts = recent.map((_, idx) => {
      const slice = recent.slice(Math.max(0, idx - 2), idx + 1);
      const avg = slice.reduce((s, item) => s + (item.pct || 0), 0) / slice.length;
      return { x: xAt(idx), y: yAt(avg) };
    });
    const rollingPath =
      rollingPts.length > 1
        ? rollingPts
            .map((p, i) => `${i === 0 ? "M" : "L"} ${p.x.toFixed(1)} ${p.y.toFixed(1)}`)
            .join(" ")
        : "";

    // Data point circles & X-axis labels
    const nodesHtml = pts
      .map((p, i) => {
        const a = p.attempt;
        const dotColor = a.pct >= 75 ? "#15803d" : a.pct >= 60 ? "#111827" : "#be123c";
        const showLabel = recent.length <= 12 || i % 2 === 0 || i === recent.length - 1;
        return `
          <g>
            <title>Attempt #${i + 1}: Unit ${a.unitId} (${a.mode === "batch" ? "Mode 1" : "Mode 2"}) — ${a.pct}% (${formatMMSS(a.durationSec)})</title>
            <circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="5" fill="${dotColor}" stroke="#ffffff" stroke-width="2" />
            ${
              showLabel
                ? `<text x="${p.x.toFixed(1)}" y="${(p.y - 9).toFixed(1)}" text-anchor="middle" font-size="10.5" font-weight="700" fill="#111827" font-family="Inter, sans-serif">${a.pct}%</text>
                   <text x="${p.x.toFixed(1)}" y="${H - 14}" text-anchor="middle" font-size="10.5" fill="#4b5563" font-family="Inter, sans-serif">#${i + 1} (U${a.unitId})</text>`
                : ""
            }
          </g>
        `;
      })
      .join("");

    stageEl.innerHTML = `
      <svg class="dash-svg-chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Accuracy progression line chart across attempts">
        <defs>
          <linearGradient id="trendAreaGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#111827" stop-opacity="0.16" />
            <stop offset="100%" stop-color="#111827" stop-opacity="0.01" />
          </linearGradient>
        </defs>
        ${gridHtml}
        ${areaPath ? `<path d="${areaPath}" fill="url(#trendAreaGrad)" />` : ""}
        ${rollingPath ? `<path d="${rollingPath}" fill="none" stroke="#6b7280" stroke-width="2" stroke-dasharray="5 4" />` : ""}
        ${pts.length > 1 ? `<path d="${linePath}" fill="none" stroke="#111827" stroke-width="2.6" />` : ""}
        ${nodesHtml}
      </svg>
    `;
  }

  // =========================================================================
  // 5. SVG Chart 2: 570-Question Bank Mastery Breakdown (Donut + Table)
  // =========================================================================

  function renderBankDonutChart(pausedSessions) {
    const containerEl = document.getElementById("chart-bank-donut");
    const metaEl = document.getElementById("chart-donut-meta");
    if (!containerEl) return;

    const poolQs =
      state.unitFilter === "all"
        ? ALL_QUESTIONS
        : getQuestionsForUnit(Number(state.unitFilter));

    if (metaEl) {
      metaEl.textContent =
        state.unitFilter === "all"
          ? `All 9 Units (${poolQs.length} Qs)`
          : `Unit ${state.unitFilter} (${poolQs.length} Qs)`;
    }

    // Collect in-progress draft question IDs from paused sessions
    const draftQIds = new Set();
    Object.values(state.sessions.batch || {}).forEach((s) => {
      if (s && !s.submitted && s.answers) {
        Object.keys(s.answers).forEach((qid) => draftQIds.add(Number(qid)));
      }
    });
    Object.values(state.sessions.single || {}).forEach((s) => {
      if (s && s.answers) {
        Object.keys(s.answers).forEach((qid) => draftQIds.add(Number(qid)));
      }
    });

    let mastered = 0;
    let incorrect = 0;
    let inProgressOnly = 0;
    let unseen = 0;

    poolQs.forEach((q) => {
      const h = state.history[q.id];
      if (h) {
        if (h.correct) mastered += 1;
        else incorrect += 1;
      } else if (draftQIds.has(q.id)) {
        inProgressOnly += 1;
      } else {
        unseen += 1;
      }
    });

    const total = Math.max(1, poolQs.length);
    const segments = [
      { label: "Mastered (Correct)", count: mastered, color: "#15803d" },
      { label: "Needs Review (Incorrect)", count: incorrect, color: "#be123c" },
      { label: "In-Progress (Paused)", count: inProgressOnly, color: "#f59e0b" },
      { label: "Unseen Questions", count: unseen, color: "#e5e7eb" },
    ];

    const r = 72;
    const cx = 100;
    const cy = 100;
    const circum = 2 * Math.PI * r;
    let offsetAccum = 0;

    const circlesHtml = segments
      .map((seg) => {
        if (seg.count <= 0) return "";
        const frac = seg.count / total;
        const dashLen = frac * circum;
        const dashOffset = -offsetAccum;
        offsetAccum += dashLen;
        return `
          <circle
            cx="${cx}"
            cy="${cy}"
            r="${r}"
            fill="none"
            stroke="${seg.color}"
            stroke-width="24"
            stroke-dasharray="${dashLen.toFixed(2)} ${circum.toFixed(2)}"
            stroke-dashoffset="${dashOffset.toFixed(2)}"
            transform="rotate(-90 ${cx} ${cy})"
          />
        `;
      })
      .join("");

    const answeredTotal = mastered + incorrect;
    const masteryPct = Math.round((mastered / total) * 100);

    const rowsHtml = segments
      .map((seg) => {
        const pct = Math.round((seg.count / total) * 100);
        return `
          <tr>
            <td><span class="donut-dot" style="background:${seg.color}"></span><strong>${escapeHtml(seg.label)}</strong></td>
            <td><strong>${seg.count}</strong> Qs</td>
            <td>${pct}%</td>
          </tr>
        `;
      })
      .join("");

    containerEl.innerHTML = `
      <div class="donut-svg-wrap">
        <svg viewBox="0 0 200 200" class="dash-svg-chart" role="img" aria-label="Question bank mastery donut chart">
          <circle cx="${cx}" cy="${cy}" r="${r}" fill="none" stroke="#f3f4f6" stroke-width="24" />
          ${circlesHtml}
          <text x="${cx}" y="${cy - 4}" text-anchor="middle" font-size="24" font-weight="800" fill="#111827" font-family="Inter, sans-serif">${masteryPct}%</text>
          <text x="${cx}" y="${cy + 16}" text-anchor="middle" font-size="11" font-weight="600" fill="#6b7280" font-family="Inter, sans-serif">${answeredTotal}/${poolQs.length} Answered</text>
        </svg>
      </div>
      <div>
        <table class="donut-breakdown-table">
          <thead>
            <tr>
              <th>Category</th>
              <th>Questions</th>
              <th>Share</th>
            </tr>
          </thead>
          <tbody>
            ${rowsHtml}
          </tbody>
        </table>
      </div>
    `;
  }

  // =========================================================================
  // 6. SVG Chart 3: Unit 1–9 Accuracy & Mastery Grouped Bar Chart
  // =========================================================================

  function renderUnitGroupedBarChart() {
    const stageEl = document.getElementById("chart-unit-bars");
    if (!stageEl) return;

    const W = 740;
    const H = 265;
    const padL = 44;
    const padR = 18;
    const padT = 22;
    const padB = 42;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const yAt = (pct) => padT + plotH - (Math.max(0, Math.min(100, pct)) / 100) * plotH;

    const yTicks = [0, 25, 50, 75, 100];
    const gridHtml = yTicks
      .map((val) => {
        const y = yAt(val).toFixed(1);
        return `
          <line x1="${padL}" y1="${y}" x2="${W - padR}" y2="${y}" stroke="#e5e7eb" stroke-width="1" />
          <text x="${padL - 8}" y="${Number(y) + 4}" text-anchor="end" font-size="11" fill="#6b7280" font-family="Inter, sans-serif">${val}%</text>
        `;
      })
      .join("");

    const groupW = plotW / UNITS.length;
    const barW = Math.min(16, (groupW - 18) / 3);

    const barsHtml = UNITS.map((u, idx) => {
      const uBatch = state.attempts.filter((a) => a.unitId === u.id && a.mode === "batch");
      const uSingle = state.attempts.filter((a) => a.unitId === u.id && a.mode === "single");
      const m1Best = uBatch.length > 0 ? Math.max(...uBatch.map((a) => a.pct)) : 0;
      const m2Best = uSingle.length > 0 ? Math.max(...uSingle.map((a) => a.pct)) : 0;

      const unitQs = getQuestionsForUnit(u.id);
      let correctInBank = 0;
      unitQs.forEach((q) => {
        if (state.history[q.id] && state.history[q.id].correct) correctInBank += 1;
      });
      const bankPct = unitQs.length > 0 ? Math.round((correctInBank / unitQs.length) * 100) : 0;

      const gx = padL + idx * groupW + groupW / 2;
      const x1 = gx - barW * 1.5 - 2;
      const x2 = gx - barW * 0.5;
      const x3 = gx + barW * 0.5 + 2;

      const drawBar = (x, pct, color, label) => {
        const h = Math.max(2, (pct / 100) * plotH);
        const y = padT + plotH - h;
        return `
          <g>
            <title>Unit ${u.id} · ${label}: ${pct}%</title>
            <rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="${barW.toFixed(1)}" height="${h.toFixed(1)}" rx="3" fill="${color}" />
            ${
              pct > 0
                ? `<text x="${(x + barW / 2).toFixed(1)}" y="${(y - 4).toFixed(1)}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#374151" font-family="Inter, sans-serif">${pct}%</text>`
                : ""
            }
          </g>
        `;
      };

      return `
        ${drawBar(x1, m1Best, "#1f2937", "Mode 1 Best")}
        ${drawBar(x2, m2Best, "#6b7280", "Mode 2 Best")}
        ${drawBar(x3, bankPct, "#10b981", "Bank Mastery")}
        <text x="${gx.toFixed(1)}" y="${H - 14}" text-anchor="middle" font-size="11" font-weight="700" fill="#111827" font-family="Inter, sans-serif">U${u.id}</text>
      `;
    }).join("");

    stageEl.innerHTML = `
      <svg class="dash-svg-chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Unit 1 to 9 accuracy comparison bar chart">
        ${gridHtml}
        ${barsHtml}
      </svg>
    `;
  }

  // =========================================================================
  // 7. SVG Chart 4: Average Time Pace per Question by Unit (Horizontal Bars)
  // =========================================================================

  function renderUnitPaceChart() {
    const stageEl = document.getElementById("chart-unit-pace");
    if (!stageEl) return;

    const W = 540;
    const H = 265;
    const padL = 48;
    const padR = 48;
    const padT = 18;
    const padB = 28;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;
    const maxSec = 120; // Scale 0s..120s (with 90s AP target line)

    const xAt = (sec) => padL + (Math.min(maxSec, Math.max(0, sec)) / maxSec) * plotW;
    const rowH = plotH / UNITS.length;

    const targetX = xAt(90).toFixed(1);

    const rowsHtml = UNITS.map((u, idx) => {
      const uAtts = state.attempts.filter((a) => a.unitId === u.id);
      const totalSec = uAtts.reduce((s, a) => s + (a.durationSec || 0), 0);
      const totalQs = uAtts.reduce(
        (s, a) => s + (a.mode === "batch" ? a.total || 0 : a.answered || 0),
        0
      );
      const avgPace = totalQs > 0 ? Math.round(totalSec / totalQs) : 0;

      const cy = padT + idx * rowH + rowH / 2;
      const barH = Math.min(13, rowH - 8);
      const barW = avgPace > 0 ? Math.max(4, xAt(avgPace) - padL) : 3;
      const barColor = avgPace === 0 ? "#e5e7eb" : avgPace <= 90 ? "#1f2937" : "#d97706";

      return `
        <g>
          <text x="${padL - 8}" y="${(cy + 4).toFixed(1)}" text-anchor="end" font-size="11" font-weight="700" fill="#111827" font-family="Inter, sans-serif">U${u.id}</text>
          <rect x="${padL}" y="${(cy - barH / 2).toFixed(1)}" width="${plotW}" height="${barH.toFixed(1)}" rx="4" fill="#f3f4f6" />
          <rect x="${padL}" y="${(cy - barH / 2).toFixed(1)}" width="${barW.toFixed(1)}" height="${barH.toFixed(1)}" rx="4" fill="${barColor}" />
          <text x="${(padL + barW + 6).toFixed(1)}" y="${(cy + 4).toFixed(1)}" font-size="10.5" font-weight="700" fill="#374151" font-family="Inter, sans-serif">${avgPace > 0 ? `${avgPace}s/Q` : "—"}</text>
        </g>
      `;
    }).join("");

    stageEl.innerHTML = `
      <svg class="dash-svg-chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Average time pace per question by unit">
        ${rowsHtml}
        <line x1="${targetX}" y1="${padT}" x2="${targetX}" y2="${H - padB}" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4 3" />
        <text x="${targetX}" y="${H - 8}" text-anchor="middle" font-size="10" font-weight="700" fill="#065f46" font-family="Inter, sans-serif">90s AP Target</text>
      </svg>
    `;
  }

  // =========================================================================
  // 8. Structured Table 2: Complete Units 1–9 & Mode Performance Summary Table
  // =========================================================================

  function renderUnitSummaryTable(pausedSessions) {
    const wrapEl = document.getElementById("dash-unit-summary-table-wrap");
    if (!wrapEl) return;

    const unitsToShow =
      state.unitFilter === "all"
        ? UNITS
        : UNITS.filter((u) => u.id === Number(state.unitFilter));

    const rowsHtml = unitsToShow
      .map((u) => {
        const unitQs = getQuestionsForUnit(u.id);
        let bankAns = 0;
        let bankCorr = 0;
        unitQs.forEach((q) => {
          const h = state.history[q.id];
          if (h) {
            bankAns += 1;
            if (h.correct) bankCorr += 1;
          }
        });
        const bankPct = unitQs.length > 0 ? Math.round((bankAns / unitQs.length) * 100) : 0;

        const uBatch = state.attempts.filter((a) => a.unitId === u.id && a.mode === "batch");
        const uSingle = state.attempts.filter((a) => a.unitId === u.id && a.mode === "single");
        const uAll = state.attempts.filter((a) => a.unitId === u.id);

        const bBest = uBatch.length > 0 ? `${Math.max(...uBatch.map((a) => a.pct))}%` : "—";
        const bAvg =
          uBatch.length > 0
            ? `${Math.round(uBatch.reduce((s, a) => s + a.pct, 0) / uBatch.length)}%`
            : "—";
        const bTime = formatDurationHuman(uBatch.reduce((s, a) => s + (a.durationSec || 0), 0));

        const sBest = uSingle.length > 0 ? `${Math.max(...uSingle.map((a) => a.pct))}%` : "—";
        const sAvg =
          uSingle.length > 0
            ? `${Math.round(uSingle.reduce((s, a) => s + a.pct, 0) / uSingle.length)}%`
            : "—";
        const sTime = formatDurationHuman(uSingle.reduce((s, a) => s + (a.durationSec || 0), 0));

        const totalSec = uAll.reduce((s, a) => s + (a.durationSec || 0), 0);
        const totalQs = uAll.reduce(
          (s, a) => s + (a.mode === "batch" ? a.total || 0 : a.answered || 0),
          0
        );
        const totalCorr = uAll.reduce((s, a) => s + (a.correct || 0), 0);
        const unitAcc = totalQs > 0 ? Math.round((totalCorr / totalQs) * 100) : 0;
        const avgPace = totalQs > 0 ? `${Math.round(totalSec / totalQs)}s/Q` : "—";
        const apBand = getApBandInfo(unitAcc, totalQs > 0);

        const pausedInUnit = pausedSessions.find((p) => p.unitId === u.id);

        return `
          <tr>
            <td>
              <span class="unit-tag-badge">U${u.id}</span>
              <strong>${escapeHtml(u.title)}</strong>
              <div style="font-size: 0.74rem; color: #6b7280; margin-top: 0.15rem;">Exam Weight: ${escapeHtml(u.exam_weight)} • ${u.question_count} Qs</div>
            </td>
            <td>
              <strong>${bankCorr}✓ / ${bankAns} Ans / ${unitQs.length} Total (${bankPct}%)</strong>
              <div class="table-mini-bar-wrap">
                <div class="table-mini-bar-fill" style="width: ${bankPct}%"></div>
              </div>
            </td>
            <td>
              <strong>${uBatch.length} Att</strong> · Best: <strong>${bBest}</strong> · Avg: <strong>${bAvg}</strong>
              <div style="font-size: 0.74rem; color: #6b7280;">Time: ${bTime}</div>
            </td>
            <td>
              <strong>${uSingle.length} Att</strong> · Best: <strong>${sBest}</strong> · Avg: <strong>${sAvg}</strong>
              <div style="font-size: 0.74rem; color: #6b7280;">Time: ${sTime}</div>
            </td>
            <td>
              <span class="status-badge ${apBand.cls}">${escapeHtml(apBand.band)}</span>
              <div style="font-size: 0.74rem; color: #6b7280; margin-top: 0.2rem;">Pace: ${avgPace}</div>
            </td>
            <td>
              <div class="table-actions-cell">
                ${
                  pausedInUnit
                    ? `<a href="${pausedInUnit.resumeUrl}" class="dash-action-link is-primary">▶ Resume (${formatMMSS(pausedInUnit.elapsedSec)})</a>`
                    : `<a href="/quiz#/unit/${u.id}" class="dash-action-link is-primary">▶ Open Unit ${u.id}</a>`
                }
                <a href="/quiz?unit=${u.id}&mode=batch&action=retake" class="dash-action-link">↺ Retake M1</a>
                <a href="/quiz?unit=${u.id}&mode=single&action=retake" class="dash-action-link">↺ Retake M2</a>
              </div>
            </td>
          </tr>
        `;
      })
      .join("");

    wrapEl.innerHTML = `
      <table class="dash-data-table">
        <thead>
          <tr>
            <th>AP Chemistry Unit</th>
            <th>Question Bank Coverage</th>
            <th>Mode 1 (10-Question Sets)</th>
            <th>Mode 2 (1-by-1 Instant)</th>
            <th>AP Band &amp; Pace</th>
            <th>Quick Actions</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  // =========================================================================
  // 9. Structured Table 3: Chronological Attempt History Log Table
  // =========================================================================

  function renderAttemptsHistoryTable() {
    const wrapEl = document.getElementById("dash-attempts-table-wrap");
    const countLabelEl = document.getElementById("dash-attempts-count-label");
    if (!wrapEl) return;

    const filtered = getFilteredAttempts().slice().reverse();
    if (countLabelEl) {
      countLabelEl.textContent = `Showing ${filtered.length} of ${state.attempts.length} recorded attempt${state.attempts.length === 1 ? "" : "s"}`;
    }

    if (filtered.length === 0) {
      wrapEl.innerHTML = `
        <div class="dash-empty-state">
          <strong>No saved attempts match the current filter.</strong> Complete and submit a 10-question set in Mode 1 or click <em>✓ Save Attempt</em> in Mode 2 on the <a href="/quiz">AP Practice Quiz</a> page to record attempts here.
        </div>
      `;
      return;
    }

    const rowsHtml = filtered
      .map((a) => {
        const denom = a.mode === "batch" ? a.total : a.answered;
        const badgeCls = a.pct >= 75 ? "badge-high" : a.pct >= 55 ? "badge-mid" : "badge-low";
        const modeText = a.mode === "batch" ? "Mode 1 · 10-Q Set" : "Mode 2 · 1-by-1";
        const paceSec = denom > 0 ? Math.round((a.durationSec || 0) / denom) : 0;
        const apInfo = getApBandInfo(a.pct, true);
        const setParam = typeof a.setIndex === "number" ? `&set=${a.setIndex}` : "";
        const retakeHref = `/quiz?unit=${a.unitId}&mode=${a.mode}${setParam}&action=retake`;

        return `
          <tr>
            <td><strong>Attempt #${a.attemptNumber || 1}</strong></td>
            <td>${escapeHtml(formatDateTime(a.timestamp))}</td>
            <td>
              <span class="unit-tag-badge">U${a.unitId}</span>
              <strong>${escapeHtml(a.unitTitle)}</strong>
            </td>
            <td>
              <strong>${modeText}</strong>
              <div style="font-size: 0.75rem; color: #4b5563;">${escapeHtml(a.scopeLabel || "")}</div>
            </td>
            <td>
              <span class="status-badge ${badgeCls}">${a.correct} / ${denom} Correct (${a.pct}%)</span>
            </td>
            <td>
              <strong>⏱ ${formatMMSS(a.durationSec)}</strong>
              <div style="font-size: 0.74rem; color: #6b7280;">${paceSec}s / question</div>
            </td>
            <td>
              <span class="status-badge ${apInfo.cls}">${escapeHtml(apInfo.band)}</span>
            </td>
            <td>
              <a href="${retakeHref}" class="dash-action-link">↺ Retake</a>
            </td>
          </tr>
        `;
      })
      .join("");

    wrapEl.innerHTML = `
      <table class="dash-data-table">
        <thead>
          <tr>
            <th>Attempt #</th>
            <th>Date &amp; Time</th>
            <th>Unit</th>
            <th>Mode &amp; Set Scope</th>
            <th>Correct Answers &amp; Score</th>
            <th>Duration &amp; Pace</th>
            <th>AP Band</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          ${rowsHtml}
        </tbody>
      </table>
    `;
  }

  // =========================================================================
  // Master Render & Event Listeners
  // =========================================================================

  function renderDashboardAll() {
    state.history = loadHistory();
    state.attempts = loadAttempts();
    state.sessions = loadSessions();

    const pausedSessions = collectPausedSessions();
    renderHeaderStatus(pausedSessions);
    renderKpiCards(pausedSessions);
    renderPausedSessionsTable(pausedSessions);
    renderAccuracyTrendChart();
    renderBankDonutChart(pausedSessions);
    renderUnitGroupedBarChart();
    renderUnitPaceChart();
    renderUnitSummaryTable(pausedSessions);
    renderAttemptsHistoryTable();
  }

  const unitFilterEl = document.getElementById("dash-global-unit-filter");
  if (unitFilterEl) {
    unitFilterEl.addEventListener("change", () => {
      state.unitFilter = unitFilterEl.value;
      renderDashboardAll();
    });
  }

  const modeFilterEl = document.getElementById("dash-global-mode-filter");
  if (modeFilterEl) {
    modeFilterEl.addEventListener("change", () => {
      state.modeFilter = modeFilterEl.value;
      renderDashboardAll();
    });
  }

  window.addEventListener("inorganic-user-synced", () => {
    renderDashboardAll();
  });

  renderDashboardAll();
})();
