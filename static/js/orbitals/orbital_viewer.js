/**
 * orbital_viewer.js — Module B: interactive 3D hydrogen-like orbital viewer.
 *
 * Renders, for chosen (n, l, m_l):
 *   • 90 % probability boundary isosurfaces (Marching Cubes on |ψ|²), split by phase
 *   • Monte-Carlo dot-density cloud sampled from |ψ|²
 *   • analytic nodal surfaces (radial spheres, conical and planar angular nodes)
 *   • a movable clipping plane to reveal internal radial nodes
 *
 * Axis mapping (physics → three.js):  x → x,  z → y (up),  y → −z
 */

import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { MarchingCubes } from 'three/addons/objects/MarchingCubes.js';
import {
  makePsi, radiusEnclosing, radialNodes, coneNodeAngles, planeNodeAngles,
} from './quantum_math.js';

const COLOR_POS = new THREE.Color(0xf59e0b); // + phase  (orange)
const COLOR_NEG = new THREE.Color(0x3b82f6); // − phase  (blue)
const COLOR_MONO = new THREE.Color(0x7dd3fc); // phase colours disabled
const CLOUD_POINTS = 32000;

function makeDotTexture() {
  const c = document.createElement('canvas');
  c.width = c.height = 64;
  const g = c.getContext('2d');
  const grad = g.createRadialGradient(32, 32, 0, 32, 32, 32);
  grad.addColorStop(0, 'rgba(255,255,255,1)');
  grad.addColorStop(0.45, 'rgba(255,255,255,0.85)');
  grad.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = grad;
  g.fillRect(0, 0, 64, 64);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  return tex;
}

function makeLabelSprite(text, color) {
  const c = document.createElement('canvas');
  c.width = c.height = 128;
  const g = c.getContext('2d');
  g.font = 'bold 72px Inter, Arial, sans-serif';
  g.textAlign = 'center';
  g.textBaseline = 'middle';
  g.fillStyle = color;
  g.fillText(text, 64, 68);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  const mat = new THREE.SpriteMaterial({ map: tex, depthTest: false, transparent: true });
  return new THREE.Sprite(mat);
}

function disposeGroup(group) {
  for (let i = group.children.length - 1; i >= 0; i--) {
    const obj = group.children[i];
    group.remove(obj);
    obj.traverse?.((o) => {
      o.geometry?.dispose?.();
      if (o.material) {
        (Array.isArray(o.material) ? o.material : [o.material]).forEach((m) => {
          m.map?.dispose?.();
          m.dispose?.();
        });
      }
    });
  }
}

export class OrbitalViewer {
  constructor(container) {
    this.container = container;
    this.options = {
      surface: true,
      cloud: true,
      phase: true,
      nodes: true,
      axes: true,
      autoRotate: true,
    };
    this.surfaceOpacity = 0.78;
    this.extent = 5;
    this.clipFraction = 1.05;
    this.visible = true;

    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.localClippingEnabled = true;
    this.renderer.setClearColor(0x141414, 1);
    container.appendChild(this.renderer.domElement);

    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(45, 1, 0.01, 10000);
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.08;
    this.controls.enablePan = true;
    this.controls.autoRotate = true;
    this.controls.autoRotateSpeed = 1.2;

    this.scene.add(new THREE.AmbientLight(0xffffff, 0.55));
    const key = new THREE.DirectionalLight(0xffffff, 1.6);
    key.position.set(3, 5, 4);
    this.scene.add(key);
    const rim = new THREE.DirectionalLight(0x93c5fd, 0.7);
    rim.position.set(-4, -2, -3);
    this.scene.add(rim);
    this.camera.add(new THREE.PointLight(0xffffff, 0.6, 0, 0));
    this.scene.add(this.camera);

    this.clipPlane = new THREE.Plane(new THREE.Vector3(-1, 0, 0), 1e6);

    this.surfaceGroup = new THREE.Group();
    this.cloudGroup = new THREE.Group();
    this.nodeGroup = new THREE.Group();
    this.axesGroup = new THREE.Group();
    this.scene.add(this.surfaceGroup, this.cloudGroup, this.nodeGroup, this.axesGroup);

    this.posMaterial = new THREE.MeshStandardMaterial({
      color: COLOR_POS, roughness: 0.32, metalness: 0.05, transparent: true,
      opacity: this.surfaceOpacity, side: THREE.DoubleSide, clippingPlanes: [this.clipPlane],
    });
    this.negMaterial = this.posMaterial.clone();
    this.negMaterial.color = COLOR_NEG.clone();
    this.negMaterial.clippingPlanes = [this.clipPlane];

    this.dotTexture = makeDotTexture();
    this.mcPos = null;
    this.mcNeg = null;
    this.mcSize = 0;

    this.nucleus = new THREE.Mesh(
      new THREE.SphereGeometry(1, 20, 16),
      new THREE.MeshBasicMaterial({ color: 0xfde68a }),
    );
    this.scene.add(this.nucleus);

    this.cloudAnim = null;
    this._resize = this._resize.bind(this);
    this._loop = this._loop.bind(this);
    this.resizeObserver = new ResizeObserver(this._resize);
    this.resizeObserver.observe(container);
    this.intersection = new IntersectionObserver((entries) => {
      this.visible = entries.some((e) => e.isIntersecting);
    });
    this.intersection.observe(container);
    this._resize();
    requestAnimationFrame(this._loop);
  }

