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
