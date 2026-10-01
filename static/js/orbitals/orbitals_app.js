/**
 * orbitals_app.js — page controller for the Atomic Orbitals section.
 *
 *   Module A: step-by-step Schrödinger derivation + explanatory graphs
 *   Module B: 3D orbital viewer controls, radial & angular graphs
 *   Module C: periodic table, configuration engine UI, orbital box diagram
 */

import {
  makeRadial, makeAngular, radialNodes, coneNodeAngles, planeNodeAngles, radiusEnclosing,
  energyEV, orbitalNameHTML, orbitalNameTex, angularFormulaTex, L_LETTERS, BOHR_RADIUS_ANGSTROM,
} from './quantum_math.js';

const COLORS = {
  pos: '#f59e0b',
  neg: '#3b82f6',
  gold: '#f5c542',
  cyan: '#38bdf8',
  grid: 'rgba(163, 163, 163,0.16)',
  axis: 'rgba(203,213,225,0.55)',
  text: '#d4d4d4',
  muted: '#a3a3a3',
  node: 'rgba(255,255,255,0.75)',
};
const BLOCK_COLORS = { s: '#f472b6', p: '#facc15', d: '#38bdf8', f: '#4ade80' };
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

/* ------------------------------------------------------------------ */
/* Shared helpers                                                      */
/* ------------------------------------------------------------------ */

/** Resize a canvas for its CSS width at device-pixel-ratio; returns ctx in CSS px. */
function prepCanvas(canvas) {
  if (!canvas.dataset.aspect) canvas.dataset.aspect = String(canvas.height / canvas.width);
  const aspect = parseFloat(canvas.dataset.aspect);
  const w = canvas.clientWidth || parseFloat(canvas.getAttribute('width'));
  const h = w * aspect;
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  if (canvas.width !== Math.round(w * dpr) || canvas.height !== Math.round(h * dpr)) {
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
  }
  const ctx = canvas.getContext('2d');
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  ctx.clearRect(0, 0, w, h);
  return { ctx, w, h };
}

function katexRender(el, tex, display = false) {
  if (!el) return;
  if (window.katex) {
    try {
      window.katex.render(tex, el, { displayMode: display, throwOnError: false });
      return;
    } catch (e) { /* fall through */ }
  }
  el.textContent = tex;
}

function waitForKatex(timeoutMs = 8000) {
  return new Promise((resolve) => {
    const t0 = performance.now();
    (function poll() {
      if (window.katex && window.renderMathInElement) resolve(true);
      else if (performance.now() - t0 > timeoutMs) resolve(false);
      else setTimeout(poll, 60);
    })();
  });
}

const fmt = (v, d = 2) => Number(v).toFixed(d);
const msLabel = (ms) => (ms > 0 ? '+½' : '−½');
const signed = (m) => (m > 0 ? `+${m}` : `${m}`);

/* ------------------------------------------------------------------ */
/* Graph drawing (shared by Module A step 4/5 and Module B)            */
/* ------------------------------------------------------------------ */

function drawRadialGraph(canvas, n, l, { compact = false } = {}) {
  const { ctx, w, h } = prepCanvas(canvas);
  const R = makeRadial(n, l, 1);
  const rMax = radiusEnclosing(n, l, 0.995, 1) * 1.05;
  const pad = { l: 46, r: 16, t: 18, b: 34 };
  const pw = w - pad.l - pad.r;
  const ph = h - pad.t - pad.b;
  const N = 600;
  const rs = [];
  const Rv = [];
  const Pv = [];
  let maxP = 0;
  let maxR = 0;
  let rPeak = 0;
  for (let i = 0; i <= N; i++) {
    const r = (rMax * i) / N;
    const v = R(r);
    const p = r * r * v * v;
    rs.push(r); Rv.push(v); Pv.push(p);
    if (p > maxP) { maxP = p; rPeak = r; }
    maxR = Math.max(maxR, Math.abs(v));
  }
  const baseY = pad.t + ph * 0.62;
  const X = (r) => pad.l + (r / rMax) * pw;
  const YP = (p) => baseY - (p / maxP) * ph * 0.58;
  const YR = (v) => baseY - (v / maxR) * ph * 0.36;

  // grid + axes
  ctx.strokeStyle = COLORS.grid;
  ctx.lineWidth = 1;
  ctx.font = '11px Inter, sans-serif';
  ctx.fillStyle = COLORS.muted;
  const step = niceStep(rMax / 8);
  for (let r = 0; r <= rMax + 1e-9; r += step) {
    ctx.beginPath(); ctx.moveTo(X(r), pad.t); ctx.lineTo(X(r), pad.t + ph); ctx.stroke();
    ctx.textAlign = 'center';
    ctx.fillText(fmt(r, step < 1 ? 1 : 0), X(r), h - pad.b + 15);
  }
  ctx.strokeStyle = COLORS.axis;
  ctx.beginPath(); ctx.moveTo(pad.l, baseY); ctx.lineTo(pad.l + pw, baseY); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l, pad.t + ph); ctx.stroke();
  ctx.fillStyle = COLORS.text;
  ctx.textAlign = 'center';
  ctx.fillText('r / a₀', pad.l + pw / 2, h - 4);

  // P(r) filled
  const grad = ctx.createLinearGradient(0, pad.t, 0, baseY);
  grad.addColorStop(0, 'rgba(245,197,66,0.55)');
  grad.addColorStop(1, 'rgba(245,197,66,0.05)');
  ctx.beginPath();
  ctx.moveTo(X(0), baseY);
  for (let i = 0; i <= N; i++) ctx.lineTo(X(rs[i]), YP(Pv[i]));
  ctx.lineTo(X(rMax), baseY);
  ctx.closePath();
  ctx.fillStyle = grad;
  ctx.fill();
  ctx.beginPath();
  for (let i = 0; i <= N; i++) (i ? ctx.lineTo : ctx.moveTo).call(ctx, X(rs[i]), YP(Pv[i]));
  ctx.strokeStyle = COLORS.gold;
  ctx.lineWidth = 2;
  ctx.stroke();

  // R(r) dashed, coloured by sign
  ctx.setLineDash([5, 4]);
  ctx.lineWidth = 1.6;
  for (let i = 0; i < N; i++) {
    ctx.strokeStyle = Rv[i] >= 0 ? COLORS.pos : COLORS.neg;
    ctx.beginPath();
    ctx.moveTo(X(rs[i]), YR(Rv[i]));
    ctx.lineTo(X(rs[i + 1]), YR(Rv[i + 1]));
    ctx.stroke();
  }
  ctx.setLineDash([]);

  // radial nodes
  const nodes = radialNodes(n, l, 1);
  ctx.font = '10px Inter, sans-serif';
  nodes.forEach((rn, idx) => {
    ctx.strokeStyle = COLORS.node;
    ctx.setLineDash([3, 3]);
    ctx.beginPath(); ctx.moveTo(X(rn), pad.t + 4); ctx.lineTo(X(rn), pad.t + ph); ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#fff';
    ctx.beginPath(); ctx.arc(X(rn), baseY, 3.5, 0, 2 * Math.PI); ctx.fill();
    ctx.textAlign = 'center';
    ctx.fillText(`node ${idx + 1}: ${fmt(rn, 2)} a₀`, X(rn), pad.t + 10 + (idx % 2) * 12);
  });

  // peak marker
  ctx.fillStyle = COLORS.gold;
  ctx.beginPath(); ctx.arc(X(rPeak), YP(maxP), 4, 0, 2 * Math.PI); ctx.fill();
  ctx.textAlign = 'left';
  ctx.fillText(`r_mp = ${fmt(rPeak, 2)} a₀`, Math.min(X(rPeak) + 7, w - 110), YP(maxP) + 4);

  // legend
  if (!compact || w > 420) {
    ctx.textAlign = 'right';
    ctx.font = '11px Inter, sans-serif';
    ctx.fillStyle = COLORS.gold;
    ctx.fillText('━ P(r) = r²R²', w - pad.r, pad.t + 12);
    ctx.fillStyle = COLORS.pos;
    ctx.fillText('┅ R(r) > 0', w - pad.r, pad.t + 26);
    ctx.fillStyle = COLORS.neg;
    ctx.fillText('┅ R(r) < 0', w - pad.r, pad.t + 40);
  }
  return { rPeak, nodes, rMax };
}