  _resize() {
    const w = Math.max(1, this.container.clientWidth);
    const h = Math.max(1, this.container.clientHeight);
    this.renderer.setSize(w, h, false);
    this.camera.aspect = w / h;
    this.camera.updateProjectionMatrix();
  }

  _loop(time) {
    requestAnimationFrame(this._loop);
    if (!this.visible) return;
    if (this.cloudAnim && this.cloudPoints) {
      const t = Math.min(1, (time - (this.cloudAnim.start ?? (this.cloudAnim.start = time))) / this.cloudAnim.duration);
      const count = Math.floor(t * t * CLOUD_POINTS);
      this.cloudPoints.geometry.setDrawRange(0, count);
      this.cloudAnim.onProgress?.(count, CLOUD_POINTS);
      if (t >= 1) this.cloudAnim = null;
    }
    this.controls.autoRotate = this.options.autoRotate;
    this.controls.update();
    this.renderer.render(this.scene, this.camera);
  }

  /** Recompute everything for a new orbital. Returns stats for the UI. */
  setOrbital(n, l, m) {
    this.n = n; this.l = l; this.m = m;
    const psi = makePsi(n, l, m, 1);
    const extent = radiusEnclosing(n, l, 0.995, 1) * 1.1;
    this.extent = extent;
    const size = n <= 2 ? 56 : n <= 4 ? 68 : 84;
    const half = size / 2;
    const size2 = size * size;
    const total = size2 * size;
    const psiGrid = new Float32Array(total);
    const dens = new Float32Array(total);
    let maxD = 0;
    let sumD = 0;
    for (let k = 0; k < size; k++) {
      const tz = ((k - half) / half) * extent; // three z = −physics y
      for (let j = 0; j < size; j++) {
        const ty = ((j - half) / half) * extent; // three y = physics z
        for (let i = 0; i < size; i++) {
          const tx = ((i - half) / half) * extent; // three x = physics x
          const v = psi(tx, -tz, ty);
          const idx = i + j * size + k * size2;
          const d = v * v;
          psiGrid[idx] = v;
          dens[idx] = d;
          sumD += d;
          if (d > maxD) maxD = d;
        }
      }
    }

    // Density threshold enclosing 90 % of total probability
    const sorted = dens.slice().sort();
    let acc = 0;
    let threshold = sorted[sorted.length - 1];
    for (let i = sorted.length - 1; i >= 0; i--) {
      acc += sorted[i];
      if (acc >= 0.9 * sumD) { threshold = sorted[i]; break; }
    }

    this._buildSurfaces(size, psiGrid, dens, maxD, threshold, extent);
    this._buildCloud(size, dens, sumD, psi, extent);
    this._buildNodes(n, l, m, extent);
    this._buildAxes(extent);
    this.nucleus.scale.setScalar(Math.max(0.05, extent * 0.012));
    this.setClip(this.clipFraction);
    this.applyOptions();
    this.resetCamera();
    return { extent, threshold, gridSize: size };
  }

  _buildSurfaces(size, psiGrid, dens, maxD, threshold, extent) {
    if (this.mcSize !== size) {
      if (this.mcPos) {
        this.surfaceGroup.remove(this.mcPos, this.mcNeg);
        this.mcPos.geometry.dispose();
        this.mcNeg.geometry.dispose();
      }
      // maxPolyCount is a TRIANGLE budget (buffers hold 9 floats per triangle)
      const maxPoly = size >= 80 ? 160000 : size >= 64 ? 120000 : 80000;
      this.mcPos = new MarchingCubes(size, this.posMaterial, false, false, maxPoly);
      this.mcNeg = new MarchingCubes(size, this.negMaterial, false, false, maxPoly);
      this.mcPos.frustumCulled = false;
      this.mcNeg.frustumCulled = false;
      this.surfaceGroup.add(this.mcPos, this.mcNeg);
      this.mcSize = size;
    }
    // reset() zeroes the field AND the cached normals (MarchingCubes only recomputes
    // a normal when its cache entry is 0, so stale normals would survive otherwise)
    this.mcPos.reset();
    this.mcNeg.reset();
    const inv = 1 / maxD;
    const fp = this.mcPos.field;
    const fn = this.mcNeg.field;
    for (let i = 0; i < dens.length; i++) {
      const d = dens[i] * inv;
      if (psiGrid[i] >= 0) { fp[i] = d; fn[i] = 0; } else { fp[i] = 0; fn[i] = d; }
    }
    const iso = threshold * inv;
    this.mcPos.isolation = iso;
    this.mcNeg.isolation = iso;
    this.mcPos.update();
    this.mcNeg.update();
    this.mcPos.scale.setScalar(extent);
    this.mcNeg.scale.setScalar(extent);
  }

