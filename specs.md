# Project Specifications & Change Log (`specs.md`)

## 2026-10-01 — Initial Creation of Rutherford's Gold Leaf Experiment Flask Web Application

### Overview of Changes
Created a complete Flask web application that visualizes Ernest Rutherford's 1909–1911 Gold Leaf (Geiger–Marsden) alpha-scattering experiment with synchronized interactive HTML5 Canvas animations, comprehensive labeled apparatus components, real-time physics calculations, and detailed educational explanations covering the setup, results, and how it changed physics.

### Exact Changes Made by File

1. **`app.py` (Created)**
   - Initialized the Flask web server with routes:
     - `GET /`: Renders the main interactive simulation interface (`templates/index.html`) with structured data for all 11 labeled apparatus parts (`EXPERIMENT_PARTS`) and selectable target foil elements (`TARGET_ELEMENTS`: Gold `Au`, Silver `Ag`, Copper `Cu`, Aluminum `Al`).
     - `GET /api/experiment-info`: Returns JSON metadata for all labeled experimental components and target materials.
     - `POST /api/scattering`: Computes classical Rutherford Coulomb scattering physics (`compute_rutherford_scattering`), returning the head-on distance of closest approach ($d_0$), actual minimum approach distance ($r_{\min}$), exact scattering angle ($\theta$ in degrees and radians), and relative differential cross-section factor ($\csc^4(\theta/2)$) for a given target atomic number $Z$, alpha kinetic energy $E_\alpha$ (MeV), and impact parameter $b$ (fm).