function niceStep(raw) {
  const p = Math.pow(10, Math.floor(Math.log10(raw)));
  const f = raw / p;
  return (f < 1.5 ? 1 : f < 3.5 ? 2 : f < 7.5 ? 5 : 10) * p;
}

/** Polar plot of |Y_lm| in the vertical plane φ = φ0 (and φ0 + π). */
function drawAngularPolar(canvas, l, m) {
  const { ctx, w, h } = prepCanvas(canvas);
  const Y = makeAngular(l, m);
  const am = Math.abs(m);
  const phi0 = m < 0 ? Math.PI / (2 * am) : 0;
  const cx = w / 2;
  const cy = h / 2;
  const scale = Math.min(w, h) * 0.4;
  const N = 720;
  const pts = [];
  let maxY = 0;
  for (let i = 0; i <= N; i++) {
    const a = (2 * Math.PI * i) / N;
    const theta = a <= Math.PI ? a : 2 * Math.PI - a;
    const phi = a <= Math.PI ? phi0 : phi0 + Math.PI;
    const v = Y(Math.cos(theta), phi);
    pts.push({ a, v });
    maxY = Math.max(maxY, Math.abs(v));
  }
  if (maxY === 0) maxY = 1;

  // axes / rings
  ctx.strokeStyle = COLORS.grid;
  for (let k = 1; k <= 3; k++) {
    ctx.beginPath(); ctx.arc(cx, cy, (scale * k) / 3, 0, 2 * Math.PI); ctx.stroke();
  }
  ctx.strokeStyle = COLORS.axis;
  ctx.beginPath(); ctx.moveTo(cx, cy - scale * 1.15); ctx.lineTo(cx, cy + scale * 1.15); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(cx - scale * 1.15, cy); ctx.lineTo(cx + scale * 1.15, cy); ctx.stroke();
  ctx.fillStyle = COLORS.text;
  ctx.font = '11px Inter, sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('z', cx + 9, cy - scale * 1.1);
  const hLabel = Math.abs(phi0) < 1e-9 ? 'x' : Math.abs(phi0 - Math.PI / 2) < 1e-9 ? 'y' : `φ=${fmt((phi0 * 180) / Math.PI, 0)}°`;
  ctx.fillText(hLabel, cx + scale * 1.12, cy - 6);

  const P = (pt) => {
    const r = (Math.abs(pt.v) / maxY) * scale;
    return [cx + r * Math.sin(pt.a), cy - r * Math.cos(pt.a)];
  };
  for (let i = 0; i < N; i++) {
    const p1 = P(pts[i]);
    const p2 = P(pts[i + 1]);
    const col = pts[i].v >= 0 ? COLORS.pos : COLORS.neg;
    ctx.fillStyle = col + '55';
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(p1[0], p1[1]); ctx.lineTo(p2[0], p2[1]); ctx.closePath(); ctx.fill();
    ctx.strokeStyle = col;
    ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(p1[0], p1[1]); ctx.lineTo(p2[0], p2[1]); ctx.stroke();
  }
  // conical nodes as dashed lines
  ctx.setLineDash([4, 4]);
  ctx.strokeStyle = COLORS.node;
  ctx.lineWidth = 1;
  for (const th of coneNodeAngles(l, m)) {
    for (const s of [1, -1]) {
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + s * scale * 1.1 * Math.sin(th), cy - scale * 1.1 * Math.cos(th));
      ctx.stroke();
    }
  }
  ctx.setLineDash([]);
  return { phi0 };
}

/* ------------------------------------------------------------------ */
/* MODULE A                                                            */
/* ------------------------------------------------------------------ */

