/**
 * quantum_math.js — Analytic hydrogen-like wavefunctions.
 *
 *   ψ_nlm(r, θ, φ) = R_nl(r) · Y_lm(θ, φ)        (real spherical harmonics)
 *
 *   R_nl(r) = N · e^{-ρ/2} · ρ^l · L^{2l+1}_{n-l-1}(ρ),   ρ = 2Zr / (n a₀)
 *   N       = sqrt( (2Z/(n a₀))³ · (n-l-1)! / (2n · (n+l)!) )
 *
 * Distances are in units of the Bohr radius a₀ = 0.529 Å.
 */

export const BOHR_RADIUS_ANGSTROM = 0.529177;
export const RYDBERG_EV = 13.6057;
export const L_LETTERS = 'spdfghi';

const FACT = [1];
for (let i = 1; i <= 30; i++) FACT[i] = FACT[i - 1] * i;
export const factorial = (k) => FACT[k];

/** Generalised (associated) Laguerre polynomial L_k^α(x) via three-term recurrence. */
export function laguerre(k, alpha, x) {
  if (k === 0) return 1;
  let Lm1 = 1;
  let L = 1 + alpha - x;
  for (let i = 1; i < k; i++) {
    const Lp1 = ((2 * i + 1 + alpha - x) * L - (i + alpha) * Lm1) / (i + 1);
    Lm1 = L;
    L = Lp1;
  }
  return L;
}

/** Associated Legendre P_l^m(x), m ≥ 0, WITHOUT the Condon–Shortley phase. */
export function assocLegendre(l, m, x) {
  let pmm = 1;
  if (m > 0) {
    const s = Math.sqrt(Math.max(0, 1 - x * x));
    let fact = 1;
    for (let i = 1; i <= m; i++) {
      pmm *= fact * s;
      fact += 2;
    }
  }
  if (l === m) return pmm;
  let pmmp1 = x * (2 * m + 1) * pmm;
  if (l === m + 1) return pmmp1;
  let pll = 0;
  for (let ll = m + 2; ll <= l; ll++) {
    pll = ((2 * ll - 1) * x * pmmp1 - (ll + m - 1) * pmm) / (ll - m);
    pmm = pmmp1;
    pmmp1 = pll;
  }
  return pll;
}

export function radialNorm(n, l, Z = 1) {
  return Math.sqrt(Math.pow((2 * Z) / n, 3) * factorial(n - l - 1) / (2 * n * factorial(n + l)));
}

/** Returns a fast closure r ↦ R_nl(r). */
export function makeRadial(n, l, Z = 1) {
  const N = radialNorm(n, l, Z);
  const k = n - l - 1;
  const alpha = 2 * l + 1;
  return (r) => {
    const rho = (2 * Z * r) / n;
    return N * Math.exp(-rho / 2) * Math.pow(rho, l) * laguerre(k, alpha, rho);
  };
}

export function angularNorm(l, m) {
  const am = Math.abs(m);
  const base = Math.sqrt(((2 * l + 1) / (4 * Math.PI)) * factorial(l - am) / factorial(l + am));
  return m === 0 ? base : base * Math.SQRT2;
}

/** Returns closure (cosθ, φ) ↦ real Y_lm. m>0 → cos(mφ), m<0 → sin(|m|φ). */
export function makeAngular(l, m) {
  const N = angularNorm(l, m);
  const am = Math.abs(m);
  return (cosT, phi) => {
    const P = assocLegendre(l, am, cosT);
    if (m === 0) return N * P;
    return m > 0 ? N * P * Math.cos(am * phi) : N * P * Math.sin(am * phi);
  };
}

/** Closure for ψ at Cartesian point (x, y, z) in a₀ (physics axes). */
export function makePsi(n, l, m, Z = 1) {
  const R = makeRadial(n, l, Z);
  const Y = makeAngular(l, m);
  return (x, y, z) => {
    const r = Math.sqrt(x * x + y * y + z * z);
    if (r < 1e-9) return R(0) * Y(1, 0);
    return R(r) * Y(z / r, Math.atan2(y, x));
  };
}