2. **`templates/index.html` (Created & Updated)**
   - Built the responsive HTML5 document structure featuring:
     - **View Mode & Model Switchers**: Toggle between *Split View (Macro + Atomic)*, *Apparatus Setup*, and *Atomic Nucleus Zoom*, as well as between *Rutherford's Nuclear Model (1911)* and *J.J. Thomson's "Plum Pudding" Model (1904)*.
     - **Simulation Control Bar**: Play/Pause toggle, Fire $\alpha$-Wave burst button, Fire Head-On (Backscatter) button, Reset Counts button, Target Foil selector, $\alpha$ Energy slider ($3.5\text{–}8.5\text{ MeV}$), Beam Rate slider, Rotatable Microscope angle slider ($-165^\circ\text{ to }+165^\circ$), and toggles for part labels, rare-scattering enhancement, and particle trails.
     - **Dual Interactive Canvas Stage**: `#macro-canvas` (1909 Geiger–Marsden vacuum chamber schematic) and `#atomic-canvas` (subatomic nuclear Coulomb repulsion zoom).
     - **Live Telemetry & Single-Particle Trajectory Calculator**: Real-time counters for total $\alpha$ particles, undeflected ($\theta < 2^\circ$), small-angle deflected ($2^\circ\text{–}90^\circ$), and backscattered ($\theta > 90^\circ$) particles, plus an angular distribution histogram (`#histogram-canvas`) and interactive impact-parameter ($b$) calculator backed by the Flask `/api/scattering` endpoint.
     - **Interactive Labeled Parts Directory**: 11 numbered component cards (`①`–`⑪`) that highlight their corresponding part on the canvas when hovered or clicked.
     - **Three-Pillar Physics Explanation & Comparison Table**: Detailed sections explaining (01) *The Experimental Setup*, (02) *Experimental Results* (including Rutherford's famous 15-inch artillery shell quote), (03) *How It Changed Physics*, and a side-by-side comparison table between Thomson's Plum Pudding Model and Rutherford's Nuclear Model using semantic HTML superscripts/subscripts and Unicode mathematical notation.

3. **`static/css/style.css` (Created)**
   - Implemented a dark scientific observatory theme using modern CSS Grid, Flexbox, logical properties (`inline-size`, `block-size`, `margin-inline`, `padding-block`), high-contrast status indicators, and responsive breakpoints.

4. **`static/js/simulation.js` (Created)**
   - Implemented the 60fps high-DPI HTML5 Canvas physics and rendering engine:
     - **Macroscopic Apparatus Renderer**: Draws the evacuated vacuum chamber, lead block containment shield, pulsing radioactive $\alpha$-source, lead collimator slit, tilted gold leaf target with holder clamps, circular $\text{ZnS}$ fluorescent screen with degree ticks and expanding green scintillation flashes on impact, rotatable viewing microscope with field-of-view cone, and all 11 interactive callout label badges (`①`–`⑪`) with leader lines.
     - **Subatomic Nuclear Zoom Renderer**: Visualizes the gold atomic lattice, vast empty electron cloud with orbiting electrons ($e^-$), impact parameter $b$ reference markers, and dense $+Ze$ nucleus (or diffuse positive sphere in Thomson mode) with real-time inverse-square Coulomb trajectory integration.
     - **Live Angular Distribution Histogram**: Log-scaled bar chart displaying counts across 6 angular bins ($0\text{–}5^\circ$, $5\text{–}20^\circ$, $20\text{–}60^\circ$, $60\text{–}90^\circ$, $90\text{–}135^\circ$, $135\text{–}180^\circ$).

---

## 2026-10-01 — Addition of Interactive Technical Schematic Diagram (`#schematic-diagram`)

### Overview of Changes
Added a comprehensive, vector-based SVG Technical Schematic Diagram of Rutherford's Gold Leaf Experiment with interactive component highlighting, switchable *Blueprint (Dark)* and *Textbook (Light)* themes, and standalone SVG file export.

### Exact Changes Made by File

1. **`templates/index.html` (Modified)**
   - Added `<section class="schematic-section" id="schematic-diagram">` containing `#rutherford-schematic-svg` (`viewBox="0 0 1280 620"`):
     - **Panel A (Left)**: Complete top-down engineering schematic of the 1909 Geiger–Marsden apparatus showing the cross-hatched lead block shield (`Pb`), radioactive $\alpha$-source, lead collimator slit with blocked diverging rays, collimated incident $\alpha$-beam, central ultra-thin gold leaf with holder clamps, circular $\text{ZnS}$ fluorescent screen with angular graduations ($0^\circ\text{–}150^\circ$), undeflected transmission rays ($\theta \approx 0^\circ$), small-angle deflected rays ($1^\circ < \theta < 90^\circ$) with $\theta$ arc, large-angle backscattered rays ($\theta > 90^\circ$), scintillation impact markers, rotatable microscope with turntable arc, vacuum chamber exhaust port (`P < 10⁻⁴ mmHg`), and all 11 interactive numbered callout badges (`①`–`⑪`).
     - **Panel B (Top-Right Inset)**: Magnified schematic of J.J. Thomson's 1904 "Plum Pudding" model showing a diffuse positive sphere with embedded electrons and straight-through $\alpha$-trajectories ($\theta < 0.02^\circ$).
     - **Panel C (Bottom-Right Inset)**: Magnified schematic of Rutherford's 1911 Nuclear Model and Coulomb scattering geometry illustrating the dense $+79e$ gold nucleus, vast empty electron cloud, impact parameter $b$ dimension arrows, distance of closest approach $r_{\min}$, scattering angle $\theta$, hyperbolic trajectories, and the Rutherford scattering equation box.
   - Added theme toggle buttons (`Blueprint (Dark)` vs. `Textbook (Light)`) and a `⬇ Download SVG` button (`#btn-download-svg`).

2. **`static/css/style.css` (Modified)**
   - Added styling rules for `.schematic-section`, `.schematic-card`, `#rutherford-schematic-svg`, `.schematic-card[data-theme="blueprint"]`, `.schematic-card[data-theme="textbook"]`, and interactive `.schem-callout` / `.schem-part` hover and active spotlight states.

3. **`static/js/simulation.js` (Modified)**
   - Updated `setHighlightedPart(partId)` to synchronize active highlights across the live HTML5 canvas, the 11 component cards, and the SVG schematic callouts/parts (`.schem-callout, .schem-part`).
   - Added hover and click event listeners on all `.schem-callout` and `.schem-part` SVG elements.
   - Added theme switching logic for `[data-schematic-theme]` buttons and client-side standalone SVG serialization/download for `#btn-download-svg`.

---

## 2026-10-01 — Removal of Theoretical Thomson Model & Addition of Real 1897 Cathode Ray Tube Experiment

### Overview of Changes
Removed all theoretical "Plum Pudding" (1904) atomic model representations and replaced them with **J.J. Thomson’s real 1897 Cathode Ray Tube (CRT) Experiment** across the interactive canvas simulations, the technical SVG schematic diagram, and the educational explanations/comparison table so that the application exclusively features real historical laboratory experiments.

### Exact Changes Made by File

1. **`templates/index.html` (Modified)**
   - Replaced the header toggle option `Thomson “Plum Pudding” (1904)` (`data-model="thomson"`) with `Thomson Cathode Ray Tube (1897)` (`data-model="thomson_crt"`).
   - Added dynamic header element IDs (`#macro-panel-tag`, `#macro-panel-title`, `#macro-panel-hint`, `#atomic-panel-tag`) to update panel titles when switching between the 1909 Rutherford Gold Leaf experiment and the 1897 Thomson Cathode Ray Tube experiment.
   - Replaced **Inset B** of `#rutherford-schematic-svg` with **`B. J.J. THOMSON CATHODE RAY TUBE EXPERIMENT (CAMBRIDGE, 1897)`**, depicting the evacuated glass CRT envelope, heated cathode ($-$), accelerating anode collimating slits ($+$), parallel electric deflection plates ($+E$ and $-E$), Helmholtz magnetic coil ($\vec{B} \otimes$), balanced undeflected electron ray ($v = E/B$), electrically deflected electron ray curving upward toward the $+$ plate, and the fluorescent scale screen.
   - Updated the **Experimental Results**, **How It Changed Physics**, and **Comparison Table** sections to remove all references to the theoretical Plum Pudding model and instead compare the two real experiments: **J.J. Thomson’s Cathode Ray Tube Experiment (1897)** and **Rutherford’s Gold Leaf Experiment (1909)**.

2. **`static/js/simulation.js` (Modified)**
   - Replaced theoretical Plum Pudding branches in `computeScatteringThetaRad`, `sampleImpactParameterFm`, `spawnAlphaPair`, and `stepSimulation` with real cathode-ray electron deflection physics (`thomson_crt`: upward electrostatic acceleration $\vec{F}_E = -e\vec{E}$ between parallel plates and balanced straight trajectories when $F_E = F_B$).
   - Added `renderThomsonCRTMacro(ctx, W, H)` to draw the full 1897 Crookes–Thomson evacuated glass cathode ray tube with 7 labeled apparatus callouts (`1. Cathode (− Electrode)`, `2. Anode Collimating Slits (+)`, `3. Electric Deflection Plates (+E / −E)`, `4. Helmholtz Magnetic Coils (B ⊗)`, `5. Deflected Cathode Ray (e⁻ Stream)`, `6. Balanced Beam (F_E = F_B → v = E/B)`, `7. Fluorescent Scale Screen`).
   - Updated `renderAtomicCanvas()` to render the magnified $\vec{E} \times \vec{B}$ parallel-plate deflection region (`Positive Plate (+V)`, `Negative Plate (−V)`, downward $\vec{E}$ field lines, $\otimes \vec{B}$ markers, parabolic electron trajectories, and the measured $e/m_e = 1.76 \times 10^{11}\text{ C/kg}$ callout) when `thomson_crt` is selected.
   - Updated `[data-model]` event listeners to synchronize both canvas headers and clear particle queues when switching between the two real experiments.

3. **`static/css/style.css` (Modified)**
   - Updated `.model-toggle .seg-btn.active[data-model="thomson_crt"]` selector to match the new `thomson_crt` experiment key.

---

## 2026-10-01 — New Section: Atomic Orbitals & Quantum Mechanics (Schrödinger → s, p, d, f → Element Configurations)

### Overview of Changes
Added a new page `/orbitals` implementing the "Interactive Quantum Mechanics Animation" specification: **Module A** (step-by-step Schrödinger derivation with animated equations and graphs), **Module B** (interactive 3D hydrogen-like orbital viewer for any n = 1–7, l, m_l) and **Module C** (periodic-table element selector with an Aufbau/Pauli/Hund configuration engine and measured exceptions). Both pages are linked by a shared header navigation.

### Exact Changes Made by File

1. **`quantum_engine.py` (New)**
   - `ELEMENTS` (118 symbols/names), `NOBLE_GASES`, `MADELUNG_ORDER` (19 subshells sorted by (n + l, n): 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p).
   - `EXCEPTIONS`: the 13 specified exceptions (Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, La, Gd, Pt, Au, Ac) with type labels and explanations, plus additional measured NIST exceptions flagged `source: "additional"` (Ce, Th, Pa, U, Np, Cm, Lr).
   - `table_position(z)` (period, group, grid row/col, block; lanthanides/actinides in rows 9–10), `madelung_configuration`, `ground_state_configuration`, `notations` (full spdf in filling order + condensed noble-gas form, Unicode and plain), `orbital_boxes` (Hund filling m_l = +l → −l, spin-up first; shows empty subshells such as Pd 5s / La 4f; per-electron n, l, m_l, m_s, fill order), `element_details` (stats: unpaired electrons, multiplicity, electrons per shell and per l, exception info with Aufbau prediction vs observed, `predicted` flag for Z ≥ 104), `all_elements`, `madelung_sequence`.

2. **`tests/test_quantum_engine.py` (New)** — checks Madelung order, electron totals for Z = 1–118, Fe/Cr/Cu/Nb/Mo/Ru/Rh/Pd/Ag/La/Gd/Pt/Au/Ac/Kr/Ar/Og notations, Hund's rule for N 2p³, unpaired counts, blocks, and unique periodic-table cells. Run: `/Users/bharen/venv/mainvenv/bin/python3 tests/test_quantum_engine.py`.

3. **`app.py` (Modified)**
   - `import quantum_engine`; new routes `GET /orbitals` (renders `orbitals.html` with elements + Madelung sequence), `GET /api/elements`, `GET /api/element/<int:z>` (404 outside 1–118).

4. **`templates/orbitals.html` (New)**
   - Header with cross-page nav and module tabs; narrative flow strip; KaTeX (0.16.11) + Three.js 0.160.0 import map (CDN).
   - Module A: 5 step tabs (Coulomb potential & TISE, Laplacian in spherical coordinates, separation of variables with l(l+1) and m², angular solution Φ/Θ/Y_l^m with L and L_z, radial solution with associated Laguerre R_nl, a₀, E_n = −13.6 Z²/n² eV and quantum-number table incl. Stern–Gerlach m_s), Prev/Next/Auto-play; LaTeX wrapped in `{% raw %}`.
   - Module B: 3D viewer stage, n/l/m_l sliders, display toggles (isosurface, cloud, phase colours, nodal surfaces, axes, auto-rotate, radial graph), clipping-plane and opacity sliders, replay/reset/PNG buttons, properties list, radial-probability and angular polar graphs, subshell reference table.
   - Module C: search (symbol/name/Z via datalist), prev/next, "Build up from H", periodic table grid, element card, exception banner, full and condensed notation, statistics, shell bars, orbital box diagram, Madelung diagonal SVG, tooltip element.

5. **`static/css/orbitals.css` (New)** — styles for hero, step tabs/panels with staggered `eq-in` equation reveal, separation diagram, viewer layout/HUD/legend, quantum-number sliders, periodic table (block colours via `color-mix`, exception outline), element card, exception banner, coloured notation, orbital boxes with `arrow-in` animation, tooltip, Madelung SVG; honours `prefers-reduced-motion`.

6. **`static/js/orbitals/quantum_math.js` (New)** — generalized Laguerre and associated Legendre (no Condon–Shortley phase) recurrences, normalized `makeRadial`, real `makeAngular`, `makePsi`, `energyEV`, `radialNodes`, `coneNodeAngles`, `planeNodeAngles`, `radiusEnclosing`, orbital names (p_x … f_y(3x²−y²)), angular formula LaTeX, `orbitalInfo`. Verified numerically: ∫r²R² dr = 1 for all n ≤ 7, ∫Y² dΩ = 1 for l ≤ 6, node counts n−l−1 and l−|m|.

7. **`static/js/orbitals/orbital_viewer.js` (New)** — `OrbitalViewer` class (Three.js): ψ sampled on a 56³/68³/84³ grid (extent = 99.5 % radial-probability radius × 1.1); density threshold enclosing 90 % probability; two `MarchingCubes` meshes (ψ > 0 orange, ψ < 0 blue; `reset()` before each update to clear cached normals; triangle budgets 80k/120k/160k); 32 000-point Monte-Carlo dot cloud sampled from |ψ|² with animated "measurement" build-up; analytic nodal surfaces (radial spheres, conical/equatorial angular nodes via `LatheGeometry`, vertical φ-planes) in translucent white; `x = c` clipping plane; axes with labels; OrbitControls rotate/pan/zoom/auto-rotate; PNG snapshot. Axis mapping physics → three: x→x, z→y, y→−z.

8. **`static/js/orbitals/orbitals_app.js` (New)** — page controller: KaTeX auto-render; Module A step navigation/auto-play and canvases (Coulomb well with E_n levels and measured Balmer lines Hα–Hδ, animated spherical-coordinate diagram, Φ single-valuedness ring with continuous m slider, angular polar plot, radial R_nl / P(r) graph with nodes); Module B slider constraints (0 ≤ l ≤ n−1, −l ≤ m_l ≤ l), presets, properties, graphs, dynamic import of the viewer with fallback message; Module C periodic table, search, API fetch + cache, notation rendering, exception banner, stats, shell bars, orbital box diagram with staggered arrow animation, hover tooltip (n, l, m_l, m_s), click-to-view-in-3D, Madelung SVG highlighting, Z = 1 → target build-up animation.

9. **`templates/index.html` (Modified)** — added `.page-nav` links (Experiments ↔ Atomic Orbitals) in the header and an `.orbitals-teaser` card before the footer linking to `/orbitals`.

10. **`static/css/style.css` (Modified)** — appended shared `.page-nav`, `.nav-link` and `.orbitals-teaser` styles.

---

## 2026-10-01 — New Section: Essential Chemical & Ionic Equations (`/reactions`) with Chemical Specimen Gallery & Virtual Laboratory Apparatus Simulator

### Overview of Changes
Added a new section `/reactions` (**Essential Chemical & Ionic Equations for High School AP/IB and First-Year University Chemistry**) containing all **187 reactions and governing equations** from the user's specification across **11 reaction categories** plus **Section 12's Canonical Equation Types Summary Table**, expanded with **19 additional essential high-school and 1st-year college reactions** (**206 total equations**). Every reaction includes KaTeX-rendered molecular, complete ionic, net ionic, redox half-reaction, and thermodynamic/equilibrium expressions, a clear explanation of what the reaction does and its driving force, observable laboratory signs, visual chemical specimen and 2D molecular structure cards (with PubChem 2D structure integration and offline-safe SVG fallback), and an interactive HTML5 Canvas **Virtual Chemistry Lab Workbench** (plus an inline card lab drawer that opens directly inside any clicked reaction card) animating the chemical process in realistic laboratory instruments.

### Exact Changes Made by File

1. **`reactions_engine.py` (Created)**
   - Defined `CHEMICALS` (~150 chemical species with `name`, `formula`, `state`, authentic physical `color`, `vessel` type (`gas`, `metal`, `crystal`, `powder`, `vial`, `solution`), PubChem `cid`, 2D molecular/crystal `geom` archetype, and physical `appearance` description).
   - Defined `CATEGORIES` (12 categories: `1. Synthesis & Combination`, `2. Decomposition`, `3. Combustion & Hydrocarbons`, `4. Single Displacement & Acid-Metal`, `5. Double Displacement — Precipitation`, `6. Acid-Base Neutralization & Ionization`, `7. Gas-Evolving Reactions`, `8. Oxidation-Reduction & Half-Reactions`, `9. Complex Ion & Amphoteric Reactions`, `10. Industrial, Environmental & Applied`, `11. Thermodynamic, Kinetic & Equilibrium Equations`, and `12. Canonical Equation Types & Added Essentials`).
   - Populated `REACTIONS` with **206 reactions**:
     - `#1–#187`: Complete verbatim coverage of all 187 reactions, ionic equations, redox half-reactions, and thermodynamic/kinetic/equilibrium governing equations from the specification.
     - `#188–#206` (`added_essential=True`): 19 important additional reactions for AP/IB and 1st-year university chemistry (Fischer Esterification, Saponification, Bromination of Ethene unsaturation test, $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$ thermal Le Châtelier equilibrium, $[\text{Co(H}_2\text{O)}_6]^{2+} \rightleftharpoons [\text{CoCl}_4]^{2-}$ coordination equilibrium, $\text{CrO}_4^{2-} \rightleftharpoons \text{Cr}_2\text{O}_7^{2-}$ pH equilibrium, Daniell Galvanic Cell, Iodometric Titration, Acidified Thiosulfate 'Disappearing Cross' Sulfur Clock, Tollens' Silver Mirror Test, Fehling's/Benedict's $\text{Cu}_2\text{O}$ Test, Prussian Blue Synthesis, Reversible Dehydration of $\text{CuSO}_4\cdot 5\text{H}_2\text{O}$, Limewater $\text{CO}_2$ Test, Human Blood Bicarbonate Buffer, Ideal Gas Law, Van der Waals Equation, Beer–Lambert Law, and Clausius–Clapeyron Equation).
   - Defined `CANONICAL_SUMMARY` (Section 12 comparison table) and helper functions `get_enriched_reactions()`, `get_reaction_by_id(rxn_id)`, and `get_all_payload()`.

2. **`tests/test_reactions_engine.py` (Created)**
   - Added unit and integration tests verifying all 206 reactions (187 spec + 19 added), 12 categories, 9 canonical summary rows, chemical resolution against `CHEMICALS`, explanation completeness, apparatus assignments, and Flask routes (`GET /reactions`, `GET /api/reactions`, `GET /api/reaction/<id>`). Verified using `/Users/bharen/venv/mainvenv/bin/python3 -m unittest discover -s tests -v`.

3. **`app.py` (Modified)**
   - Imported `reactions_engine` and added routes:
     - `GET /reactions`: Renders `templates/reactions.html` with the full reactions payload.
     - `GET /api/reactions`: Returns the complete JSON catalog of 206 reactions, categories, chemicals, and canonical summary table.
     - `GET /api/reaction/<int:rxn_id>`: Returns enriched JSON for a single reaction or HTTP 404.

4. **`templates/reactions.html` (Created)**
   - Built the page layout featuring:
     - Shared 3-page navigation header (`Rutherford & Thomson Experiments`, `Atomic Orbitals & Quantum Mechanics`, `Essential Chemical Reactions`) and a horizontal quick-jump Category Ribbon.
     - **Top Interactive Virtual Chemistry Lab Workbench** (`#lab-workbench`) with `#wb-canvas`, Play/Pause, Add Reagent / Trigger Pulse, Reset, Microscopic Ion/Particle Inset toggle, PubChem 2D Structures toggle, Reaction Progress scrubber, Lab Speed slider, Prev/Next reaction buttons, live digital thermometer/signal readouts, observation & mechanism panels, and active chemical specimen strip.
     - **Search, Filter & Quick Jump Toolbar** with instant search across all 206 reactions, a Jump-to-Equation selector (`#1–#206`), and 8 feature filter chips (`All`, `Core Spec`, `Added Essentials`, `Has Complete/Net Ionic`, `Has Half-Reactions`, `Forms Precipitate`, `Evolves Gas`, `High-Temp / Flame`).
     - **Two-Column Catalog Layout** with a sticky left category classification sidebar and the categorized reaction cards feed plus Section 12's Canonical Summary Table with one-click `Simulate #ID ⚗️` buttons.

5. **`static/css/reactions.css` (Created)**
   - Styled the Virtual Chemistry Lab Workbench, category ribbon, sticky sidebar, reaction cards, equation tags, chemical specimen/structure cards, inline card lab drawer, and canonical table. Applied `content-visibility: auto; contain-intrinsic-size: auto 720px;` on category sections and `contain-intrinsic-size: auto 340px;` on reaction cards for smooth 60fps scrolling across 206 equations.

6. **`static/js/reactions/reactions_app.js` (Created)**
   - Implemented custom SVG laboratory vessel generators (`gas` cylinder with gauge, `metal` lustrous strip on watch glass, `crystal` faceted crystals, `powder` mound, `vial` reagent bottle, `solution` graduated beaker) and 2D molecular/crystal geometry SVG generators (`diatomic`, `bent`, `linear3`, `trigonal`, `pyramidal`, `tetrahedral`, `octahedral`, `crystal`/`ionic`) paired with live PubChem 2D structure images (`https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/PNG`) and automatic offline fallback.
   - Implemented lazy `IntersectionObserver` KaTeX equation rendering, instant search/filter/category navigation, and synchronized **Inline Lab Instrument Drawers** that open directly inside any clicked reaction card as well as in the top workbench.
   - Built the multi-archetype HTML5 Canvas laboratory apparatus simulator supporting burette & pH/potentiometric titrations with live sigmoidal curves, voltaic cells with salt bridges & electron flow, Hoffmann electrolysis cells, Bunsen burner crucibles, thermite rail-weld crucibles, fume-hood nitric acid vessels with $\text{NO}_2$ clouds, heated test-tube gas-delivery rigs, high-pressure catalytic reactors, calorimeters, UV-Vis spectrophotometers, precipitation beakers with settling crystals, and a toggleable Submicroscopic Particle View inset.

7. **`templates/index.html` & `templates/orbitals.html` (Modified)**
   - Added `<a href="{{ url_for('reactions') }}" class="nav-link">Essential Chemical Reactions</a>` to `.page-nav` so all three sections of the application are accessible from every page.


---

## 2026-10-01 — Gray & White Theme and App Rename ("Inorganic Chemistry: Introduction")

**Request:** "Keep the Gray and white theme, the name of the app should be Inorganic Chemistry: Introduction"

1. **`static/css/theme.css` (NEW, linked LAST in all three templates)**
   - `:root` overrides: light-gray page (`--bg-base #f3f4f6`), white cards/surfaces, dark text (`#111827 / #374151 / #6b7280`), charcoal chrome accent (`--accent-gold #374151`), deepened scientific accents for contrast on white, `--screen-bg #1f1f1f` for animation "instrument screens".
   - New `.app-brand` header style; charcoal active states for nav links, ribbons, sidebar items and filter chips; restyled `.btn-primary`, `.btn-accent`, `.btn-secondary`, `.btn-sim-rxn`, `.btn-table-sim`.
   - Charcoal backgrounds for canvases that draw light content (`#histogram-canvas`, `.step-visual canvas`, `.graph-canvas`, `.canvas-wrapper`, `.viewer-stage`, `#wb-canvas`, `.inline-lab-canvas`, `.chem-visual-row`); viewer HUD text `#e5e5e5`.
   - Reactions/orbitals tweaks (white cards, softer shadows, periodic-table selection border, tooltip text), neutral gray `.wb-instrument-tag` / `.rxn-apparatus-pill`, and `white-space: nowrap` for scrubber labels.

2. **`static/css/style.css`, `orbitals.css`, `reactions.css` (Modified via script)**
   - Hard-coded dark navy colours converted with `scratch/apply_gray_theme.py`: page chrome inverted to white/light gray (`color` → text palette, other properties → surface palette; `--*` variables and `:root` skipped); "screen" selectors (blueprint schematic, canvases, 3D viewer, lab workbench) desaturated from navy to neutral charcoal.

3. **JS canvases desaturated (slate/navy → neutral grays)**
   - `static/js/simulation.js`, `static/js/orbitals/orbitals_app.js`, `static/js/orbitals/orbital_viewer.js` (Three.js clear colour `0x050914` → `0x141414`), `static/js/reactions/reactions_app.js`.
   - `reactions_app.js`: category pills now use charcoal text (`color: #1f2937`) on a tinted background with the category colour as border.

4. **Templates**
   - `index.html`, `orbitals.html`, `reactions.html`: `<title>` prefixed with "Inorganic Chemistry: Introduction — …", `theme.css` linked last, `<a class="app-brand">Inorganic Chemistry: Introduction</a>` added to each header.
   - `index.html`: inline SVG colours desaturated; footer now reads "Inorganic Chemistry: Introduction • Rutherford Gold Leaf & Thomson Cathode Ray Experiments • Built with Flask & HTML5 Canvas".
   - `reactions.html`: Section 12 pill made gray.

5. **Backups** of the original (dark-theme) CSS, JS and templates are stored in the conversation scratch folder `scratch/theme_backup/`.

6. **Verification:** `node --check` passes for all four JS files; unit tests pass; `/`, `/orbitals`, `/reactions` return 200 and were checked visually with headless Chrome screenshots.

---

## 2026-10-01 — Reactions Page Split into Separate Views + Prominent Section Headers

**Request:** "I want the reactions to be in their separate views instead of one long view. And for each of the section have a very visible section header at the beginning of the section." (Chosen layout: one section per view; clicking a reaction opens its own dedicated view with a Back link.)

1. **Hash-routed views (`static/js/reactions/reactions_app.js`)**
   - New router: `#/section/<1-12>` (Section View) and `#/reaction/<id>` (Reaction View); default `#/section/1`. Browser Back/Forward works. Functions added: `parseRoute`, `applyRoute`, `navigateTo`, `clearSearch`, `renderSectionView`, `renderReactionView`, `renderReactionDetail`, `buildSectionBannerHtml`, `buildEquationRowsHtml`, `reactionsInSection`, `matchesFeatureFilter`, `matchesSearch`, `syncNavActive`, `sectionTitle`, `hydrateCards`.
   - View switches use `document.startViewTransition` (cross-fade + morphing banner, with fallback when unsupported), reset scroll to top, and move focus to the new view's heading (accessibility).
   - **Section View:** shows only the selected section — large banner, compact reaction cards (number, subcategory, molecular + net-ionic equation, "What This Reaction Does" explanation, chemical formula chips, apparatus, "Open Reaction & Lab Animation →"), and a Previous/Next section pager. Clicking anywhere on a card opens the reaction. Section 12 shows the canonical summary table followed by the 19 added 1st-year reactions.
   - **Reaction View:** "← Back to Section N" breadcrumb with "Reaction k of n in this section", a compact copy of the section banner, the lab workbench (animation, controls, telemetry, explanation, observation), an "All Equations" panel, the full chemical specimen gallery (SVG + PubChem images), and Previous/Next reaction pager (the last reaction links on to the next section).
   - Feature filter chips now filter within the current section. Search covers all sections and shows results grouped under dark section header bars (clicking one clears the search and opens that section). The "Open Reaction" dropdown navigates to the reaction view.
   - Removed the "All Categories" long view, the inline per-card lab drawer (`mountInlineDrawer`), and the old `renderCatalog`/`matchesFilter`; the lab canvas is only rendered while the Reaction View is visible (saves CPU).
   - Fix: canvas precipitate label now names the solid product (e.g. `AgCl(s)↓`) instead of the last listed chemical (was `NaNO₃(s)↓` for #62).

2. **`templates/reactions.html`**
   - Restructured `<main>` into `#section-view` (toolbar, section sidebar, `#section-banner`, summary table, `#reactions-feed-container`, `#section-pager`) and `#reaction-view` (`#reaction-breadcrumb`, `#reaction-section-banner`, `#lab-workbench`, `#reaction-detail`, `#reaction-pager`).
   - Ribbon pills and sidebar items are now `<a href="#/section/N">` links; "All Categories" entries removed; summary-table buttons are `<a href="#/reaction/ID">` links; removed the workbench specimen strip, extra-equation box and global Prev/Next buttons (replaced by the reaction pager).

3. **`static/css/reactions.css`** (new "Separate Views" block at the end)
   - `.section-banner`: charcoal full-width header with a 12px category-colour left border, bottom colour bar, 88px numbered badge, "SECTION N OF 12" eyebrow, large title (`clamp(1.75rem, 2.7vw, 2.5rem)`), description, pattern + stats chips, and Prev/Next section buttons; `--compact` variant for the reaction view.
   - Responsive 2-column card grid, compact card footer and formula chips, search-group header bars, pager cards, breadcrumb button, detail panels, `.reactions-page [hidden]{display:none!important}`, and `prefers-reduced-motion` handling for view transitions.

4. **Verification:** `node --check` OK; jsdom DOM test (`scratch/mc/test_views.js`, 26 checks: routing, sidebar/ribbon navigation, filters, card → reaction view, breadcrumb, pagers, search grouping, Section 12, jump select, no runtime errors) all pass; unit tests pass; headless-Chrome screenshots of Section 5, Section 12 and Reaction #62 reviewed. Backups of the pre-change files are in `scratch/views_backup/`.

---

## 2026-10-01 — Removed Redundant Top Section Ribbon (Reactions Page)

**Request:** "The top bar of Sections (list of section buttons) is redundant, remove it."

- `templates/reactions.html`: deleted the `.category-ribbon-wrap` / `#top-category-ribbon` block (the row of section pills under the page header). Section navigation is now through the left "Reaction Sections" sidebar, the ← / → buttons in each section banner, the bottom Previous/Next section pager, and the "Back to Section" breadcrumb in reaction views.
- `static/js/reactions/reactions_app.js`: comment updated ("Section links (sidebar)"); no logic change — active-state syncing still targets `[data-cat]` (sidebar items).
- The now-unused `.category-ribbon*` / `.ribbon-pill` CSS rules are left in place (harmless).
- Verification: jsdom view test updated (checks sidebar active state and that the ribbon is absent) — 27/27 pass; screenshot of `#/section/3` reviewed.

---

## 2026-10-01 — Git Repository Setup (for GitHub)

**Request:** "Create a new repository in my github and commit this app there." (Chosen: private repo `inorganic-chemistry-introduction`.)

- Initialised a local Git repository (branch `main`) in the project folder and created the initial commit with all source files.
- Added `.gitignore` (Python caches, virtualenvs, `.env*`, `.DS_Store`, editor folders, `node_modules/`).
- Added `requirements.txt` (`Flask>=3.0,<4` — the only runtime dependency; KaTeX/Three.js come from CDN).
- Added `README.md` (app overview of the three pages, run instructions, tests, project layout).
- Remote `origin` set to `https://github.com/haren-bh/inorganic-chemistry-introduction.git` and pushed (`main -> main`).

---

## 2026-10-01 — Google Cloud Run Deployment (`haren-main` / `us-central1`)

**Request:** "Deploy this to cloud run under haren-main project us-central1 region"

1. **`Dockerfile` (NEW)**
   - Added a `python:3.12-slim` container build installing `requirements.txt` and serving `app:app` with Gunicorn (`exec gunicorn --bind :${PORT:-8080} --workers 2 --threads 4 --timeout 0 app:app`).

2. **`.dockerignore` (NEW)**
   - Excluded `.git`, `__pycache__`, virtual environments, `.env*`, editor directories, and `tests/` from the container build context.

3. **`requirements.txt` (Modified)**
   - Added `gunicorn>=21.2.0,<24` alongside `Flask>=3.0,<4`.

4. **`app.py` (Modified)**
   - Imported `os`, updated the top-level docstring to describe all three sections of *Inorganic Chemistry: Introduction*, and updated `if __name__ == "__main__":` to read `PORT`, `HOST`, and `FLASK_DEBUG` from environment variables.

5. **Deployment & Verification**
   - Deployed via Cloud Run MCP (`deploy_local_folder`) to project `haren-main`, region `us-central1`, service `inorganic-chemistry-introduction`.
   - Live Service URL: `https://inorganic-chemistry-introduction-nad4p273qa-uc.a.run.app`
   - Verified `/`, `/orbitals`, `/reactions`, and `/api/reactions` all return HTTP `200`.

---

## 2026-10-03 — New Section: AP Chemistry Practice & Exam Quiz (`/quiz`) Across Units 1–9 (450 Questions, 2 Practice Modes)

### Overview of Changes
Added a new section `/quiz` (**AP Chemistry Practice & Exam Quiz**) aligned with the official College Board AP Chemistry Course and Exam Description (CED) and Khan Academy AP Chemistry curriculum across all **9 AP Chemistry Units** with **50 exam-level multiple-choice questions per unit** (**450 questions total** across all 91 CED topics). Implemented two interactive practice modes:
- **Mode 1 (10 Questions at a Time — Score at End)**: Students work through structured 10-question sets (`Set 1: Q1–Q10` through `Set 5: Q41–Q50` per unit, or a randomized 10-question draw), submit at the end to receive their score (`X/10` and percentage), and review all 10 correct answers alongside detailed step-by-step explanations.
- **Mode 2 (1 Question at a Time — Instant Feedback)**: Students answer one question at a time, immediately see whether their selected option is **Correct (`✓`)** or **Incorrect (`✗`)**, and view the detailed AP Chemistry explanation with KaTeX-rendered equations and calculations.

### Exact Changes Made by File

1. **`quiz_data/__init__.py` & `quiz_data/unit_1.py` .. `quiz_data/unit_9.py` (Created)**
   - Authored 50 AP Exam-difficulty multiple-choice questions per unit (450 total) with data tables (`<table class="quiz-data-table">`), reaction equations, 4 answer choices (`A`–`D`), balanced answer distributions, and step-by-step explanations:
     - `quiz_data/unit_1.py`: **Unit 1: Atomic Structure and Properties** (`7–9% of exam`, CED Topics `1.1`–`1.8`, 50 questions).
     - `quiz_data/unit_2.py`: **Unit 2: Molecular and Ionic Compound Structure and Properties** (`7–9%`, CED Topics `2.1`–`2.7`, 50 questions).
     - `quiz_data/unit_3.py`: **Unit 3: Intermolecular Forces and Properties** (`18–22%`, CED Topics `3.1`–`3.13`, 50 questions).
     - `quiz_data/unit_4.py`: **Unit 4: Chemical Reactions** (`7–9%`, CED Topics `4.1`–`4.9`, 50 questions).
     - `quiz_data/unit_5.py`: **Unit 5: Kinetics** (`7–9%`, CED Topics `5.1`–`5.11`, 50 questions).
     - `quiz_data/unit_6.py`: **Unit 6: Thermochemistry** (`7–9%`, CED Topics `6.1`–`6.9`, 50 questions).
     - `quiz_data/unit_7.py`: **Unit 7: Equilibrium** (`7–9%`, CED Topics `7.1`–`7.14`, 50 questions).
     - `quiz_data/unit_8.py`: **Unit 8: Acids and Bases** (`11–15%`, CED Topics `8.1`–`8.10`, 50 questions).
     - `quiz_data/unit_9.py`: **Unit 9: Thermodynamics and Electrochemistry** (`7–9%`, CED Topics `9.1`–`9.10`, 50 questions).

2. **`quiz_engine.py` (Created)**
   - Aggregates `quiz_data.unit_1` through `quiz_data.unit_9`, enriches all 450 questions with global IDs (`1..450`), unit metadata, 10-question set numbers (`1..5`), and letter keys (`A`–`D`), and provides the official **AP Chemistry Equations & Physical Constants Sheet** (`AP_REFERENCE_SHEET`).
   - Exposes `get_all_payload()`, `get_units_summary()`, `get_unit_by_id(unit_id)`, and `get_question_by_id(q_id)`.

3. **`app.py` (Modified)**
   - Imported `quiz_engine` and added routes:
     - `GET /quiz`: Renders `templates/quiz.html` with all 9 units, 450 questions, and the AP Reference Sheet.
     - `GET /api/quiz/units`: Returns JSON summary of all 9 AP Chemistry units and topic counts.
     - `GET /api/quiz/unit/<int:unit_id>`: Returns JSON for a single unit (`1..9`) and its 50 questions (404 if invalid).
     - `GET /api/quiz/question/<int:q_id>`: Returns JSON for a single question (`1..450`, 404 if invalid).

4. **`templates/quiz.html` (Created)**
   - Built the Gray & White themed Quiz interface featuring:
     - Top **Practice Mode Switcher** toggling between **Mode 1: 10 Questions at a Time (Score at End)** and **Mode 2: 1 Question at a Time (Instant Feedback)**.
     - Collapsible **AP Chemistry Equations & Physical Constants Sheet** (`#ap-ref-drawer`) rendered with KaTeX.
     - Sticky left **AP Chemistry Units (1–9) Sidebar** displaying each unit's title, official exam weight (`7–9%`, `18–22%`, `11–15%`), question count (`50 Qs`), and live mastery progress bar.
     - Prominent charcoal **Unit Header Banner** (`#quiz-unit-banner`), CED Topic Filter dropdown, Difficulty filter, keyword search, Mode 1 set selector pills (`Set 1`–`Set 5` + `Random 10-Question Set`), score summary banner (`#batch-score-banner`), and Mode 2 interactive 50-question map grid (`#single-qgrid`).

5. **`static/css/quiz.css` (Created)**
   - Styled the mode switcher, reference sheet drawer, unit progress bars, 10-question set controls, score circle banner, stimulus data tables, option buttons (`is-selected`, `opt-correct-answer`, `opt-wrong-selected`), and explanation boxes in the application's gray and white theme, including `@supports not (accent-color: ...)` progressive enhancement fallbacks.

6. **`static/js/quiz/quiz_app.js` (Created)**
   - Implemented hash-routed unit navigation (`#/unit/<1-9>`), KaTeX math rendering (`$...$` and `$$...$$`), CED topic/difficulty/search filtering, Mode 1 batch set answering and end-of-set scoring with full answer/explanation reveal, Mode 2 single-question immediate evaluation and explanation reveal, and `localStorage` mastery persistence.

7. **`templates/index.html`, `templates/orbitals.html`, `templates/reactions.html`, `README.md` (Modified)**
   - Added `<a href="{{ url_for('quiz') }}" class="nav-link">AP Chemistry Quiz</a>` to the shared `.page-nav` header across all pages and documented `/quiz` in `README.md`.

8. **`tests/test_quiz_engine.py` (Created)**
   - Added unit and integration tests verifying all 9 units, exam weights, 450 questions, 91 CED topics, option/explanation schemas, and Flask routes (`/quiz`, `/api/quiz/units`, `/api/quiz/unit/<id>`, `/api/quiz/question/<id>`).

---

## 2026-10-03 — AP Chemistry Quiz Audit: Fall 2024 CED Alignment, Error Fixes, and 120 New Blind-Spot Questions (450 → 570)

**Request:** "Check the quiz questions and see if those match the AP Chemistry level and see how much of the content do the questions cover. If there are any blind spots add more questions."

### Overview of Changes
- **Audit scope:** all 450 questions were reviewed, unit by unit, against the official College Board *AP Chemistry Course and Exam Description* (Effective Fall 2024; the June 2026 clarifications changed no content).
- **Each question was checked for:** AP level, answer accuracy (every key and number recomputed), CED exclusion statements, Essential Knowledge (EK) coverage, science-practice mix, and answer-key balance.
- **Verdict:** the original items were at genuine AP Exam level.
- **Problems found:**
  - 62 items with factual or numerical errors. In 8 of them, the keyed answer was false or did not follow from the item's own data (U1 Q4, U2 Q6, U5 Q40, U6 Q16/Q31/Q36, U8 Q21, U9 Q9).
  - 36 items testing content excluded by the CED
  - strongly skewed answer keys in Units 3 and 9 (for example, Unit 9 had 40 of 53 keys = A)
  - no graphical or particulate figures at all
  - a reference sheet that did not match the official 2025 equation sheet
  - topic numbering from the superseded 2019 CED (7.13, 7.14, 9.6–9.10)
- **Added:** 120 new questions targeted at the blind spots found. EK coverage rose from 225/241 (93%) to 241/241 (100%), and the bank went from 0 to 62 inline SVG figures.

### Exact Changes Made by File

1. **`quiz_data/unit_7.py`, `quiz_data/unit_8.py`, `quiz_data/unit_9.py`: restructure to the Fall 2024 CED**
   - Old 7.13 (pH and solubility) moved to **8.11** (Unit 8 Q51–Q54).
   - Old 7.14 (free energy of dissolution) moved to **9.6** (Unit 9 Q51–Q53).
   - Unit 9 topics 9.6–9.10 renumbered to **9.7–9.11**.
   - Topic titles in Units 1, 2, 3 and 5 renamed to the Fall 2024 wording.
   - Fixed two string-escape bugs in `unit_8.py`: a `\a` in Q10 had become a BEL control character, and a `\t` in Q32 had become a TAB.

2. **`quiz_data/unit_1.py` … `quiz_data/unit_9.py`: per-unit review**
   - Every key was re-derived. Factual and numeric errors were fixed.
   - Items testing CED-excluded content were rewritten in place, keeping the same topic and number.
   - Options were re-ordered where needed for key balance, and numeric options sorted.
   - Letter references in explanations ("Option A") were removed, and markdown `**`/`*` that rendered literally was replaced with HTML.
   - New blind-spot questions were appended under an `Added 2026-10-03` header in each file.
   - **Unit 1 (50 → 60):**
     - Fixed Q4, Q6, Q11, Q28, Q46 and Q47.
     - Rewrote Q9 (Br₂ molecular-ion spectrum, excluded by 1.2) as an Rb-isotope item, and Q35 (photoelectric effect, not in the CED) as Na⁺ vs Ne PES.
     - Q51–Q60 add 4 SVGs: Li mass spectrum, particulate diagrams, Na PES on a log axis, IE₁ vs Z.
     - New EKs covered: estimating from periodicity (1.7.A.3), electronegativity, quantitative Coulomb's law, and group reactivity trends.
   - **Unit 2 (50 → 60):**
     - Fixed Q6 (false key: electronegativity vs ionization energy), Q9, Q22 and Q32; fixed Lewis electron counts in Q36, Q39, Q41 and Q48; fixed Q49.
     - Rewrote Q4 (Fajans' rules) and removed crystal-structure terms from Q17, Q24 and Q27 (2.3 exclusion).
     - Re-ordered options in Q14, Q35, Q37 and Q42.
     - Q51–Q60 add 4 SVGs: HCl and H₂/He₂ potential-energy curves, CsF lattice, Mg electron sea.
   - **Unit 3 (50 → 80):**
     - No wrong keys were found.
     - Fixed data and explanations in Q1 (LDF strength comes from contact area), Q4 (ΔH°vap of COS was given at 25 °C, where COS is a gas), Q10, Q19, Q26, Q34 (Dye A/B/C renamed X/Y/Z), Q38, Q39 and Q49 (Cu²⁺ λmax ≈ 800 nm, not 635 nm). Also fixed the UNIT_META text and the 3.1/3.9/3.12 headers.
     - Rewrote 7 items on excluded topics: Q22 (Graham's law), Q24 (van der Waals constants), Q25 (compressibility factor), Q40 (Henry's law), Q42 (IR functional groups), Q43 (microwave selection rule) and Q45 (photoelectric effect).
     - Keys for Q1–Q50 rebalanced from A15/B26/C8/D1 to A12/B13/C13/D12 by re-ordering 11 items.
     - Q51–Q65 (topics 3.1–3.6) add 6 SVGs: HCl dipole orientations, noncovalent sites in a folded protein, ionic vs metallic layer shift, crystalline vs amorphous solid, P vs T line, KE distributions. They also add real-gas data items.
     - Q66–Q80 (topics 3.7–3.13) add 10 SVGs:
     - acetone–water H-bond
     - particulate dilution
     - TLC plate with ruler
     - pentane/heptane distillation curve
     - NaCl/I₂ in water/hexane layers
     - molecular energy levels
     - EM spectrum
     - to-scale atomic levels
     - Beer–Lambert calibration line plus dilution
     - measuring away from λ_max
   - **Unit 4 (50 → 60):**
     - Fixed Q2 (HCl was limiting, so no CO₂ could form), Q10, Q23, Q34 (impossible conductivity data) and Q42.
     - Rewrote excluded content in Q21 (coordination chemistry / Lewis acids), Q38 (rote solubility rules), Q48 and a Q42 distractor (oxidizing/reducing-agent terms), and Q6/Q8 (precipitate now given or deduced).
     - Re-ordered Q14, Q28 and Q33.
     - Q51–Q60 add 4 SVGs: CaCl₂ dissolution, Pb(NO₃)₂ + KI precipitate, HCl/NaOH titration curve, strong vs weak acid. They also cover a gas-stoichiometry question, a titration-error question and a half-reaction balancing question.
   - **Unit 5 (50 → 60):**
     - Fixed Q40 (wrong slow step in the phosgene mechanism; key now Rate = k[Cl₂]^{3/2}[CO]), Q14, Q46 and Q24.
     - Rewrote Q28 (Arrhenius-plot calculation, 5.6 exclusion) as an SVG energy profile, and Q42 (steady-state derivation) as a pre-equilibrium item.
     - Re-ordered Q8, Q12, Q16 and Q25.
     - Q51–Q60 add 5 SVGs: [A] and ln[A] vs t, collision containers, Maxwell–Boltzmann, two-step profile, enzyme-catalysed profile.
   - **Unit 6 (50 → 60):**
     - Fixed Q5, Q6, Q16 (key 60.0 → 60.9 °C), Q19, Q21, Q31 (data gave −171) and Q36 (391.5 keyed as 391).
     - Rewrote Q5 and Q20 (internal energy / PV work, an excluded distinction) and the Q9/Q10 explanations (state functions, 6.9 exclusion).
     - Fixed the Q40 letter reference.
     - Q51–Q60 add 5 SVGs: endothermic energy diagram, metal/water temperature–time curve, calorimetry extrapolation, cooling curve, bond-enthalpy pathway.
   - **Unit 7 (43 → 60):**
     - Fixed Q3 (³⁷Cl is stable, so the item now uses ³⁶Cl), Q16 (Kp for H₂O(g)), Q18, Q23, Q42, Q24 and Q32.
     - Rewrote Q21 (Kc↔Kp conversion, 7.3 exclusion) as a 7.6.A.4 item.
     - Q44–Q60 add 11 SVGs: rate–time, Q–time, concentration–time, particulate and Ksp-curve figures. Every topic now has at least 4 items.
   - **Unit 8 (54 → 70):**
     - Fixed Q9, Q21 (titration table recomputed), Q31 and Q53.
     - Rewrote Q40, Q43, Q45 and the Q50 explanation (buffer pH-change calculations, 8.9/8.10 exclusion); Q52 and Q54 (solubility as a function of pH, 8.11 exclusion); and Q15 (polyprotic species concentration).
     - Q55–Q70 add 9 SVGs: four titration curves (including diprotic and weak base/strong acid), particulate diagrams, lactic acid, and a CaF₂ solubility-vs-pH graph.
   - **Unit 9 (53 → 60):**
     - Keys rebalanced from A40/B6/C3/D4 to A15/B15/C15/D15.
     - Fixed Q1, Q4, Q9 (ΔS° now −146.4), Q11, Q16, Q19, Q34, Q36, Q38, Q43 and Q52. "Spontaneous" was replaced by "thermodynamically favored" throughout.
     - Rewrote Q18 (organic kinetic vs thermodynamic product) as a CED 9.4 item, replaced a Q33 distractor that relied on +/− electrode labels (9.8 exclusion), and removed "reducing agent" wording from Q38.
     - Q54–Q60 add 3 SVGs: Maxwell–Boltzmann vs T, ΔG° vs T, a Cu/Ag cell driven by a power supply. They also cover a qualitative Nernst / Le Châtelier item and electroplating error analysis.

3. **`quiz_engine.py`**
   - `AP_REFERENCE_SHEET` now mirrors the official *AP Chemistry Equations and Constants (Effective 2025)*:
     - constants, unit conversions, metric prefixes and unit symbols
     - the five official equation sections, each with its legend
   - Added Coulomb's law, the combined gas law, Ka/Kb, pKw = pKa + pKb and I = q/t.
   - Removed items that are not on the 2025 sheet: Graham's law, M₁V₁ = M₂V₂, e, eV, 62.36 L·Torr and kPa.
   - All 103 TeX strings were verified with KaTeX.
   - Every question now gets a stable `uid` (`u{unit}q{n}`) and a content hash `rev`, so saved progress survives renumbering and edits.

4. **`templates/quiz.html`**
   - The subtitle and sidebar show the per-unit question range dynamically.
   - The reference drawer was rebuilt from the new sheet structure: constants table, conversions, prefixes, unit-symbol chips, and equation cards with legends.
   - Topic placeholder now reads "All Unit Topics"; the Question Map range is now `#qgrid-range`; the Unit 3 tip was updated.

5. **`static/css/quiz.css`**
   - Styles for the new reference-sheet blocks (`.ref-subhead`, `.ref-conversion-list`, `.ref-prefix-table`, `.ref-unit-symbols`, `.ref-legend`).
   - Responsive figure styles (`.quiz-figure-wrap`, `.quiz-figure`, figcaption, plus a fallback rule for any inline `<svg>` in the stimulus box), in the gray and white theme.

6. **`static/js/quiz/quiz_app.js`**
   - Progress is now saved under `inorganic_chem_ap_quiz_v2`, keyed by `uid`. Entries whose `rev` no longer matches are dropped, and the legacy v1 key is removed.
   - "Question X of N", the jump list, the Question Map range and the set-count banner now use each unit's real size instead of a hard-coded 50.

7. **`tests/test_quiz_engine.py`** (rewritten), now checking:
   - the 91 Fall 2024 CED topic titles and per-unit counts (60/60/80/60/60/60/60/70/60 = 570)
   - schema, `uid`/`rev`, and sequential numbering
   - per-topic minimums (Unit 3 ≥ 5, others ≥ 4) and answer-key balance (18–32% per letter per unit)
   - no control characters, and no `$` math inside SVG; every SVG has `role="img"` and an `aria-label`
   - the official 2025 reference-sheet content
   - lookups and Flask routes

8. **`README.md`:** quiz description and project layout updated (570 questions, Fall 2024 CED, figures, 2025 equation sheet).

**Verification:**
- `validate_unit.py` passes for all 9 units: exact counts, at least 4 items per topic (Unit 3 at least 5), key balance, KaTeX parse of all math segments, SVG rules, no letter references.
- `final_audit.py`: 570 questions and 0 near-duplicate pairs (token Jaccard ≥ 0.72).
- Every new SVG was rendered (`svg_preview.py`) and inspected by its reviewer. The lead spot-checked about 20 figures and re-derived sample numeric keys.
- `python -m unittest discover -s tests -v`: 13/13 OK.
- Flask test client: `/quiz` returns 200 with 570 questions; units [60, 60, 80, 60, 60, 60, 60, 70, 60]; `/api/quiz/question/570` returns 200 and `/571` returns 404.
- Headless Chrome via CDP rendered Unit 3 Q72, Unit 9 Q58, Unit 8 Q62 and Unit 1 Q57 in Mode 2:
  - each shows "Question N of M (Unit u)", the SVG at 560 px, KaTeX rendered, and no raw `$`
  - the reference drawer shows 103 KaTeX expressions with 0 errors
  - the only console message was a pre-existing favicon 404
- Per-unit review reports and pre-change backups are kept in the session scratch folder.

---

## 2026-10-03 — Google Cloud Run Redeployment with AP Chemistry Quiz (`haren-main` / `us-central1`)

**Request:** "Ok deploy this app /Users/bharen/Documents/Code/schrodinger to the cloud run , refer to specs.md to see previous deployment."

1. **`Dockerfile` (Modified)**
   - Updated the container image build steps to include `quiz_engine.py` (`COPY app.py quantum_engine.py reactions_engine.py quiz_engine.py ./`) and the `quiz_data/` package (`COPY quiz_data ./quiz_data`) alongside `templates/` and `static/`.

2. **Deployment & Verification**
   - Deployed `/Users/bharen/Documents/Code/schrodinger` via Cloud Run MCP (`deploy_local_folder`) to project `haren-main`, region `us-central1`, service `inorganic-chemistry-introduction`.
   - Live Service URL: `https://inorganic-chemistry-introduction-nad4p273qa-uc.a.run.app`

---

## 2026-10-03 — Compact Sticky Site Header (Maximum 10% Viewport Height)

**Request:** "The header of the app is taking up too much space, the header should take maximum 10 percent height of the screen."

1. **`templates/index.html` (Modified)**
   - Moved `.header-controls` (the `Simulation View Mode` and `Real Historical Experiment Selection` segmented controls) out of the sticky `<header class="site-header">` and into a `.workspace-header-bar` at the top of `<section class="simulation-workspace">` inside `<main>`.

2. **`templates/orbitals.html` (Modified)**
   - Moved `.module-tabs-wrap` (`A · Schrödinger Derivation`, `B · 3D Orbital Viewer`, `C · Element Configurations`) out of `<header class="site-header">` and into `<section class="orb-hero">` inside `<main>`.

3. **`static/css/style.css`, `static/css/orbitals.css`, `static/css/theme.css` (Modified)**
   - Constrained `.site-header` and `.header-inner` with `max-block-size: 10vh; max-block-size: 10dvh;` and converted `.header-inner` (`padding-block: 0.38rem; padding-inline: 1.25rem; flex-wrap: nowrap;`) and `.brand-group` into a single-row inline layout (~48–52px tall, ~5–6% of desktop viewport height).
   - Styled `.app-brand` and `.brand-group h1` (`font-size: clamp(0.92rem, 1.15vw, 1.08rem)`) inline with a subtle vertical divider (`::after`), hid `.site-header .badge-era` and `.site-header .subtitle` inside the sticky top bar, and compacted `.page-nav` / `.nav-link` (`padding-block: 0.3rem; font-size: 0.78rem; white-space: nowrap`).
   - Added `.workspace-header-bar` styles in `static/css/style.css` and updated `scroll-padding-block-start: 72px` in `static/css/orbitals.css`.

---

## 2026-10-03 — Single-Line Unit & Section Sub-Bar (`.section-banner`)

**Request:** "The sub bar is also too big, the one attached. Just a single line that mentions the title and has the navigation is enough."

1. **`static/js/quiz/quiz_app.js` (Modified)**
   - Updated `renderUnitBanner()` (`#quiz-unit-banner`) to render only the compact unit badge (`U1`–`U9`), the unit title (`<h2 class="section-banner-title">`), and the horizontal `← Unit` / `Unit →` navigation buttons on a single line.

2. **`static/js/reactions/reactions_app.js` (Modified)**
   - Updated `buildSectionBannerHtml()` (`#section-banner` and `#reaction-section-banner`) to render only the compact section number badge, the section title (`Section N: ...`), and the horizontal `← Section` / `Section →` navigation buttons on a single line.

3. **`static/css/reactions.css` (Modified)**
   - Converted `.section-banner` into a compact single-row flex bar (`padding: 0.5rem 0.9rem 0.55rem 1rem`), shrunk `.section-banner-num` from `88px × 88px` to `30px × 30px`, styled `.section-banner-title` as a single line (`font-size: clamp(1rem, 1.3vw, 1.18rem); white-space: nowrap`), hid `.section-banner-eyebrow`, `.section-banner-desc`, and `.section-banner-meta`, and laid out `.section-banner-nav` horizontally (`flex-direction: row`).

---

## 2026-10-03 — Per-Unit & Per-Mode Quiz Retakes, Live Timers, LocalStorage Attempt History & Past Performance Dashboard

**Request:** "Allow the student to retake the quiz per section and per mode. However save all the statistics in localstorage as attempts. Keep track of time , correct answers. Create a section that shows your past performances in an easy to understand dashboard. Remove reset history button."

1. **`templates/quiz.html` (Modified)**
   - Removed the `↺ Reset History` button (`#btn-reset-progress`) from `.mode-bar-right` and added a `📊 Past Performance` jump button (`#btn-jump-dashboard` with live attempt counter `#nav-attempt-count`).
   - Added live elapsed timer badges (`#batch-timer-badge` / `#batch-timer-val` in Mode 1 and `#single-timer-badge` / `#single-timer-val` in Mode 2) and explicit per-unit, per-mode retake controls (`#btn-retake-unit-batch` "↺ Retake Unit (Mode 1)", `#btn-clear-batch` "↺ Retake This Set", `#btn-save-single-attempt` "✓ Save Attempt", and `#btn-retake-unit-single` "↺ Retake Unit (Mode 2)"), plus an inline `#unit-attempt-strip` showing past attempt statistics for the active unit and mode.
   - Added `<section class="quiz-dashboard-section" id="quiz-performance-dashboard">` featuring 4 KPI summary cards (`#dash-kpi-grid`), a 9-Unit × 2-Mode breakdown grid (`#dash-unit-matrix`) with one-click `↺ Retake Mode 1` and `↺ Retake Mode 2` buttons, and a filterable chronological attempt history table (`#dash-attempts-wrap`, filtered by `#dash-filter-unit` and `#dash-filter-mode`).

2. **`static/js/quiz/quiz_app.js` (Modified)**
   - Added persistent `localStorage` stores for historical attempts (`inorganic_chem_ap_quiz_attempts_v1`) and active per-unit, per-mode sessions (`inorganic_chem_ap_quiz_sessions_v1`).
   - Separated active Mode 1 (`batchByUnitSet`) and Mode 2 (`singleByUnit`) state per unit so students can take and retake any unit in Mode 1 or Mode 2 independently while preserving all prior attempts.
   - Implemented a 1-second active timer engine tracking `elapsedSec` per set in Mode 1 and per unit in Mode 2, recording `durationSec`, `correct`, `answered`, `total`, `pct`, `attemptNumber`, and ISO `timestamp` on every attempt submission or retake.
   - Implemented `renderDashboard()` and `renderUnitAttemptStrip()` to display cumulative accuracy, AP score band estimates, study time/pace per question, per-unit/mode best & average scores, and chronological attempt logs.

3. **`static/css/quiz.css` (Modified)**
   - Added gray-and-white theme styles for `.quiz-timer-badge`, `.unit-attempt-strip`, `.quiz-dashboard-section`, `.dash-kpi-grid`, `.dash-unit-matrix`, `.dash-attempts-table`, `.attempt-mode-badge`, and `.attempt-score-pill`.

4. **`tests/test_quiz_engine.py` (Modified)**
   - Updated `test_flask_quiz_routes` to verify the presence of `quiz-performance-dashboard`, `btn-retake-unit-batch`, and `btn-retake-unit-single`, and the removal of `btn-reset-progress`.

---

## 2026-10-03 — First-Screen Username Prompt, Per-User Data Assignment & Google Cloud Storage (`haren-agent-storage`) Sync

**Request:** "Ask for the user name in the first screen and assign the data to that user. Sync up the data in cloud storage haren-agent-storage , save the data there and once the user logs in with a particular username the data should be retrieved from cloud storage."

1. **`cloud_storage.py` (Created)**
   - Implemented the Google Cloud Storage synchronization engine targeting bucket `haren-agent-storage` (`gs://haren-agent-storage/inorganic-chemistry-introduction/users/<username>.json`):
     - `normalize_username(raw)`: Sanitizes usernames to lowercase alphanumeric characters, underscores, dots, and hyphens (`1–64` characters).
     - `_gcs_read_object(username)` and `_gcs_write_object(username, payload)`: Reads and writes per-user JSON objects in `gs://haren-agent-storage/inorganic-chemistry-introduction/users/<username>.json` using the official `google-cloud-storage` Python SDK (on Cloud Run) or the Google Cloud Storage JSON REST API with OAuth2 bearer tokens from the Metadata Server, Application Default Credentials (`~/.config/gcloud/application_default_credentials.json`), or `gcloud auth print-access-token` (with macOS `/etc/ssl/cert.pem` SSL context support), plus a local mirror under `.user_data_cache/<username>.json`.
     - `merge_user_payloads(base, incoming)`: Non-destructively merges `history`, `attempts` (deduplicated by `id`, sorted chronologically, with sequential `attemptNumber` per `(unitId, mode, scopeKey)`), and active `sessions` (`batchByUnitSet` and `singleByUnit`).
     - `get_user_data(username)` and `save_user_data(username, incoming_payload, merge=True)`: High-level load and save functions.

2. **`app.py`, `Dockerfile`, `requirements.txt`, `.gitignore`, `.dockerignore` (Modified)**
   - Added `GET /api/user/<username>` and `POST /api/user/<username>` in `app.py` to retrieve and persist a user's quiz history, attempts, and active sessions in `gs://haren-agent-storage`.
   - Added `cloud_storage.py` to `Dockerfile`, `google-cloud-storage>=2.14.0,<4` to `requirements.txt`, and `.user_data_cache/` to `.gitignore` and `.dockerignore`.

3. **`static/js/user_sync.js` (Created) & `static/css/theme.css` (Modified)**
   - Prompts the student for their username on the first screen via a native `<dialog id="user-login-dialog">` modal (`showModal()`) whenever no active user is stored in `localStorage` (`inorganic_chem_active_user`), and injects a compact user profile chip (`#btn-switch-user` showing `👤 <username>`, Cloud Storage sync badge `☁️ Synced`, and `Switch User`) into `.site-header .header-inner` across all 4 pages while keeping `.site-header` `<= 10dvh`.
   - Scopes all `localStorage` keys per user (`inorganic_chem_ap_quiz_v2__<username>`, `inorganic_chem_ap_quiz_attempts_v1__<username>`, `inorganic_chem_ap_quiz_sessions_v1__<username>`), migrates any pre-login un-scoped data once, fetches existing user data from `GET /api/user/<username>` (`haren-agent-storage`) upon login, merges and saves back via `POST /api/user/<username>`, and dispatches `inorganic-user-synced`.

4. **`static/js/quiz/quiz_app.js` & `templates/index.html`, `templates/orbitals.html`, `templates/reactions.html`, `templates/quiz.html` (Modified)**
   - Included `static/js/user_sync.js` across all 4 templates.
   - Updated `quiz_app.js` (`loadHistory`, `saveHistory`, `loadAttempts`, `saveAttempts`, `loadSessions`, `saveSessions`) to read/write the active user's scoped keys, automatically push updates to `POST /api/user/<username>` (`haren-agent-storage`) when answers or attempts are saved, and reload all quiz & Past Performance Dashboard data whenever a user logs in or switches usernames (`inorganic-user-synced`).

5. **`tests/test_quiz_engine.py` (Modified)**
   - Added `test_user_cloud_storage_api_and_merge` verifying `user_sync.js` inclusion across all 4 pages and testing `GET /api/user/<username>` and `POST /api/user/<username>` profile retrieval and attempt merging.

6. **Cloud Run Service Account IAM Access & Redeployment to `gs://haren-agent-storage` (`2026-10-03`)**
   - Inspected Cloud Run service `inorganic-chemistry-introduction` (`project=haren-main`, `region=us-central1`), which runs as service account `78833623456-compute@developer.gserviceaccount.com`.
   - Granted `roles/storage.objectAdmin` on bucket `gs://haren-agent-storage` (`us-central1`) to `serviceAccount:78833623456-compute@developer.gserviceaccount.com` via `gcloud storage buckets add-iam-policy-binding gs://haren-agent-storage --member="serviceAccount:78833623456-compute@developer.gserviceaccount.com" --role="roles/storage.objectAdmin" --project=haren-main`.
   - Redeployed `inorganic-chemistry-introduction` to Cloud Run (revision `inorganic-chemistry-introduction-00003-str`, URL: `https://inorganic-chemistry-introduction-nad4p273qa-uc.a.run.app` / `https://inorganic-chemistry-introduction-78833623456.us-central1.run.app`).
   - Verified end-to-end live `POST` and `GET` calls against `https://inorganic-chemistry-introduction-nad4p273qa-uc.a.run.app/api/user/<username>`, confirming `cloud_synced: True`, `cloud_error: None`, and object persistence in `gs://haren-agent-storage/inorganic-chemistry-introduction/users/<username>.json`.

---

## 2026-10-03 — Dedicated Performance Dashboard (`/dashboard`) with SVG Charts & Tables, plus Manual Quiz Timer Start/Pause/Resume & Leave-and-Resume Persistence

**Request:** "The performance dashboard should be its own section, right now its on the quiz page it its too much clutter. Use more graphs and charts and tables instead of current format. Currently when you go to the quiz page the quiz timer starts immediately, make it so that it only starts after the user clicks the start button. Add resume and pause button. If the user leaves the page user should be able to resume from where he left."

1. **`app.py` (Modified)**
   - Added `@app.route("/dashboard")` (`def dashboard():`) rendering `templates/dashboard.html` with `payload`, `units`, `total_units`, and `total_questions`.

2. **`templates/index.html`, `templates/orbitals.html`, `templates/reactions.html`, `templates/quiz.html` (Modified)**
   - Added `<a href="{{ url_for('dashboard') }}" class="nav-link"><span>8</span> Performance Dashboard</a>` to `.page-nav` across all pages.
   - Removed the inline `#quiz-performance-dashboard` section from `templates/quiz.html` so `/quiz` is completely focused on quiz practice without dashboard clutter, and updated `#btn-jump-dashboard` (`📊 Performance Dashboard`) to navigate directly to `/dashboard`.
   - Added explicit timer control groups in both Mode 1 (`#btn-batch-timer-start`, `#btn-batch-timer-pause`, `#btn-batch-timer-resume`, `#batch-timer-state-tag`, `#batch-timer-dot`) and Mode 2 (`#btn-single-timer-start`, `#btn-single-timer-pause`, `#btn-single-timer-resume`, `#single-timer-state-tag`, `#single-timer-dot`), plus `<section class="quiz-timer-gate-banner" id="quiz-timer-gate-banner" hidden aria-live="polite"></section>`.

3. **`templates/dashboard.html`, `static/css/dashboard.css`, `static/js/dashboard/dashboard_app.js` (Created)**
   - Built the dedicated `/dashboard` section (`AP Chemistry Performance & Attempt Analytics Dashboard`) featuring:
     - **5 KPI Summary Cards (`#dash-kpi-grid`)**: Saved Quiz Attempts, Cumulative Accuracy & AP Band, 570-Question Bank Mastery, Active Study Time & Average Pace, and Paused/Resumable Sessions count.
     - **Active & Paused Quiz Sessions Table (`#dash-paused-table-wrap`)**: Lists all in-progress/paused Mode 1 sets and Mode 2 unit sessions with saved question progress (`X / Y`), elapsed time (`MM:SS`), and one-click `▶ Resume Quiz` (`/quiz?unit=X&mode=Y&set=Z&action=resume`) and `↺ Restart Fresh` links.
     - **SVG Line & Area Chart (`#chart-accuracy-trend`)**: Plots chronological attempt accuracy (`0%–100%`) with shaded area, 3-attempt rolling average trend line, and AP Score 4 (`60%`) / AP Score 5 (`75%`) reference lines.
     - **SVG Donut / Ring Chart & Breakdown Table (`#chart-bank-donut`)**: Visualizes the 570-question bank across *Mastered (Correct)*, *Needs Review (Incorrect)*, *In-Progress (Paused)*, and *Unseen Questions*.
     - **SVG Grouped Bar Chart (`#chart-unit-bars`)**: Compares *Mode 1 Best (%)*, *Mode 2 Best (%)*, and *Bank Mastery (%)* across Units 1–9 (`U1`–`U9`).
     - **SVG Horizontal Bar Chart (`#chart-unit-pace`)**: Compares average seconds per question (`s/Q`) across Units 1–9 against the `90s AP Target` vertical reference line.
     - **Complete Units 1–9 & Mode Analytics Table (`#dash-unit-summary-table-wrap`)**: Sticky-header table displaying CED exam weight, question bank progress bar, Mode 1 & Mode 2 attempt counts/best/average/time, AP readiness band, pace, and one-click Open/Resume/Retake actions.
     - **Chronological Attempt History Log Table (`#dash-attempts-table-wrap`)**: Filterable by Unit (`#dash-global-unit-filter`) and Mode (`#dash-global-mode-filter`) with Attempt #, timestamp, unit, mode/set scope, score pill, duration/pace, AP band, and `↺ Retake`.

4. **`static/js/quiz/quiz_app.js`, `static/css/quiz.css`, `static/js/user_sync.js`, `cloud_storage.py` (Modified)**
   - Updated quiz session state (`getBatchSession`, `getSingleSession`) to track `timerState` (`"not_started"` | `"running"` | `"paused"` | `"completed"`), `updatedAt`, and `sessions.lastLocation` (`{ mode, unitId, batchSetIndex, updatedAt }`).
   - Changed the 1-second timer interval so `elapsedSec` **never** starts ticking automatically on page load or unit/mode/set switch; it only increments after the student clicks **`▶ Start Quiz`** (`startOrResumeActiveTimer()`).
   - Added **`⏸ Pause`** (`pauseActiveTimer()`) and **`▶ Resume`** (`startOrResumeActiveTimer()`) controls in both Mode 1 and Mode 2 toolbars as well as in `#quiz-timer-gate-banner`.
   - Locked unrevealed multiple-choice options while the timer is `"not_started"` or `"paused"`, prompting the student to click **`▶ Start Quiz`** or **`▶ Resume Quiz`** first.
   - Added `pagehide`, `beforeunload`, and `visibilitychange` listeners (`pauseAllRunningSessions(true)`) and `saveSessions()` logic that automatically pauses any running timer and saves `lastLocation`, `elapsedSec`, `answers`, and `singleIndex` to `localStorage` and Cloud Storage (`haren-agent-storage`) whenever the user leaves `/quiz`.
   - Added `applyInitialRouteAndResume()` and `findMostRecentResumableLocation()` so returning to `/quiz` (or clicking `▶ Resume` from `/dashboard`) automatically restores the exact unit, mode, set, question position, answers, and elapsed time in the `"paused"` state ready to resume.

5. **`tests/test_quiz_engine.py` (Modified)**
   - Updated `test_flask_quiz_routes` and `test_user_cloud_storage_api_and_merge` to verify `/dashboard` charts and tables, the removal of inline `#quiz-performance-dashboard` from `/quiz`, the presence of Start/Pause/Resume timer controls on `/quiz`, and `lastLocation` persistence across user profile syncs.

6. **`templates/dashboard.html`, `static/css/theme.css`, `static/js/dashboard/dashboard_app.js` (Header & Storage Key Alignment Fix — `2026-10-03`)**
   - Included `static/css/reactions.css`, `static/css/quiz.css`, and `static/css/theme.css` in `templates/dashboard.html` and matched the `.site-header > .header-inner > .brand-group` + `.page-nav` structure used by `templates/quiz.html` so the compact `<= 10dvh` header, gray-and-white theme controls, and `.user-header-chip` render cleanly without overflow.
   - Aligned `static/js/dashboard/dashboard_app.js` storage keys (`inorganic_chem_ap_quiz_v2`, `inorganic_chem_ap_quiz_attempts_v1`, `inorganic_chem_ap_quiz_sessions_v1` via `window.InorganicUserSync`) and `Q_BY_UID` answer deserialization with `static/js/quiz/quiz_app.js`.

---

## 2026-10-03 — Replacement of All Top Headers with a Retractable Left Sidebar Navigation

**Request:** "Replace all the header sections with a retractable side bar."

1. **`templates/index.html`, `templates/orbitals.html`, `templates/reactions.html`, `templates/quiz.html`, `templates/dashboard.html` (Modified)**
   - Replaced `<header class="site-header">...</header>` across all 5 application pages with `<aside class="site-sidebar" id="site-sidebar" aria-label="Application Sidebar Navigation">`:
     - **`.sidebar-top`**: Contains the `.sidebar-brand` (`IC` monogram badge + `Inorganic Chemistry` title + `AP & Quantum Lab` subtitle) and the `#btn-toggle-sidebar` (`«` / `»`) retract/expand button (`title="Retract / Expand Sidebar (Ctrl+B)"`).
     - **`.sidebar-page-context`**: Displays the current page's `.badge-era`, `<h1>` heading, and `<p class="subtitle">` when the sidebar is expanded.
     - **`<nav class="page-nav" aria-label="Sections">`**: Vertical navigation rail with numbered section badges (`01`–`05`) and full labels for *Rutherford & Thomson Experiments* (`/`), *Atomic Orbitals & Quantum Mechanics* (`/orbitals`), *Essential Chemical Reactions* (`/reactions`), *AP Chemistry Quiz* (`/quiz`), and *Performance Dashboard* (`/dashboard`).
     - **`<div class="sidebar-footer" id="sidebar-user-mount"></div>`**: Dedicated bottom footer mount for the student username and Cloud Storage (`haren-agent-storage`) sync chip.

2. **`static/js/user_sync.js` (Modified)**
   - Added `SIDEBAR_COLLAPSED_KEY = "inorganic_chem_sidebar_collapsed"`, `applySidebarCollapsedState(isCollapsed)`, `loadSidebarCollapsedState()`, and `initRetractableSidebar()` to persist the retracted/expanded state across page loads, toggle `sidebar-collapsed` on `document.documentElement` and `document.body` via `#btn-toggle-sidebar` or `Ctrl+B`/`Cmd+B`, update `aria-expanded` and `.sidebar-toggle-icon` (`«` vs `»`), and dispatch `window.resize` events so HTML5/WebGL canvases resize automatically.
   - Updated `injectHeaderUserChip()` to mount `#header-user-bar` inside `#sidebar-user-mount` at the bottom of `.site-sidebar`.

3. **`static/css/style.css`, `static/css/theme.css`, `static/css/orbitals.css` (Modified)**
   - Defined `:root { --sidebar-width: 260px; }` and `html.sidebar-collapsed, body.sidebar-collapsed { --sidebar-width: 60px; }` with `body { padding-inline-start: var(--sidebar-width, 260px); transition: padding-inline-start 0.2s ease; }`.
   - Styled the gray-and-white `.site-sidebar` in both **Expanded (`260px`)** and **Retracted (`60px` compact icon/badge rail)** states, hiding text labels and centering the `IC` brand mark, `01`–`05` badges, and `👤` user profile chip when retracted.
   - Updated `scroll-padding-block-start` in `static/css/orbitals.css` from `72px` to `16px`.

4. **`tests/test_quiz_engine.py` (Modified)**
   - Added `test_all_pages_render_retractable_sidebar` verifying that all 5 routes (`/`, `/orbitals`, `/reactions`, `/quiz`, `/dashboard`) render `.site-sidebar`, `#btn-toggle-sidebar`, and `#sidebar-user-mount` and contain no legacy `<header class="site-header">`.

---

## 2026-10-03 — Sidebar Submenus (`Chemistry Topics` & `AP Chemistry Quiz` Units 1–9), Atom SVG Brand, Compact `AP Chemistry` Top Header with Lab Equipment SVGs, and Default Instant Feedback Mode with `Timed Mode` Toggle

**Request:**
1. Remove the `.sidebar-page-context` text block (`COLLEGE BOARD AP CHEMISTRY CED...`) from the sidebar top.
2. Put `01 Rutherford & Thomson Experiments`, `02 Atomic Orbitals & Quantum Mechanics`, and `03 Essential Chemical Reactions` as sub-topics under main `Chemistry Topics` in the sidebar.
3. Put all 9 AP Chemistry Quiz units (`U1`–`U9`) as a submenu under `AP Chemistry Quiz` in the sidebar, and remove the quiz units sidebar from the main central area on `/quiz`.
4. Inside `/quiz`, remove the top mode bar, make **Instant Feedback** mode (`single`) the default, and add a **`Timed Mode`** button (`#btn-toggle-timed-mode`) that toggles to the timed batch quiz mode (`batch`) and allows reverting back to Instant Feedback mode at any time (`#btn-toggle-timed-mode` / `#btn-revert-instant-mode`).
5. Keep a compact top header (`<= 10%` viewport height) with **`AP Chemistry`** as the App Title and a row of chemistry laboratory equipment and atomic SVGs (Atom, Test Tube, Erlenmeyer Flask, Graduated Beaker, Bunsen Burner, Florence Boiling Flask, Volumetric Burette, Test Tube Rack, Benzene Ring).
6. Remove `Inorganic Chemistry / AP & Quantum Lab` from the sidebar top and replace it with an SVG image of an atom (`.sidebar-atom-svg`: nucleus with 3 intersecting elliptical orbits and orbiting electrons).

### Exact Changes Made by File

1. **`app.py` (Modified)**
   - Added `@app.context_processor` (`inject_navigation_units()`) so `nav_units` (all 9 official AP Chemistry units) is injected into every page template for the global sidebar submenu.

2. **`templates/_chrome.html` (Created) & `templates/index.html`, `templates/orbitals.html`, `templates/reactions.html`, `templates/quiz.html`, `templates/dashboard.html` (Modified)**
   - Created `templates/_chrome.html` and included it across all 5 templates:
     - **Sidebar Top (`.sidebar-top`)**: Replaced `[Inorganic Chemistry AP & Quantum Lab]` with `.sidebar-atom-svg` (central proton/neutron nucleus cluster with 3 intersecting elliptical orbits and electrons) alongside `#btn-toggle-sidebar`.
     - **Removed `.sidebar-page-context`** text block from the sidebar.
     - **`Chemistry Topics` Group (`#sidebar-group-topics`)**: Collapsible `<details open>` group containing sub-topic links `01 Rutherford & Thomson Experiments` (`/`), `02 Atomic Orbitals & Quantum Mechanics` (`/orbitals`), and `03 Essential Chemical Reactions` (`/reactions`).
     - **`AP Chemistry Quiz` Group (`#sidebar-group-quiz`)**: Collapsible `<details open>` group containing `#quiz-unit-sidebar` with all 9 AP Chemistry units (`U1`–`U9`), linking directly to `#/unit/<id>` on `/quiz` or `/quiz?unit=<id>` from other pages.
     - **`05 Performance Dashboard`**: Top-level link to `/dashboard`.
     - **Compact Top Header (`<header class="site-header" id="site-header">`, `block-size: 54px; max-block-size: 10dvh`)**: Displays the **`AP Chemistry`** app title and `.header-lab-svgs` containing 9 vector SVGs (Atom, Test Tube, Erlenmeyer Flask, Graduated Beaker, Bunsen Burner, Round-Bottom Florence Flask, Titration Burette, Test Tube Rack, and Molecular Benzene Ring).

3. **`templates/quiz.html`, `static/js/quiz/quiz_app.js`, `static/css/quiz.css`, `static/css/theme.css` (Modified)**
   - Removed `<section class="quiz-mode-bar">` and `<aside class="catalog-sidebar quiz-sidebar">` from `templates/quiz.html`, making `.quiz-layout-single-col` full-width in the central area.
   - Changed default `state.mode` in `static/js/quiz/quiz_app.js` to `"single"` (**Instant Feedback Mode**) and made `#single-controls-panel` visible by default.
   - Added `#btn-toggle-timed-mode` (`⏱ Timed Mode` ↔ `← Instant Feedback Mode`) in `.quiz-filters-row` and `#btn-revert-instant-mode` (`← Instant Feedback Mode`) in `#batch-controls-panel` so students can switch to Timed Mode (`batch`) and revert to Instant Feedback Mode (`single`) at any time.
   - Added click handling on `#quiz-unit-sidebar` in `static/js/quiz/quiz_app.js` to switch units in-place when on `/quiz`.

4. **`tests/test_quiz_engine.py` (Modified)**
   - Updated `test_flask_quiz_routes` and `test_all_pages_render_retractable_sidebar` to verify all 6 requirements across all 5 routes.