const ModuleA = {
  step: 1,
  playing: false,
  timer: null,
  raf: null,

  init() {
    $$('.step-tab').forEach((t) => t.addEventListener('click', () => { this.stop(); this.setStep(+t.dataset.step); }));
    $('#step-prev').addEventListener('click', () => { this.stop(); this.setStep(Math.max(1, this.step - 1)); });
    $('#step-next').addEventListener('click', () => { this.stop(); this.setStep(Math.min(5, this.step + 1)); });
    $('#step-play').addEventListener('click', () => (this.playing ? this.stop() : this.play()));

    const ring = $('#ring-m');
    ring.addEventListener('input', () => this.drawRing());
    const pl = $('#polar-l');
    const pm = $('#polar-m');
    pl.addEventListener('input', () => {
      const l = +pl.value;
      pm.min = -l; pm.max = l;
      if (Math.abs(+pm.value) > l) pm.value = 0;
      this.drawPolarStep();
    });
    pm.addEventListener('input', () => this.drawPolarStep());
    const rn = $('#rad-n');
    const rl = $('#rad-l');
    rn.addEventListener('input', () => {
      rl.max = +rn.value - 1;
      if (+rl.value > +rl.max) rl.value = rl.max;
      this.drawRadialStep();
    });
    rl.addEventListener('input', () => this.drawRadialStep());
    window.addEventListener('resize', () => this.drawCurrent());
    this.setStep(1);
    this.animate();
  },

  setStep(k) {
    this.step = k;
    $$('.step-tab').forEach((t) => {
      const s = +t.dataset.step;
      t.classList.toggle('active', s === k);
      t.classList.toggle('done', s < k);
      t.setAttribute('aria-selected', String(s === k));
    });
    $$('.step-panel').forEach((p) => p.classList.toggle('active', +p.dataset.step === k));
    $('#step-progress-bar').style.inlineSize = `${k * 20}%`;
    this.stepStart = performance.now();
    requestAnimationFrame(() => this.drawCurrent());
  },

  play() {
    this.playing = true;
    $('#step-play').textContent = '⏸ Pause';
    if (this.step === 5) this.setStep(1);
    this.timer = setInterval(() => {
      if (this.step >= 5) { this.stop(); return; }
      this.setStep(this.step + 1);
    }, 9000);
  },

  stop() {
    this.playing = false;
    clearInterval(this.timer);
    $('#step-play').textContent = '▶ Auto-play';
  },

  drawCurrent() {
    if (this.step === 4) { this.drawRing(); this.drawPolarStep(); }
    if (this.step === 5) this.drawRadialStep();
  },

  animate() {
    const loop = (t) => {
      this.raf = requestAnimationFrame(loop);
      const panel = $('#module-a');
      const rect = panel.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      if (this.step === 1) this.drawStep1(t);
      if (this.step === 2) this.drawStep2(t);
    };
    this.raf = requestAnimationFrame(loop);
  },

  drawStep1(t) {
    const canvas = $('#canvas-step1');
    const { ctx, w, h } = prepCanvas(canvas);
    const pad = { l: 52, r: 20, t: 20, b: 36 };
    const rMax = 40;
    const eMin = -16;
    const eMax = 3;
    const X = (r) => pad.l + (r / rMax) * (w - pad.l - pad.r);
    const Yv = (e) => pad.t + ((eMax - e) / (eMax - eMin)) * (h - pad.t - pad.b);
    ctx.font = '11px Inter, sans-serif';
    // axes
    ctx.strokeStyle = COLORS.grid;
    for (let e = -15; e <= 0; e += 5) {
      ctx.beginPath(); ctx.moveTo(pad.l, Yv(e)); ctx.lineTo(w - pad.r, Yv(e)); ctx.stroke();
      ctx.fillStyle = COLORS.muted; ctx.textAlign = 'right';
      ctx.fillText(`${e}`, pad.l - 6, Yv(e) + 4);
    }
    ctx.strokeStyle = COLORS.axis;
    ctx.beginPath(); ctx.moveTo(pad.l, Yv(0)); ctx.lineTo(w - pad.r, Yv(0)); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(pad.l, pad.t); ctx.lineTo(pad.l, h - pad.b); ctx.stroke();
    ctx.fillStyle = COLORS.text;
    ctx.textAlign = 'center';
    ctx.fillText('r / a₀', (pad.l + w) / 2, h - 8);
    ctx.save(); ctx.translate(14, h / 2); ctx.rotate(-Math.PI / 2); ctx.fillText('Energy (eV)', 0, 0); ctx.restore();
    for (let r = 0; r <= rMax; r += 10) { ctx.fillStyle = COLORS.muted; ctx.fillText(String(r), X(r), h - pad.b + 14); }

    // Coulomb well V(r) = −27.211/r eV
    const grad = ctx.createLinearGradient(0, Yv(eMin), 0, Yv(0));
    grad.addColorStop(0, 'rgba(56,189,248,0.25)');
    grad.addColorStop(1, 'rgba(56,189,248,0.02)');
    ctx.beginPath();
    ctx.moveTo(X(27.211 / 16), Yv(eMin));
    for (let r = 27.211 / 16; r <= rMax; r += 0.1) ctx.lineTo(X(r), Yv(-27.211 / r));
    ctx.lineTo(X(rMax), Yv(eMin));
    ctx.closePath();
    ctx.fillStyle = grad; ctx.fill();
    ctx.beginPath();
    for (let r = 27.211 / 16; r <= rMax; r += 0.1) ctx.lineTo(X(r), Yv(-27.211 / r));
    ctx.strokeStyle = COLORS.cyan; ctx.lineWidth = 2.2; ctx.stroke();
    ctx.fillStyle = COLORS.cyan; ctx.textAlign = 'left';
    ctx.fillText('V(r) = −Ze²/(4πε₀r)', X(3.2), Yv(-12));

    // energy levels up to turning point r = 2n²
    for (let n = 1; n <= 6; n++) {
      const E = energyEV(n);
      const rt = Math.min(rMax, 2 * n * n);
      ctx.strokeStyle = n === 2 ? COLORS.gold : 'rgba(245,197,66,0.6)';
      ctx.lineWidth = n === 2 ? 2 : 1.3;
      ctx.beginPath(); ctx.moveTo(X(0), Yv(E)); ctx.lineTo(X(rt), Yv(E)); ctx.stroke();
      ctx.fillStyle = COLORS.gold;
      ctx.textAlign = 'left';
      if (n <= 4) ctx.fillText(`n=${n}  E=${fmt(E, 2)} eV`, X(rt) + 6, Yv(E) + 4);
    }
    // Balmer transitions (measured wavelengths) appearing in sequence
    const lines = [
      { from: 3, color: '#ef4444', label: 'Hα 656.3 nm' },
      { from: 4, color: '#22d3ee', label: 'Hβ 486.1 nm' },
      { from: 5, color: '#818cf8', label: 'Hγ 434.0 nm' },
      { from: 6, color: '#a855f7', label: 'Hδ 410.2 nm' },
    ];
    const phase = ((t - (this.stepStart || 0)) / 900) % (lines.length + 2);
    lines.forEach((ln, i) => {
      if (phase < i + 0.2 && !reduceMotion) return;
      const x = X(1.2 + i * 1.6);
      const y1 = Yv(energyEV(ln.from));
      const y2 = Yv(energyEV(2));
      ctx.strokeStyle = ln.color; ctx.fillStyle = ln.color; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x, y1); ctx.lineTo(x, y2 - 6); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(x - 4, y2 - 8); ctx.lineTo(x + 4, y2 - 8); ctx.lineTo(x, y2); ctx.closePath(); ctx.fill();
      ctx.save(); ctx.translate(x - 4, y2 + 14 + i * 12); ctx.textAlign = 'left';
      ctx.font = '10px Inter, sans-serif';
      ctx.fillText(ln.label, 0, 0); ctx.restore();
    });
  },

  drawStep2(t) {
    const canvas = $('#canvas-step2');
    const { ctx, w, h } = prepCanvas(canvas);
    const s = Math.min(w, h) * 0.36;
    const cx = w * 0.45;
    const cy = h * 0.6;
    const proj = (x, y, z) => [cx + y * s - x * s * 0.55, cy - z * s + x * s * 0.38];
    const time = reduceMotion ? 0 : (t - (this.stepStart || 0)) / 1000;
    const theta = 0.95 + 0.25 * Math.sin(time * 0.8);
    const phi = 0.75 + 0.35 * Math.sin(time * 0.55 + 1);
    const r = 1;
    const P = [r * Math.sin(theta) * Math.cos(phi), r * Math.sin(theta) * Math.sin(phi), r * Math.cos(theta)];
    const line = (a, b, color, width = 1.5, dash = []) => {
      const p = proj(...a); const q = proj(...b);
      ctx.strokeStyle = color; ctx.lineWidth = width; ctx.setLineDash(dash);
      ctx.beginPath(); ctx.moveTo(p[0], p[1]); ctx.lineTo(q[0], q[1]); ctx.stroke(); ctx.setLineDash([]);
    };
    const label = (pt, text, color, dx = 0, dy = 0) => {
      const p = proj(...pt); ctx.fillStyle = color; ctx.font = '600 13px Inter, sans-serif'; ctx.textAlign = 'center';
      ctx.fillText(text, p[0] + dx, p[1] + dy);
    };
    // xy-plane disc
    ctx.fillStyle = 'rgba(56,189,248,0.06)';
    ctx.beginPath();
    for (let i = 0; i <= 64; i++) { const a = (i / 64) * 2 * Math.PI; const p = proj(1.2 * Math.cos(a), 1.2 * Math.sin(a), 0); i ? ctx.lineTo(...p) : ctx.moveTo(...p); }
    ctx.fill();
    line([0, 0, 0], [1.4, 0, 0], '#f87171', 1.6); label([1.55, 0, 0], 'x', '#f87171');
    line([0, 0, 0], [0, 1.4, 0], '#4ade80', 1.6); label([0, 1.52, 0], 'y', '#4ade80');
    line([0, 0, 0], [0, 0, 1.35], '#60a5fa', 1.6); label([0, 0, 1.47], 'z', '#60a5fa');
    // r vector, projections
    line([0, 0, 0], P, COLORS.gold, 2.5);
    line(P, [P[0], P[1], 0], 'rgba(255,255,255,0.5)', 1, [4, 4]);
    line([0, 0, 0], [P[0], P[1], 0], 'rgba(255,255,255,0.5)', 1, [4, 4]);
    // θ arc
    ctx.beginPath();
    for (let i = 0; i <= 30; i++) {
      const th = (theta * i) / 30; const rr = 0.35;
      const p = proj(rr * Math.sin(th) * Math.cos(phi), rr * Math.sin(th) * Math.sin(phi), rr * Math.cos(th));
      i ? ctx.lineTo(...p) : ctx.moveTo(...p);
    }
    ctx.strokeStyle = '#f472b6'; ctx.lineWidth = 2; ctx.stroke();
    label([0.45 * Math.sin(theta / 2) * Math.cos(phi), 0.45 * Math.sin(theta / 2) * Math.sin(phi), 0.45 * Math.cos(theta / 2)], 'θ', '#f472b6', 8, 0);
    // φ arc
    ctx.beginPath();
    for (let i = 0; i <= 30; i++) { const ph = (phi * i) / 30; const p = proj(0.42 * Math.cos(ph), 0.42 * Math.sin(ph), 0); i ? ctx.lineTo(...p) : ctx.moveTo(...p); }
    ctx.strokeStyle = '#a78bfa'; ctx.stroke();
    label([0.55 * Math.cos(phi / 2), 0.55 * Math.sin(phi / 2), 0], 'φ', '#a78bfa', 0, 12);
    // point + r label
    const pp = proj(...P);
    ctx.fillStyle = COLORS.gold; ctx.beginPath(); ctx.arc(pp[0], pp[1], 6, 0, 2 * Math.PI); ctx.fill();
    label(P.map((v) => v * 0.55), 'r', COLORS.gold, -10, -4);
    ctx.fillStyle = COLORS.text; ctx.font = '12px JetBrains Mono, monospace'; ctx.textAlign = 'left';
    ctx.fillText(`θ = ${fmt((theta * 180) / Math.PI, 0)}°   φ = ${fmt((phi * 180) / Math.PI, 0)}°`, 14, 22);
    ctx.fillText('electron (e⁻) at (r, θ, φ)', pp[0] + 10, pp[1] - 8);
    ctx.fillStyle = '#fde68a'; ctx.beginPath(); const o = proj(0, 0, 0); ctx.arc(o[0], o[1], 4, 0, 2 * Math.PI); ctx.fill();
    ctx.fillStyle = COLORS.muted; ctx.fillText('nucleus +Ze', o[0] + 8, o[1] + 16);
  },

  drawRing() {
    const canvas = $('#canvas-step4-ring');
    const m = +$('#ring-m').value;
    $('#ring-m-val').textContent = fmt(m, 2);
    const { ctx, w, h } = prepCanvas(canvas);
    const cx = w / 2; const cy = h / 2;
    const R0 = Math.min(w, h) * 0.3;
    const A = Math.min(w, h) * 0.1;
    ctx.strokeStyle = COLORS.grid; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.arc(cx, cy, R0, 0, 2 * Math.PI); ctx.stroke();
    const N = 400;
    for (let i = 0; i < N; i++) {
      const a1 = (2 * Math.PI * i) / N; const a2 = (2 * Math.PI * (i + 1)) / N;
      const v1 = Math.cos(m * a1); const v2 = Math.cos(m * a2);
      ctx.strokeStyle = v1 >= 0 ? COLORS.pos : COLORS.neg; ctx.lineWidth = 2.4;
      ctx.beginPath();
      ctx.moveTo(cx + (R0 + A * v1) * Math.cos(a1), cy - (R0 + A * v1) * Math.sin(a1));
      ctx.lineTo(cx + (R0 + A * v2) * Math.cos(a2), cy - (R0 + A * v2) * Math.sin(a2));
      ctx.stroke();
    }
    const integer = Math.abs(m - Math.round(m)) < 1e-6;
    const vStart = 1; const vEnd = Math.cos(m * 2 * Math.PI);
    ctx.strokeStyle = integer ? COLORS.gold : '#f43f5e'; ctx.lineWidth = integer ? 2 : 4;
    ctx.beginPath(); ctx.moveTo(cx + R0 + A * vStart, cy); ctx.lineTo(cx + R0 + A * vEnd, cy); ctx.stroke();
    ctx.fillStyle = integer ? COLORS.gold : '#f43f5e';
    ctx.beginPath(); ctx.arc(cx + R0 + A * vStart, cy, 4, 0, 2 * Math.PI); ctx.fill();
    ctx.font = '11px Inter, sans-serif'; ctx.textAlign = 'center'; ctx.fillStyle = COLORS.text;
    ctx.fillText('φ = 0 ≡ 2π', cx + R0 + A + 4, cy - 12);
    ctx.fillText(`Re Φ = cos(${fmt(m, 2)} φ)`, cx, cy + 4);
    const st = $('#ring-status');
    st.textContent = integer
      ? `m = ${Math.round(m)} (integer): Φ(0) = Φ(2π) — single-valued, allowed.`
      : `m = ${fmt(m, 2)}: Φ(2π) = ${fmt(vEnd, 2)} ≠ Φ(0) = 1 — multi-valued, forbidden!`;
    st.classList.toggle('bad', !integer);
  },

  drawPolarStep() {
    const l = +$('#polar-l').value;
    const m = +$('#polar-m').value;
    $('#polar-l-val').textContent = l;
    $('#polar-m-val').textContent = signed(m);
    drawAngularPolar($('#canvas-step4-polar'), l, m);
    $('#polar-caption').innerHTML = `${orbitalNameHTML('', l, m) || 's'} — ${l} angular node${l === 1 ? '' : 's'}, |L| = √${l * (l + 1)} ħ, L<sub>z</sub> = ${signed(m)} ħ`;
  },

  drawRadialStep() {
    const n = +$('#rad-n').value;
    const l = +$('#rad-l').value;
    $('#rad-n-val').textContent = n;
    $('#rad-l-val').textContent = l;
    const info = drawRadialGraph($('#canvas-step5'), n, l);
    $('#rad-caption').innerHTML = `${n}${L_LETTERS[l]}: E<sub>${n}</sub> = ${fmt(energyEV(n), 3)} eV · ${info.nodes.length} radial node${info.nodes.length === 1 ? '' : 's'} · ⟨r⟩ = ${fmt((3 * n * n - l * (l + 1)) / 2, 1)} a₀`;
  },
};

