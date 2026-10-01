# Inorganic Chemistry: Introduction

An interactive Flask web app for high-school (AP/IB) and first-year university chemistry.

## Sections

| Page | Route | What it contains |
|------|-------|------------------|
| Rutherford & Thomson Experiments | `/` | Animated Rutherford gold-foil scattering (with schematic diagram and histogram) and Thomson's cathode-ray tube experiment. |
| Atomic Orbitals & Quantum Mechanics | `/orbitals` | Step-by-step Schrödinger derivation for hydrogen-like atoms, interactive 3D s/p/d/f orbital viewer (Three.js), and an element-configuration engine for Z = 1–118. |
| Essential Chemical Reactions | `/reactions` | 206 reactions in 12 sections, each section in its own view; each reaction opens a dedicated view with an animated lab-instrument simulation, all equations (molecular, ionic, half-reactions), explanation and chemical specimen images. |

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5000>.

## Tests

```bash
python -m unittest discover -s tests -v
```

## Project layout

```
app.py               Flask routes + JSON APIs
quantum_engine.py    Hydrogen-like wavefunctions, quantum numbers, electron configurations
reactions_engine.py  Reaction catalogue (equations, explanations, chemicals, lab metadata)
templates/           Jinja2 pages (index, orbitals, reactions)
static/css/          Styles (gray & white theme in theme.css)
static/js/           Canvas / Three.js animations and page logic
tests/               Unit tests
specs.md             Dated change log
```

KaTeX and Three.js are loaded from the jsDelivr CDN, so an internet connection is needed for equation rendering and the 3D orbital viewer.