export function energyEV(n, Z = 1) {
  return (-RYDBERG_EV * Z * Z) / (n * n);
}

/** Radial node positions (in a₀) — zeros of the Laguerre polynomial. */
export function radialNodes(n, l, Z = 1) {
  const k = n - l - 1;
  if (k <= 0) return [];
  const alpha = 2 * l + 1;
  const roots = [];
  const rhoMax = 4 * n + 4 * n * n + 20;
  const steps = 6000;
  let prevX = 1e-6;
  let prevV = laguerre(k, alpha, prevX);
  for (let i = 1; i <= steps && roots.length < k; i++) {
    const x = (rhoMax * i) / steps;
    const v = laguerre(k, alpha, x);
    if (prevV === 0 || prevV * v < 0) {
      let a = prevX;
      let b = x;
      let fa = prevV;
      for (let it = 0; it < 60; it++) {
        const mid = 0.5 * (a + b);
        const fm = laguerre(k, alpha, mid);
        if (fa * fm <= 0) b = mid;
        else { a = mid; fa = fm; }
      }
      roots.push((0.5 * (a + b) * n) / (2 * Z));
    }
    prevX = x;
    prevV = v;
  }
  return roots;
}

/** Polar angles θ (radians) of conical angular nodes: zeros of P_l^|m|(cosθ) in (-1, 1). */
export function coneNodeAngles(l, m) {
  const am = Math.abs(m);
  const count = l - am;
  if (count <= 0) return [];
  const roots = [];
  const steps = 3997; // odd so no sample lands exactly on the symmetric root x = 0
  let prevX = -1 + 1e-7;
  let prevV = assocLegendre(l, am, prevX);
  for (let i = 1; i <= steps; i++) {
    const x = -1 + 1e-7 + ((2 - 2e-7) * i) / steps;
    const v = assocLegendre(l, am, x);
    if (prevV * v < 0) {
      let a = prevX;
      let b = x;
      let fa = prevV;
      for (let it = 0; it < 60; it++) {
        const mid = 0.5 * (a + b);
        const fm = assocLegendre(l, am, mid);
        if (fa * fm <= 0) b = mid;
        else { a = mid; fa = fm; }
      }
      roots.push(Math.acos(0.5 * (a + b)));
    }
    prevX = x;
    prevV = v;
  }
  return roots;
}

/** Azimuthal angles φ of vertical nodal planes (each plane contains the z-axis). */
export function planeNodeAngles(m) {
  const am = Math.abs(m);
  const out = [];
  for (let k = 0; k < am; k++) {
    out.push(m > 0 ? (Math.PI / 2 + k * Math.PI) / am : (k * Math.PI) / am);
  }
  return out;
}

/** Radius enclosing a given fraction of radial probability ∫ r²R² dr. */
export function radiusEnclosing(n, l, fraction = 0.999, Z = 1) {
  const R = makeRadial(n, l, Z);
  const rMax = (n * (4 * n + 10)) / Z;
  const steps = 8000;
  const dr = rMax / steps;
  let total = 0;
  const cum = new Float64Array(steps + 1);
  for (let i = 1; i <= steps; i++) {
    const r = i * dr;
    const v = R(r);
    total += r * r * v * v * dr;
    cum[i] = total;
  }
  const target = fraction * total;
  for (let i = 1; i <= steps; i++) if (cum[i] >= target) return i * dr;
  return rMax;
}

const ORBITAL_NAMES = {
  0: { 0: 's' },
  1: { 0: 'p_z', 1: 'p_x', [-1]: 'p_y' },
  2: { 0: 'd_{z^2}', 1: 'd_{xz}', [-1]: 'd_{yz}', 2: 'd_{x^2-y^2}', [-2]: 'd_{xy}' },
  3: {
    0: 'f_{z^3}', 1: 'f_{xz^2}', [-1]: 'f_{yz^2}', 2: 'f_{z(x^2-y^2)}', [-2]: 'f_{xyz}',
    3: 'f_{x(x^2-3y^2)}', [-3]: 'f_{y(3x^2-y^2)}',
  },
};