/* ------------------------------------------------------------------ */
/* MODULE B                                                            */
/* ------------------------------------------------------------------ */

const PRESETS = [
  [1, 0, 0], [2, 0, 0], [2, 1, 0], [2, 1, 1], [3, 0, 0], [3, 1, -1], [3, 2, 0], [3, 2, -2],
  [3, 2, 2], [4, 0, 0], [4, 2, 1], [4, 3, 0], [4, 3, -2], [4, 3, 3], [5, 3, 1], [6, 0, 0],
];

const ModuleB = {
  viewer: null,
  n: 2, l: 1, m: 0,
  pending: null,

  async init() {
    const chips = $('#preset-chips');
    PRESETS.forEach(([n, l, m]) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'chip';
      b.innerHTML = orbitalNameHTML(n, l, m);
      b.dataset.key = `${n},${l},${m}`;
      b.addEventListener('click', () => this.set(n, l, m));
      chips.appendChild(b);
    });
    $('#qn-n').addEventListener('input', () => this.fromSliders('n'));
    $('#qn-l').addEventListener('input', () => this.fromSliders('l'));
    $('#qn-m').addEventListener('input', () => this.fromSliders('m'));

    const opt = (id, key) => $(id).addEventListener('change', (e) => this.viewer?.setOption(key, e.target.checked));
    opt('#opt-surface', 'surface');
    opt('#opt-cloud', 'cloud');
    opt('#opt-phase', 'phase');
    opt('#opt-nodes', 'nodes');
    opt('#opt-axes', 'axes');
    opt('#opt-rotate', 'autoRotate');
    $('#opt-graph').addEventListener('change', (e) => {
      $('#graph-row').hidden = !e.target.checked;
      if (e.target.checked) this.drawGraphs();
    });
    $('#clip').addEventListener('input', (e) => this.updateClip(+e.target.value));
    $('#surface-opacity').addEventListener('input', (e) => {
      $('#opacity-val').textContent = fmt(e.target.value, 2);
      this.viewer?.setSurfaceOpacity(+e.target.value);
    });
    $('#btn-buildup').addEventListener('click', () => this.replayCloud());
    $('#btn-reset-cam').addEventListener('click', () => this.viewer?.resetCamera());
    $('#btn-snapshot').addEventListener('click', () => {
      if (!this.viewer) return;
      const a = document.createElement('a');
      a.href = this.viewer.snapshot();
      a.download = `orbital_${this.n}${L_LETTERS[this.l]}_m${this.m}.png`;
      a.click();
    });
    window.addEventListener('resize', () => this.drawGraphs());

    this.syncSliders();
    this.updateInfo();
    this.drawGraphs();

    try {
      const mod = await import('./orbital_viewer.js');
      this.viewer = new mod.OrbitalViewer($('#viewer-stage'));
      this.rebuild();
    } catch (err) {
      console.error('3D viewer failed to load', err);
      $('#viewer-fallback').hidden = false;
    }
  },

  fromSliders(changed) {
    let n = +$('#qn-n').value;
    let l = +$('#qn-l').value;
    let m = +$('#qn-m').value;
    if (changed === 'n' && l > n - 1) l = n - 1;
    if (Math.abs(m) > l) m = 0;
    this.set(n, l, m, { fromSlider: true });
  },

  set(n, l, m, { scroll = false } = {}) {
    this.n = n; this.l = l; this.m = m;
    this.syncSliders();
    this.updateInfo();
    this.drawGraphs();
    if (scroll) $('#module-b').scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
    clearTimeout(this.pending);
    this.pending = setTimeout(() => this.rebuild(), 140);
  },

  syncSliders() {
    const { n, l, m } = this;
    const sl = $('#qn-l');
    const sm = $('#qn-m');
    $('#qn-n').value = n;
    sl.max = n - 1; sl.value = l;
    sm.min = -l; sm.max = l; sm.value = m;
    $('#qn-n-val').textContent = n;
    $('#qn-l-val').textContent = l;
    $('#qn-m-val').textContent = signed(m);
    $$('.chip').forEach((c) => c.classList.toggle('active', c.dataset.key === `${n},${l},${m}`));
  },

  rebuild() {
    if (!this.viewer) return;
    const overlay = $('#viewer-overlay');
    overlay.hidden = false;
    // Let the overlay paint before the (synchronous) grid computation
    requestAnimationFrame(() => setTimeout(() => {
      const t0 = performance.now();
      const stats = this.viewer.setOrbital(this.n, this.l, this.m);
      const dt = performance.now() - t0;
      overlay.hidden = true;
      this.stats = stats;
      this.updateClip(+$('#clip').value);
      const nc = this.viewer.nodeCounts;
      $('#viewer-hud').innerHTML =
        `${orbitalNameHTML(this.n, this.l, this.m)} · grid ${stats.gridSize}³ · ${dt.toFixed(0)} ms<br>` +
        `isosurface: |ψ|² encloses 90 % probability<br>` +
        `nodes shown: ${nc.radial} sphere · ${nc.cones} cone/plane(θ) · ${nc.planes} plane(φ)`;
      this.replayCloud();
    }, 16));
  },

  replayCloud() {
    if (!this.viewer) return;
    const out = $('#cloud-progress');
    this.viewer.animateCloud((count, total) => {
      out.textContent = `Simulated position measurements: ${count.toLocaleString()} / ${total.toLocaleString()}`;
    }, reduceMotion ? 10 : 2600);
    $('#opt-cloud').checked = true;
  },

  updateClip(v) {
    this.viewer?.setClip(v);
    const ext = this.viewer?.extent ?? radiusEnclosing(this.n, this.l, 0.995) * 1.1;
    $('#clip-val').textContent = v >= 1 ? 'off' : `${fmt(v * ext, 1)} a₀`;
  },

  updateInfo() {
    const { n, l, m } = this;
    $('#viewer-title').innerHTML = `${orbitalNameHTML(n, l, m)} orbital <small class="muted">(n=${n}, l=${l}, m<sub>l</sub>=${signed(m)})</small>`;
    katexRender($('#orbital-formula'),
      `\\psi_{${n}${l}${m}} = R_{${n}${l}}(r)\\,Y_{${l}}^{${m}}(\\theta,\\phi),\\quad ${angularFormulaTex(l, m)}`);
    const nodes = radialNodes(n, l, 1);
    const cones = coneNodeAngles(l, m);
    const planes = planeNodeAngles(m);
    const coneTxt = cones.length
      ? cones.map((a) => (Math.abs(a - Math.PI / 2) < 1e-6 ? 'xy-plane' : `${fmt((a * 180) / Math.PI, 1)}°`)).join(', ')
      : '—';
    const rows = [
      ['Orbital', orbitalNameHTML(n, l, m)],
      ['Energy E<sub>n</sub>', `${fmt(energyEV(n), 3)} eV`],
      ['Radial nodes (n−l−1)', `${nodes.length}${nodes.length ? ` @ ${nodes.map((r) => fmt(r, 2)).join(', ')} a₀` : ''}`],
      ['Angular nodes (l)', `${l}`],
      ['  · conical θ', coneTxt],
      ['  · planar φ', planes.length ? planes.map((p) => `${fmt((p * 180) / Math.PI, 0)}°`).join(', ') : '—'],
      ['Total nodes (n−1)', `${n - 1}`],
      ['|L| = √(l(l+1)) ħ', `${fmt(Math.sqrt(l * (l + 1)), 3)} ħ`],
      ['L<sub>z</sub> = m<sub>l</sub> ħ', `${signed(m)} ħ`],
      ['Subshell degeneracy', `${2 * l + 1} orbitals`],
      ['Shell degeneracy n²', `${n * n} orbitals (${2 * n * n} e⁻)`],
      ['⟨r⟩', `${fmt((3 * n * n - l * (l + 1)) / 2, 1)} a₀ = ${fmt(((3 * n * n - l * (l + 1)) / 2) * BOHR_RADIUS_ANGSTROM, 2)} Å`],
    ];
    $('#orbital-props').innerHTML = rows.map(([k, v]) => `<dt>${k}</dt><dd>${v}</dd>`).join('');
  },

  drawGraphs() {
    if ($('#graph-row').hidden) return;
    drawRadialGraph($('#radial-canvas'), this.n, this.l);
    const { phi0 } = drawAngularPolar($('#angular-canvas'), this.l, this.m);
    $('#angular-pill').innerHTML = `|Y<sub>${this.l},${this.m}</sub>| in plane φ = ${fmt((phi0 * 180) / Math.PI, 0)}°`;
  },
};

