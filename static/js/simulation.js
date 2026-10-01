/**
 * Interactive Physics Simulation for Rutherford's Gold Leaf Experiment (1909-1911)
 * Renders synchronized Macroscopic Apparatus and Subatomic Nuclear Zoom views,
 * interactive component labels, scintillation flashes, and live telemetry.
 */

(() => {
  "use strict";

  // DOM References
  const macroCanvas = document.getElementById("macro-canvas");
  const atomicCanvas = document.getElementById("atomic-canvas");
  const histCanvas = document.getElementById("histogram-canvas");
  const macroCtx = macroCanvas.getContext("2d");
  const atomicCtx = atomicCanvas.getContext("2d");
  const histCtx = histCanvas.getContext("2d");

  const stageEl = document.getElementById("canvas-stage");
  const btnPlayPause = document.getElementById("btn-play-pause");
  const playIcon = document.getElementById("play-icon");
  const playText = document.getElementById("play-text");
  const btnFireBurst = document.getElementById("btn-fire-burst");
  const btnFireHeadOn = document.getElementById("btn-fire-headon");
  const btnReset = document.getElementById("btn-reset");
  const btnClearHighlight = document.getElementById("btn-clear-highlight");
  const btnTestSingle = document.getElementById("btn-test-single");

  const selectTarget = document.getElementById("select-target");
  const sliderEnergy = document.getElementById("slider-energy");
  const sliderRate = document.getElementById("slider-rate");
  const sliderMicroscope = document.getElementById("slider-microscope");
  const sliderImpact = document.getElementById("slider-impact");

  const valEnergy = document.getElementById("val-energy");
  const valRate = document.getElementById("val-rate");
  const valMicroscope = document.getElementById("val-microscope");
  const valImpact = document.getElementById("val-impact");

  const toggleLabels = document.getElementById("toggle-labels");
  const toggleExaggerate = document.getElementById("toggle-exaggerate");
  const toggleTrails = document.getElementById("toggle-trails");

  const statTotal = document.getElementById("stat-total");
  const statStraight = document.getElementById("stat-straight");
  const statSmall = document.getElementById("stat-small");
  const statBack = document.getElementById("stat-back");
  const pctStraight = document.getElementById("pct-straight");
  const pctSmall = document.getElementById("pct-small");
  const pctBack = document.getElementById("pct-back");

  const calcTheta = document.getElementById("calc-theta");
  const calcRmin = document.getElementById("calc-rmin");
  const calcD0 = document.getElementById("calc-d0");

  const atomicPanelTitle = document.getElementById("atomic-panel-title");
  const atomicModelBadge = document.getElementById("atomic-model-badge");

  // Simulation State
  const state = {
    running: true,
    viewMode: "split", // 'split' | 'macro' | 'atomic'
    atomicModel: "rutherford", // 'rutherford' | 'thomson'
    targetKey: "Au",
    targetZ: 79,
    targetColor: "#f5c542",
    energyMeV: 5.5,
    rateLevel: 3, // 1..5
    microscopeAngleDeg: 25,
    showLabels: true,
    exaggerateRare: true,
    showTrails: true,
    highlightedPartId: null,
    impactParamFm: 15.0,

    // Particle & Scintillation Arrays
    macroParticles: [],
    scintillations: [],
    atomicParticles: [],
    labelHitBoxes: [],

    // Live Counts
    counts: {
      total: 0,
      straight: 0,
      small: 0,
      back: 0,
      bins: [0, 0, 0, 0, 0, 0], // [0-5°, 5-20°, 20-60°, 60-90°, 90-135°, 135-180°]
    },

    time: 0,
    spawnAccumulator: 0,
    isDraggingMicroscope: false,
  };

  const RATE_NAMES = ["Very Low", "Low", "Medium", "High", "Intense"];

  // Resize & High-DPI handling
  function resizeCanvas(canvas, ctx) {
    const rect = canvas.parentElement
      ? canvas.parentElement.getBoundingClientRect()
      : canvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    const width = Math.max(200, Math.floor(rect.width));
    const height = Math.max(110, Math.floor(rect.height));
    if (canvas.width !== width * dpr || canvas.height !== height * dpr) {
      canvas.width = width * dpr;
      canvas.height = height * dpr;
    }
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { width, height };
  }

  function resizeHistCanvas() {
    const rect = histCanvas.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    const width = Math.max(180, Math.floor(rect.width));
    const height = Math.max(95, Math.floor(rect.height));
    if (histCanvas.width !== width * dpr || histCanvas.height !== height * dpr) {
      histCanvas.width = width * dpr;
      histCanvas.height = height * dpr;
    }
    histCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { width, height };
  }

  // Physics Helper: Compute scattering/deflection angle (rad)
  function computeScatteringThetaRad(bFm, zTarget, energyMeV, model) {
    if (model === "thomson_crt") {
      // In Thomson's 1897 Cathode Ray Tube, electrons deflect upward toward the + plate
      // (typically 18° to 32° depending on plate voltage / beam energy) or pass straight when balanced by B
      if (Math.abs(bFm) > 160) {
        return (Math.random() - 0.5) * 0.015; // Balanced beam (F_E = F_B)
      }
      const baseDeflectionRad = (24 * Math.PI) / 180 * (5.5 / energyMeV);
      return baseDeflectionRad + (Math.random() - 0.5) * 0.06;
    }
    const ke2 = 1.4399645; // MeV * fm
    const d0 = (2 * zTarget * ke2) / energyMeV;
    const absB = Math.max(0.05, Math.abs(bFm));
    const theta = 2 * Math.atan(d0 / (2 * absB));
    return bFm >= 0 ? theta : -theta;
  }

  // Generate an impact parameter b (fm) for spawning particles
  function sampleImpactParameterFm(forcedMode = null) {
    if (forcedMode === "headon") {
      const sign = Math.random() < 0.5 ? 1 : -1;
      return sign * (0.8 + Math.random() * 6.5);
    }

    if (state.atomicModel === "thomson_crt") {
      // ~75% deflected by E-field toward + plate, ~25% balanced by B-field (v = E/B)
      return Math.random() < 0.75 ? 40 + Math.random() * 60 : 200;
    }

    const r = Math.random();
    if (state.exaggerateRare) {
      // Visual teaching mode: ~72% straight, ~20% small/moderate deflection, ~8% backscatter
      if (r < 0.72) {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (450 + Math.random() * 1400);
      } else if (r < 0.92) {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (22 + Math.random() * 160);
      } else {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (1.2 + Math.random() * 16);
      }
    } else {
      // Realistic rarity mode: >98.5% straight, ~1.35% small deflection, ~0.15% backscatter
      if (r < 0.985) {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (500 + Math.random() * 2000);
      } else if (r < 0.9985) {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (22 + Math.random() * 180);
      } else {
        const sign = Math.random() < 0.5 ? 1 : -1;
        return sign * (1.5 + Math.random() * 15);
      }
    }
  }

  // Classify scattering category from angle in degrees
  function classifyAngle(absDeg) {
    if (absDeg < 2.0) return "straight";
    if (absDeg <= 90.0) return "small";
    return "back";
  }

  function getCategoryColor(category) {
    if (category === "straight") return "#38bdf8";
    if (category === "small") return "#fb923c";
    return "#f43f5e";
  }

  // Spawn a pair of synchronized particles (one in Macro view, one in Atomic/Field view)
  function spawnAlphaPair(forcedMode = null, customBFm = null) {
    const bFm = customBFm !== null ? customBFm : sampleImpactParameterFm(forcedMode);
    const thetaRad = computeScatteringThetaRad(
      bFm,
      state.targetZ,
      state.energyMeV,
      state.atomicModel
    );
    const absDeg = Math.abs((thetaRad * 180) / Math.PI);
    const category = classifyAngle(absDeg);
    const isHighlighted = customBFm !== null || forcedMode === "headon";

    // 1. Macro particle
    state.macroParticles.push({
      phase: "incoming", // 'incoming' | 'scattered'
      progress: 0,
      yJitter: (Math.random() - 0.5) * 6,
      thetaRad,
      absDeg,
      category,
      isHighlighted,
      trail: [],
    });

    // 2. Atomic / Field Zoom particle
    let yNorm;
    if (state.atomicModel === "thomson_crt") {
      yNorm = (Math.random() - 0.5) * 0.16;
    } else if (customBFm !== null) {
      yNorm = Math.max(-0.85, Math.min(0.85, bFm / 130));
    } else if (category === "back") {
      yNorm = (bFm >= 0 ? 1 : -1) * (0.015 + Math.random() * 0.075);
    } else if (category === "small") {
      yNorm = (bFm >= 0 ? 1 : -1) * (0.1 + Math.random() * 0.28);
    } else {
      yNorm = (bFm >= 0 ? 1 : -1) * (0.36 + Math.random() * 0.52);
    }

    state.atomicParticles.push({
      xNorm: -0.95,
      yNorm,
      vx: 0.014 * Math.sqrt(state.energyMeV / 5.5),
      vy: 0,
      bFm,
      category,
      isHighlighted,
      trail: [],
    });
  }

  function recordDetection(absDeg, category) {
    state.counts.total += 1;
    if (category === "straight") state.counts.straight += 1;
    else if (category === "small") state.counts.small += 1;
    else state.counts.back += 1;

    if (absDeg < 5) state.counts.bins[0] += 1;
    else if (absDeg < 20) state.counts.bins[1] += 1;
    else if (absDeg < 60) state.counts.bins[2] += 1;
    else if (absDeg <= 90) state.counts.bins[3] += 1;
    else if (absDeg <= 135) state.counts.bins[4] += 1;
    else state.counts.bins[5] += 1;

    updateTelemetryDOM();
  }

  function updateTelemetryDOM() {
    const { total, straight, small, back } = state.counts;
    statTotal.textContent = total.toLocaleString();
    statStraight.textContent = straight.toLocaleString();
    statSmall.textContent = small.toLocaleString();
    statBack.textContent = back.toLocaleString();

    if (total > 0) {
      pctStraight.textContent = `${((straight / total) * 100).toFixed(1)}% (Pass Straight)`;
      pctSmall.textContent = `${((small / total) * 100).toFixed(1)}% (Deflected)`;
      pctBack.textContent = `${((back / total) * 100).toFixed(2)}% (Nuclear Rebound)`;
    } else {
      pctStraight.textContent = "0.0% (Pass Straight)";
      pctSmall.textContent = "0.0% (Deflected)";
      pctBack.textContent = "0.0% (Nuclear Rebound)";
    }
  }

  // Update Physics Step
  function stepSimulation(dt) {
    state.time += dt;

    // Spawn particles based on beam rate
    const spawnPerSec = [0, 3.5, 7, 13, 22, 35][state.rateLevel] || 12;
    state.spawnAccumulator += spawnPerSec * dt;
    while (state.spawnAccumulator >= 1) {
      state.spawnAccumulator -= 1;
      spawnAlphaPair();
    }

    const speedFactor = Math.sqrt(state.energyMeV / 5.5);

    // Update Macro Particles
    for (let i = state.macroParticles.length - 1; i >= 0; i--) {
      const p = state.macroParticles[i];
      const stepAmt = dt * 1.45 * speedFactor;
      p.progress += stepAmt;

      if (p.phase === "incoming" && p.progress >= 1.0) {
        p.phase = "scattered";
        p.progress = p.progress - 1.0;
      } else if (p.phase === "scattered" && p.progress >= 1.0) {
        // Reached detector screen -> create scintillation flash!
        state.scintillations.push({
          angleRad: p.thetaRad,
          category: p.category,
          age: 0,
          maxAge: p.category === "back" ? 1.4 : 0.85,
          isHighlighted: p.isHighlighted,
        });
        recordDetection(p.absDeg, p.category);
        state.macroParticles.splice(i, 1);
      }
    }

    // Update Scintillations
    for (let i = state.scintillations.length - 1; i >= 0; i--) {
      const s = state.scintillations[i];
      s.age += dt;
      if (s.age >= s.maxAge) {
        state.scintillations.splice(i, 1);
      }
    }

    // Update Atomic / Field Zoom Particles
    for (let i = state.atomicParticles.length - 1; i >= 0; i--) {
      const ap = state.atomicParticles[i];
      ap.trail.push({ x: ap.xNorm, y: ap.yNorm });
      if (ap.trail.length > 48) ap.trail.shift();

      if (state.atomicModel === "rutherford") {
        // Repulsive inverse-square Coulomb force from nucleus at (0, 0)
        const dx = ap.xNorm;
        const dy = ap.yNorm;
        const r2 = dx * dx + dy * dy + 0.0005;
        const r = Math.sqrt(r2);

        const strength = 0.00023 * (state.targetZ / 79) * (5.5 / state.energyMeV);
        const force = strength / r2;
        ap.vx += (dx / r) * force;
        ap.vy += (dy / r) * force;
      } else {
        // Thomson 1897 Cathode Ray Tube: Uniform upward electric force F_E = -eE between plates (-0.45 < x < 0.45)
        if (ap.xNorm > -0.45 && ap.xNorm < 0.45 && ap.category !== "straight") {
          ap.vy += 0.00026 * (5.5 / state.energyMeV);
        }
      }

      // Normalize speed to prevent numerical blow-up at closest approach
      const targetSpeed = 0.016 * speedFactor;
      const curSpeed = Math.hypot(ap.vx, ap.vy);
      if (curSpeed > targetSpeed * 1.15) {
        ap.vx = (ap.vx / curSpeed) * targetSpeed;
        ap.vy = (ap.vy / curSpeed) * targetSpeed;
      }

      ap.xNorm += ap.vx;
      ap.yNorm += ap.vy;

      if (
        ap.xNorm > 1.05 ||
        ap.xNorm < -1.05 ||
        ap.yNorm > 1.05 ||
        ap.yNorm < -1.05
      ) {
        state.atomicParticles.splice(i, 1);
      }
    }
  }

  // Helper: Draw a rounded rectangle
  function roundRect(ctx, x, y, w, h, r) {
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, r);
  }

  // =========================================================================
  // RENDER MACROSCOPIC APPARATUS CANVAS
  // =========================================================================
  function renderMacroCanvas() {
    const { width: W, height: H } = resizeCanvas(macroCanvas, macroCtx);
    const ctx = macroCtx;
    ctx.clearRect(0, 0, W, H);

    if (state.atomicModel === "thomson_crt") {
      renderThomsonCRTMacro(ctx, W, H);
      return;
    }

    // Subtle scientific grid background
    ctx.save();
    ctx.strokeStyle = "rgba(163, 163, 163, 0.05)";
    ctx.lineWidth = 1;
    const gridStep = 28;
    for (let x = 0; x < W; x += gridStep) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, H);
      ctx.stroke();
    }
    for (let y = 0; y < H; y += gridStep) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
      ctx.stroke();
    }
    ctx.restore();

    // Key geometric coordinates
    const cx = W * 0.58;
    const cy = H * 0.51;
    const screenR = Math.min(W * 0.31, H * 0.37);
    const chamberR = screenR * 1.17;

    const sourceBoxW = Math.min(92, W * 0.13);
    const sourceBoxH = Math.min(68, H * 0.16);
    const sourceX = Math.max(24, cx - chamberR - sourceBoxW - 22);
    const sourceY = cy - sourceBoxH / 2;
    const sourceCoreX = sourceX + sourceBoxW * 0.38;

    const collimatorX = cx - screenR * 0.72;

    const isPartHighlighted = (id) => state.highlightedPartId === id;

    // -----------------------------------------------------------------------
    // 8. Evacuated Vacuum Chamber (Outer Housing)
    // -----------------------------------------------------------------------
    ctx.save();
    ctx.beginPath();
    ctx.arc(cx, cy, chamberR, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(31, 31, 31, 0.72)";
    ctx.fill();
    ctx.lineWidth = isPartHighlighted("vacuum_chamber") ? 4 : 2;
    ctx.strokeStyle = isPartHighlighted("vacuum_chamber")
      ? "#f5c542"
      : "rgba(163, 163, 163, 0.3)";
    ctx.setLineDash([8, 5]);
    ctx.stroke();
    ctx.restore();

    // Vacuum Chamber entrance tunnel from lead shield
    ctx.save();
    ctx.fillStyle = "rgba(31, 31, 31, 0.9)";
    ctx.strokeStyle = "rgba(163, 163, 163, 0.3)";
    ctx.lineWidth = 1.5;
    ctx.fillRect(sourceX + sourceBoxW, cy - 15, cx - screenR - (sourceX + sourceBoxW) + 8, 30);
    ctx.strokeRect(sourceX + sourceBoxW, cy - 15, cx - screenR - (sourceX + sourceBoxW) + 8, 30);
    ctx.restore();

    // -----------------------------------------------------------------------
    // 2. Lead Block Containment Shield & 1. Radioactive Alpha Source
    // -----------------------------------------------------------------------
    ctx.save();
    if (isPartHighlighted("lead_shield")) {
      ctx.shadowColor = "#f5c542";
      ctx.shadowBlur = 18;
    }
    roundRect(ctx, sourceX, sourceY, sourceBoxW, sourceBoxH, 6);
    const leadGrad = ctx.createLinearGradient(sourceX, sourceY, sourceX, sourceY + sourceBoxH);
    leadGrad.addColorStop(0, "#555555");
    leadGrad.addColorStop(0.5, "#404040");
    leadGrad.addColorStop(1, "#2e2e2e");
    ctx.fillStyle = leadGrad;
    ctx.fill();
    ctx.lineWidth = isPartHighlighted("lead_shield") ? 3 : 2;
    ctx.strokeStyle = isPartHighlighted("lead_shield") ? "#f5c542" : "#a3a3a3";
    ctx.stroke();

    // Internal borehole channel in lead shield
    ctx.fillStyle = "#141414";
    ctx.fillRect(sourceCoreX, cy - 7, sourceX + sourceBoxW - sourceCoreX + 2, 14);
    ctx.restore();

    // 1. Radioactive Alpha Source Capsule inside Lead Block
    ctx.save();
    const pulse = 0.75 + 0.25 * Math.sin(state.time * 5);
    if (isPartHighlighted("alpha_source")) {
      ctx.shadowColor = "#f5c542";
      ctx.shadowBlur = 20;
    } else {
      ctx.shadowColor = "#38bdf8";
      ctx.shadowBlur = 12 * pulse;
    }
    ctx.beginPath();
    ctx.arc(sourceCoreX, cy, 8, 0, Math.PI * 2);
    ctx.fillStyle = "#38bdf8";
    ctx.fill();
    ctx.beginPath();
    ctx.arc(sourceCoreX, cy, 4, 0, Math.PI * 2);
    ctx.fillStyle = "#e0f2fe";
    ctx.fill();
    ctx.restore();

    // -----------------------------------------------------------------------
    // 3. Lead Collimator Slit (Diaphragm)
    // -----------------------------------------------------------------------
    ctx.save();
    const slitGap = 11;
    const jawH = 28;
    const jawW = 10;
    if (isPartHighlighted("collimator")) {
      ctx.shadowColor = "#f5c542";
      ctx.shadowBlur = 16;
    }
    ctx.fillStyle = "#737373";
    ctx.strokeStyle = isPartHighlighted("collimator") ? "#f5c542" : "#d4d4d4";
    ctx.lineWidth = isPartHighlighted("collimator") ? 2.5 : 1.2;
    // Upper jaw
    ctx.fillRect(collimatorX - jawW / 2, cy - slitGap / 2 - jawH, jawW, jawH);
    ctx.strokeRect(collimatorX - jawW / 2, cy - slitGap / 2 - jawH, jawW, jawH);
    // Lower jaw
    ctx.fillRect(collimatorX - jawW / 2, cy + slitGap / 2, jawW, jawH);
    ctx.strokeRect(collimatorX - jawW / 2, cy + slitGap / 2, jawW, jawH);
    ctx.restore();

    // -----------------------------------------------------------------------
    // 6. Circular Zinc Sulfide (ZnS) Fluorescent Screen
    // -----------------------------------------------------------------------
    ctx.save();
    const gapAngle = 0.13; // Opening on the left (pi) for incoming beam
    if (isPartHighlighted("zns_screen")) {
      ctx.shadowColor = "#4ade80";
      ctx.shadowBlur = 18;
    }
    // Outer metallic backing ring
    ctx.beginPath();
    ctx.arc(cx, cy, screenR + 4, -Math.PI + gapAngle, Math.PI - gapAngle);
    ctx.strokeStyle = "#404040";
    ctx.lineWidth = 8;
    ctx.stroke();

    // Inner ZnS fluorescent phosphor coating
    ctx.beginPath();
    ctx.arc(cx, cy, screenR, -Math.PI + gapAngle, Math.PI - gapAngle);
    ctx.strokeStyle = isPartHighlighted("zns_screen") ? "#f5c542" : "#22c55e";
    ctx.lineWidth = 4;
    ctx.stroke();

    // Angular degree tick marks around ZnS screen
    ctx.fillStyle = "rgba(163, 163, 163, 0.72)";
    ctx.font = "600 10px 'JetBrains Mono', monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    const degreeTicks = [0, 30, 60, 90, 120, 150, -30, -60, -90, -120, -150];
    for (const deg of degreeTicks) {
      const rad = (deg * Math.PI) / 180;
      const tx1 = cx + Math.cos(rad) * (screenR + 7);
      const ty1 = cy - Math.sin(rad) * (screenR + 7);
      const tx2 = cx + Math.cos(rad) * (screenR + 12);
      const ty2 = cy - Math.sin(rad) * (screenR + 12);
      ctx.beginPath();
      ctx.moveTo(tx1, ty1);
      ctx.lineTo(tx2, ty2);
      ctx.strokeStyle = "rgba(163, 163, 163, 0.45)";
      ctx.lineWidth = 1;
      ctx.stroke();

      if (deg % 60 === 0 || deg === 0 || Math.abs(deg) === 90) {
        const lx = cx + Math.cos(rad) * (screenR - 14);
        const ly = cy - Math.sin(rad) * (screenR - 14);
        ctx.fillText(`${Math.abs(deg)}°`, lx, ly);
      }
    }
    ctx.restore();

    // -----------------------------------------------------------------------
    // 4 & 9 & 10 & 11. Guide Ray Lines & Active Alpha Particle Trajectories
    // -----------------------------------------------------------------------
    // Incident beam core glow (sourceCoreX -> cx)
    ctx.save();
    const beamGrad = ctx.createLinearGradient(sourceCoreX, cy, cx, cy);
    beamGrad.addColorStop(0, "rgba(56, 189, 248, 0.45)");
    beamGrad.addColorStop(1, "rgba(56, 189, 248, 0.25)");
    ctx.strokeStyle = isPartHighlighted("alpha_beam") ? "#f5c542" : beamGrad;
    ctx.lineWidth = isPartHighlighted("alpha_beam") ? 6 : 4;
    ctx.beginPath();
    ctx.moveTo(sourceCoreX, cy);
    ctx.lineTo(cx, cy);
    ctx.stroke();

    // Undeflected continuation beam (cx -> 0 deg on screen)
    ctx.strokeStyle = isPartHighlighted("undeflected_beam")
      ? "#f5c542"
      : "rgba(56, 189, 248, 0.22)";
    ctx.lineWidth = isPartHighlighted("undeflected_beam") ? 6 : 3.5;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + screenR, cy);
    ctx.stroke();

    // Reference schematic rays for Small Deflection (10) & Backscatter (11)
    if (state.showTrails || state.highlightedPartId) {
      // Sample small deflection reference ray (+28 deg and -22 deg)
      const smallAngles = [(28 * Math.PI) / 180, (-24 * Math.PI) / 180];
      ctx.save();
      ctx.setLineDash([4, 4]);
      ctx.strokeStyle = isPartHighlighted("small_deflection")
        ? "#f5c542"
        : "rgba(251, 146, 60, 0.38)";
      ctx.lineWidth = isPartHighlighted("small_deflection") ? 3 : 1.4;
      for (const a of smallAngles) {
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(cx + Math.cos(a) * screenR, cy - Math.sin(a) * screenR);
        ctx.stroke();
      }

      // Sample backscatter reference ray (+142 deg and -138 deg)
      const backAngles = [(142 * Math.PI) / 180, (-138 * Math.PI) / 180];
      ctx.strokeStyle = isPartHighlighted("large_deflection")
        ? "#f5c542"
        : "rgba(244, 63, 94, 0.42)";
      ctx.lineWidth = isPartHighlighted("large_deflection") ? 3 : 1.5;
      for (const a of backAngles) {
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(cx + Math.cos(a) * screenR, cy - Math.sin(a) * screenR);
        ctx.stroke();
      }
      ctx.restore();
    }
    ctx.restore();

    // Render Live Moving Alpha Particles in Macro View
    ctx.save();
    for (const p of state.macroParticles) {
      let px, py;
      if (p.phase === "incoming") {
        px = sourceCoreX + (cx - sourceCoreX) * p.progress;
        py = cy + p.yJitter * (1 - 0.5 * p.progress);
      } else {
        px = cx + Math.cos(p.thetaRad) * screenR * p.progress;
        py = cy - Math.sin(p.thetaRad) * screenR * p.progress;
      }

      const color = p.phase === "incoming" ? "#38bdf8" : getCategoryColor(p.category);

      if (state.showTrails && p.phase === "scattered") {
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(px, py);
        ctx.strokeStyle =
          p.category === "back"
            ? "rgba(244, 63, 94, 0.55)"
            : p.category === "small"
            ? "rgba(251, 146, 60, 0.45)"
            : "rgba(56, 189, 248, 0.2)";
        ctx.lineWidth = p.isHighlighted ? 2.8 : 1.5;
        ctx.stroke();
      }

      ctx.beginPath();
      ctx.arc(px, py, p.isHighlighted ? 5 : 3.2, 0, Math.PI * 2);
      ctx.fillStyle = p.isHighlighted ? "#f5c542" : color;
      ctx.fill();
    }
    ctx.restore();

    // -----------------------------------------------------------------------
    // 5. Ultra-Thin Gold Leaf (Au Foil) at Center (cx, cy)
    // -----------------------------------------------------------------------
    ctx.save();
    const foilHalfLen = 32;
    const foilAngle = -0.18; // Slight tilt for 3D visual clarity
    const fx1 = cx + Math.sin(foilAngle) * foilHalfLen;
    const fy1 = cy - Math.cos(foilAngle) * foilHalfLen;
    const fx2 = cx - Math.sin(foilAngle) * foilHalfLen;
    const fy2 = cy + Math.cos(foilAngle) * foilHalfLen;

    if (isPartHighlighted("gold_foil")) {
      ctx.shadowColor = "#f5c542";
      ctx.shadowBlur = 22;
    } else {
      ctx.shadowColor = state.targetColor;
      ctx.shadowBlur = 10;
    }

    ctx.beginPath();
    ctx.moveTo(fx1, fy1);
    ctx.lineTo(fx2, fy2);
    ctx.strokeStyle = state.targetColor;
    ctx.lineWidth = isPartHighlighted("gold_foil") ? 6.5 : 4.5;
    ctx.lineCap = "round";
    ctx.stroke();

    // Foil holder clamps
    ctx.fillStyle = "#a3a3a3";
    ctx.beginPath();
    ctx.arc(fx1, fy1, 4, 0, Math.PI * 2);
    ctx.arc(fx2, fy2, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();

    // -----------------------------------------------------------------------
    // Scintillation Flashes on the ZnS Screen
    // -----------------------------------------------------------------------
    ctx.save();
    for (const s of state.scintillations) {
      const sx = cx + Math.cos(s.angleRad) * screenR;
      const sy = cy - Math.sin(s.angleRad) * screenR;
      const t = s.age / s.maxAge;
      const alpha = Math.max(0, 1 - t);
      const radius = 4 + t * (s.category === "back" ? 20 : 13);

      // Expanding scintillation ring
      ctx.beginPath();
      ctx.arc(sx, sy, radius, 0, Math.PI * 2);
      ctx.strokeStyle =
        s.category === "back"
          ? `rgba(244, 63, 94, ${alpha * 0.9})`
          : s.category === "small"
          ? `rgba(251, 146, 60, ${alpha * 0.85})`
          : `rgba(74, 222, 128, ${alpha * 0.85})`;
      ctx.lineWidth = 2;
      ctx.stroke();

      // Bright green ZnS phosphor flash core
      ctx.beginPath();
      ctx.arc(sx, sy, 3.5 * (1 - 0.4 * t), 0, Math.PI * 2);
      ctx.fillStyle = `rgba(134, 239, 172, ${alpha})`;
      ctx.fill();
    }
    ctx.restore();

    // -----------------------------------------------------------------------
    // 7. Rotatable Viewing Microscope
    // -----------------------------------------------------------------------
    const micRad = (state.microscopeAngleDeg * Math.PI) / 180;
    const micScreenX = cx + Math.cos(micRad) * (screenR + 6);
    const micScreenY = cy - Math.sin(micRad) * (screenR + 6);
    const micOuterX = cx + Math.cos(micRad) * (screenR + 38);
    const micOuterY = cy - Math.sin(micRad) * (screenR + 38);

    ctx.save();
    if (isPartHighlighted("microscope")) {
      ctx.shadowColor = "#f5c542";
      ctx.shadowBlur = 18;
    }

    // Field of view cone inside screen
    ctx.beginPath();
    ctx.moveTo(micScreenX, micScreenY);
    const fovSpread = 0.11;
    ctx.arc(cx, cy, screenR, -micRad - fovSpread, -micRad + fovSpread);
    ctx.closePath();
    ctx.fillStyle = "rgba(74, 222, 128, 0.18)";
    ctx.fill();

    // Microscope barrel
    ctx.beginPath();
    ctx.moveTo(micScreenX, micScreenY);
    ctx.lineTo(micOuterX, micOuterY);
    ctx.strokeStyle = isPartHighlighted("microscope") ? "#f5c542" : "#e5e5e5";
    ctx.lineWidth = 9;
    ctx.lineCap = "round";
    ctx.stroke();

    // Eyepiece cap
    ctx.beginPath();
    ctx.arc(micOuterX, micOuterY, 6, 0, Math.PI * 2);
    ctx.fillStyle = "#f5c542";
    ctx.fill();
    ctx.restore();

    // -----------------------------------------------------------------------
    // Render Interactive Callout Labels (1 through 11)
    // -----------------------------------------------------------------------
    state.labelHitBoxes = [];
    if (state.showLabels) {
      const smallSampleRad = (28 * Math.PI) / 180;
      const backSampleRad = (142 * Math.PI) / 180;

      const callouts = [
        {
          id: "alpha_source",
          num: "1",
          text: "α-Source (Ra/Rn)",
          ax: sourceCoreX,
          ay: cy - 8,
          lx: Math.max(76, sourceCoreX + 6),
          ly: cy - 88,
        },
        {
          id: "lead_shield",
          num: "2",
          text: "Lead Block Shield",
          ax: sourceX + sourceBoxW * 0.6,
          ay: sourceY + sourceBoxH,
          lx: Math.max(82, sourceX + sourceBoxW * 0.55),
          ly: cy + 88,
        },
        {
          id: "collimator",
          num: "3",
          text: "Lead Collimator Slit",
          ax: collimatorX,
          ay: cy - 22,
          lx: collimatorX - 18,
          ly: cy - 128,
        },
        {
          id: "alpha_beam",
          num: "4",
          text: "Incident α-Beam (He²⁺)",
          ax: (collimatorX + cx) * 0.5,
          ay: cy + 4,
          lx: collimatorX + 12,
          ly: cy + 124,
        },
        {
          id: "gold_foil",
          num: "5",
          text: `Thin ${state.targetKey} Leaf (~0.4 μm)`,
          ax: cx,
          ay: cy - 28,
          lx: cx - 35,
          ly: Math.max(26, cy - screenR - 36),
        },
        {
          id: "zns_screen",
          num: "6",
          text: "Circular ZnS Screen",
          ax: cx + Math.cos(-1.15) * screenR,
          ay: cy - Math.sin(-1.15) * screenR,
          lx: cx + screenR * 0.45,
          ly: Math.min(H - 24, cy + screenR + 34),
        },
        {
          id: "microscope",
          num: "7",
          text: `Microscope (${state.microscopeAngleDeg}°)`,
          ax: micOuterX,
          ay: micOuterY,
          lx: Math.min(W - 88, micOuterX + 54),
          ly: Math.max(28, Math.min(H - 28, micOuterY - 18)),
        },
        {
          id: "vacuum_chamber",
          num: "8",
          text: "Vacuum Chamber",
          ax: cx + Math.cos(2.15) * chamberR,
          ay: cy - Math.sin(2.15) * chamberR,
          lx: cx - chamberR * 0.72,
          ly: Math.max(26, cy - chamberR - 14),
        },
        {
          id: "undeflected_beam",
          num: "9",
          text: "Undeflected (>99%)",
          ax: cx + screenR * 0.72,
          ay: cy,
          lx: Math.min(W - 88, cx + screenR + 48),
          ly: cy + 36,
        },
        {
          id: "small_deflection",
          num: "10",
          text: "Small Deflection",
          ax: cx + Math.cos(smallSampleRad) * (screenR * 0.65),
          ay: cy - Math.sin(smallSampleRad) * (screenR * 0.65),
          lx: Math.min(W - 88, cx + screenR * 0.85),
          ly: Math.max(26, cy - screenR * 0.88),
        },
        {
          id: "large_deflection",
          num: "11",
          text: "Backscattered (~1 in 8,000)",
          ax: cx + Math.cos(backSampleRad) * (screenR * 0.62),
          ay: cy - Math.sin(backSampleRad) * (screenR * 0.62),
          lx: cx - screenR * 0.62,
          ly: Math.min(H - 24, cy + screenR * 0.92),
        },
      ];

      ctx.save();
      ctx.font = "600 11px 'Inter', sans-serif";
      for (const c of callouts) {
        const active = isPartHighlighted(c.id);
        const textWidth = ctx.measureText(c.text).width;
        const pillW = textWidth + 30;
        const pillH = 22;
        const px = Math.max(6, Math.min(W - pillW - 6, c.lx - pillW / 2));
        const py = Math.max(6, Math.min(H - pillH - 6, c.ly - pillH / 2));

        // Leader line from anchor to label pill
        ctx.beginPath();
        ctx.moveTo(c.ax, c.ay);
        ctx.lineTo(px + pillW / 2, py + pillH / 2);
        ctx.strokeStyle = active ? "#f5c542" : "rgba(163, 163, 163, 0.55)";
        ctx.lineWidth = active ? 2.2 : 1.15;
        ctx.stroke();

        // Anchor dot on component
        ctx.beginPath();
        ctx.arc(c.ax, c.ay, active ? 4.5 : 3, 0, Math.PI * 2);
        ctx.fillStyle = active ? "#f5c542" : "#38bdf8";
        ctx.fill();

        // Pill background
        roundRect(ctx, px, py, pillW, pillH, 11);
        ctx.fillStyle = active ? "#f5c542" : "rgba(31, 31, 31, 0.92)";
        ctx.fill();
        ctx.lineWidth = active ? 2 : 1;
        ctx.strokeStyle = active ? "#fef08a" : "rgba(163, 163, 163, 0.4)";
        ctx.stroke();

        // Number circle inside pill
        ctx.beginPath();
        ctx.arc(px + 11, py + pillH / 2, 8, 0, Math.PI * 2);
        ctx.fillStyle = active ? "#1f1f1f" : "rgba(245, 197, 66, 0.2)";
        ctx.fill();

        ctx.fillStyle = active ? "#f5c542" : "#f5c542";
        ctx.font = "800 9.5px 'JetBrains Mono', monospace";
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        ctx.fillText(c.num, px + 11, py + pillH / 2 + 0.5);

        // Label text
        ctx.fillStyle = active ? "#121212" : "#fafafa";
        ctx.font = active ? "700 11px 'Inter', sans-serif" : "600 11px 'Inter', sans-serif";
        ctx.textAlign = "left";
        ctx.fillText(c.text, px + 23, py + pillH / 2 + 0.5);

        state.labelHitBoxes.push({
          id: c.id,
          x: px,
          y: py,
          w: pillW,
          h: pillH,
        });
      }
      ctx.restore();
    }
  }

  // =========================================================================
  // RENDER THOMSON 1897 CATHODE RAY TUBE (MACRO APPARATUS VIEW)
  // =========================================================================
  function renderThomsonCRTMacro(ctx, W, H) {
    // Subtle grid background
    ctx.save();
    ctx.strokeStyle = "rgba(163, 163, 163, 0.05)";
    ctx.lineWidth = 1;
    for (let x = 0; x < W; x += 28) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, H);
      ctx.stroke();
    }
    for (let y = 0; y < H; y += 28) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
      ctx.stroke();
    }
    ctx.restore();

    const cy = H * 0.52;
    const tubeLeft = W * 0.08;
    const neckEnd = W * 0.44;
    const plateStart = W * 0.44;
    const plateEnd = W * 0.62;
    const screenX = W * 0.88;
    const neckHalfH = Math.min(34, H * 0.09);
    const flareHalfH = Math.min(135, H * 0.33);

    const cathodeX = tubeLeft + 26;
    const anode1X = tubeLeft + (neckEnd - tubeLeft) * 0.48;
    const anode2X = tubeLeft + (neckEnd - tubeLeft) * 0.72;
    const plateMidX = (plateStart + plateEnd) * 0.5;

    // 1. Evacuated Glass Crookes-Thomson Tube Envelope
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(tubeLeft, cy - neckHalfH);
    ctx.lineTo(plateEnd, cy - neckHalfH);
    ctx.lineTo(screenX, cy - flareHalfH);
    ctx.quadraticCurveTo(screenX + 18, cy, screenX, cy + flareHalfH);
    ctx.lineTo(plateEnd, cy + neckHalfH);
    ctx.lineTo(tubeLeft, cy + neckHalfH);
    ctx.quadraticCurveTo(tubeLeft - 14, cy, tubeLeft, cy - neckHalfH);
    ctx.closePath();
    ctx.fillStyle = "rgba(56, 189, 248, 0.05)";
    ctx.fill();
    ctx.lineWidth = 2.2;
    ctx.strokeStyle = "rgba(163, 163, 163, 0.45)";
    ctx.stroke();
    ctx.restore();

    // 2. Heated Cathode (- Electrode)
    ctx.save();
    ctx.shadowColor = "#38bdf8";
    ctx.shadowBlur = 14;
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.beginPath();
    ctx.moveTo(cathodeX, cy - neckHalfH * 0.65);
    ctx.lineTo(cathodeX, cy + neckHalfH * 0.65);
    ctx.stroke();
    ctx.restore();

    // 3. Accelerating & Collimating Anode Slits (+)
    ctx.save();
    ctx.fillStyle = "#f5c542";
    for (const ax of [anode1X, anode2X]) {
      ctx.fillRect(ax - 3, cy - neckHalfH + 3, 6, neckHalfH - 8);
      ctx.fillRect(ax - 3, cy + 5, 6, neckHalfH - 8);
    }
    ctx.restore();

    // 4. Parallel Electric Deflection Plates (+E Top, -E Bottom)
    ctx.save();
    // Top Plate (+E)
    ctx.fillStyle = "#f43f5e";
    ctx.fillRect(plateStart, cy - neckHalfH + 4, plateEnd - plateStart, 6);
    // Bottom Plate (-E)
    ctx.fillStyle = "#38bdf8";
    ctx.fillRect(plateStart, cy + neckHalfH - 10, plateEnd - plateStart, 6);

    // Downward E-field lines between plates
    ctx.strokeStyle = "rgba(244, 63, 94, 0.28)";
    ctx.setLineDash([3, 3]);
    for (let x = plateStart + 12; x < plateEnd - 8; x += 18) {
      ctx.beginPath();
      ctx.moveTo(x, cy - neckHalfH + 10);
      ctx.lineTo(x, cy + neckHalfH - 10);
      ctx.stroke();
    }
    ctx.restore();

    // 5. External Helmholtz Electromagnet Coils (B Field)
    ctx.save();
    const coilR = neckHalfH * 1.45;
    ctx.beginPath();
    ctx.arc(plateMidX, cy, coilR, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(167, 139, 250, 0.1)";
    ctx.fill();
    ctx.strokeStyle = "rgba(167, 139, 250, 0.65)";
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 4]);
    ctx.stroke();
    ctx.restore();

    // 6. Fluorescent Phosphor Scale Screen on Right Wall
    ctx.save();
    ctx.beginPath();
    ctx.moveTo(screenX, cy - flareHalfH + 4);
    ctx.quadraticCurveTo(screenX + 16, cy, screenX, cy + flareHalfH - 4);
    ctx.strokeStyle = "#22c55e";
    ctx.lineWidth = 5;
    ctx.stroke();
    ctx.restore();

    // 7. Reference Rays & Live Cathode Ray Electrons (e-)
    const deflectEndY = cy - flareHalfH * 0.62;
    ctx.save();
    // Balanced straight beam (v = E/B)
    ctx.setLineDash([5, 4]);
    ctx.strokeStyle = "rgba(74, 222, 128, 0.45)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(cathodeX, cy);
    ctx.lineTo(screenX + 6, cy);
    ctx.stroke();

    // Electrically deflected beam curve (curving toward + plate)
    ctx.setLineDash([]);
    ctx.strokeStyle = "rgba(56, 189, 248, 0.45)";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(cathodeX, cy);
    ctx.lineTo(plateStart, cy);
    ctx.quadraticCurveTo(plateEnd, cy, screenX + 4, deflectEndY);
    ctx.stroke();

    // Render live moving electrons along the CRT
    for (const p of state.macroParticles) {
      const totalProg = p.phase === "incoming" ? p.progress * 0.45 : 0.45 + p.progress * 0.55;
      const px = cathodeX + (screenX - cathodeX) * totalProg;
      let py = cy;
      const isBalanced = p.category === "straight";
      if (!isBalanced && px > plateStart) {
        const u = (px - plateStart) / (screenX - plateStart);
        py = cy - u * u * (cy - deflectEndY);
      }

      ctx.beginPath();
      ctx.arc(px, py, 3.5, 0, Math.PI * 2);
      ctx.fillStyle = isBalanced ? "#4ade80" : "#38bdf8";
      ctx.fill();
    }

    // Phosphor screen glow spots
    const pulse = 0.75 + 0.25 * Math.sin(state.time * 6);
    ctx.beginPath();
    ctx.arc(screenX + 4, deflectEndY, 10 * pulse, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(74, 222, 128, 0.45)";
    ctx.fill();
    ctx.beginPath();
    ctx.arc(screenX + 4, deflectEndY, 4.5, 0, Math.PI * 2);
    ctx.fillStyle = "#86efac";
    ctx.fill();

    ctx.beginPath();
    ctx.arc(screenX + 6, cy, 7 * pulse, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(74, 222, 128, 0.35)";
    ctx.fill();
    ctx.restore();

    // 8. Labeled Callouts for Thomson's 1897 Cathode Ray Tube
    if (state.showLabels) {
      ctx.save();
      ctx.font = "600 11px 'Inter', sans-serif";
      drawAtomicCallout(ctx, cathodeX, cy - 18, cathodeX + 42, cy - 92, "1. Cathode (− Electrode)", "#38bdf8");
      drawAtomicCallout(ctx, anode1X + 18, cy + 18, anode1X + 12, cy + 95, "2. Anode Collimating Slits (+)", "#f5c542");
      drawAtomicCallout(ctx, plateMidX, cy - neckHalfH, plateMidX - 10, cy - 112, "3. Electric Deflection Plates (+E / −E)", "#f43f5e");
      drawAtomicCallout(ctx, plateMidX, cy + coilR, plateMidX + 15, cy + 115, "4. Helmholtz Magnetic Coils (B ⊗)", "#a78bfa");
      drawAtomicCallout(ctx, (plateEnd + screenX) * 0.5, (cy + deflectEndY) * 0.5, (plateEnd + screenX) * 0.48, deflectEndY - 36, "5. Deflected Cathode Ray (e⁻ Stream)", "#38bdf8");
      drawAtomicCallout(ctx, (plateEnd + screenX) * 0.55, cy, (plateEnd + screenX) * 0.55, cy + 56, "6. Balanced Beam (F_E = F_B → v = E/B)", "#4ade80");
      drawAtomicCallout(ctx, screenX + 4, deflectEndY + 25, screenX - 65, cy + flareHalfH + 22, "7. Fluorescent Scale Screen", "#22c55e");
      ctx.restore();
    }
  }

  // =========================================================================
  // RENDER SUBATOMIC NUCLEAR ZOOM OR THOMSON E×B DEFLECTION FIELD ZOOM
  // =========================================================================
  function renderAtomicCanvas() {
    const { width: W, height: H } = resizeCanvas(atomicCanvas, atomicCtx);
    const ctx = atomicCtx;
    ctx.clearRect(0, 0, W, H);

    const cx = W * 0.52;
    const cy = H * 0.5;
    const atomRadius = Math.min(W, H) * 0.36;

    if (state.atomicModel === "rutherford") {
      // Background Neighboring Gold Atoms in Foil Lattice (Top & Bottom)
      const neighborOffsets = [-atomRadius * 1.65, atomRadius * 1.65];
      for (const dy of neighborOffsets) {
        ctx.save();
        ctx.beginPath();
        ctx.arc(cx, cy + dy, atomRadius * 0.72, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(245, 197, 66, 0.12)";
        ctx.setLineDash([4, 4]);
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(cx, cy + dy, 6, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(245, 197, 66, 0.45)";
        ctx.fill();
        ctx.restore();
      }

      // ---------------------------------------------------------------------
      // RUTHERFORD NUCLEAR ATOM VIEW (1911)
      // ---------------------------------------------------------------------
      ctx.save();
      const cloudGrad = ctx.createRadialGradient(cx, cy, 8, cx, cy, atomRadius);
      cloudGrad.addColorStop(0, "rgba(245, 197, 66, 0.16)");
      cloudGrad.addColorStop(0.25, "rgba(245, 197, 66, 0.04)");
      cloudGrad.addColorStop(1, "rgba(56, 189, 248, 0.02)");
      ctx.beginPath();
      ctx.arc(cx, cy, atomRadius, 0, Math.PI * 2);
      ctx.fillStyle = cloudGrad;
      ctx.fill();
      ctx.strokeStyle = "rgba(56, 189, 248, 0.25)";
      ctx.setLineDash([6, 5]);
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Inner orbital shells
      for (const frac of [0.48, 0.75]) {
        ctx.beginPath();
        ctx.arc(cx, cy, atomRadius * frac, 0, Math.PI * 2);
        ctx.strokeStyle = "rgba(163, 163, 163, 0.12)";
        ctx.stroke();
      }
      ctx.restore();

      // Orbiting Electrons (e-)
      ctx.save();
      const electronOrbits = [
        { r: atomRadius * 0.48, speed: 1.4, count: 3 },
        { r: atomRadius * 0.75, speed: -0.95, count: 5 },
        { r: atomRadius * 0.98, speed: 0.65, count: 6 },
      ];
      for (const orb of electronOrbits) {
        for (let k = 0; k < orb.count; k++) {
          const angle = state.time * orb.speed + (k * Math.PI * 2) / orb.count;
          const ex = cx + Math.cos(angle) * orb.r;
          const ey = cy + Math.sin(angle) * orb.r;
          ctx.beginPath();
          ctx.arc(ex, ey, 3.2, 0, Math.PI * 2);
          ctx.fillStyle = "#38bdf8";
          ctx.fill();
        }
      }
      ctx.restore();

      // Impact Parameter (b) Reference Line
      const bNorm = Math.min(0.75, state.impactParamFm / 130);
      const bY = cy - bNorm * atomRadius;
      ctx.save();
      ctx.setLineDash([3, 3]);
      ctx.strokeStyle = "rgba(248, 250, 252, 0.35)";
      ctx.beginPath();
      ctx.moveTo(24, cy);
      ctx.lineTo(cx, cy);
      ctx.moveTo(24, bY);
      ctx.lineTo(cx, bY);
      ctx.stroke();

      if (Math.abs(cy - bY) > 12) {
        ctx.setLineDash([]);
        ctx.strokeStyle = "#f5c542";
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(52, cy);
        ctx.lineTo(52, bY);
        ctx.stroke();
        ctx.fillStyle = "#f5c542";
        ctx.font = "700 11px 'JetBrains Mono', monospace";
        ctx.fillText(`b = ${state.impactParamFm} fm`, 60, (cy + bY) / 2 + 4);
      }
      ctx.restore();

      // Dense Central Nucleus (+Ze) with Nucleon Cluster
      ctx.save();
      ctx.shadowColor = state.targetColor;
      ctx.shadowBlur = 22;
      const nucRadius = 14;
      const nucleons = [
        { dx: -4, dy: -3, c: "#ef4444" },
        { dx: 4, dy: -4, c: "#f5c542" },
        { dx: -5, dy: 4, c: "#f5c542" },
        { dx: 5, dy: 4, c: "#ef4444" },
        { dx: 0, dy: -6, c: "#a3a3a3" },
        { dx: -6, dy: 0, c: "#a3a3a3" },
        { dx: 6, dy: 0, c: "#ef4444" },
        { dx: 0, dy: 6, c: "#a3a3a3" },
        { dx: 0, dy: 0, c: "#f5c542" },
      ];
      for (const n of nucleons) {
        ctx.beginPath();
        ctx.arc(cx + n.dx, cy + n.dy, 5.5, 0, Math.PI * 2);
        ctx.fillStyle = n.c;
        ctx.fill();
      }
      ctx.beginPath();
      ctx.arc(cx, cy, nucRadius, 0, Math.PI * 2);
      ctx.strokeStyle = "#fef08a";
      ctx.lineWidth = 1.5;
      ctx.stroke();
      ctx.restore();
    } else {
      // ---------------------------------------------------------------------
      // THOMSON 1897 CATHODE RAY TUBE DEFLECTION PLATES ZOOM (E & B FIELDS)
      // ---------------------------------------------------------------------
      const plateW = W * 0.52;
      const plateX = cx - plateW / 2;
      const plateHalfGap = H * 0.28;
      const topPlateY = cy - plateHalfGap;
      const botPlateY = cy + plateHalfGap;

      ctx.save();
      // Top Positive Plate (+V)
      roundRect(ctx, plateX, topPlateY - 14, plateW, 14, 4);
      ctx.fillStyle = "#f43f5e";
      ctx.fill();
      // Bottom Negative Plate (-V)
      roundRect(ctx, plateX, botPlateY, plateW, 14, 4);
      ctx.fillStyle = "#38bdf8";
      ctx.fill();

      // Electric field lines (downward from + plate to - plate) & B-field markers
      ctx.strokeStyle = "rgba(244, 63, 94, 0.25)";
      ctx.fillStyle = "rgba(167, 139, 250, 0.45)";
      ctx.font = "700 12px 'JetBrains Mono', monospace";
      ctx.textAlign = "center";
      ctx.setLineDash([4, 4]);
      for (let x = plateX + 28; x < plateX + plateW - 16; x += 46) {
        ctx.beginPath();
        ctx.moveTo(x, topPlateY);
        ctx.lineTo(x, botPlateY);
        ctx.stroke();
        ctx.fillText("⊗ B", x, cy - 34);
        ctx.fillText("E ↓", x, cy + 42);
      }
      ctx.restore();
    }

    // -----------------------------------------------------------------------
    // Render Incoming & Deflecting Particles in Zoom View
    // -----------------------------------------------------------------------
    ctx.save();
    for (const ap of state.atomicParticles) {
      const px = cx + ap.xNorm * (W * 0.46);
      const py = cy - ap.yNorm * atomRadius;
      const color =
        state.atomicModel === "thomson_crt"
          ? ap.category === "straight"
            ? "#4ade80"
            : "#38bdf8"
          : getCategoryColor(ap.category);

      if (state.showTrails && ap.trail.length > 1) {
        ctx.beginPath();
        for (let j = 0; j < ap.trail.length; j++) {
          const tx = cx + ap.trail[j].x * (W * 0.46);
          const ty = cy - ap.trail[j].y * atomRadius;
          if (j === 0) ctx.moveTo(tx, ty);
          else ctx.lineTo(tx, ty);
        }
        ctx.strokeStyle = ap.isHighlighted
          ? "#f5c542"
          : state.atomicModel === "thomson_crt"
          ? ap.category === "straight"
            ? "rgba(74, 222, 128, 0.65)"
            : "rgba(56, 189, 248, 0.78)"
          : ap.category === "back"
          ? "rgba(244, 63, 94, 0.78)"
          : ap.category === "small"
          ? "rgba(251, 146, 60, 0.68)"
          : "rgba(56, 189, 248, 0.36)";
        ctx.lineWidth = ap.isHighlighted ? 3 : 1.8;
        ctx.stroke();
      }

      const r = ap.isHighlighted ? 5.5 : 4;
      ctx.beginPath();
      ctx.arc(px, py, r, 0, Math.PI * 2);
      ctx.fillStyle = ap.isHighlighted ? "#f5c542" : color;
      ctx.fill();
    }
    ctx.restore();

    // -----------------------------------------------------------------------
    // Subatomic / Field Labels Overlay
    // -----------------------------------------------------------------------
    if (state.showLabels) {
      ctx.save();
      ctx.font = "600 11px 'Inter', sans-serif";

      if (state.atomicModel === "rutherford") {
        drawAtomicCallout(
          ctx,
          cx + 12,
          cy - 10,
          cx + 85,
          cy - 48,
          `${state.targetKey} Nucleus (+${state.targetZ}e, >99.9% mass)`,
          "#f5c542"
        );
        drawAtomicCallout(
          ctx,
          cx + atomRadius * 0.68,
          cy + atomRadius * 0.68,
          cx + atomRadius * 0.55,
          cy + atomRadius * 0.92,
          "Vast Empty Space & Electron Cloud (e⁻)",
          "#38bdf8"
        );
        drawAtomicCallout(
          ctx,
          cx - 38,
          cy + 18,
          cx - 125,
          cy + 74,
          "Strong Coulomb Repulsion (F ∝ 1/r²)",
          "#f43f5e"
        );
      } else {
        const plateHalfGap = H * 0.28;
        drawAtomicCallout(
          ctx,
          cx,
          cy - plateHalfGap - 14,
          cx,
          cy - plateHalfGap - 42,
          "Positive Plate (+V) Attracts e⁻ Upward (F_E = −eE)",
          "#f43f5e"
        );
        drawAtomicCallout(
          ctx,
          cx,
          cy + plateHalfGap + 14,
          cx,
          cy + plateHalfGap + 42,
          "Negative Plate (−V) Repels Cathode Ray Electrons",
          "#38bdf8"
        );
        drawAtomicCallout(
          ctx,
          cx + 45,
          cy - 28,
          cx + 95,
          cy - 75,
          "Measured Ratio: e / m_e = 1.76 × 10¹¹ C/kg",
          "#f5c542"
        );
      }
      ctx.restore();
    }
  }

  function drawAtomicCallout(ctx, ax, ay, lx, ly, text, accentColor) {
    const padX = 10;
    const pillH = 22;
    const textW = ctx.measureText(text).width;
    const pillW = textW + padX * 2;
    const px = lx - pillW / 2;
    const py = ly - pillH / 2;

    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.lineTo(lx, ly);
    ctx.strokeStyle = accentColor;
    ctx.lineWidth = 1.3;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(ax, ay, 3.2, 0, Math.PI * 2);
    ctx.fillStyle = accentColor;
    ctx.fill();

    roundRect(ctx, px, py, pillW, pillH, 10);
    ctx.fillStyle = "rgba(31, 31, 31, 0.92)";
    ctx.fill();
    ctx.strokeStyle = accentColor;
    ctx.lineWidth = 1.2;
    ctx.stroke();

    ctx.fillStyle = "#fafafa";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(text, lx, ly + 0.5);
  }

  // =========================================================================
  // RENDER LIVE ANGULAR DISTRIBUTION HISTOGRAM
  // =========================================================================
  function renderHistogram() {
    const { width: W, height: H } = resizeHistCanvas();
    const ctx = histCtx;
    ctx.clearRect(0, 0, W, H);

    const labels = ["0–5°", "5–20°", "20–60°", "60–90°", "90–135°", "135–180°"];
    const colors = ["#4ade80", "#fb923c", "#fb923c", "#fb923c", "#f43f5e", "#f43f5e"];
    const bins = state.counts.bins;
    const maxLog = Math.max(1, ...bins.map((b) => Math.log10(b + 1)));

    const padLeft = 14;
    const padRight = 14;
    const padTop = 18;
    const padBottom = 24;
    const plotW = W - padLeft - padRight;
    const plotH = H - padTop - padBottom;
    const slotW = plotW / labels.length;

    ctx.font = "600 10px 'JetBrains Mono', monospace";
    ctx.textAlign = "center";

    for (let i = 0; i < labels.length; i++) {
      const count = bins[i];
      // Log-scaled bar height so rare backscattering is clearly visible alongside 0-5 deg peak
      const ratio = count > 0 ? Math.max(0.1, Math.log10(count + 1) / maxLog) : 0.02;
      const barH = ratio * plotH;
      const bx = padLeft + i * slotW + slotW * 0.16;
      const bw = slotW * 0.68;
      const by = padTop + plotH - barH;

      roundRect(ctx, bx, by, bw, barH, 3);
      ctx.fillStyle = colors[i];
      ctx.fill();

      ctx.fillStyle = "#d4d4d4";
      ctx.fillText(count.toString(), bx + bw / 2, Math.max(10, by - 5));

      ctx.fillStyle = "#a3a3a3";
      ctx.fillText(labels[i], bx + bw / 2, H - 7);
    }
  }

  // =========================================================================
  // FLASK API SINGLE-PARTICLE CALCULATOR
  // =========================================================================
  async function updateSingleParticleCalculator(fireParticle = false) {
    const bFm = parseFloat(sliderImpact.value);
    state.impactParamFm = bFm;
    valImpact.textContent = bFm.toFixed(1);

    try {
      const response = await fetch("/api/scattering", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          target: state.targetKey,
          energy_mev: state.energyMeV,
          impact_parameter_fm: bFm,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        calcTheta.textContent = `${data.scattering_angle_deg.toFixed(1)}°`;
        calcRmin.textContent = `${data.actual_closest_approach_fm.toFixed(1)} fm`;
        calcD0.textContent = `${data.head_on_closest_approach_fm.toFixed(1)} fm`;
      }
    } catch (_) {
      // Fallback local calculation if offline
      const thetaRad = computeScatteringThetaRad(
        bFm,
        state.targetZ,
        state.energyMeV,
        "rutherford"
      );
      const deg = Math.abs((thetaRad * 180) / Math.PI);
      calcTheta.textContent = `${deg.toFixed(1)}°`;
    }

    if (fireParticle) {
      spawnAlphaPair(null, bFm);
    }
  }

  // =========================================================================
  // INTERACTIVE UI EVENT LISTENERS
  // =========================================================================
  function setHighlightedPart(partId) {
    state.highlightedPartId = partId;
    document.querySelectorAll(".part-card").forEach((card) => {
      card.classList.toggle("active", card.dataset.partId === partId);
    });
    document.querySelectorAll(".schem-callout, .schem-part").forEach((el) => {
      el.classList.toggle("active", el.dataset.partId === partId);
    });
  }

  // Part Cards hover & click
  document.querySelectorAll(".part-card").forEach((card) => {
    const id = card.dataset.partId;
    card.addEventListener("mouseenter", () => setHighlightedPart(id));
    card.addEventListener("focus", () => setHighlightedPart(id));
    card.addEventListener("click", () => {
      setHighlightedPart(state.highlightedPartId === id ? null : id);
    });
  });

  // Schematic SVG Callouts & Parts hover & click
  document.querySelectorAll(".schem-callout, .schem-part").forEach((el) => {
    const id = el.dataset.partId;
    if (!id) return;
    el.addEventListener("mouseenter", () => setHighlightedPart(id));
    el.addEventListener("click", () => {
      setHighlightedPart(state.highlightedPartId === id ? null : id);
    });
  });

  // Schematic Theme Switcher (Blueprint Dark vs Textbook Light)
  const schematicContainer = document.getElementById("schematic-container");
  document.querySelectorAll("[data-schematic-theme]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document
        .querySelectorAll("[data-schematic-theme]")
        .forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      if (schematicContainer) {
        schematicContainer.dataset.theme = btn.dataset.schematicTheme;
      }
    });
  });

  // Download SVG Schematic Diagram
  const btnDownloadSvg = document.getElementById("btn-download-svg");
  const schematicSvg = document.getElementById("rutherford-schematic-svg");
  if (btnDownloadSvg && schematicSvg) {
    btnDownloadSvg.addEventListener("click", () => {
      const clonedSvg = schematicSvg.cloneNode(true);
      const isTextbook =
        schematicContainer && schematicContainer.dataset.theme === "textbook";
      const styleEl = document.createElementNS("http://www.w3.org/2000/svg", "style");
      styleEl.textContent = `
        svg { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; color: ${
          isTextbook ? "rgba(31, 31, 31,0.06)" : "rgba(56,189,248,0.075)"
        }; }
        .schem-bg { fill: ${isTextbook ? "#ffffff" : "#151515"}; }
        .schem-chamber-fill { fill: ${isTextbook ? "#f4f4f4" : "#1e1e1e"}; }
        .schem-inset-box { fill: ${isTextbook ? "#fafafa" : "#1f1f1f"}; stroke: ${
        isTextbook ? "#d4d4d4" : "#404040"
      }; stroke-width: 1.5; }
        .schem-divider { stroke: #737373; stroke-width: 1.5; }
        .schem-panel-heading { fill: ${
          isTextbook ? "#1f1f1f" : "#f5c542"
        }; font-family: monospace; font-size: 12.5px; font-weight: 800; }
        .schem-panel-sub { fill: ${isTextbook ? "#555555" : "#a3a3a3"}; font-size: 11.5px; }
        .schem-deg-text { fill: ${
          isTextbook ? "#404040" : "#a3a3a3"
        }; font-family: monospace; font-size: 10.5px; font-weight: 600; }
        .schem-annotation { fill: ${isTextbook ? "#2e2e2e" : "#d4d4d4"}; font-size: 11px; }
        .schem-code-label { fill: ${
          isTextbook ? "#1f1f1f" : "#fafafa"
        }; font-family: monospace; font-size: 11px; font-weight: 700; }
        .schem-math-label { fill: ${
          isTextbook ? "#b45309" : "#f5c542"
        }; font-family: monospace; font-size: 12px; font-weight: 800; }
        .schem-formula-box { fill: ${
          isTextbook ? "#fef3c7" : "#1e1b18"
        }; stroke: #d97706; stroke-width: 1.2; }
        .schem-formula-text { fill: ${
          isTextbook ? "#78350f" : "#fef08a"
        }; font-family: monospace; font-size: 11px; font-weight: 700; }
        .callout-line { stroke: #737373; stroke-width: 1.4; }
        .callout-pill { fill: ${isTextbook ? "#ffffff" : "#1f1f1f"}; stroke: #737373; stroke-width: 1.2; }
        .callout-num-bg { fill: ${
          isTextbook ? "#fef3c7" : "#2e2618"
        }; stroke: #f5c542; stroke-width: 1; }
        .callout-num { fill: ${
          isTextbook ? "#92400e" : "#f5c542"
        }; font-family: monospace; font-size: 10px; font-weight: 800; text-anchor: middle; }
        .callout-text { fill: ${
          isTextbook ? "#1f1f1f" : "#fafafa"
        }; font-size: 11.5px; font-weight: 600; }
      `;
      clonedSvg.insertBefore(styleEl, clonedSvg.firstChild);

      const serializer = new XMLSerializer();
      const svgString =
        '<?xml version="1.0" encoding="UTF-8"?>\n' + serializer.serializeToString(clonedSvg);
      const blob = new Blob([svgString], { type: "image/svg+xml;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.download = "rutherford-gold-leaf-schematic.svg";
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    });
  }

  btnClearHighlight.addEventListener("click", () => setHighlightedPart(null));

  // Click or Drag on Macro Canvas (for labels & rotatable microscope)
  macroCanvas.addEventListener("pointerdown", (e) => {
    const rect = macroCanvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;

    // Check if user clicked a callout label pill
    for (const box of state.labelHitBoxes) {
      if (mx >= box.x && mx <= box.x + box.w && my >= box.y && my <= box.y + box.h) {
        setHighlightedPart(state.highlightedPartId === box.id ? null : box.id);
        return;
      }
    }

    // Otherwise allow dragging microscope angle around the chamber center
    const cx = rect.width * 0.58;
    const cy = rect.height * 0.51;
    const dist = Math.hypot(mx - cx, my - cy);
    const screenR = Math.min(rect.width * 0.31, rect.height * 0.37);
    if (Math.abs(dist - screenR) < 52) {
      state.isDraggingMicroscope = true;
      updateMicroscopeFromPointer(mx, my, cx, cy);
    }
  });

  window.addEventListener("pointermove", (e) => {
    if (!state.isDraggingMicroscope) return;
    const rect = macroCanvas.getBoundingClientRect();
    const mx = e.clientX - rect.left;
    const my = e.clientY - rect.top;
    const cx = rect.width * 0.58;
    const cy = rect.height * 0.51;
    updateMicroscopeFromPointer(mx, my, cx, cy);
  });

  window.addEventListener("pointerup", () => {
    state.isDraggingMicroscope = false;
  });

  function updateMicroscopeFromPointer(mx, my, cx, cy) {
    const angleRad = Math.atan2(-(my - cy), mx - cx);
    let deg = Math.round((angleRad * 180) / Math.PI / 5) * 5;
    deg = Math.max(-165, Math.min(165, deg));
    state.microscopeAngleDeg = deg;
    sliderMicroscope.value = deg;
    valMicroscope.textContent = `${deg}°`;
  }

  // View Mode Switcher (Split / Macro / Atomic)
  document.querySelectorAll("[data-view]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-view]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.viewMode = btn.dataset.view;
      stageEl.className = `canvas-stage view-${state.viewMode}`;
    });
  });

  // Real Historical Experiment Switcher (Rutherford 1909 Gold Leaf vs Thomson 1897 Cathode Ray Tube)
  const macroPanelTag = document.getElementById("macro-panel-tag");
  const macroPanelTitle = document.getElementById("macro-panel-title");
  const macroPanelHint = document.getElementById("macro-panel-hint");
  const atomicPanelTag = document.getElementById("atomic-panel-tag");

  document.querySelectorAll("[data-model]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-model]").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.atomicModel = btn.dataset.model;
      state.macroParticles = [];
      state.atomicParticles = [];
      state.scintillations = [];
      if (state.atomicModel === "rutherford") {
        if (macroPanelTag) macroPanelTag.textContent = "MACROSCOPIC VIEW • TOP-DOWN SCHEMATIC";
        if (macroPanelTitle)
          macroPanelTitle.textContent = "1909 Geiger–Marsden Vacuum Chamber Apparatus";
        if (macroPanelHint)
          macroPanelHint.textContent =
            "Click any numbered label ①–⑪ or drag the microscope along the ZnS ring";
        if (atomicPanelTag) atomicPanelTag.textContent = "SUBATOMIC SCALE • ~10⁻¹⁴ m ZOOM";
        atomicPanelTitle.textContent =
          "Gold Leaf Atomic Lattice & Nuclear Coulomb Repulsion";
        atomicModelBadge.textContent = `Experiment: Rutherford α-Scattering (+${state.targetZ}e Nucleus)`;
      } else {
        if (macroPanelTag) macroPanelTag.textContent = "MACROSCOPIC VIEW • CAVENDISH LAB 1897";
        if (macroPanelTitle)
          macroPanelTitle.textContent = "1897 J.J. Thomson Cathode Ray Tube Apparatus";
        if (macroPanelHint)
          macroPanelHint.textContent =
            "Electrons (e⁻) deflected by Electric (E) & Magnetic (B) fields";
        if (atomicPanelTag) atomicPanelTag.textContent = "DEFLECTION REGION ZOOM • E & B FIELDS";
        atomicPanelTitle.textContent =
          "Cathode Ray Electron Deflection Between Parallel Plates (F_E = −eE)";
        atomicModelBadge.textContent = "Experiment: Discovery of the Electron (1897)";
      }
    });
  });

  // Play / Pause
  btnPlayPause.addEventListener("click", () => {
    state.running = !state.running;
    playIcon.textContent = state.running ? "⏸" : "▶";
    playText.textContent = state.running ? "Pause" : "Resume";
  });

  // Fire Burst
  btnFireBurst.addEventListener("click", () => {
    for (let i = 0; i < 18; i++) {
      spawnAlphaPair();
    }
  });

  // Fire Head-On (Guaranteed Backscattering demonstration)
  btnFireHeadOn.addEventListener("click", () => {
    spawnAlphaPair("headon");
  });

  // Reset Counters
  btnReset.addEventListener("click", () => {
    state.counts.total = 0;
    state.counts.straight = 0;
    state.counts.small = 0;
    state.counts.back = 0;
    state.counts.bins = [0, 0, 0, 0, 0, 0];
    state.macroParticles = [];
    state.atomicParticles = [];
    state.scintillations = [];
    updateTelemetryDOM();
  });

  // Controls & Sliders
  selectTarget.addEventListener("change", () => {
    const key = selectTarget.value;
    const t = window.TARGET_ELEMENTS[key];
    if (t) {
      state.targetKey = key;
      state.targetZ = t.Z;
      state.targetColor = t.color;
      if (state.atomicModel === "rutherford") {
        atomicModelBadge.textContent = `Experiment: Rutherford α-Scattering (+${state.targetZ}e Nucleus)`;
      }
      updateSingleParticleCalculator(false);
    }
  });

  sliderEnergy.addEventListener("input", () => {
    state.energyMeV = parseFloat(sliderEnergy.value);
    valEnergy.textContent = state.energyMeV.toFixed(1);
    updateSingleParticleCalculator(false);
  });

  sliderRate.addEventListener("input", () => {
    state.rateLevel = parseInt(sliderRate.value, 10);
    valRate.textContent = RATE_NAMES[state.rateLevel - 1] || "Medium";
  });

  sliderMicroscope.addEventListener("input", () => {
    state.microscopeAngleDeg = parseInt(sliderMicroscope.value, 10);
    valMicroscope.textContent = `${state.microscopeAngleDeg}°`;
  });

  sliderImpact.addEventListener("input", () => {
    updateSingleParticleCalculator(false);
  });

  btnTestSingle.addEventListener("click", () => {
    updateSingleParticleCalculator(true);
  });

  toggleLabels.addEventListener("change", () => {
    state.showLabels = toggleLabels.checked;
  });

  toggleExaggerate.addEventListener("change", () => {
    state.exaggerateRare = toggleExaggerate.checked;
  });

  toggleTrails.addEventListener("change", () => {
    state.showTrails = toggleTrails.checked;
  });

  // Seed initial particles so canvas is immediately lively on load
  for (let i = 0; i < 10; i++) {
    spawnAlphaPair();
    state.macroParticles[i].progress = Math.random();
  }
  updateSingleParticleCalculator(false);

  // Main Animation Loop
  let lastFrameTime = performance.now();
  function animate(now) {
    const dt = Math.min(0.05, (now - lastFrameTime) / 1000);
    lastFrameTime = now;

    if (state.running) {
      stepSimulation(dt);
    }

    if (state.viewMode !== "atomic") {
      renderMacroCanvas();
    }
    if (state.viewMode !== "macro") {
      renderAtomicCanvas();
    }
    renderHistogram();

    requestAnimationFrame(animate);
  }

  requestAnimationFrame(animate);
})();
