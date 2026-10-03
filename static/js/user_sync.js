/**
 * User Profile & Google Cloud Storage (`haren-agent-storage`) Sync Controller
 * - Prompts for username on the first screen via a native <dialog> modal
 * - Scopes all quiz statistics (history, attempts, active sessions) to the active username
 * - Syncs & retrieves user data from `/api/user/<username>` (backed by `gs://haren-agent-storage`)
 */

(function () {
  "use strict";

  const ACTIVE_USER_KEY = "inorganic_chem_active_user";
  const RECENT_USERS_KEY = "inorganic_chem_recent_users";
  const LEGACY_MIGRATED_KEY = "inorganic_chem_legacy_migrated_v1";

  const BASE_HISTORY_KEY = "inorganic_chem_ap_quiz_v2";
  const BASE_ATTEMPTS_KEY = "inorganic_chem_ap_quiz_attempts_v1";
  const BASE_SESSIONS_KEY = "inorganic_chem_ap_quiz_sessions_v1";

  let activeUser = loadActiveUser();
  let syncStatus = {
    state: "idle", // "idle" | "syncing" | "synced" | "local" | "error"
    cloudSynced: false,
    bucket: "haren-agent-storage",
    updatedAt: null,
    error: null,
  };
  let pushTimer = null;

  function normalizeUsername(raw) {
    if (!raw || typeof raw !== "string") return "";
    let cleaned = raw.trim().toLowerCase().replace(/\s+/g, "_");
    cleaned = cleaned.replace(/[^a-z0-9_.-]/g, "");
    cleaned = cleaned.replace(/^[._-]+|[._-]+$/g, "");
    return cleaned.slice(0, 64);
  }

  function loadActiveUser() {
    try {
      const raw = localStorage.getItem(ACTIVE_USER_KEY);
      if (!raw) return null;
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== "object") return null;
      const username = normalizeUsername(parsed.username || "");
      if (!username) return null;
      return {
        username,
        displayName: String(parsed.displayName || username).trim() || username,
      };
    } catch (_) {
      return null;
    }
  }

  function saveActiveUser(userObj) {
    activeUser = userObj;
    try {
      if (userObj && userObj.username) {
        localStorage.setItem(ACTIVE_USER_KEY, JSON.stringify(userObj));
        addRecentUser(userObj);
      } else {
        localStorage.removeItem(ACTIVE_USER_KEY);
      }
    } catch (_) {
      // Ignore storage errors
    }
  }

  function loadRecentUsers() {
    try {
      const raw = localStorage.getItem(RECENT_USERS_KEY);
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return [];
      return parsed.filter((u) => u && typeof u.username === "string" && normalizeUsername(u.username));
    } catch (_) {
      return [];
    }
  }

  function addRecentUser(userObj) {
    try {
      const list = loadRecentUsers().filter((u) => u.username !== userObj.username);
      list.unshift({ username: userObj.username, displayName: userObj.displayName || userObj.username });
      localStorage.setItem(RECENT_USERS_KEY, JSON.stringify(list.slice(0, 8)));
    } catch (_) {
      // Ignore storage errors
    }
  }

  function scopedKey(baseKey, username) {
    const u = normalizeUsername(username || (activeUser && activeUser.username) || "");
    return u ? `${baseKey}__${u}` : baseKey;
  }

  function getHistoryStorageKey(username) {
    return scopedKey(BASE_HISTORY_KEY, username);
  }

  function getAttemptsStorageKey(username) {
    return scopedKey(BASE_ATTEMPTS_KEY, username);
  }

  function getSessionsStorageKey(username) {
    return scopedKey(BASE_SESSIONS_KEY, username);
  }

  function safeParseJson(raw, fallback) {
    if (!raw) return fallback;
    try {
      const parsed = JSON.parse(raw);
      return parsed !== null && parsed !== undefined ? parsed : fallback;
    } catch (_) {
      return fallback;
    }
  }

  function migrateLegacyUnscopedDataOnce(username) {
    try {
      if (localStorage.getItem(LEGACY_MIGRATED_KEY)) return;
      const hKey = getHistoryStorageKey(username);
      const aKey = getAttemptsStorageKey(username);
      const sKey = getSessionsStorageKey(username);

      const hasScoped =
        localStorage.getItem(hKey) ||
        localStorage.getItem(aKey) ||
        localStorage.getItem(sKey);

      const legacyH = localStorage.getItem(BASE_HISTORY_KEY);
      const legacyA = localStorage.getItem(BASE_ATTEMPTS_KEY);
      const legacyS = localStorage.getItem(BASE_SESSIONS_KEY);

      if (!hasScoped && (legacyH || legacyA || legacyS)) {
        if (legacyH) localStorage.setItem(hKey, legacyH);
        if (legacyA) localStorage.setItem(aKey, legacyA);
        if (legacyS) localStorage.setItem(sKey, legacyS);
      }
      localStorage.setItem(LEGACY_MIGRATED_KEY, username);
    } catch (_) {
      // Ignore storage errors
    }
  }

  function readLocalPayloadForUser(username) {
    const history = safeParseJson(localStorage.getItem(getHistoryStorageKey(username)), {});
    const attempts = safeParseJson(localStorage.getItem(getAttemptsStorageKey(username)), []);
    const sessions = safeParseJson(localStorage.getItem(getSessionsStorageKey(username)), {
      batchByUnitSet: {},
      singleByUnit: {},
      lastLocation: null,
    });
    return {
      history: history && typeof history === "object" && !Array.isArray(history) ? history : {},
      attempts: Array.isArray(attempts) ? attempts : [],
      sessions:
        sessions && typeof sessions === "object" && !Array.isArray(sessions)
          ? {
              batchByUnitSet:
                sessions.batchByUnitSet && typeof sessions.batchByUnitSet === "object"
                  ? sessions.batchByUnitSet
                  : {},
              singleByUnit:
                sessions.singleByUnit && typeof sessions.singleByUnit === "object"
                  ? sessions.singleByUnit
                  : {},
              lastLocation:
                sessions.lastLocation && typeof sessions.lastLocation === "object"
                  ? sessions.lastLocation
                  : null,
            }
          : { batchByUnitSet: {}, singleByUnit: {}, lastLocation: null },
    };
  }

  function mergeClientPayloads(cloudData, localData) {
    const mergedHistory = Object.assign({}, cloudData.history || {}, localData.history || {});

    // Merge attempts by id and recompute sequential attemptNumber per (unitId, mode, scopeKey)
    const byId = new Map();
    const combinedAttempts = [].concat(cloudData.attempts || [], localData.attempts || []);
    combinedAttempts.forEach((att, idx) => {
      if (!att || typeof att !== "object") return;
      const id = String(att.id || `att_${att.timestamp || idx}_${att.unitId}_${att.mode}`);
      const copy = Object.assign({}, att, { id });
      byId.set(id, copy);
    });

    const mergedAttempts = Array.from(byId.values()).sort(
      (a, b) => (Number(a.timestamp) || 0) - (Number(b.timestamp) || 0)
    );

    const counters = {};
    mergedAttempts.forEach((att) => {
      const cKey = `${att.unitId}|${att.mode}|${att.scopeKey || ""}`;
      counters[cKey] = (counters[cKey] || 0) + 1;
      att.attemptNumber = counters[cKey];
    });

    const cloudBatch = (cloudData.sessions && cloudData.sessions.batchByUnitSet) || {};
    const localBatch = (localData.sessions && localData.sessions.batchByUnitSet) || {};
    const mergedBatch = Object.assign({}, cloudBatch);
    Object.keys(localBatch).forEach((k) => {
      const lEntry = localBatch[k];
      const cEntry = mergedBatch[k];
      if (!cEntry) {
        mergedBatch[k] = lEntry;
        return;
      }
      const lCount = Object.keys((lEntry && lEntry.answers) || {}).length;
      const cCount = Object.keys((cEntry && cEntry.answers) || {}).length;
      const lElapsed = Number((lEntry && lEntry.elapsedSec) || 0);
      const cElapsed = Number((cEntry && cEntry.elapsedSec) || 0);
      if ((lEntry && lEntry.submitted && !cEntry.submitted) || lCount > cCount || (lCount === cCount && lElapsed >= cElapsed)) {
        mergedBatch[k] = lEntry;
      }
    });

    const cloudSingle = (cloudData.sessions && cloudData.sessions.singleByUnit) || {};
    const localSingle = (localData.sessions && localData.sessions.singleByUnit) || {};
    const mergedSingle = Object.assign({}, cloudSingle);
    Object.keys(localSingle).forEach((k) => {
      const lEntry = localSingle[k];
      const cEntry = mergedSingle[k];
      if (!cEntry) {
        mergedSingle[k] = lEntry;
        return;
      }
      const lCount = Object.keys((lEntry && lEntry.answers) || {}).length;
      const cCount = Object.keys((cEntry && cEntry.answers) || {}).length;
      const lElapsed = Number((lEntry && lEntry.elapsedSec) || 0);
      const cElapsed = Number((cEntry && cEntry.elapsedSec) || 0);
      if (lCount > cCount || (lCount === cCount && lElapsed >= cElapsed)) {
        mergedSingle[k] = lEntry;
      }
    });

    const cloudLoc = (cloudData.sessions && cloudData.sessions.lastLocation) || null;
    const localLoc = (localData.sessions && localData.sessions.lastLocation) || null;
    let mergedLocation = localLoc || cloudLoc || null;
    if (cloudLoc && localLoc) {
      mergedLocation =
        String(localLoc.updatedAt || "") >= String(cloudLoc.updatedAt || "") ? localLoc : cloudLoc;
    }

    return {
      history: mergedHistory,
      attempts: mergedAttempts,
      sessions: {
        batchByUnitSet: mergedBatch,
        singleByUnit: mergedSingle,
        lastLocation: mergedLocation,
      },
    };
  }

  function writeLocalPayloadForUser(username, payload) {
    try {
      localStorage.setItem(getHistoryStorageKey(username), JSON.stringify(payload.history || {}));
      localStorage.setItem(getAttemptsStorageKey(username), JSON.stringify(payload.attempts || []));
      localStorage.setItem(
        getSessionsStorageKey(username),
        JSON.stringify(payload.sessions || { batchByUnitSet: {}, singleByUnit: {} })
      );
    } catch (_) {
      // Ignore quota errors
    }
  }

  // =========================================================================
  // Cloud Sync Operations (`/api/user/<username>` -> `haren-agent-storage`)
  // =========================================================================

  async function syncWithCloud(userObj) {
    if (!userObj || !userObj.username) return null;
    const username = userObj.username;
    migrateLegacyUnscopedDataOnce(username);

    syncStatus.state = "syncing";
    updateHeaderUserUI();
    dispatchSyncEvent();

    const localData = readLocalPayloadForUser(username);

    try {
      const getResp = await fetch(`/api/user/${encodeURIComponent(username)}`, {
        method: "GET",
        headers: { Accept: "application/json" },
        cache: "no-store",
      });

      if (!getResp.ok) {
        throw new Error(`HTTP ${getResp.status}`);
      }

      const getResult = await getResp.json();
      const cloudData = (getResult && getResult.data) || {
        history: {},
        attempts: [],
        sessions: { batchByUnitSet: {}, singleByUnit: {} },
      };

      const merged = mergeClientPayloads(cloudData, localData);
      writeLocalPayloadForUser(username, merged);

      // Push back to Cloud Storage so haren-agent-storage always has the latest merged user file
      const postResp = await fetch(`/api/user/${encodeURIComponent(username)}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          display_name: userObj.displayName || username,
          history: merged.history,
          attempts: merged.attempts,
          sessions: merged.sessions,
          merge: true,
        }),
      });

      if (postResp.ok) {
        const postResult = await postResp.json();
        if (postResult && postResult.data) {
          writeLocalPayloadForUser(username, postResult.data);
        }
        syncStatus = {
          state: postResult.cloud_synced ? "synced" : "local",
          cloudSynced: Boolean(postResult.cloud_synced),
          bucket: postResult.bucket || "haren-agent-storage",
          updatedAt: (postResult.data && postResult.data.updated_at) || new Date().toISOString(),
          error: postResult.cloud_error || null,
        };
      } else {
        syncStatus = {
          state: getResult.cloud_synced ? "synced" : "local",
          cloudSynced: Boolean(getResult.cloud_synced),
          bucket: getResult.bucket || "haren-agent-storage",
          updatedAt: cloudData.updated_at || new Date().toISOString(),
          error: null,
        };
      }
    } catch (err) {
      syncStatus = {
        state: "error",
        cloudSynced: false,
        bucket: "haren-agent-storage",
        updatedAt: null,
        error: err && err.message ? err.message : "Network error",
      };
    }

    updateHeaderUserUI();
    dispatchSyncEvent();
    return readLocalPayloadForUser(username);
  }

  async function pushCurrentUserToCloud(options) {
    if (!activeUser || !activeUser.username) return null;
    const username = activeUser.username;
    const merge = options && typeof options.merge === "boolean" ? options.merge : true;
    const localData = readLocalPayloadForUser(username);

    syncStatus.state = "syncing";
    updateHeaderUserUI();

    try {
      const resp = await fetch(`/api/user/${encodeURIComponent(username)}`, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          display_name: activeUser.displayName || username,
          history: localData.history,
          attempts: localData.attempts,
          sessions: localData.sessions,
          merge,
        }),
      });
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      const resJson = await resp.json();
      syncStatus = {
        state: resJson.cloud_synced ? "synced" : "local",
        cloudSynced: Boolean(resJson.cloud_synced),
        bucket: resJson.bucket || "haren-agent-storage",
        updatedAt: (resJson.data && resJson.data.updated_at) || new Date().toISOString(),
        error: resJson.cloud_error || null,
      };
    } catch (err) {
      syncStatus = {
        state: "error",
        cloudSynced: false,
        bucket: "haren-agent-storage",
        updatedAt: null,
        error: err && err.message ? err.message : "Sync failed",
      };
    }

    updateHeaderUserUI();
    dispatchSyncEvent({ silentQuizReload: true });
    return syncStatus;
  }

  function schedulePush(options) {
    if (pushTimer) clearTimeout(pushTimer);
    pushTimer = setTimeout(() => {
      pushTimer = null;
      pushCurrentUserToCloud(options);
    }, 350);
  }

  function dispatchSyncEvent(extraDetail) {
    window.dispatchEvent(
      new CustomEvent("inorganic-user-synced", {
        detail: Object.assign(
          {
            user: activeUser,
            syncStatus,
          },
          extraDetail || {}
        ),
      })
    );
  }

  // =========================================================================
  // Header User Chip & First-Screen Username <dialog> Modal
  // =========================================================================

  function escapeHtml(str) {
    return String(str ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  const SIDEBAR_COLLAPSED_KEY = "inorganic_chem_sidebar_collapsed";

  function applySidebarCollapsedState(isCollapsed) {
    document.documentElement.classList.toggle("sidebar-collapsed", Boolean(isCollapsed));
    if (document.body) {
      document.body.classList.toggle("sidebar-collapsed", Boolean(isCollapsed));
    }
    const toggleBtn = document.getElementById("btn-toggle-sidebar");
    if (toggleBtn) {
      toggleBtn.setAttribute("aria-expanded", isCollapsed ? "false" : "true");
      toggleBtn.title = isCollapsed
        ? "Expand Navigation Sidebar (Ctrl+B)"
        : "Retract Navigation Sidebar (Ctrl+B)";
      const iconEl = toggleBtn.querySelector(".sidebar-toggle-icon");
      if (iconEl) {
        iconEl.textContent = isCollapsed ? "»" : "«";
      }
    }
  }

  function loadSidebarCollapsedState() {
    try {
      return localStorage.getItem(SIDEBAR_COLLAPSED_KEY) === "1";
    } catch (_) {
      return false;
    }
  }

  function initRetractableSidebar() {
    const initialCollapsed = loadSidebarCollapsedState();
    applySidebarCollapsedState(initialCollapsed);

    const toggleBtn = document.getElementById("btn-toggle-sidebar");
    if (toggleBtn && !toggleBtn.dataset.boundSidebarToggle) {
      toggleBtn.dataset.boundSidebarToggle = "1";
      toggleBtn.addEventListener("click", () => {
        const nextCollapsed = !document.documentElement.classList.contains("sidebar-collapsed");
        try {
          localStorage.setItem(SIDEBAR_COLLAPSED_KEY, nextCollapsed ? "1" : "0");
        } catch (_) {
          // Ignore storage errors
        }
        applySidebarCollapsedState(nextCollapsed);
        window.dispatchEvent(new Event("resize"));
        setTimeout(() => window.dispatchEvent(new Event("resize")), 230);
      });
    }

    if (!window.__inorganicSidebarShortcutBound) {
      window.__inorganicSidebarShortcutBound = true;
      window.addEventListener("keydown", (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "b") {
          const tag = (e.target && e.target.tagName) || "";
          if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
          e.preventDefault();
          const btn = document.getElementById("btn-toggle-sidebar");
          if (btn) btn.click();
        }
      });
    }
  }

  // Apply persisted sidebar state immediately
  applySidebarCollapsedState(loadSidebarCollapsedState());

  function injectHeaderUserChip() {
    const mountTarget =
      document.getElementById("sidebar-user-mount") ||
      document.querySelector(".site-sidebar") ||
      document.querySelector(".site-header .header-inner");
    if (!mountTarget || document.getElementById("header-user-bar")) return;

    const bar = document.createElement("div");
    bar.className = "header-user-bar";
    bar.id = "header-user-bar";
    bar.innerHTML = `
      <button type="button" class="user-profile-chip" id="btn-switch-user" title="Switch student username or sync with Cloud Storage (haren-agent-storage)">
        <span class="user-chip-avatar" aria-hidden="true">👤</span>
        <span class="user-chip-name" id="header-username-label">Sign In</span>
        <span class="user-chip-sync" id="header-sync-badge" data-sync-state="idle">☁️ Cloud Sync</span>
        <span class="user-chip-action">Switch User</span>
      </button>
    `;
    mountTarget.appendChild(bar);

    const switchBtn = document.getElementById("btn-switch-user");
    if (switchBtn) {
      switchBtn.addEventListener("click", () => {
        openUserLoginModal(true);
      });
    }
  }

  function updateHeaderUserUI() {
    const nameEl = document.getElementById("header-username-label");
    const syncEl = document.getElementById("header-sync-badge");

    if (nameEl) {
      nameEl.textContent = activeUser ? activeUser.displayName || activeUser.username : "Set Username";
    }
    if (syncEl) {
      syncEl.setAttribute("data-sync-state", syncStatus.state);
      if (!activeUser) {
        syncEl.textContent = "☁️ Not signed in";
      } else if (syncStatus.state === "syncing") {
        syncEl.textContent = "⟳ Syncing…";
      } else if (syncStatus.state === "synced") {
        syncEl.textContent = "☁️ Synced";
        syncEl.title = `Synced to Google Cloud Storage bucket ${syncStatus.bucket}`;
      } else if (syncStatus.state === "local") {
        syncEl.textContent = "💾 Saved";
        syncEl.title = syncStatus.error
          ? `Saved locally (${syncStatus.error})`
          : "Saved in local & server storage";
      } else if (syncStatus.state === "error") {
        syncEl.textContent = "⚠️ Local only";
      } else {
        syncEl.textContent = "☁️ Cloud Sync";
      }
    }
  }

  function ensureUserLoginDialog() {
    let dialog = document.getElementById("user-login-dialog");
    if (dialog) return dialog;

    dialog = document.createElement("dialog");
    dialog.id = "user-login-dialog";
    dialog.className = "user-login-dialog";
    dialog.setAttribute("aria-labelledby", "user-dialog-title");

    dialog.innerHTML = `
      <form class="user-dialog-card" id="user-login-form" method="dialog" novalidate>
        <div class="user-dialog-head">
          <span class="user-dialog-eyebrow">STUDENT PROFILE • CLOUD STORAGE SYNC</span>
          <h2 id="user-dialog-title">Enter Your Username</h2>
          <p class="user-dialog-sub">
            Enter your username to load or save your AP Chemistry quiz progress, unit attempts, completion times, and accuracy dashboard in Google Cloud Storage (<code>haren-agent-storage</code>).
          </p>
        </div>

        <div class="user-dialog-body">
          <label class="user-input-label" for="user-login-input">
            <span>Student Username</span>
            <input
              type="text"
              id="user-login-input"
              name="username"
              class="user-login-input"
              placeholder="e.g. alex_chem or haren"
              autocomplete="username"
              maxlength="64"
              required
            >
          </label>
          <div class="user-dialog-hint">
            Use letters, numbers, underscores, or hyphens. Logging in with an existing username automatically retrieves your saved attempts from <strong>haren-agent-storage</strong>.
          </div>

          <div class="user-recent-wrap" id="user-recent-wrap" hidden>
            <span class="user-recent-label">Recent profiles on this browser:</span>
            <div class="user-recent-chips" id="user-recent-chips"></div>
          </div>

          <div class="user-dialog-status" id="user-login-status" role="status" aria-live="polite" hidden></div>
        </div>

        <div class="user-dialog-actions">
          <button type="button" class="btn btn-secondary" id="btn-user-login-cancel" hidden>
            Cancel
          </button>
          <button type="submit" class="btn btn-primary" id="btn-user-login-submit">
            Continue &amp; Sync Cloud Data →
          </button>
        </div>
      </form>
    `;

    document.body.appendChild(dialog);

    // Light dismiss fallback when switching user (closedby="any")
    if (!("closedBy" in HTMLDialogElement.prototype)) {
      dialog.addEventListener("click", (e) => {
        if (e.target === dialog && dialog.getAttribute("closedby") === "any") {
          dialog.close();
        }
      });
    }

    // Prevent Escape key from closing the modal if no user is set yet
    dialog.addEventListener("cancel", (e) => {
      if (!activeUser) {
        e.preventDefault();
      }
    });

    const cancelBtn = document.getElementById("btn-user-login-cancel");
    if (cancelBtn) {
      cancelBtn.addEventListener("click", () => {
        if (activeUser) dialog.close();
      });
    }

    const recentChipsEl = document.getElementById("user-recent-chips");
    if (recentChipsEl) {
      recentChipsEl.addEventListener("click", (e) => {
        const chip = e.target.closest("[data-select-username]");
        if (!chip) return;
        const u = chip.getAttribute("data-select-username");
        const input = document.getElementById("user-login-input");
        if (input && u) {
          input.value = u;
          input.focus();
        }
      });
    }

    const form = document.getElementById("user-login-form");
    if (form) {
      form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const input = document.getElementById("user-login-input");
        const statusEl = document.getElementById("user-login-status");
        const submitBtn = document.getElementById("btn-user-login-submit");

        const rawName = input ? input.value.trim() : "";
        const norm = normalizeUsername(rawName);

        if (!norm) {
          if (statusEl) {
            statusEl.hidden = false;
            statusEl.className = "user-dialog-status is-error";
            statusEl.textContent = "Please enter a valid username (letters, numbers, underscores, or hyphens).";
          }
          if (input) input.focus();
          return;
        }

        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = "Retrieving from haren-agent-storage…";
        }
        if (statusEl) {
          statusEl.hidden = false;
          statusEl.className = "user-dialog-status is-loading";
          statusEl.textContent = `Syncing profile "${norm}" with Cloud Storage (haren-agent-storage)…`;
        }

        const userObj = {
          username: norm,
          displayName: rawName || norm,
        };
        saveActiveUser(userObj);
        updateHeaderUserUI();

        await syncWithCloud(userObj);

        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = "Continue & Sync Cloud Data →";
        }
        if (statusEl) {
          statusEl.hidden = true;
        }

        if (dialog.open) {
          dialog.close();
        }
      });
    }

    return dialog;
  }

  function renderRecentUserChips() {
    const wrap = document.getElementById("user-recent-wrap");
    const chipsEl = document.getElementById("user-recent-chips");
    if (!wrap || !chipsEl) return;

    const recent = loadRecentUsers();
    if (recent.length === 0) {
      wrap.hidden = true;
      return;
    }

    wrap.hidden = false;
    chipsEl.innerHTML = recent
      .map(
        (u) => `
        <button type="button" class="user-recent-chip ${
          activeUser && activeUser.username === u.username ? "active" : ""
        }" data-select-username="${escapeHtml(u.username)}">
          👤 ${escapeHtml(u.displayName || u.username)}
        </button>
      `
      )
      .join("");
  }

  function openUserLoginModal(allowCancel) {
    const dialog = ensureUserLoginDialog();
    const canCancel = Boolean(allowCancel && activeUser);
    dialog.setAttribute("closedby", canCancel ? "any" : "none");

    const cancelBtn = document.getElementById("btn-user-login-cancel");
    if (cancelBtn) cancelBtn.hidden = !canCancel;

    const statusEl = document.getElementById("user-login-status");
    if (statusEl) statusEl.hidden = true;

    renderRecentUserChips();

    const input = document.getElementById("user-login-input");
    if (input) {
      input.value = activeUser ? activeUser.displayName || activeUser.username : "";
    }

    if (!dialog.open) {
      if (typeof dialog.showModal === "function") {
        dialog.showModal();
      } else {
        dialog.setAttribute("open", "");
      }
    }
    if (input) {
      setTimeout(() => {
        input.focus();
        input.select();
      }, 20);
    }
  }

  // Expose public API for quiz_app.js and other pages
  window.InorganicUserSync = {
    getActiveUser: () => activeUser,
    getUsername: () => (activeUser ? activeUser.username : ""),
    getDisplayName: () => (activeUser ? activeUser.displayName || activeUser.username : "Guest"),
    getSyncStatus: () => syncStatus,
    getHistoryStorageKey: () => getHistoryStorageKey(activeUser && activeUser.username),
    getAttemptsStorageKey: () => getAttemptsStorageKey(activeUser && activeUser.username),
    getSessionsStorageKey: () => getSessionsStorageKey(activeUser && activeUser.username),
    openUserLoginModal: () => openUserLoginModal(true),
    syncNow: () => (activeUser ? syncWithCloud(activeUser) : Promise.resolve(null)),
    schedulePush,
    pushNow: pushCurrentUserToCloud,
  };

  function bootUserSync() {
    initRetractableSidebar();
    injectHeaderUserChip();
    ensureUserLoginDialog();
    updateHeaderUserUI();

    if (!activeUser) {
      openUserLoginModal(false);
    } else {
      syncWithCloud(activeUser);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootUserSync);
  } else {
    bootUserSync();
  }
})();