/* ------------------------------------------------------------------ */
/* MODULE C                                                            */
/* ------------------------------------------------------------------ */

const ModuleC = {
  elements: window.ELEMENTS || [],
  cache: new Map(),
  z: 26,
  building: null,

  init() {
    this.buildTable();
    this.buildMadelungSVG();
    const search = $('#element-search');
    search.addEventListener('change', () => this.search(search.value));
    search.addEventListener('keydown', (e) => { if (e.key === 'Enter') this.search(search.value); });
    $('#el-prev').addEventListener('click', () => this.select(Math.max(1, this.z - 1)));
    $('#el-next').addEventListener('click', () => this.select(Math.min(118, this.z + 1)));
    $('#btn-build-z').addEventListener('click', () => this.toggleBuild());
    $('#btn-replay-fill').addEventListener('click', () => this.render(this.cache.get(this.z), { replay: true }));
    this.initTooltip();
    this.select(26);
  },

  buildTable() {
    const grid = $('#ptable');
    const frag = document.createDocumentFragment();
    for (const e of this.elements) {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = `pt-cell blk-bg-${e.block}${e.is_exception ? ' exc' : ''}`;
      b.style.gridRow = e.row;
      b.style.gridColumn = e.col;
      b.dataset.z = e.z;
      b.title = `${e.name} (Z = ${e.z})${e.is_exception ? ' — Aufbau exception' : ''}`;
      b.innerHTML = `<span class="pt-z">${e.z}</span><span class="pt-sym">${e.symbol}</span><span class="pt-name">${e.name}</span>`;
      b.addEventListener('click', () => { this.stopBuild(); this.select(e.z); });
      frag.appendChild(b);
    }
    for (const [row, label] of [[6, '57–71'], [7, '89–103']]) {
      const p = document.createElement('div');
      p.className = 'pt-placeholder';
      p.style.gridRow = row;
      p.style.gridColumn = 3;
      p.textContent = label;
      frag.appendChild(p);
    }
    grid.appendChild(frag);
  },

  search(raw) {
    const q = raw.trim();
    if (!q) return;
    let z = null;
    const paren = q.match(/\((\d+)\)\s*$/);
    if (paren) z = +paren[1];
    else if (/^\d+$/.test(q)) z = +q;
    else {
      const lc = q.toLowerCase();
      const hit = this.elements.find((e) => e.symbol.toLowerCase() === lc)
        || this.elements.find((e) => e.name.toLowerCase() === lc)
        || this.elements.find((e) => e.name.toLowerCase().startsWith(lc));
      if (hit) z = hit.z;
    }
    if (z && z >= 1 && z <= 118) { this.stopBuild(); this.select(z); }
  },

  async fetchElement(z) {
    if (this.cache.has(z)) return this.cache.get(z);
    const res = await fetch(`/api/element/${z}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    this.cache.set(z, data);
    return data;
  },

  async select(z, opts = {}) {
    const prevZ = this.z;
    this.z = z;
    $$('.pt-cell').forEach((c) => c.classList.toggle('selected', +c.dataset.z === z));
    try {
      const data = await this.fetchElement(z);
      if (this.z !== z) return;
      this.render(data, { ...opts, prevZ });
    } catch (err) {
      $('#element-head').textContent = `Could not load element ${z}: ${err.message}`;
    }
  },

  render(d, { replay = false, incremental = false, prevZ = 0 } = {}) {
    if (!d) return;
    const color = BLOCK_COLORS[d.block];
    $('#element-head').innerHTML = `
      <div class="el-tile" style="background: color-mix(in srgb, ${color} 30%, #121212)">
        <span class="t-z">${d.z}</span><span class="t-sym">${d.symbol}</span>
      </div>
      <div class="el-meta">
        <h3>${d.name}</h3>
        <p>Z = ${d.z} · Period ${d.period} · ${d.group ? `Group ${d.group}` : (d.period === 6 ? 'Lanthanide' : 'Actinide')} · <span style="color:${color}">${d.block}-block</span></p>
        ${d.exception ? '<span class="badge" style="color:#fda4af;border-color:rgba(244,63,94,.5)">Aufbau exception</span>' : ''}
        ${d.predicted ? '<span class="badge badge-pred">Predicted (superheavy — not yet measured)</span>' : ''}
      </div>`;

    const spanify = (list) => list.map((s) => {
      const sup = String(s.count).replace(/\d/g, (c) => '⁰¹²³⁴⁵⁶⁷⁸⁹'[c]);
      return `<span class="ss ss-${L_LETTERS[s.l]}">${s.label}${sup}</span>`;
    }).join('');
    $('#config-full').innerHTML = spanify(d.configuration.subshells);
    $('#config-condensed').innerHTML = (d.configuration.core ? `<span class="core">[${d.configuration.core}]</span>` : '') + spanify(d.configuration.valence_subshells);

    const banner = $('#exception-banner');
    if (d.exception) {
      banner.hidden = false;
      banner.innerHTML = `
        <h4>⚠ Stability exception — ${d.exception.type}</h4>
        <div class="exc-compare">
          <span>Aufbau predicts</span><span class="strike">${d.exception.aufbau_prediction}</span>
          <span>Measured</span><span class="ok">${d.exception.observed}</span>
        </div>
        <p style="margin:0">${d.exception.reason}</p>
        <p style="margin:.35rem 0 0;font-size:.76rem;color:var(--text-muted)">
          Thermodynamic origin: the ground state is whichever arrangement minimises the <em>total</em> energy.
          When two subshells are nearly degenerate, gains in exchange energy (parallel spins) and reduced
          pairing repulsion can outweigh the small orbital-energy cost of promoting an electron.
          ${d.exception.source === 'additional' ? 'Source: NIST Atomic Spectra Database (additional measured exception).' : ''}
        </p>`;
    } else {
      banner.hidden = true;
      banner.innerHTML = '';
    }

    const st = d.stats;
    const stat = (title, value, sub = '') => `<div class="stat-box"><span class="stat-title">${title}</span><span class="stat-value">${value}</span>${sub ? `<span class="stat-sub">${sub}</span>` : ''}</div>`;
    $('#element-stats').innerHTML = [
      stat('Electrons', st.total_electrons),
      stat('Unpaired e⁻', st.unpaired_electrons, st.unpaired_electrons ? 'paramagnetic' : 'diamagnetic'),
      stat('Multiplicity 2S+1', st.spin_multiplicity, `S = ${st.unpaired_electrons}/2`),
      stat('Outer shell', `n = ${st.outer_shell_n}`, `${st.outer_shell_electrons} e⁻`),
      stat('Subshells', st.occupied_subshells, 'occupied'),
      stat('s / p / d / f', `${st.electrons_by_l.s}/${st.electrons_by_l.p}/${st.electrons_by_l.d}/${st.electrons_by_l.f}`, 'electrons'),
    ].join('');

    $('#shell-bars').innerHTML = st.electrons_per_shell.map((s) => {
      const cap = 2 * s.n * s.n;
      return `<div class="shell-bar"><span>n=${s.n} (${'KLMNOPQ'[s.n - 1]})</span><div class="shell-track"><div class="shell-fill" style="inline-size:${(100 * s.count) / cap}%"></div></div><span>${s.count}/${cap}</span></div>`;
    }).join('');

    this.renderBoxes(d, { replay, incremental, prevZ });
    this.updateMadelung(d);
  },

  renderBoxes(d, { incremental = false, prevZ = 0 } = {}) {
    const total = d.electrons.length;
    const stepMs = reduceMotion ? 0 : Math.max(18, Math.min(110, 2600 / total));
    const container = $('#box-diagram');
    container.innerHTML = d.boxes.map((b) => {
      const boxes = b.orbitals.map((o) => {
        const arrows = o.electrons.map((e) => {
          const instant = incremental && e.order <= prevZ;
          const delay = instant ? 0 : incremental ? 0 : e.order * stepMs;
          const style = instant ? 'animation:none' : `--d:${delay}`;
          return `<span class="arrow ${e.ms > 0 ? 'up' : 'down'}" style="${style}" data-n="${e.n}" data-l="${e.l}" data-ml="${e.ml}" data-ms="${e.ms}" data-order="${e.order}">${e.ms > 0 ? '↑' : '↓'}</span>`;
        }).join('');
        return `<button type="button" class="orb-box" data-n="${b.n}" data-l="${b.l}" data-ml="${o.ml}" aria-label="${b.label} orbital m_l=${o.ml}">${arrows}<span class="ml">${signed(o.ml)}</span></button>`;
      }).join('');
      return `<div class="ss-row${b.count ? '' : ' empty'}" data-l="${b.l}">
        <span class="ss-label">${b.label}<small>n+l=${b.n_plus_l}</small></span>
        <div class="ss-boxes">${boxes}</div>
        <span class="ss-count">${b.count}/${b.capacity}</span>
      </div>`;
    }).join('');
    container.querySelectorAll('.orb-box').forEach((btn) => {
      btn.addEventListener('click', () => {
        ModuleB.set(+btn.dataset.n, +btn.dataset.l, +btn.dataset.ml, { scroll: true });
      });
    });
  },

  initTooltip() {
    const tip = $('#e-tooltip');
    const container = $('#box-diagram');
    container.addEventListener('mouseover', (e) => {
      const a = e.target.closest('.arrow');
      const box = e.target.closest('.orb-box');
      if (a) {
        const n = +a.dataset.n; const l = +a.dataset.l; const ml = +a.dataset.ml; const ms = +a.dataset.ms;
        tip.innerHTML = `<b>Electron #${a.dataset.order}</b> · ${n}${L_LETTERS[l]}<br>n = ${n}, l = ${l}, m<sub>l</sub> = ${signed(ml)}, m<sub>s</sub> = ${msLabel(ms)}<br><span style="color:var(--text-muted)">Click to view ${orbitalNameHTML(n, l, ml)} in 3D</span>`;
        tip.hidden = false;
      } else if (box) {
        const n = +box.dataset.n; const l = +box.dataset.l; const ml = +box.dataset.ml;
        tip.innerHTML = `<b>${n}${L_LETTERS[l]}</b> orbital, m<sub>l</sub> = ${signed(ml)} (empty slot)<br><span style="color:var(--text-muted)">Click to view ${orbitalNameHTML(n, l, ml)} in 3D</span>`;
        tip.hidden = false;
      }
    });
    container.addEventListener('mousemove', (e) => {
      if (tip.hidden) return;
      const x = Math.min(window.innerWidth - tip.offsetWidth - 8, e.clientX + 14);
      const y = Math.min(window.innerHeight - tip.offsetHeight - 8, e.clientY + 14);
      tip.style.left = `${x}px`;
      tip.style.top = `${y}px`;
    });
    container.addEventListener('mouseout', (e) => {
      if (!e.relatedTarget || !container.contains(e.relatedTarget) || !e.relatedTarget.closest('.orb-box')) tip.hidden = true;
    });
  },

  buildMadelungSVG() {
    const svg = $('#madelung-svg');
    const NS = 'http://www.w3.org/2000/svg';
    const pos = (n, l) => [56 + l * 62, 34 + (n - 1) * 42];
    const order = window.MADELUNG || [];
    const has = new Set(order.map((s) => `${s.n},${s.l}`));
    let html = '<defs><marker id="m-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="rgba(56,189,248,0.7)"/></marker></defs>';
    ['s', 'p', 'd', 'f'].forEach((L, l) => { html += `<text class="m-head" x="${56 + l * 62}" y="12">l=${l} (${L})</text>`; });
    for (let k = 1; k <= 8; k++) {
      const cells = order.filter((s) => s.n + s.l === k).sort((a, b) => a.n - b.n);
      if (!cells.length) continue;
      const [x1, y1] = pos(cells[0].n, cells[0].l);
      const [x2, y2] = pos(cells[cells.length - 1].n, cells[cells.length - 1].l);
      html += `<line class="m-diag" x1="${x1 + 22}" y1="${y1 - 15}" x2="${x2 - 20}" y2="${y2 + 14}"/>`;
    }
    for (let n = 1; n <= 7; n++) {
      for (let l = 0; l < Math.min(n, 4); l++) {
        if (!has.has(`${n},${l}`)) continue;
        const [x, y] = pos(n, l);
        html += `<rect class="m-cell" data-key="${n},${l}" x="${x - 19}" y="${y - 13}" width="38" height="26" rx="5"/>`;
        html += `<text class="m-text" data-key="${n},${l}" x="${x}" y="${y + 1}">${n}${L_LETTERS[l]}</text>`;
      }
    }
    svg.innerHTML = html;
  },

  updateMadelung(d) {
    const occupied = new Set(d.boxes.filter((b) => b.count > 0).map((b) => `${b.n},${b.l}`));
    $$('#madelung-svg [data-key]').forEach((el) => el.classList.toggle('on', occupied.has(el.dataset.key)));
    $$('#madelung-svg rect[data-key]').forEach((el) => {
      const key = el.dataset.key;
      const box = d.boxes.find((b) => `${b.n},${b.l}` === key);
      if (box && box.count > 0) {
        const frac = box.count / box.capacity;
        const col = BLOCK_COLORS[L_LETTERS[box.l]];
        el.style.fill = `color-mix(in srgb, ${col} ${Math.round(15 + frac * 45)}%, #121212)`;
      } else {
        el.style.fill = '';
      }
    });
  },

  toggleBuild() {
    if (this.building) { this.stopBuild(); return; }
    const target = this.z > 1 ? this.z : 118;
    const interval = reduceMotion ? 60 : Math.max(140, Math.min(450, 14000 / target));
    let z = 1;
    this.z = 0; // start from an empty atom so only the newly added electron animates
    $('#btn-build-z').textContent = '⏹ Stop build-up';
    const tick = async () => {
      if (!this.building) return;
      await this.select(z, { incremental: true });
      if (z >= target) { this.stopBuild(); return; }
      z += 1;
      this.building = setTimeout(tick, interval);
    };
    this.building = setTimeout(tick, 0);
  },

  stopBuild() {
    if (this.building) clearTimeout(this.building);
    this.building = null;
    $('#btn-build-z').textContent = '▶ Build up from H';
  },
};

/* ------------------------------------------------------------------ */
/* Boot                                                                */
/* ------------------------------------------------------------------ */

async function boot() {
  const katexReady = await waitForKatex();
  if (katexReady) {
    window.renderMathInElement(document.body, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\(', right: '\\)', display: false },
      ],
      throwOnError: false,
      ignoredClasses: ['ptable', 'box-diagram'],
    });
  }
  ModuleA.init();
  ModuleC.init();
  await ModuleB.init();
}

boot();

export { ModuleA, ModuleB, ModuleC, drawRadialGraph, drawAngularPolar, orbitalNameTex };
