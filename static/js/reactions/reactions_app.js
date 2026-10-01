/**
 * Essential Chemical & Ionic Equations — Interactive Virtual Chemistry Lab
 * Powers:
 *  1. 206-reaction categorized reference catalog with KaTeX rendering
 *  2. SVG Chemical Specimen Vessels + 2D Molecular Geometry + PubChem 2D Structure loader
 *  3. Interactive HTML5 Canvas Laboratory Apparatus Simulator (top workbench + inline card drawer)
 */

(function () {
  "use strict";

  const payloadEl = document.getElementById("reactions-payload-json");
  if (!payloadEl) return;
  const PAYLOAD = JSON.parse(payloadEl.textContent);
  const REACTIONS = PAYLOAD.reactions || [];
  const CATEGORIES = PAYLOAD.categories || [];
  const RXN_BY_ID = new Map(REACTIONS.map((r) => [r.id, r]));

  // Apparatus human-readable labels
  const APPARATUS_LABELS = {
    gas_synthesis: "Gas Eudiometer & Spark Igniter",
    industrial_reactor: "Catalytic High-Pressure Reactor",
    bunsen_crucible: "Bunsen Burner & Crucible Assembly",
    thermal_tube: "Heated Test Tube & Gas Delivery Rig",
    volcano: "Exothermic Decomposition Crucible",
    electrolysis: "Hoffmann Electrolysis Voltameter",
    photochemical: "UV Photochemical Exposure Stage",
    flame_combustion: "Combustion Burner & Condenser Train",
    calorimeter: "Calorimeter & Digital Thermocouple",
    acid_metal_flask: "Acid–Metal Flask & Gas Syringe",
    metal_displacement: "Single-Displacement Deposition Beaker",
    halogen_displacement: "Two-Phase Halogen Extraction Cylinder",
    alkali_water: "Pneumatic Trough & Alkali Shield",
    precipitation: "Precipitation Beaker & Dropper Pipet",
    titration: "Burette, Stir Plate & Digital pH Meter",
    equilibrium_beaker: "Thermostated Equilibrium Vessel",
    gas_evolution: "Gas-Evolution Flask & Diagnostic Trap",
    redox_titration: "Redox Burette & Potentiometric Cell",
    fume_hood_nitric: "Ventilated Fume Hood & Nitric Vessel",
    voltaic_cell: "Galvanic Half-Cells, Salt Bridge & Voltmeter",
    complex_ion: "Coordination Complexation Beaker",
    thermite: "Aluminothermic Crucible & Sand Mold",
    kinetics_spectrometer: "UV-Vis Spectrophotometer & Rate Logger",
  };

  // Application State
  const state = {
    selectedCat: 1,
    activeFilter: "all",
    searchQuery: "",
    activeRxnId: 1,
    playing: true,
    progress: 0.0, // 0..1
    speed: 1.0,
    pulseBoost: 0.0,
    showMicro: true,
    showPubchem: true,
    lastFrameTime: performance.now(),
  };

  // =========================================================================
  // 1. SVG Chemical Specimen & 2D Molecular Geometry Generators
  // =========================================================================

  function escapeHtml(str) {
    return String(str || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function buildVesselSvg(chem) {
    const c = chem.color || "#38bdf8";
    const v = chem.vessel || "solution";

    if (v === "gas") {
      return `<svg class="chem-vessel-svg" viewBox="0 0 64 64" aria-hidden="true">
        <rect x="20" y="16" width="24" height="40" rx="8" fill="#2e2e2e" stroke="#737373" stroke-width="1.6"/>
        <rect x="22" y="20" width="20" height="32" rx="6" fill="${c}" fill-opacity="0.45"/>
        <rect x="28" y="9" width="8" height="7" rx="2" fill="#a3a3a3"/>
        <circle cx="42" cy="12" r="5" fill="#1f1f1f" stroke="#d4d4d4" stroke-width="1.3"/>
        <line x1="42" y1="12" x2="45" y2="9" stroke="#ef4444" stroke-width="1.3"/>
        <circle cx="28" cy="30" r="2.2" fill="${c}" opacity="0.9"/>
        <circle cx="35" cy="26" r="1.8" fill="${c}" opacity="0.8"/>
        <circle cx="33" cy="38" r="2.4" fill="${c}" opacity="0.85"/>
        <circle cx="27" cy="43" r="1.7" fill="${c}" opacity="0.75"/>
      </svg>`;
    }

    if (v === "metal") {
      return `<svg class="chem-vessel-svg" viewBox="0 0 64 64" aria-hidden="true">
        <ellipse cx="32" cy="48" rx="24" ry="7" fill="#1f1f1f" stroke="#555555" stroke-width="1.4"/>
        <polygon points="16,44 24,24 46,24 50,44" fill="${c}" stroke="#fafafa" stroke-width="1" stroke-opacity="0.45"/>
        <polygon points="24,24 29,18 49,18 46,24" fill="#ffffff" fill-opacity="0.32"/>
        <line x1="26" y1="28" x2="36" y2="40" stroke="#ffffff" stroke-width="1.6" stroke-opacity="0.55" stroke-linecap="round"/>
      </svg>`;
    }

    if (v === "crystal" || v === "powder") {
      const isCrystal = v === "crystal";
      return `<svg class="chem-vessel-svg" viewBox="0 0 64 64" aria-hidden="true">
        <path d="M8,44 Q32,56 56,44" fill="none" stroke="#a3a3a3" stroke-width="2.2" stroke-linecap="round"/>
        <ellipse cx="32" cy="44" rx="23" ry="5.5" fill="#2e2e2e" fill-opacity="0.7"/>
        ${
          isCrystal
            ? `<polygon points="20,43 26,22 33,43" fill="${c}" stroke="#ffffff" stroke-width="0.8" stroke-opacity="0.5"/>
               <polygon points="29,44 36,18 44,44" fill="${c}" stroke="#ffffff" stroke-width="0.8" stroke-opacity="0.6"/>
               <polygon points="15,44 21,30 27,44" fill="${c}" fill-opacity="0.85"/>
               <polygon points="39,44 45,27 50,44" fill="${c}" fill-opacity="0.9"/>`
            : `<path d="M14,44 Q32,20 50,44 Z" fill="${c}" stroke="#ffffff" stroke-width="0.7" stroke-opacity="0.35"/>
               <circle cx="26" cy="36" r="1.3" fill="#ffffff" fill-opacity="0.5"/>
               <circle cx="35" cy="33" r="1.2" fill="#ffffff" fill-opacity="0.45"/>
               <circle cx="31" cy="40" r="1.4" fill="#ffffff" fill-opacity="0.4"/>`
        }
      </svg>`;
    }

    if (v === "vial") {
      return `<svg class="chem-vessel-svg" viewBox="0 0 64 64" aria-hidden="true">
        <rect x="24" y="10" width="16" height="6" rx="2" fill="#f59e0b"/>
        <path d="M26,16 L26,22 L18,28 L18,54 Q18,57 21,57 L43,57 Q46,57 46,54 L46,28 L38,22 L38,16 Z"
              fill="#1f1f1f" stroke="#a3a3a3" stroke-width="1.6"/>
        <path d="M19.5,35 L44.5,35 L44.5,53.5 Q44.5,55.5 42.5,55.5 L21.5,55.5 Q19.5,55.5 19.5,53.5 Z"
              fill="${c}" fill-opacity="0.78"/>
        <ellipse cx="32" cy="35" rx="12.5" ry="2.2" fill="#ffffff" fill-opacity="0.35"/>
      </svg>`;
    }

    // Default: laboratory graduated beaker with colored solution
    return `<svg class="chem-vessel-svg" viewBox="0 0 64 64" aria-hidden="true">
      <path d="M14,14 L18,14 L18,52 Q18,56 22,56 L44,56 Q48,56 48,52 L48,14 L50,14"
            fill="none" stroke="#d4d4d4" stroke-width="1.8" stroke-linecap="round"/>
      <path d="M19.5,28 L46.5,28 L46.5,51.5 Q46.5,54.5 43.5,54.5 L22.5,54.5 Q19.5,54.5 19.5,51.5 Z"
            fill="${c}" fill-opacity="0.72"/>
      <ellipse cx="33" cy="28" rx="13.5" ry="2.5" fill="${c}" stroke="#ffffff" stroke-width="0.7" stroke-opacity="0.5"/>
      <line x1="40" y1="22" x2="45" y2="22" stroke="#a3a3a3" stroke-width="1.2"/>
      <line x1="40" y1="32" x2="45" y2="32" stroke="#a3a3a3" stroke-width="1.2"/>
      <line x1="40" y1="42" x2="45" y2="42" stroke="#a3a3a3" stroke-width="1.2"/>
    </svg>`;
  }

  function buildGeometrySvg(chem) {
    const c = chem.color || "#38bdf8";
    const g = chem.geom || "tetrahedral";

    if (g === "diatomic") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <line x1="19" y1="30" x2="45" y2="30" stroke="#a3a3a3" stroke-width="3"/>
        <line x1="19" y1="35" x2="45" y2="35" stroke="#a3a3a3" stroke-width="3"/>
        <circle cx="19" cy="32.5" r="10" fill="${c}" stroke="#ffffff" stroke-width="1"/>
        <circle cx="45" cy="32.5" r="10" fill="${c}" stroke="#ffffff" stroke-width="1"/>
      </svg>`;
    }

    if (g === "bent") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <line x1="32" y1="22" x2="16" y2="44" stroke="#d4d4d4" stroke-width="3"/>
        <line x1="32" y1="22" x2="48" y2="44" stroke="#d4d4d4" stroke-width="3"/>
        <circle cx="32" cy="22" r="10" fill="#ef4444" stroke="#ffffff" stroke-width="1"/>
        <circle cx="16" cy="44" r="7" fill="${c}" stroke="#ffffff" stroke-width="1"/>
        <circle cx="48" cy="44" r="7" fill="${c}" stroke="#ffffff" stroke-width="1"/>
      </svg>`;
    }

    if (g === "linear3") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <line x1="12" y1="30" x2="52" y2="30" stroke="#d4d4d4" stroke-width="2.5"/>
        <line x1="12" y1="34" x2="52" y2="34" stroke="#d4d4d4" stroke-width="2.5"/>
        <circle cx="12" cy="32" r="7.5" fill="#ef4444"/>
        <circle cx="32" cy="32" r="9" fill="${c}" stroke="#ffffff" stroke-width="1"/>
        <circle cx="52" cy="32" r="7.5" fill="#ef4444"/>
      </svg>`;
    }

    if (g === "pyramidal" || g === "trigonal") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <line x1="32" y1="24" x2="14" y2="46" stroke="#d4d4d4" stroke-width="2.6"/>
        <line x1="32" y1="24" x2="32" y2="50" stroke="#d4d4d4" stroke-width="2.6"/>
        <line x1="32" y1="24" x2="50" y2="46" stroke="#d4d4d4" stroke-width="2.6"/>
        <circle cx="32" cy="24" r="9.5" fill="${c}" stroke="#ffffff" stroke-width="1"/>
        <circle cx="14" cy="46" r="6.5" fill="#e5e5e5"/>
        <circle cx="32" cy="50" r="6.5" fill="#e5e5e5"/>
        <circle cx="50" cy="46" r="6.5" fill="#e5e5e5"/>
      </svg>`;
    }

    if (g === "octahedral") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <line x1="32" y1="10" x2="32" y2="54" stroke="#a3a3a3" stroke-width="2"/>
        <line x1="12" y1="24" x2="52" y2="40" stroke="#a3a3a3" stroke-width="2"/>
        <line x1="12" y1="40" x2="52" y2="24" stroke="#a3a3a3" stroke-width="2"/>
        <circle cx="32" cy="32" r="9.5" fill="${c}" stroke="#ffffff" stroke-width="1.2"/>
        <circle cx="32" cy="10" r="4.8" fill="#38bdf8"/>
        <circle cx="32" cy="54" r="4.8" fill="#38bdf8"/>
        <circle cx="12" cy="24" r="4.8" fill="#38bdf8"/>
        <circle cx="52" cy="40" r="4.8" fill="#38bdf8"/>
        <circle cx="12" cy="40" r="4.8" fill="#38bdf8"/>
        <circle cx="52" cy="24" r="4.8" fill="#38bdf8"/>
      </svg>`;
    }

    if (g === "crystal" || g === "ionic" || g === "metal") {
      return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
        <rect x="16" y="16" width="22" height="22" fill="none" stroke="#737373" stroke-width="1.4"/>
        <rect x="26" y="26" width="22" height="22" fill="none" stroke="#a3a3a3" stroke-width="1.4"/>
        <line x1="16" y1="16" x2="26" y2="26" stroke="#737373" stroke-width="1.4"/>
        <line x1="38" y1="16" x2="48" y2="26" stroke="#737373" stroke-width="1.4"/>
        <line x1="16" y1="38" x2="26" y2="48" stroke="#737373" stroke-width="1.4"/>
        <line x1="38" y1="38" x2="48" y2="48" stroke="#737373" stroke-width="1.4"/>
        <circle cx="16" cy="16" r="4.5" fill="${c}"/>
        <circle cx="38" cy="16" r="4" fill="#e5e5e5"/>
        <circle cx="16" cy="38" r="4" fill="#e5e5e5"/>
        <circle cx="38" cy="38" r="4.5" fill="${c}"/>
        <circle cx="26" cy="26" r="4" fill="#e5e5e5"/>
        <circle cx="48" cy="26" r="4.5" fill="${c}"/>
        <circle cx="26" cy="48" r="4.5" fill="${c}"/>
        <circle cx="48" cy="48" r="4" fill="#e5e5e5"/>
      </svg>`;
    }

    // Default tetrahedral / organic ball-and-stick
    return `<svg class="chem-geom-svg" viewBox="0 0 64 64" aria-hidden="true">
      <line x1="32" y1="32" x2="32" y2="11" stroke="#d4d4d4" stroke-width="2.5"/>
      <line x1="32" y1="32" x2="13" y2="46" stroke="#d4d4d4" stroke-width="2.5"/>
      <line x1="32" y1="32" x2="51" y2="46" stroke="#d4d4d4" stroke-width="2.5"/>
      <line x1="32" y1="32" x2="42" y2="24" stroke="#a3a3a3" stroke-width="2"/>
      <circle cx="32" cy="32" r="9" fill="${c}" stroke="#ffffff" stroke-width="1"/>
      <circle cx="32" cy="11" r="5.5" fill="#e5e5e5"/>
      <circle cx="13" cy="46" r="5.5" fill="#e5e5e5"/>
      <circle cx="51" cy="46" r="5.5" fill="#e5e5e5"/>
      <circle cx="43" cy="23" r="4.5" fill="#a3a3a3"/>
    </svg>`;
  }

  function buildChemicalCardHtml(chem) {
    const vesselSvg = buildVesselSvg(chem);
    const geomSvg = buildGeometrySvg(chem);
    const hasCid = Boolean(chem.cid) && state.showPubchem;
    const pubchemUrl = hasCid
      ? `https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/${chem.cid}/PNG?image_size=120x120`
      : "";

    return `<div class="chem-card" title="${escapeHtml(chem.name)} (${escapeHtml(chem.formula)})">
      <div class="chem-visual-row">
        ${vesselSvg}
        ${
          hasCid
            ? `<img class="chem-pubchem-img" src="${pubchemUrl}" alt="2D structure of ${escapeHtml(chem.name)}" loading="lazy" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
               <span style="display:none">${geomSvg}</span>`
            : geomSvg
        }
      </div>
      <div class="chem-info-head">
        <span class="chem-formula">${escapeHtml(chem.formula)}</span>
        <span class="chem-state-badge">(${escapeHtml(chem.state)})</span>
      </div>
      <div class="chem-name">${escapeHtml(chem.name)}</div>
      <div class="chem-appearance">${escapeHtml(chem.appearance)}</div>
    </div>`;
  }

  // =========================================================================
  // 2. KaTeX Helper & Lazy Equation Rendering
  // =========================================================================

  function renderTexToElement(el, tex, displayMode = false) {
    if (!el || !tex) return;
    if (window.katex) {
      try {
        window.katex.render(tex, el, {
          throwOnError: false,
          displayMode: displayMode,
          strict: false,
        });
        el.dataset.rendered = "1";
        return;
      } catch (_err) {
        // Fallback to readable text
      }
    }
    el.textContent = tex;
  }

  const katexObserver =
    "IntersectionObserver" in window
      ? new IntersectionObserver(
          (entries, obs) => {
            for (const entry of entries) {
              if (entry.isIntersecting) {
                const container = entry.target;
                container.querySelectorAll("[data-tex]").forEach((node) => {
                  if (!node.dataset.rendered) {
                    renderTexToElement(node, node.dataset.tex, false);
                  }
                });
                obs.unobserve(container);
              }
            }
          },
          { rootMargin: "320px 0px" }
        )
      : null;

  function hydrateKatexInContainer(container) {
    if (!container) return;
    container.querySelectorAll("[data-tex]").forEach((node) => {
      if (!node.dataset.rendered) {
        renderTexToElement(node, node.dataset.tex, false);
      }
    });
  }

  // =========================================================================
  // 3. Section Views (one section per view), Filters, Search & Cards
  // =========================================================================

  const CAT_BY_ID = new Map(CATEGORIES.map((c) => [Number(c.id), c]));
  const SUMMARY_SECTION_ID = 12;
  const TOTAL_SECTIONS = CATEGORIES.length;

  /** Category title without its leading "N. " (the number is shown separately in headers). */
  function sectionTitle(cat) {
    return String(cat?.title || "").replace(/^\s*\d+\.\s*/, "");
  }

  /** Reactions that belong to a section. Section 12 lists the added 1st-year essentials. */
  function reactionsInSection(catId) {
    const cid = Number(catId);
    if (cid === SUMMARY_SECTION_ID) return REACTIONS.filter((r) => r.added_essential);
    return REACTIONS.filter((r) => Number(r.category_id) === cid);
  }

  function matchesFeatureFilter(rxn) {
    const f = state.activeFilter;
    const eqs = rxn.equations || {};
    const lab = rxn.lab || {};
    if (f === "spec" && rxn.added_essential) return false;
    if (f === "added" && !rxn.added_essential) return false;
    if (f === "ionic" && !eqs.net_ionic && !eqs.complete_ionic) return false;
    if (f === "redox" && !eqs.reduction_half && !eqs.oxidation_half) return false;
    if (f === "precip" && !lab.precipitate_color) return false;
    if (f === "gas" && !lab.gas_label) return false;
    if (f === "thermal" && !lab.flame_color && (lab.temperature_c || 25) <= 60) return false;
    return true;
  }

  function matchesSearch(rxn) {
    const q = state.searchQuery.toLowerCase().trim();
    if (!q) return true;
    if (`#${rxn.id}` === q || String(rxn.id) === q) return true;
    const eqs = rxn.equations || {};
    const lab = rxn.lab || {};
    const haystack = [
      `#${rxn.id}`,
      rxn.title,
      rxn.subcategory,
      rxn.category_title,
      rxn.explanation,
      lab.observation,
      eqs.molecular,
      eqs.net_ionic || "",
      ...(rxn.chemicals || []),
      ...(rxn.chemical_details || []).map((c) => `${c.name} ${c.formula}`),
    ]
      .join(" ")
      .toLowerCase();
    return haystack.includes(q);
  }

  /** Large, high-contrast header shown at the start of every section (and reaction) view. */
  function buildSectionBannerHtml(cat, { compact = false, headingId = "section-heading" } = {}) {
    const idx = Number(cat.id);
    const list = reactionsInSection(idx);
    const nIonic = list.filter((r) => r.equations?.net_ionic || r.equations?.complete_ionic).length;
    const nRedox = list.filter((r) => r.equations?.reduction_half || r.equations?.oxidation_half).length;
    const prevCat = CAT_BY_ID.get(idx - 1);
    const nextCat = CAT_BY_ID.get(idx + 1);

    const stats =
      idx === SUMMARY_SECTION_ID
        ? `<span class="section-banner-stat"><strong>${PAYLOAD.canonical_summary?.length || 9}</strong> reaction archetypes</span>
           <span class="section-banner-stat"><strong>${list.length}</strong> added 1st-year reactions</span>`
        : `<span class="section-banner-stat"><strong>${list.length}</strong> reactions</span>
           ${nIonic ? `<span class="section-banner-stat"><strong>${nIonic}</strong> with ionic equations</span>` : ""}
           ${nRedox ? `<span class="section-banner-stat"><strong>${nRedox}</strong> with half-reactions</span>` : ""}`;

    const nav = compact
      ? ""
      : `<div class="section-banner-nav">
          ${
            prevCat
              ? `<a class="section-nav-btn" href="#/section/${prevCat.id}" title="${escapeHtml(sectionTitle(prevCat))}">← Section ${prevCat.id}</a>`
              : `<span class="section-nav-btn is-disabled" aria-disabled="true">← Section</span>`
          }
          ${
            nextCat
              ? `<a class="section-nav-btn" href="#/section/${nextCat.id}" title="${escapeHtml(sectionTitle(nextCat))}">Section ${nextCat.id} →</a>`
              : `<span class="section-nav-btn is-disabled" aria-disabled="true">Section →</span>`
          }
        </div>`;

    return `
      <div class="section-banner-num" aria-hidden="true">${idx}</div>
      <div class="section-banner-body">
        <div class="section-banner-eyebrow">Section ${idx} of ${TOTAL_SECTIONS} · ${escapeHtml(cat.short || "")}</div>
        <h2 class="section-banner-title" id="${headingId}" tabindex="-1">${escapeHtml(sectionTitle(cat))}</h2>
        ${compact ? "" : `<p class="section-banner-desc">${escapeHtml(cat.description || "")}</p>`}
        <div class="section-banner-meta">
          <span class="section-banner-pattern">${escapeHtml(cat.pattern || "")}</span>
          ${stats}
        </div>
      </div>
      ${nav}`;
  }

  function buildEquationRowsHtml(rxn, { full = true } = {}) {
    const eqs = rxn.equations || {};
    const rows = [
      [rxn.category_id === 11 ? "Law / Expression" : "Molecular Equation", "", eqs.molecular, true],
      ["Complete Ionic", "tag-complete", full ? eqs.complete_ionic : null],
      ["Net Ionic", "tag-net", eqs.net_ionic],
      ["Reduction Half", "tag-half", full ? eqs.reduction_half : null],
      ["Oxidation Half", "tag-half", full ? eqs.oxidation_half : null],
      ["Governing / Thermo", "tag-gov", full ? eqs.governing : null],
    ];
    return rows
      .filter(([, , tex]) => Boolean(tex))
      .map(
        ([label, cls, tex, primary]) => `<div class="eq-row ${primary ? "eq-primary" : ""}">
          <span class="eq-tag ${cls}">${label}</span>
          <span class="eq-math" data-tex="${escapeHtml(tex)}"></span>
        </div>`
      )
      .join("");
  }

  /** Compact card used in section views — clicking opens the dedicated reaction view. */
  function buildReactionCardHtml(rxn) {
    const lab = rxn.lab || {};
    const appLabel = APPARATUS_LABELS[lab.apparatus] || "Virtual Chemistry Apparatus";
    const chips = (rxn.chemical_details || [])
      .slice(0, 6)
      .map((c) => `<span class="chem-chip" title="${escapeHtml(c.name)}">${escapeHtml(c.formula)}</span>`)
      .join("");

    return `<article class="rxn-card rxn-card--compact" id="rxn-card-${rxn.id}" data-rxn-id="${rxn.id}">
      <div class="rxn-card-top">
        <div class="rxn-meta-badges">
          <span class="rxn-num-badge">#${rxn.id}</span>
          <span class="rxn-subcat-badge">${escapeHtml(rxn.subcategory)}</span>
          ${rxn.added_essential ? `<span class="rxn-added-badge">★ Added 1st-Year Essential</span>` : ""}
        </div>
      </div>

      <h3 class="rxn-title"><a class="rxn-title-link" href="#/reaction/${rxn.id}">${escapeHtml(rxn.title)}</a></h3>

      <div class="rxn-equations-stack">
        ${buildEquationRowsHtml(rxn, { full: false })}
      </div>

      <div class="rxn-explain-pane">
        <div class="pane-label">What This Reaction Does</div>
        <p>${escapeHtml(rxn.explanation)}</p>
      </div>

      <div class="rxn-card-foot">
        <div class="chem-chip-row">${chips}</div>
        <span class="rxn-apparatus-pill">⚗️ ${escapeHtml(appLabel)}</span>
        <a class="btn-sim-rxn" href="#/reaction/${rxn.id}">Open Reaction &amp; Lab Animation →</a>
      </div>
    </article>`;
  }

  function hydrateCards(root) {
    root.querySelectorAll(".rxn-card").forEach((card) => {
      if (katexObserver) katexObserver.observe(card);
      else hydrateKatexInContainer(card);
    });
  }

  function syncNavActive(catId) {
    document.querySelectorAll("[data-cat]").forEach((el) => {
      const isActive = String(el.dataset.cat) === String(catId);
      el.classList.toggle("active", isActive);
      if (isActive) el.setAttribute("aria-current", "true");
      else el.removeAttribute("aria-current");
    });
  }

  function renderSectionView(catId) {
    const cat = CAT_BY_ID.get(Number(catId)) || CATEGORIES[0];
    state.selectedCat = Number(cat.id);
    syncNavActive(cat.id);

    const bannerEl = document.getElementById("section-banner");
    const feedEl = document.getElementById("reactions-feed-container");
    const counterEl = document.getElementById("rxn-results-counter");
    const summaryEl = document.getElementById("category-section-12");
    const pagerEl = document.getElementById("section-pager");
    if (!feedEl || !bannerEl) return;

    const q = state.searchQuery.trim();

    // ---- Global search results (grouped by section, each with a visible header) ----
    if (q) {
      bannerEl.style.setProperty("--cat-color", "#9ca3af");
      bannerEl.innerHTML = `
        <div class="section-banner-num" aria-hidden="true">⌕</div>
        <div class="section-banner-body">
          <div class="section-banner-eyebrow">Search across all sections</div>
          <h2 class="section-banner-title" id="section-heading" tabindex="-1">Results for “${escapeHtml(q)}”</h2>
          <p class="section-banner-desc">Clear the search box to return to Section ${cat.id}: ${escapeHtml(sectionTitle(cat))}.</p>
        </div>`;
      if (summaryEl) summaryEl.hidden = true;

      let total = 0;
      let html = "";
      for (const c of CATEGORIES) {
        if (Number(c.id) === SUMMARY_SECTION_ID) continue;
        const list = reactionsInSection(c.id).filter((r) => matchesFeatureFilter(r) && matchesSearch(r));
        if (!list.length) continue;
        total += list.length;
        html += `<section class="search-group">
          <a class="search-group-header" href="#/section/${c.id}" style="--cat-color: ${c.color}">
            <span class="search-group-num">${c.id}</span>
            <span class="search-group-title">Section ${c.id} · ${escapeHtml(sectionTitle(c))}</span>
            <span class="search-group-count">${list.length} match${list.length === 1 ? "" : "es"}</span>
          </a>
          <div class="reactions-grid">${list.map(buildReactionCardHtml).join("")}</div>
        </section>`;
      }
      if (counterEl) counterEl.innerHTML = `Found <strong>${total}</strong> of ${REACTIONS.length} reactions in all sections`;
      feedEl.innerHTML =
        html ||
        `<div class="empty-state"><h3>No reactions match “${escapeHtml(q)}”</h3><p>Try a formula (e.g. AgCl), a name (e.g. Haber) or a reaction number.</p></div>`;
      if (pagerEl) pagerEl.innerHTML = "";
      hydrateCards(feedEl);
      return;
    }

    // ---- Single section view ----
    bannerEl.style.setProperty("--cat-color", cat.color);
    bannerEl.innerHTML = buildSectionBannerHtml(cat);

    const isSummary = Number(cat.id) === SUMMARY_SECTION_ID;
    if (summaryEl) summaryEl.hidden = !isSummary;

    const all = reactionsInSection(cat.id);
    const list = all.filter(matchesFeatureFilter);
    if (counterEl) {
      counterEl.innerHTML = `Showing <strong>${list.length}</strong> of ${all.length} reactions in Section ${cat.id}`;
    }

    let html = "";
    if (isSummary) {
      html += `<h3 class="feed-subheading">★ Added 1st-Year Essential Reactions</h3>`;
    }
    html += list.length
      ? `<div class="reactions-grid">${list.map(buildReactionCardHtml).join("")}</div>`
      : `<div class="empty-state"><h3>No reactions in this section match the current filter</h3><p>Choose “All Equations” to see every reaction in Section ${cat.id}.</p></div>`;
    feedEl.innerHTML = html;
    hydrateCards(feedEl);

    // Bottom pager — previous / next section
    if (pagerEl) {
      const prevCat = CAT_BY_ID.get(Number(cat.id) - 1);
      const nextCat = CAT_BY_ID.get(Number(cat.id) + 1);
      pagerEl.innerHTML = `
        ${
          prevCat
            ? `<a class="pager-card pager-prev" href="#/section/${prevCat.id}" style="--cat-color:${prevCat.color}">
                 <small>← Previous section</small><strong>${prevCat.id}. ${escapeHtml(sectionTitle(prevCat))}</strong></a>`
            : `<span></span>`
        }
        ${
          nextCat
            ? `<a class="pager-card pager-next" href="#/section/${nextCat.id}" style="--cat-color:${nextCat.color}">
                 <small>Next section →</small><strong>${nextCat.id}. ${escapeHtml(sectionTitle(nextCat))}</strong></a>`
            : `<span></span>`
        }`;
    }
  }

  // =========================================================================
  // 4. Reaction View (dedicated view per reaction) & Workbench Controller
  // =========================================================================

  function selectReactionForLab(rxnId) {
    const rxn = RXN_BY_ID.get(Number(rxnId));
    if (!rxn) return;
    state.activeRxnId = rxn.id;
    state.progress = 0.05;
    state.playing = true;
    state.pulseBoost = 1.0;
    updateTopWorkbenchMetadata(rxn);
  }

  function renderReactionDetail(rxn) {
    const detailEl = document.getElementById("reaction-detail");
    if (!detailEl) return;
    const chems = rxn.chemical_details || [];
    detailEl.innerHTML = `
      <div class="detail-panel">
        <h3 class="detail-heading">All Equations for Reaction #${rxn.id}</h3>
        <div class="rxn-equations-stack">${buildEquationRowsHtml(rxn, { full: true })}</div>
      </div>
      <div class="detail-panel">
        <h3 class="detail-heading">Chemical Specimens &amp; Molecular Structures (${chems.length} species)</h3>
        <div class="chem-specimens-grid">${chems.map(buildChemicalCardHtml).join("")}</div>
      </div>`;
    hydrateKatexInContainer(detailEl);
  }

  function renderReactionView(rxnId) {
    const rxn = RXN_BY_ID.get(Number(rxnId)) || REACTIONS[0];
    if (!rxn) return;
    const cat = CAT_BY_ID.get(Number(rxn.category_id)) || CATEGORIES[0];
    // Remember which section the user came from (Section 12 lists added reactions)
    const fromCat =
      Number(state.selectedCat) === SUMMARY_SECTION_ID && rxn.added_essential ? CAT_BY_ID.get(SUMMARY_SECTION_ID) : cat;
    syncNavActive(fromCat.id);
    state.selectedCat = Number(fromCat.id);

    const siblings = reactionsInSection(fromCat.id);
    const pos = siblings.findIndex((r) => r.id === rxn.id);
    const prevRxn = pos > 0 ? siblings[pos - 1] : null;
    const nextRxn = pos >= 0 && pos < siblings.length - 1 ? siblings[pos + 1] : null;

    const crumbEl = document.getElementById("reaction-breadcrumb");
    if (crumbEl) {
      crumbEl.innerHTML = `
        <a class="breadcrumb-back" href="#/section/${fromCat.id}">← Back to Section ${fromCat.id}: ${escapeHtml(sectionTitle(fromCat))}</a>
        <span class="breadcrumb-pos">Reaction ${pos + 1} of ${siblings.length} in this section</span>`;
    }

    const bannerEl = document.getElementById("reaction-section-banner");
    if (bannerEl) {
      bannerEl.style.setProperty("--cat-color", fromCat.color);
      bannerEl.innerHTML = buildSectionBannerHtml(fromCat, { compact: true, headingId: "reaction-section-heading" });
    }

    selectReactionForLab(rxn.id);
    renderReactionDetail(rxn);

    const pagerEl = document.getElementById("reaction-pager");
    if (pagerEl) {
      const nextSection = CAT_BY_ID.get(Number(fromCat.id) + 1);
      pagerEl.innerHTML = `
        ${
          prevRxn
            ? `<a class="pager-card pager-prev" href="#/reaction/${prevRxn.id}" style="--cat-color:${fromCat.color}">
                 <small>← Previous reaction</small><strong>#${prevRxn.id} · ${escapeHtml(prevRxn.title)}</strong></a>`
            : `<a class="pager-card pager-prev" href="#/section/${fromCat.id}" style="--cat-color:${fromCat.color}">
                 <small>← Start of section</small><strong>Back to Section ${fromCat.id} overview</strong></a>`
        }
        ${
          nextRxn
            ? `<a class="pager-card pager-next" href="#/reaction/${nextRxn.id}" style="--cat-color:${fromCat.color}">
                 <small>Next reaction →</small><strong>#${nextRxn.id} · ${escapeHtml(nextRxn.title)}</strong></a>`
            : nextSection
              ? `<a class="pager-card pager-next" href="#/section/${nextSection.id}" style="--cat-color:${nextSection.color}">
                   <small>End of section — next section →</small><strong>${nextSection.id}. ${escapeHtml(sectionTitle(nextSection))}</strong></a>`
              : `<span></span>`
        }`;
    }
  }

  function syncPlayButtonText() {
    const playBtn = document.getElementById("wb-btn-play");
    if (playBtn) {
      playBtn.textContent = state.playing ? "Pause Animation" : "Resume Animation";
    }
  }

  function updateTopWorkbenchMetadata(rxn) {
    const lab = rxn.lab || {};
    const eqs = rxn.equations || {};
    const appLabel = APPARATUS_LABELS[lab.apparatus] || "Virtual Chemistry Apparatus";

    const catBadge = document.getElementById("wb-cat-badge");
    const appBadge = document.getElementById("wb-apparatus-badge");
    const titleEl = document.getElementById("wb-title");
    const eqBar = document.getElementById("wb-equation-bar");
    const obsEl = document.getElementById("wb-observation-text");
    const expEl = document.getElementById("wb-explanation-text");
    const subcatEl = document.getElementById("wb-subcat-readout");
    const signalEl = document.getElementById("wb-signal-readout");

    if (catBadge) catBadge.textContent = rxn.category_title;
    if (appBadge) appBadge.textContent = appLabel;
    if (titleEl) titleEl.textContent = `#${rxn.id} · ${rxn.title}`;
    if (eqBar) renderTexToElement(eqBar, eqs.molecular, false);
    if (obsEl) obsEl.textContent = lab.observation;
    if (expEl) expEl.textContent = rxn.explanation;
    if (subcatEl) subcatEl.textContent = rxn.subcategory;

    let sig = "Aqueous Reaction";
    if (lab.precipitate_color) sig = "Precipitate (s)↓";
    else if (lab.gas_label) sig = `Gas: ${lab.gas_label}↑`;
    else if (lab.flame_color) sig = "Exothermic Flame";
    else if (lab.apparatus === "voltaic_cell") sig = "Galvanic E°_cell";
    else if (lab.apparatus === "titration" || lab.apparatus === "redox_titration") sig = "Volumetric Endpoint";
    else if (lab.apparatus === "complex_ion") sig = "Ligand Field Shift";
    if (signalEl) signalEl.textContent = sig;

    syncPlayButtonText();
  }

  // =========================================================================
  // 4b. Hash Router — #/section/<n> and #/reaction/<id>
  // =========================================================================

  function parseRoute() {
    const h = window.location.hash || "";
    let m = h.match(/^#\/reaction\/(\d+)/);
    if (m && RXN_BY_ID.has(Number(m[1]))) return { view: "reaction", id: Number(m[1]) };
    m = h.match(/^#\/section\/(\d+)/);
    if (m && CAT_BY_ID.has(Number(m[1]))) return { view: "section", cat: Number(m[1]) };
    return { view: "section", cat: Number(state.selectedCat) || 1 };
  }

  function applyRoute({ initial = false } = {}) {
    const route = parseRoute();
    const sectionView = document.getElementById("section-view");
    const reactionView = document.getElementById("reaction-view");

    const update = () => {
      if (route.view === "reaction") {
        if (sectionView) sectionView.hidden = true;
        if (reactionView) reactionView.hidden = false;
        document.body.dataset.view = "reaction";
        clearSearch();
        renderReactionView(route.id);
      } else {
        if (reactionView) reactionView.hidden = true;
        if (sectionView) sectionView.hidden = false;
        document.body.dataset.view = "section";
        renderSectionView(route.cat);
      }
      window.scrollTo({ top: 0, behavior: "instant" });
    };

    const focusHeading = () => {
      const target =
        route.view === "reaction" ? document.getElementById("wb-title") : document.getElementById("section-heading");
      target?.focus({ preventScroll: true });
    };

    if (initial || !document.startViewTransition) {
      update();
      if (!initial) focusHeading();
      return;
    }
    const transition = document.startViewTransition(update);
    transition.finished.finally(focusHeading);
  }

  function navigateTo(hash) {
    if (window.location.hash === hash) applyRoute();
    else window.location.hash = hash;
  }

  function clearSearch() {
    state.searchQuery = "";
    const searchInput = document.getElementById("rxn-search-input");
    const clearBtn = document.getElementById("rxn-search-clear");
    if (searchInput) searchInput.value = "";
    if (clearBtn) clearBtn.hidden = true;
  }

  // =========================================================================
  // 5. HTML5 Canvas Laboratory Apparatus Renderer (23 Instrument Archetypes)
  // =========================================================================

  function hexToRgba(hex, alpha) {
    const clean = String(hex || "#38bdf8").replace("#", "");
    const num = parseInt(clean.length === 3 ? clean.replace(/(.)/g, "$1$1") : clean, 16) || 0x38bdf8;
    const r = (num >> 16) & 255;
    const g = (num >> 8) & 255;
    const b = num & 255;
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
  }

  function lerpColor(hexA, hexB, t) {
    const parse = (h) => {
      const c = String(h || "#38bdf8").replace("#", "");
      const n = parseInt(c.length === 3 ? c.replace(/(.)/g, "$1$1") : c, 16) || 0x38bdf8;
      return [(n >> 16) & 255, (n >> 8) & 255, n & 255];
    };
    const [r1, g1, b1] = parse(hexA);
    const [r2, g2, b2] = parse(hexB);
    const u = Math.max(0, Math.min(1, t));
    const r = Math.round(r1 + (r2 - r1) * u);
    const g = Math.round(g1 + (g2 - g1) * u);
    const b = Math.round(b1 + (b2 - b1) * u);
    return `rgb(${r}, ${g}, ${b})`;
  }

  function drawCalloutLabel(ctx, x, y, text, targetX, targetY, color = "#38bdf8") {
    ctx.save();
    if (targetX !== undefined && targetY !== undefined) {
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(targetX, targetY);
      ctx.strokeStyle = hexToRgba(color, 0.65);
      ctx.lineWidth = 1.3;
      ctx.stroke();

      ctx.beginPath();
      ctx.arc(targetX, targetY, 3, 0, Math.PI * 2);
      ctx.fillStyle = color;
      ctx.fill();
    }
    ctx.font = "600 11.5px Inter, system-ui, sans-serif";
    const padX = 7;
    const w = ctx.measureText(text).width + padX * 2;
    const h = 21;
    ctx.fillStyle = "rgba(18, 18, 18, 0.88)";
    ctx.strokeStyle = hexToRgba(color, 0.6);
    ctx.lineWidth = 1.1;
    ctx.beginPath();
    ctx.roundRect(x - w / 2, y - h / 2, w, h, 5);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#f4f4f4";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, x, y + 0.5);
    ctx.restore();
  }

  function drawBunsenBurner(ctx, cx, baseY, flameColor, intensity, timeSec) {
    ctx.save();
    // Heavy cast-iron base
    ctx.fillStyle = "#404040";
    ctx.strokeStyle = "#737373";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.roundRect(cx - 32, baseY - 12, 64, 12, 4);
    ctx.fill();
    ctx.stroke();

    // Gas inlet tube
    ctx.beginPath();
    ctx.moveTo(cx - 20, baseY - 16);
    ctx.lineTo(cx - 52, baseY - 16);
    ctx.strokeStyle = "#f59e0b";
    ctx.lineWidth = 4;
    ctx.stroke();

    // Chimney barrel & air collar
    ctx.fillStyle = "#555555";
    ctx.fillRect(cx - 8, baseY - 68, 16, 56);
    ctx.fillStyle = "#a3a3a3";
    ctx.fillRect(cx - 11, baseY - 26, 22, 10);

    // Animated outer + inner roaring cone flame
    if (intensity > 0.02) {
      const flicker = Math.sin(timeSec * 19) * 3.5 + Math.cos(timeSec * 11) * 2;
      const hOuter = (42 + flicker) * Math.min(1.2, intensity + 0.35);
      const col = flameColor || "#38bdf8";

      const grad = ctx.createRadialGradient(cx, baseY - 72, 3, cx, baseY - 70 - hOuter * 0.45, hOuter);
      grad.addColorStop(0, "#ffffff");
      grad.addColorStop(0.35, col);
      grad.addColorStop(1, "rgba(56, 189, 248, 0)");

      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.moveTo(cx - 11, baseY - 68);
      ctx.quadraticCurveTo(cx - 16, baseY - 68 - hOuter * 0.6, cx + flicker * 0.3, baseY - 68 - hOuter);
      ctx.quadraticCurveTo(cx + 16, baseY - 68 - hOuter * 0.6, cx + 11, baseY - 68);
      ctx.closePath();
      ctx.fill();

      // Inner blue reducing cone
      ctx.fillStyle = "rgba(125, 211, 252, 0.85)";
      ctx.beginPath();
      ctx.moveTo(cx - 5, baseY - 68);
      ctx.lineTo(cx, baseY - 68 - hOuter * 0.42);
      ctx.lineTo(cx + 5, baseY - 68);
      ctx.closePath();
      ctx.fill();
    }
    ctx.restore();
  }

  function drawGlassBeaker(ctx, x, y, w, h, liqColor, fillRatio, precipColor, precipRatio, gasLabel, timeSec) {
    ctx.save();
    const liqH = h * Math.max(0.12, Math.min(0.88, fillRatio));
    const liqTop = y + h - liqH;

    // Liquid body
    ctx.fillStyle = hexToRgba(liqColor, 0.56);
    ctx.beginPath();
    ctx.roundRect(x + 4, liqTop, w - 8, liqH - 3, [0, 0, 10, 10]);
    ctx.fill();

    // Liquid meniscus
    ctx.fillStyle = hexToRgba(liqColor, 0.82);
    ctx.beginPath();
    ctx.ellipse(x + w / 2, liqTop, (w - 8) / 2, 5, 0, 0, Math.PI * 2);
    ctx.fill();

    // Precipitate layer settling + falling particles
    if (precipColor && precipRatio > 0.02) {
      const pH = Math.min(26, 6 + precipRatio * 20);
      ctx.fillStyle = precipColor;
      ctx.beginPath();
      ctx.roundRect(x + 6, y + h - pH - 4, w - 12, pH, [4, 4, 9, 9]);
      ctx.fill();

      // Falling precipitate snow crystals
      for (let i = 0; i < 24; i++) {
        const px = x + 14 + ((i * 37) % (w - 28));
        const fall = ((timeSec * 38 + i * 17) % Math.max(12, liqH - pH - 8));
        const py = liqTop + 6 + fall;
        if (py < y + h - pH - 4) {
          ctx.fillStyle = precipColor;
          ctx.beginPath();
          ctx.arc(px, py, 2.3, 0, Math.PI * 2);
          ctx.fill();
        }
      }
    }

    // Gas effervescence bubbles
    if (gasLabel && precipRatio > 0.03) {
      for (let i = 0; i < 18; i++) {
        const bx = x + 16 + ((i * 29) % (w - 32));
        const rise = ((timeSec * 55 + i * 19) % Math.max(16, liqH - 6));
        const by = y + h - 10 - rise;
        ctx.strokeStyle = "rgba(255,255,255,0.8)";
        ctx.fillStyle = "rgba(255,255,255,0.35)";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(bx, by, 2.8 + (i % 2), 0, Math.PI * 2);
        ctx.fill();
        ctx.stroke();
      }
    }

    // Beaker borosilicate outline & graduation ticks
    ctx.strokeStyle = "rgba(226, 232, 240, 0.85)";
    ctx.lineWidth = 2.4;
    ctx.beginPath();
    ctx.moveTo(x - 5, y);
    ctx.lineTo(x + 2, y + 6);
    ctx.lineTo(x + 2, y + h - 10);
    ctx.quadraticCurveTo(x + 2, y + h, x + 12, y + h);
    ctx.lineTo(x + w - 12, y + h);
    ctx.quadraticCurveTo(x + w - 2, y + h, x + w - 2, y + h - 10);
    ctx.lineTo(x + w - 2, y + 6);
    ctx.lineTo(x + w + 4, y);
    ctx.stroke();

    // Graduation markings
    ctx.strokeStyle = "rgba(163, 163, 163, 0.55)";
    ctx.lineWidth = 1.2;
    ctx.font = "10px ui-monospace, monospace";
    ctx.fillStyle = "rgba(203, 213, 225, 0.7)";
    for (let m = 1; m <= 3; m++) {
      const gy = y + h - (h * 0.22 * m);
      ctx.beginPath();
      ctx.moveTo(x + w - 18, gy);
      ctx.lineTo(x + w - 6, gy);
      ctx.stroke();
      ctx.fillText(`${m * 50}mL`, x + w - 46, gy + 3);
    }
    ctx.restore();
  }

  function drawMicroscopicZoomInset(ctx, rxn, prog, timeSec) {
    if (!state.showMicro) return;
    const ix = 615;
    const iy = 22;
    const iw = 225;
    const ih = 152;
    const chems = rxn.chemical_details || [];
    const lab = rxn.lab || {};

    ctx.save();
    ctx.fillStyle = "rgba(12, 12, 12, 0.92)";
    ctx.strokeStyle = "rgba(56, 189, 248, 0.55)";
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.roundRect(ix, iy, iw, ih, 10);
    ctx.fill();
    ctx.stroke();

    // Header bar
    ctx.fillStyle = "rgba(56, 189, 248, 0.16)";
    ctx.beginPath();
    ctx.roundRect(ix + 1, iy + 1, iw - 2, 24, [9, 9, 0, 0]);
    ctx.fill();

    ctx.fillStyle = "#7dd3fc";
    ctx.font = "700 10.5px Inter, system-ui, sans-serif";
    ctx.fillText("🔬 SUBMICROSCOPIC PARTICLE VIEW", ix + 10, iy + 16);

    // Draw dynamic reacting species inside the inset
    const nParticles = Math.max(6, Math.min(12, chems.length * 3));
    for (let i = 0; i < nParticles; i++) {
      const chem = chems[i % Math.max(1, chems.length)] || { formula: "Ion", color: "#38bdf8" };
      const isProduct = i >= nParticles / 2;
      const angle = timeSec * (1.3 + (i % 3) * 0.4) + i * 1.1;
      const rad = 22 + (i % 3) * 16;
      let px = ix + iw / 2 + Math.cos(angle) * rad * 1.3;
      let py = iy + 82 + Math.sin(angle * 1.2) * (rad * 0.65);

      // If precipitation, settle product ions into a crystal lattice at the bottom of inset
      if (lab.precipitate_color && isProduct && prog > 0.3) {
        const colIdx = i % 5;
        const rowIdx = Math.floor((i - nParticles / 2) / 5);
        const targetX = ix + 65 + colIdx * 22;
        const targetY = iy + ih - 22 - rowIdx * 16;
        const blend = Math.min(1, (prog - 0.3) / 0.5);
        px = px * (1 - blend) + targetX * blend;
        py = py * (1 - blend) + targetY * blend;
      }

      ctx.beginPath();
      ctx.arc(px, py, 9.5, 0, Math.PI * 2);
      ctx.fillStyle = chem.color || "#38bdf8";
      ctx.fill();
      ctx.lineWidth = 1;
      ctx.strokeStyle = "#ffffff";
      ctx.stroke();

      ctx.fillStyle = "#1f1f1f";
      ctx.font = "700 7.5px ui-monospace, monospace";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(String(chem.formula || "").slice(0, 5), px, py);
    }

    // Bottom caption inside inset
    ctx.fillStyle = "#a3a3a3";
    ctx.font = "10px Inter, system-ui, sans-serif";
    ctx.textAlign = "left";
    const modeLabel = lab.precipitate_color
      ? "Ionic lattice nucleation (Q_sp > K_sp)"
      : rxn.equations?.reduction_half
      ? "Electron transfer (Ox + n e⁻ → Red)"
      : rxn.category_id === 6
      ? "Proton transfer (H⁺ / OH⁻)"
      : "Molecular collisions & bond rearrangement";
    ctx.fillText(modeLabel, ix + 10, iy + ih - 8);
    ctx.restore();
  }

  function renderLabCanvas(canvas, rxn, prog, timeSec) {
    if (!canvas || !rxn) return;
    const ctx = canvas.getContext("2d");
    const W = canvas.width;
    const H = canvas.height;
    const lab = rxn.lab || {};
    const app = lab.apparatus || "precipitation";
    const chems = rxn.chemical_details || [];
    const rChem1 = chems[0]?.formula || "Reactant A";
    const rChem2 = chems[1]?.formula || "Reactant B";
    const pChem =
      (lab.precipitate_color && chems.slice(2).find((c) => c.state === "s")?.formula) ||
      chems[chems.length - 1]?.formula ||
      "Product";

    ctx.clearRect(0, 0, W, H);

    // Subtle scientific grid & lab benchtop surface
    ctx.save();
    ctx.strokeStyle = "rgba(163, 163, 163, 0.06)";
    ctx.lineWidth = 1;
    for (let gx = 40; gx < W; gx += 40) {
      ctx.beginPath();
      ctx.moveTo(gx, 0);
      ctx.lineTo(gx, H);
      ctx.stroke();
    }
    for (let gy = 40; gy < H; gy += 40) {
      ctx.beginPath();
      ctx.moveTo(0, gy);
      ctx.lineTo(W, gy);
      ctx.stroke();
    }

    // Lab Benchtop Slate
    ctx.fillStyle = "#1a1a1a";
    ctx.fillRect(0, H - 54, W, 54);
    ctx.strokeStyle = "rgba(56, 189, 248, 0.28)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, H - 54);
    ctx.lineTo(W, H - 54);
    ctx.stroke();
    ctx.restore();

    const benchY = H - 54;
    const mixColor = lerpColor(lab.color_a || "#38bdf8", lab.color_prod || "#38bdf8", prog);

    // Dispatch by laboratory apparatus archetype
    if (app === "titration" || app === "redox_titration") {
      // Ring stand
      ctx.fillStyle = "#555555";
      ctx.fillRect(115, 38, 8, benchY - 38);
      ctx.fillRect(85, benchY - 10, 95, 10);
      // Burette clamp
      ctx.fillStyle = "#a3a3a3";
      ctx.fillRect(123, 86, 68, 6);

      // Graduated Burette
      const bx = 188;
      const by = 32;
      const bw = 22;
      const bh = 165;
      ctx.strokeStyle = "#e5e5e5";
      ctx.lineWidth = 2;
      ctx.strokeRect(bx, by, bw, bh);
      const titrantFill = (1 - prog * 0.65) * (bh - 12);
      ctx.fillStyle = hexToRgba(lab.color_b || "#9333ea", 0.72);
      ctx.fillRect(bx + 2, by + bh - titrantFill - 4, bw - 4, titrantFill);

      // Stopcock valve
      ctx.fillStyle = "#f59e0b";
      ctx.fillRect(bx - 6, by + bh, bw + 12, 7);
      // Falling drops from burette tip
      const dropY = by + bh + 12 + ((timeSec * 140) % 52);
      ctx.fillStyle = lab.color_b || "#38bdf8";
      ctx.beginPath();
      ctx.arc(bx + bw / 2, dropY, 3.5, 0, Math.PI * 2);
      ctx.fill();

      // Magnetic Stirrer Plate
      ctx.fillStyle = "#2e2e2e";
      ctx.strokeStyle = "#737373";
      ctx.beginPath();
      ctx.roundRect(142, benchY - 22, 116, 22, 5);
      ctx.fill();
      ctx.stroke();

      // Erlenmeyer / Beaker on stir plate
      drawGlassBeaker(ctx, 152, benchY - 132, 96, 110, mixColor, 0.48 + prog * 0.2, lab.precipitate_color, prog, lab.gas_label, timeSec);
      // Spinning magnetic stir bar
      const barW = 22 * Math.cos(timeSec * 10);
      ctx.strokeStyle = "#ffffff";
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(200 - barW / 2, benchY - 30);
      ctx.lineTo(200 + barW / 2, benchY - 30);
      ctx.stroke();

      // Live Titration Curve Plot (pH or E vs Volume)
      const px = 335;
      const py = 195;
      const pw = 250;
      const ph = 165;
      ctx.fillStyle = "rgba(18, 18, 18, 0.9)";
      ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
      ctx.beginPath();
      ctx.roundRect(px, py, pw, ph, 10);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#a3a3a3";
      ctx.font = "600 11px Inter, sans-serif";
      ctx.fillText(app === "redox_titration" ? "Potentiometric Curve E (V) vs V_titrant" : "Live pH Titration Curve (Equivalence at 50%)", px + 14, py + 20);

      // Sigmoidal titration curve
      ctx.beginPath();
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.2;
      for (let i = 0; i <= 100; i++) {
        const u = i / 100;
        const sigY = 1 / (1 + Math.exp(-(u - 0.5) * 18));
        const cxp = px + 24 + u * (pw - 42);
        const cyp = py + ph - 24 - sigY * (ph - 56);
        if (i === 0) ctx.moveTo(cxp, cyp);
        else ctx.lineTo(cxp, cyp);
      }
      ctx.stroke();

      // Current progress marker on curve
      const curSig = 1 / (1 + Math.exp(-(prog - 0.5) * 18));
      const dotX = px + 24 + prog * (pw - 42);
      const dotY = py + ph - 24 - curSig * (ph - 56);
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath();
      ctx.arc(dotX, dotY, 5.5, 0, Math.PI * 2);
      ctx.fill();

      const pHVal = (1.5 + curSig * 11.2).toFixed(2);
      drawCalloutLabel(ctx, 88, 60, `Burette: ${rChem2}`, bx, by + 40, "#38bdf8");
      drawCalloutLabel(ctx, 82, 290, `Analyte: ${rChem1}`, 152, benchY - 80, "#22c55e");
      drawCalloutLabel(ctx, 460, 165, app === "redox_titration" ? `ORP Endpoint Progress: ${(prog * 100).toFixed(0)}%` : `Digital pH Meter: pH ${pHVal}`, dotX, dotY, "#f43f5e");
    } else if (app === "voltaic_cell" || app === "electrolysis") {
      const isElectro = app === "electrolysis";
      // Two half-cell beakers (or unified electrolytic cell)
      drawGlassBeaker(ctx, 130, benchY - 150, 130, 150, lab.color_a || "#e0f2fe", 0.72, null, prog, isElectro ? "H₂" : null, timeSec);
      drawGlassBeaker(ctx, 340, benchY - 150, 130, 150, lerpColor(lab.color_b || "#0284c7", lab.color_prod || "#38bdf8", prog), 0.72, null, prog, isElectro ? "O₂/Cl₂" : null, timeSec);

      // Electrodes
      ctx.fillStyle = "#a3a3a3";
      ctx.fillRect(175, benchY - 175, 18, 135);
      ctx.fillStyle = isElectro ? "#737373" : "#d97706";
      ctx.fillRect(405, benchY - 175, 18, 135);

      // Salt bridge (U-tube)
      ctx.strokeStyle = "rgba(253, 224, 71, 0.75)";
      ctx.lineWidth = 14;
      ctx.lineCap = "round";
      ctx.beginPath();
      ctx.moveTo(225, benchY - 95);
      ctx.lineTo(225, benchY - 165);
      ctx.lineTo(375, benchY - 165);
      ctx.lineTo(375, benchY - 95);
      ctx.stroke();

      // External wire & Voltmeter / DC Power Supply
      ctx.strokeStyle = "#d4d4d4";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(184, benchY - 175);
      ctx.lineTo(184, 72);
      ctx.lineTo(414, 72);
      ctx.lineTo(414, benchY - 175);
      ctx.stroke();

      // Animated electrons e- along top wire
      for (let i = 0; i < 6; i++) {
        const ex = 184 + (((timeSec * 85 + i * 38) % 230));
        ctx.fillStyle = "#facc15";
        ctx.beginPath();
        ctx.arc(ex, 72, 4.5, 0, Math.PI * 2);
        ctx.fill();
      }

      // Meter Housing
      ctx.fillStyle = "#1f1f1f";
      ctx.strokeStyle = "#facc15";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(245, 42, 110, 54, 8);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#fde047";
      ctx.font = "700 13px ui-monospace, monospace";
      ctx.textAlign = "center";
      ctx.fillText(isElectro ? "DC POWER" : "VOLTMETER", 300, 60);
      ctx.font = "700 15px ui-monospace, monospace";
      ctx.fillText(isElectro ? "4.50 V DC" : "+1.10 V", 300, 82);

      drawCalloutLabel(ctx, 115, 165, isElectro ? `Cathode (−): ${rChem1}` : `Anode (−): ${rChem1}`, 184, benchY - 140, "#38bdf8");
      drawCalloutLabel(ctx, 515, 165, isElectro ? `Anode (+): ${pChem}` : `Cathode (+): ${rChem2}`, 414, benchY - 140, "#f59e0b");
      drawCalloutLabel(ctx, 300, 195, isElectro ? "Ion Migration Membrane" : "KNO₃ Salt Bridge (K⁺ / NO₃⁻)", 300, benchY - 165, "#fde047");
    } else if (app === "bunsen_crucible" || app === "volcano" || app === "thermite") {
      const cx = 285;
      // Ring stand & support ring
      ctx.fillStyle = "#555555";
      ctx.fillRect(150, 55, 9, benchY - 55);
      ctx.fillRect(159, benchY - 145, 175, 5);

      if (app !== "volcano") {
        drawBunsenBurner(ctx, cx, benchY, lab.flame_color || "#38bdf8", 0.5 + prog * 0.7, timeSec);
      }

      // Crucible / reaction cone
      ctx.fillStyle = app === "thermite" ? "#7c2d12" : "#d4d4d4";
      ctx.strokeStyle = "#fafafa";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - 46, benchY - 195);
      ctx.lineTo(cx - 32, benchY - 145);
      ctx.lineTo(cx + 32, benchY - 145);
      ctx.lineTo(cx + 46, benchY - 195);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Solid reactant/product mound inside crucible
      ctx.fillStyle = mixColor;
      ctx.beginPath();
      ctx.moveTo(cx - 34, benchY - 162);
      ctx.quadraticCurveTo(cx, benchY - 205 - (app === "volcano" ? prog * 35 : 0), cx + 34, benchY - 162);
      ctx.closePath();
      ctx.fill();

      // Sparks & incandescent glow for thermite / volcano / combustion
      if (prog > 0.1) {
        for (let i = 0; i < 22; i++) {
          const ang = -Math.PI / 2 + Math.sin(i * 2.3 + timeSec * 7) * 0.95;
          const dist = ((timeSec * 120 + i * 19) % 110) * prog;
          const sx = cx + Math.cos(ang) * dist;
          const sy = benchY - 185 + Math.sin(ang) * dist;
          ctx.fillStyle = lab.flame_color || "#fb923c";
          ctx.beginPath();
          ctx.arc(sx, sy, 2.8, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // If thermite, show molten white-hot Fe(l) stream pouring into sand mold below!
      if (app === "thermite" && prog > 0.25) {
        ctx.fillStyle = "#fef08a";
        ctx.fillRect(cx - 5, benchY - 145, 10, 125);
        ctx.fillStyle = "#f97316";
        ctx.beginPath();
        ctx.roundRect(cx - 55, benchY - 26, 110, 26, 5);
        ctx.fill();
      }

      drawCalloutLabel(ctx, 115, 115, `Crucible Charge: ${rChem1} + ${rChem2}`, cx - 35, benchY - 175, "#f59e0b");
      drawCalloutLabel(ctx, 455, 155, `Product: ${pChem} (${lab.temperature_c || 650} °C)`, cx + 35, benchY - 175, "#38bdf8");
      drawCalloutLabel(ctx, 455, 315, app === "thermite" ? "Molten Fe(l) Collector Mold" : "Bunsen Burner Heat Source (Δ)", cx + 12, benchY - 45, "#fb923c");
    } else if (app === "thermal_tube" || app === "gas_evolution" || app === "acid_metal_flask" || app === "fume_hood_nitric") {
      // Reaction Flask / Test Tube on left + Gas Delivery Tube + Collection / Trap on right
      const fx = 165;
      const fy = benchY - 150;
      drawGlassBeaker(
        ctx,
        fx,
        fy,
        105,
        150,
        mixColor,
        0.55,
        lab.precipitate_color,
        prog,
        lab.gas_label || "Gas",
        timeSec
      );

      // If fume_hood_nitric, draw reddish-brown NO2 cloud inside flask & hood sash
      if (app === "fume_hood_nitric") {
        ctx.fillStyle = `rgba(180, 83, 9, ${0.2 + prog * 0.55})`;
        ctx.beginPath();
        ctx.roundRect(fx + 6, fy + 8, 93, 75, 8);
        ctx.fill();
      }

      // Rubber stopper & glass delivery tube to collection cylinder/trap
      ctx.fillStyle = "#404040";
      ctx.fillRect(fx + 28, fy - 10, 48, 14);
      ctx.strokeStyle = "#a3a3a3";
      ctx.lineWidth = 5;
      ctx.beginPath();
      ctx.moveTo(fx + 52, fy - 10);
      ctx.lineTo(fx + 52, fy - 42);
      ctx.lineTo(425, fy - 42);
      ctx.lineTo(425, benchY - 35);
      ctx.stroke();

      // Right-hand water trough / diagnostic trap beaker
      drawGlassBeaker(
        ctx,
        365,
        benchY - 145,
        125,
        145,
        "#38bdf8",
        0.68,
        rxn.id === 201 ? "#ffffff" : null,
        prog,
        lab.gas_label || "Gas",
        timeSec
      );

      drawCalloutLabel(ctx, 105, 150, `Reaction Vessel: ${rChem1} + ${rChem2}`, fx + 20, fy + 55, "#38bdf8");
      drawCalloutLabel(ctx, 300, 145, `Gas Delivery Tube (${lab.gas_label || pChem})`, 300, fy - 42, "#2dd4bf");
      drawCalloutLabel(ctx, 485, 210, `Gas Collector / Trap: ${pChem}`, 430, benchY - 95, "#a855f7");
    } else if (app === "industrial_reactor" || app === "gas_synthesis" || app === "flame_combustion") {
      // Industrial / Gas Synthesis Reactor Chamber
      const rx = 185;
      const ry = 105;
      const rw = 220;
      const rh = 225;

      ctx.fillStyle = "#2e2e2e";
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.roundRect(rx, ry, rw, rh, 18);
      ctx.fill();
      ctx.stroke();

      // Catalyst bed / glow zone inside chamber
      const glowGrad = ctx.createRadialGradient(rx + rw / 2, ry + rh / 2, 10, rx + rw / 2, ry + rh / 2, 95);
      glowGrad.addColorStop(0, hexToRgba(lab.flame_color || "#f59e0b", 0.35 + prog * 0.45));
      glowGrad.addColorStop(1, "rgba(31, 31, 31, 0)");
      ctx.fillStyle = glowGrad;
      ctx.fillRect(rx + 8, ry + 8, rw - 16, rh - 16);

      // Catalyst bed pellets
      ctx.fillStyle = "#737373";
      for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 7; c++) {
          ctx.beginPath();
          ctx.arc(rx + 36 + c * 24, ry + 95 + r * 20, 7, 0, Math.PI * 2);
          ctx.fill();
        }
      }

      // Inlet & Outlet pipes with animated gas stream
      ctx.fillStyle = "#404040";
      ctx.fillRect(95, ry + 40, 90, 18);
      ctx.fillRect(rx + rw, ry + rh - 65, 95, 18);

      for (let i = 0; i < 14; i++) {
        const gx = 100 + ((timeSec * 90 + i * 28) % 390);
        const gy = gx < rx + rw / 2 ? ry + 49 : ry + rh - 56;
        ctx.fillStyle = gx < rx + rw / 2 ? "#38bdf8" : "#4ade80";
        ctx.beginPath();
        ctx.arc(gx, gy, 4, 0, Math.PI * 2);
        ctx.fill();
      }

      drawCalloutLabel(ctx, 115, 95, `Feed Stream: ${rChem1} + ${rChem2}`, 135, ry + 49, "#38bdf8");
      drawCalloutLabel(ctx, 295, 72, `Reaction Chamber (${lab.temperature_c || 450} °C)`, rx + rw / 2, ry + 95, "#f59e0b");
      drawCalloutLabel(ctx, 495, 315, `Product Outlet: ${pChem}`, rx + rw + 55, ry + rh - 56, "#4ade80");
    } else if (app === "calorimeter" || app === "kinetics_spectrometer") {
      const isSpec = app === "kinetics_spectrometer";
      // Left: Cuvette / Calorimeter Vessel
      drawGlassBeaker(ctx, 155, benchY - 155, 115, 155, mixColor, 0.72, lab.precipitate_color, prog, lab.gas_label, timeSec);

      if (isSpec) {
        // Light beam I_0 -> Cuvette -> Detector I
        ctx.fillStyle = "rgba(250, 204, 21, 0.38)";
        ctx.fillRect(65, benchY - 95, 90, 18);
        ctx.fillStyle = `rgba(250, 204, 21, ${Math.max(0.08, 0.38 * (1 - prog * 0.7))})`;
        ctx.fillRect(270, benchY - 95, 65, 18);
      }

      // Right: Real-Time Scientific Logger Plot
      const px = 345;
      const py = 190;
      const pw = 245;
      const ph = 175;
      ctx.fillStyle = "rgba(18, 18, 18, 0.92)";
      ctx.strokeStyle = "rgba(56, 189, 248, 0.45)";
      ctx.beginPath();
      ctx.roundRect(px, py, pw, ph, 10);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = "#a3a3a3";
      ctx.font = "600 11px Inter, sans-serif";
      ctx.fillText(isSpec ? "Spectrophotometric Rate Trace [A](t)" : "Calorimetric Enthalpy / ΔG Profile", px + 14, py + 22);

      ctx.beginPath();
      ctx.strokeStyle = "#4ade80";
      ctx.lineWidth = 2.4;
      for (let i = 0; i <= 100; i++) {
        const u = i / 100;
        const yVal = isSpec ? Math.exp(-u * 3.2) : 0.5 + 0.38 * Math.sin(u * Math.PI);
        const cxp = px + 22 + u * (pw - 40);
        const cyp = py + ph - 22 - yVal * (ph - 55);
        if (i === 0) ctx.moveTo(cxp, cyp);
        else ctx.lineTo(cxp, cyp);
      }
      ctx.stroke();

      const curVal = isSpec ? Math.exp(-prog * 3.2) : 0.5 + 0.38 * Math.sin(prog * Math.PI);
      const curX = px + 22 + prog * (pw - 40);
      const curY = py + ph - 22 - curVal * (ph - 55);
      ctx.fillStyle = "#facc15";
      ctx.beginPath();
      ctx.arc(curX, curY, 5.5, 0, Math.PI * 2);
      ctx.fill();

      drawCalloutLabel(ctx, 110, 155, isSpec ? `Optical Cell: ${rChem1}` : `Calorimeter: ${rChem1}`, 175, benchY - 95, "#38bdf8");
      drawCalloutLabel(ctx, 465, 165, `Live Data Logger (${(prog * 100).toFixed(0)}%)`, curX, curY, "#4ade80");
    } else {
      // Default: Precipitation / Complex-Ion / Single-Displacement / Equilibrium / Alkali-Water Beaker & Dropper Pipet
      const bx = 215;
      const by = benchY - 170;
      const bw = 155;
      const bh = 170;

      drawGlassBeaker(
        ctx,
        bx,
        by,
        bw,
        bh,
        mixColor,
        0.58 + prog * 0.16,
        lab.precipitate_color,
        prog,
        lab.gas_label,
        timeSec
      );

      // If metal_displacement, draw immersed metal strip & dendritic crystals growing on it
      if (app === "metal_displacement") {
        ctx.save();
        ctx.translate(bx + bw / 2, by + 18);
        ctx.rotate(-0.18);
        ctx.fillStyle = "#a3a3a3";
        ctx.fillRect(-9, 0, 18, 130);
        // Plated metal coating
        ctx.fillStyle = lab.precipitate_color || "#d97706";
        ctx.fillRect(-11, 45, 22, 82 * prog);
        ctx.restore();
      }

      // Dropper Pipet above beaker adding reagent B
      const pipX = bx + bw / 2;
      const pipY = 42;
      ctx.fillStyle = "#f43f5e";
      ctx.beginPath();
      ctx.ellipse(pipX, pipY, 12, 18, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = "#e5e5e5";
      ctx.lineWidth = 2;
      ctx.strokeRect(pipX - 5, pipY + 16, 10, 52);

      // Falling reagent drops
      const dropY = pipY + 74 + ((timeSec * 135) % 68);
      ctx.fillStyle = lab.color_b || "#38bdf8";
      ctx.beginPath();
      ctx.arc(pipX, dropY, 4, 0, Math.PI * 2);
      ctx.fill();

      drawCalloutLabel(ctx, 125, 65, `Dropper Reagent: ${rChem2}`, pipX - 6, pipY + 40, "#f43f5e");
      drawCalloutLabel(ctx, 110, 235, `Initial Solution: ${rChem1}`, bx + 12, by + 85, "#38bdf8");
      drawCalloutLabel(
        ctx,
        490,
        295,
        lab.precipitate_color
          ? `Precipitate Settling: ${pChem}(s)↓`
          : `Product Phase: ${pChem}`,
        bx + bw - 18,
        by + bh - 24,
        "#facc15"
      );
    }

    // Bottom status banner inside canvas
    ctx.save();
    ctx.fillStyle = "rgba(31, 31, 31, 0.88)";
    ctx.fillRect(14, H - 44, W - 28, 34);
    ctx.fillStyle = "#38bdf8";
    ctx.font = "700 12px Inter, system-ui, sans-serif";
    ctx.fillText(`#${rxn.id} ${rxn.title}`, 26, H - 23);
    ctx.fillStyle = "#d4d4d4";
    ctx.font = "500 11.5px Inter, system-ui, sans-serif";
    ctx.textAlign = "right";
    ctx.fillText(
      `Progress: ${(prog * 100).toFixed(0)}%  •  T = ${(25 + ((lab.temperature_c || 25) - 25) * prog).toFixed(1)} °C`,
      W - 26,
      H - 23
    );
    ctx.restore();

    // Submicroscopic Particle Zoom Inset
    drawMicroscopicZoomInset(ctx, rxn, prog, timeSec);
  }

  // =========================================================================
  // 6. Animation Loop & Event Bindings
  // =========================================================================

  function tick(now) {
    const dt = Math.min(0.05, (now - state.lastFrameTime) / 1000);
    state.lastFrameTime = now;
    const timeSec = now / 1000;

    // The lab canvas only lives in the reaction view — skip all work while a section view is shown
    const reactionView = document.getElementById("reaction-view");
    if (!reactionView || reactionView.hidden) {
      requestAnimationFrame(tick);
      return;
    }

    if (state.playing) {
      const boost = 1 + state.pulseBoost * 1.8;
      state.progress += dt * 0.14 * state.speed * boost;
      if (state.progress > 1.0) {
        state.progress = 0.0;
      }
      state.pulseBoost = Math.max(0, state.pulseBoost - dt * 1.5);

      const progInput = document.getElementById("wb-progress");
      const progVal = document.getElementById("wb-progress-val");
      if (progInput) progInput.value = (state.progress * 100).toFixed(1);
      if (progVal) progVal.textContent = `${Math.round(state.progress * 100)}%`;
    }

    const activeRxn = RXN_BY_ID.get(state.activeRxnId) || REACTIONS[0];
    if (activeRxn) {
      const targetTemp = activeRxn.lab?.temperature_c || 25;
      const curTemp = 25 + (targetTemp - 25) * state.progress;
      const tempEl = document.getElementById("wb-temp-readout");
      if (tempEl) tempEl.textContent = `${curTemp.toFixed(1)} °C`;

      const wbCanvas = document.getElementById("wb-canvas");
      renderLabCanvas(wbCanvas, activeRxn, state.progress, timeSec);
    }

    requestAnimationFrame(tick);
  }

  function populateJumpSelect() {
    const sel = document.getElementById("rxn-jump-select");
    if (!sel) return;
    let opts = `<option value="">Open Reaction (#1 – #${REACTIONS.length})...</option>`;
    for (const r of REACTIONS) {
      opts += `<option value="${r.id}">#${r.id} — ${escapeHtml(r.title)} (${escapeHtml(r.category_short)})</option>`;
    }
    sel.innerHTML = opts;
  }

  function bindEvents() {
    window.addEventListener("hashchange", () => applyRoute());

    // Section links (sidebar): clear any search so the chosen section is shown
    document.querySelectorAll("a[data-cat]").forEach((link) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        clearSearch();
        navigateTo(`#/section/${link.dataset.cat}`);
      });
    });

    // Feature Filter Chips (apply within the current section)
    document.querySelectorAll("[data-filter]").forEach((chip) => {
      chip.addEventListener("click", () => {
        state.activeFilter = chip.dataset.filter;
        document.querySelectorAll("[data-filter]").forEach((c) => c.classList.toggle("active", c === chip));
        renderSectionView(state.selectedCat);
      });
    });

    // Search Box (searches all sections)
    const searchInput = document.getElementById("rxn-search-input");
    const clearBtn = document.getElementById("rxn-search-clear");
    if (searchInput) {
      searchInput.addEventListener("input", () => {
        state.searchQuery = searchInput.value;
        if (clearBtn) clearBtn.hidden = !state.searchQuery;
        renderSectionView(state.selectedCat);
      });
    }
    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        if (searchInput) searchInput.value = "";
        state.searchQuery = "";
        clearBtn.hidden = true;
        renderSectionView(state.selectedCat);
        searchInput?.focus();
      });
    }

    // Open-reaction dropdown
    const jumpSelect = document.getElementById("rxn-jump-select");
    if (jumpSelect) {
      jumpSelect.addEventListener("change", () => {
        const id = Number(jumpSelect.value);
        jumpSelect.value = "";
        if (id) navigateTo(`#/reaction/${id}`);
      });
    }

    // Click anywhere on a reaction card opens its dedicated view
    const feedEl = document.getElementById("reactions-feed-container");
    if (feedEl) {
      feedEl.addEventListener("click", (e) => {
        const groupHeader = e.target.closest(".search-group-header");
        if (groupHeader) {
          e.preventDefault();
          clearSearch();
          navigateTo(groupHeader.getAttribute("href"));
          return;
        }
        if (e.target.closest("a")) return; // real links navigate by themselves
        const card = e.target.closest(".rxn-card");
        if (card) navigateTo(`#/reaction/${card.dataset.rxnId}`);
      });
    }

    // Workbench Controls
    document.getElementById("wb-btn-play")?.addEventListener("click", () => {
      state.playing = !state.playing;
      syncPlayButtonText();
    });

    document.getElementById("wb-btn-step")?.addEventListener("click", () => {
      state.pulseBoost = 1.0;
      state.playing = true;
      if (state.progress > 0.9) state.progress = 0.12;
      syncPlayButtonText();
    });

    document.getElementById("wb-btn-reset")?.addEventListener("click", () => {
      state.progress = 0.0;
      state.playing = true;
      syncPlayButtonText();
    });

    const progSlider = document.getElementById("wb-progress");
    if (progSlider) {
      progSlider.addEventListener("input", () => {
        state.progress = Number(progSlider.value) / 100;
        const progVal = document.getElementById("wb-progress-val");
        if (progVal) progVal.textContent = `${Math.round(state.progress * 100)}%`;
      });
    }

    const speedSlider = document.getElementById("wb-speed");
    if (speedSlider) {
      speedSlider.addEventListener("input", () => {
        state.speed = Number(speedSlider.value);
        const speedVal = document.getElementById("wb-speed-val");
        if (speedVal) speedVal.textContent = `${state.speed.toFixed(2)}×`;
      });
    }

    document.getElementById("wb-chk-micro")?.addEventListener("change", (e) => {
      state.showMicro = e.target.checked;
    });

    document.getElementById("wb-chk-pubchem")?.addEventListener("change", (e) => {
      state.showPubchem = e.target.checked;
      const activeRxn = RXN_BY_ID.get(state.activeRxnId);
      if (activeRxn) renderReactionDetail(activeRxn);
    });
  }

  function init() {
    populateJumpSelect();
    bindEvents();
    // Hydrate Canonical Summary Table KaTeX
    const summarySection = document.getElementById("category-section-12");
    if (summarySection) hydrateKatexInContainer(summarySection);
    if (!window.location.hash) {
      history.replaceState(null, "", "#/section/1");
    }
    applyRoute({ initial: true });
    requestAnimationFrame(tick);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