  _buildCloud(size, dens, sumD, psi, extent) {
    disposeGroup(this.cloudGroup);
    const cdf = new Float64Array(dens.length);
    let acc = 0;
    for (let i = 0; i < dens.length; i++) { acc += dens[i]; cdf[i] = acc; }
    const positions = new Float32Array(CLOUD_POINTS * 3);
    const signs = new Int8Array(CLOUD_POINTS);
    const half = size / 2;
    const cell = extent / half;
    const size2 = size * size;
    for (let p = 0; p < CLOUD_POINTS; p++) {
      const u = Math.random() * sumD;
      let lo = 0;
      let hi = cdf.length - 1;
      while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (cdf[mid] < u) lo = mid + 1; else hi = mid;
      }
      const k = Math.floor(lo / size2);
      const j = Math.floor((lo - k * size2) / size);
      const i = lo - k * size2 - j * size;
      const tx = ((i - half) / half) * extent + (Math.random() - 0.5) * cell;
      const ty = ((j - half) / half) * extent + (Math.random() - 0.5) * cell;
      const tz = ((k - half) / half) * extent + (Math.random() - 0.5) * cell;
      positions[3 * p] = tx;
      positions[3 * p + 1] = ty;
      positions[3 * p + 2] = tz;
      signs[p] = psi(tx, -tz, ty) >= 0 ? 1 : -1;
    }
    const geom = new THREE.BufferGeometry();
    geom.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geom.setAttribute('color', new THREE.BufferAttribute(new Float32Array(CLOUD_POINTS * 3), 3));
    geom.computeBoundingSphere();
    const mat = new THREE.PointsMaterial({
      size: extent * 0.011, sizeAttenuation: true, vertexColors: true, map: this.dotTexture,
      transparent: true, opacity: 0.8, depthWrite: false, alphaTest: 0.05,
      clippingPlanes: [this.clipPlane],
    });
    this.cloudSigns = signs;
    this.cloudPoints = new THREE.Points(geom, mat);
    this.cloudGroup.add(this.cloudPoints);
    this._colorCloud();
  }

  _colorCloud() {
    if (!this.cloudPoints) return;
    const col = this.cloudPoints.geometry.getAttribute('color');
    for (let p = 0; p < CLOUD_POINTS; p++) {
      const c = this.options.phase ? (this.cloudSigns[p] > 0 ? COLOR_POS : COLOR_NEG) : COLOR_MONO;
      col.setXYZ(p, c.r, c.g, c.b);
    }
    col.needsUpdate = true;
  }

  _buildNodes(n, l, m, extent) {
    disposeGroup(this.nodeGroup);
    const mat = () => new THREE.MeshBasicMaterial({
      color: 0xffffff, transparent: true, opacity: 0.17, side: THREE.DoubleSide,
      depthWrite: false, clippingPlanes: [this.clipPlane],
    });
    const lineMat = () => new THREE.LineBasicMaterial({
      color: 0xffffff, transparent: true, opacity: 0.45, clippingPlanes: [this.clipPlane],
    });
    const R = extent * 0.92;
    this.nodeCounts = { radial: 0, cones: 0, planes: 0 };

    // Radial nodes: spheres where R_nl(r) = 0
    for (const r of radialNodes(n, l, 1)) {
      const s = new THREE.Mesh(new THREE.SphereGeometry(r, 48, 32), mat());
      s.userData.kind = 'radial';
      this.nodeGroup.add(s);
      const ring = new THREE.LineLoop(
        new THREE.BufferGeometry().setFromPoints(
          Array.from({ length: 96 }, (_, i) => new THREE.Vector3(r * Math.cos((i / 96) * 2 * Math.PI), 0, r * Math.sin((i / 96) * 2 * Math.PI))),
        ),
        lineMat(),
      );
      this.nodeGroup.add(ring);
      this.nodeCounts.radial++;
    }

    // Conical (or equatorial planar) angular nodes: P_l^|m|(cos θ) = 0
    for (const theta of coneNodeAngles(l, m)) {
      const pts = [new THREE.Vector2(0, 0), new THREE.Vector2(R * Math.sin(theta), R * Math.cos(theta))];
      const cone = new THREE.Mesh(new THREE.LatheGeometry(pts, 96), mat());
      this.nodeGroup.add(cone);
      const rr = R * Math.sin(theta);
      const yy = R * Math.cos(theta);
      const rim = new THREE.LineLoop(
        new THREE.BufferGeometry().setFromPoints(
          Array.from({ length: 96 }, (_, i) => new THREE.Vector3(rr * Math.cos((i / 96) * 2 * Math.PI), yy, rr * Math.sin((i / 96) * 2 * Math.PI))),
        ),
        lineMat(),
      );
      this.nodeGroup.add(rim);
      this.nodeCounts.cones++;
    }

    // Vertical planar nodes containing the z-axis: cos(mφ)=0 or sin(|m|φ)=0
    for (const phi of planeNodeAngles(m)) {
      const plane = new THREE.Mesh(new THREE.PlaneGeometry(2 * R, 2 * R), mat());
      plane.rotation.y = phi; // physics (cosφ, sinφ, 0) → three (cosφ, 0, −sinφ)
      this.nodeGroup.add(plane);
      const edges = new THREE.LineSegments(new THREE.EdgesGeometry(plane.geometry), lineMat());
      edges.rotation.y = phi;
      this.nodeGroup.add(edges);
      this.nodeCounts.planes++;
    }
  }

  _buildAxes(extent) {
    disposeGroup(this.axesGroup);
    const L = extent * 1.02;
    const defs = [
      { dir: new THREE.Vector3(1, 0, 0), color: '#f87171', label: 'x' },
      { dir: new THREE.Vector3(0, 0, -1), color: '#4ade80', label: 'y' },
      { dir: new THREE.Vector3(0, 1, 0), color: '#60a5fa', label: 'z' },
    ];
    for (const d of defs) {
      const geom = new THREE.BufferGeometry().setFromPoints([d.dir.clone().multiplyScalar(-L), d.dir.clone().multiplyScalar(L)]);
      const line = new THREE.Line(geom, new THREE.LineBasicMaterial({ color: d.color, transparent: true, opacity: 0.55 }));
      this.axesGroup.add(line);
      const sprite = makeLabelSprite(d.label, d.color);
      sprite.position.copy(d.dir.clone().multiplyScalar(L * 1.07));
      sprite.scale.setScalar(extent * 0.12);
      this.axesGroup.add(sprite);
    }
  }

  applyOptions() {
    this.surfaceGroup.visible = this.options.surface;
    this.cloudGroup.visible = this.options.cloud;
    this.nodeGroup.visible = this.options.nodes;
    this.axesGroup.visible = this.options.axes;
    const phase = this.options.phase;
    this.posMaterial.color.copy(phase ? COLOR_POS : COLOR_MONO);
    this.negMaterial.color.copy(phase ? COLOR_NEG : COLOR_MONO);
    this._colorCloud();
  }

  setOption(key, value) {
    this.options[key] = value;
    this.applyOptions();
  }

  setSurfaceOpacity(v) {
    this.surfaceOpacity = v;
    this.posMaterial.opacity = v;
    this.negMaterial.opacity = v;
  }

  /** fraction ∈ [−1, 1.05]: plane x = fraction·extent; everything with x > plane is cut away. */
  setClip(fraction) {
    this.clipFraction = fraction;
    this.clipPlane.constant = fraction >= 1 ? 1e6 : fraction * this.extent;
  }

  animateCloud(onProgress, duration = 2600) {
    if (!this.cloudPoints) return;
    this.options.cloud = true;
    this.applyOptions();
    this.cloudPoints.geometry.setDrawRange(0, 0);
    this.cloudAnim = { start: null, duration, onProgress };
  }

  resetCamera() {
    const d = this.extent * 2.7;
    this.camera.position.set(d * 0.62, d * 0.48, d * 0.62);
    this.camera.near = this.extent * 0.01;
    this.camera.far = this.extent * 40;
    this.camera.updateProjectionMatrix();
    this.controls.target.set(0, 0, 0);
    this.controls.minDistance = this.extent * 0.3;
    this.controls.maxDistance = this.extent * 8;
    this.controls.update();
  }

  snapshot() {
    this.renderer.render(this.scene, this.camera);
    return this.renderer.domElement.toDataURL('image/png');
  }
}