/** LaTeX-ish orbital name, e.g. "3d_{xy}". */
export function orbitalNameTex(n, l, m) {
  const base = ORBITAL_NAMES[l]?.[m];
  if (base) return `${n}${base}`;
  return `${n}${L_LETTERS[l]}_{m=${m}}`;
}

/** Plain-text / HTML orbital name, e.g. "3d<sub>xy</sub>". */
export function orbitalNameHTML(n, l, m) {
  const base = ORBITAL_NAMES[l]?.[m];
  if (!base) return `${n}${L_LETTERS[l]}<sub>m=${m}</sub>`;
  const [letter, sub] = base.split('_');
  if (!sub) return `${n}${letter}`;
  const cleaned = sub.replace(/[{}]/g, '').replace(/\^2/g, '²').replace(/\^3/g, '³');
  return `${n}${letter}<sub>${cleaned}</sub>`;
}

const ANGULAR_TEX = {
  '0,0': 'Y_{00} = \\frac{1}{\\sqrt{4\\pi}}',
  '1,0': 'p_z \\propto \\cos\\theta \\;(\\propto z)',
  '1,1': 'p_x \\propto \\sin\\theta\\cos\\phi \\;(\\propto x)',
  '1,-1': 'p_y \\propto \\sin\\theta\\sin\\phi \\;(\\propto y)',
  '2,0': 'd_{z^2} \\propto 3\\cos^2\\theta - 1',
  '2,1': 'd_{xz} \\propto \\sin\\theta\\cos\\theta\\cos\\phi',
  '2,-1': 'd_{yz} \\propto \\sin\\theta\\cos\\theta\\sin\\phi',
  '2,2': 'd_{x^2-y^2} \\propto \\sin^2\\theta\\cos 2\\phi',
  '2,-2': 'd_{xy} \\propto \\sin^2\\theta\\sin 2\\phi',
  '3,0': 'f_{z^3} \\propto 5\\cos^3\\theta - 3\\cos\\theta',
  '3,1': 'f_{xz^2} \\propto \\sin\\theta(5\\cos^2\\theta-1)\\cos\\phi',
  '3,-1': 'f_{yz^2} \\propto \\sin\\theta(5\\cos^2\\theta-1)\\sin\\phi',
  '3,2': 'f_{z(x^2-y^2)} \\propto \\sin^2\\theta\\cos\\theta\\cos 2\\phi',
  '3,-2': 'f_{xyz} \\propto \\sin^2\\theta\\cos\\theta\\sin 2\\phi',
  '3,3': 'f_{x(x^2-3y^2)} \\propto \\sin^3\\theta\\cos 3\\phi',
  '3,-3': 'f_{y(3x^2-y^2)} \\propto \\sin^3\\theta\\sin 3\\phi',
};

export function angularFormulaTex(l, m) {
  const key = `${l},${m}`;
  if (ANGULAR_TEX[key]) return ANGULAR_TEX[key];
  const trig = m === 0 ? '' : m > 0 ? `\\cos(${m}\\phi)` : `\\sin(${Math.abs(m)}\\phi)`;
  return `Y \\propto P_{${l}}^{${Math.abs(m)}}(\\cos\\theta)\\,${trig}`;
}

/** Summary of quantum numbers and derived quantities for display. */
export function orbitalInfo(n, l, m, Z = 1) {
  return {
    n, l, m,
    subshell: `${n}${L_LETTERS[l]}`,
    energy: energyEV(n, Z),
    radialNodes: n - l - 1,
    angularNodes: l,
    totalNodes: n - 1,
    L: Math.sqrt(l * (l + 1)),
    Lz: m,
    degeneracy: 2 * l + 1,
    radialNodePositions: radialNodes(n, l, Z),
    coneAngles: coneNodeAngles(l, m),
    planeAngles: planeNodeAngles(m),
  };
}
