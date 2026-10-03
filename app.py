"""
Inorganic Chemistry: Introduction — Flask web application featuring:
1. Rutherford's Gold Leaf Scattering & Thomson's Cathode Ray Experiments
2. Atomic Orbitals & Quantum Mechanics (Schrödinger equation, 3D viewer, Z=1–118)
3. Essential Chemical & Ionic Equations (206 reactions across 12 sections with lab simulator)
4. AP Chemistry Practice & Exam Quiz (450 exam-level questions across Units 1–9 with 2 practice modes)
"""

import math
import os
from flask import Flask, jsonify, render_template, request

import cloud_storage
import quantum_engine
import quiz_engine
import reactions_engine

app = Flask(__name__)

# Physical constants in SI / atomic units for Rutherford scattering calculations
COULOMB_KE2_MEV_FM = 1.4399645  # e^2 / (4 * pi * epsilon_0) in MeV * fm
Z_ALPHA = 2  # Helium-4 nucleus charge (+2e)

TARGET_ELEMENTS = {
    "Au": {"name": "Gold (Au)", "symbol": "Au", "Z": 79, "mass_number": 197, "color": "#f5c542"},
    "Ag": {"name": "Silver (Ag)", "symbol": "Ag", "Z": 47, "mass_number": 108, "color": "#cbd5e1"},
    "Cu": {"name": "Copper (Cu)", "symbol": "Cu", "Z": 29, "mass_number": 63, "color": "#e07a5f"},
    "Al": {"name": "Aluminum (Al)", "symbol": "Al", "Z": 13, "mass_number": 27, "color": "#94a3b8"},
}

EXPERIMENT_PARTS = [
    {
        "id": "alpha_source",
        "number": 1,
        "name": "Radioactive Alpha (α) Source",
        "short_label": "α-Particle Source (Ra/Rn)",
        "category": "Source & Collimation",
        "description": (
            "A sample of radium (Ra) or radon (Rn) that spontaneously emits high-energy "
            "alpha particles (He²⁺ nuclei, consisting of 2 protons and 2 neutrons) "
            "traveling at ~1.5 × 10⁷ m/s (~5% the speed of light, ~5.5 MeV)."
        ),
    },
    {
        "id": "lead_shield",
        "number": 2,
        "name": "Lead Block Containment Shield",
        "short_label": "Lead Block Shield",
        "category": "Source & Collimation",
        "description": (
            "A thick lead enclosure that absorbs alpha and gamma radiation in all directions "
            "except through a narrow exit channel, protecting the detector from stray particles."
        ),
    },
    {
        "id": "collimator",
        "number": 3,
        "name": "Lead Collimator Slit (Diaphragm)",
        "short_label": "Lead Collimator Slit",
        "category": "Source & Collimation",
        "description": (
            "A narrow aperture in a lead plate that filters out diverging alpha particles, "
            "producing a tightly focused, parallel pencil beam aimed directly at the gold foil."
        ),
    },
    {
        "id": "alpha_beam",
        "number": 4,
        "name": "Incident Alpha Particle Beam (He²⁺)",
        "short_label": "Incident α-Beam",
        "category": "Beam & Trajectories",
        "description": (
            "A collimated stream of positively charged helium nuclei (+2e) directed toward "
            "the center of the gold leaf target."
        ),
    },
    {
        "id": "gold_foil",
        "number": 5,
        "name": "Ultra-Thin Gold Leaf (Au Foil)",
        "short_label": "Gold Leaf (~0.4 μm)",
        "category": "Target",
        "description": (
            "Malleable gold hammered to an extreme thinness of ~4 × 10⁻⁵ cm (~400 nm, "
            "or ~1,000 atoms thick) so alpha particles pass through without being completely stopped."
        ),
    },
    {
        "id": "zns_screen",
        "number": 6,
        "name": "Circular Zinc Sulfide (ZnS) Fluorescent Screen",
        "short_label": "ZnS Fluorescent Screen",
        "category": "Detection System",
        "description": (
            "A nearly 360° circular ring coated with zinc sulfide (ZnS). Each time an alpha "
            "particle strikes the coating, it produces a tiny, brief flash of light (scintillation)."
        ),
    },
    {
        "id": "microscope",
        "number": 7,
        "name": "Rotatable Viewing Microscope",
        "short_label": "Rotatable Microscope",
        "category": "Detection System",
        "description": (
            "A low-power microscope attached to a rotatable mount outside the screen, allowing "
            "Geiger and Marsden to count scintillation flashes at any scattering angle θ."
        ),
    },
    {
        "id": "vacuum_chamber",
        "number": 8,
        "name": "Evacuated Vacuum Chamber",
        "short_label": "Vacuum Chamber",
        "category": "Apparatus Housing",
        "description": (
            "An airtight chamber pumped free of air. Without a vacuum, alpha particles would "
            "collide with nitrogen and oxygen molecules and lose energy within a few centimeters."
        ),
    },
    {
        "id": "undeflected_beam",
        "number": 9,
        "name": "Undeflected Alpha Particles (θ ≈ 0°)",
        "short_label": "Undeflected (>99%)",
        "category": "Beam & Trajectories",
        "description": (
            "Over 99% of alpha particles pass straight through the gold foil with virtually no "
            "deflection, proving that the atom is mostly empty space."
        ),
    },
    {
        "id": "small_deflection",
        "number": 10,
        "name": "Small-Angle Deflected Particles (1° < θ < 90°)",
        "short_label": "Small Deflection",
        "category": "Beam & Trajectories",
        "description": (
            "A small fraction of alpha particles pass moderately close to a positively charged "
            "gold nucleus and experience electrostatic (Coulomb) repulsion, deflecting by a few degrees."
        ),
    },
    {
        "id": "large_deflection",
        "number": 11,
        "name": "Large-Angle / Backscattered Particles (θ > 90°)",
        "short_label": "Backscattered (~1 in 8,000)",
        "category": "Beam & Trajectories",
        "description": (
            "About 1 in 8,000 alpha particles make a nearly head-on approach to the massive, "
            "compact +79e gold nucleus and rebound backward at angles greater than 90° (up to ~180°)."
        ),
    },
]


def compute_rutherford_scattering(z_target: int, energy_mev: float, impact_param_fm: float) -> dict:
    """
    Calculate exact classical Rutherford scattering parameters for an alpha particle
    incident on a target nucleus of atomic number z_target.
    """
    energy_mev = max(0.5, min(20.0, energy_mev))
    # Distance of closest approach in a head-on collision (b = 0):
    # d_0 = (Z_alpha * Z_target * e^2) / (4 * pi * epsilon_0 * E_alpha)
    d0_fm = (Z_ALPHA * z_target * COULOMB_KE2_MEV_FM) / energy_mev

    # Scattering angle: tan(theta / 2) = d0 / (2 * b)
    if abs(impact_param_fm) < 1e-6:
        theta_rad = math.pi
    else:
        theta_rad = 2.0 * math.atan(d0_fm / (2.0 * abs(impact_param_fm)))

    theta_deg = math.degrees(theta_rad)

    # Actual distance of closest approach for arbitrary impact parameter b:
    # r_min = (d0 / 2) * (1 + csc(theta / 2))
    sin_half = math.sin(theta_rad / 2.0)
    if sin_half > 1e-6:
        r_min_fm = (d0_fm / 2.0) * (1.0 + 1.0 / sin_half)
    else:
        r_min_fm = abs(impact_param_fm)

    # Relative differential cross-section factor: 1 / sin^4(theta / 2)
    cross_section_factor = 1.0 / max(sin_half ** 4, 1e-8)

    return {
        "z_target": z_target,
        "energy_mev": round(energy_mev, 2),
        "impact_parameter_fm": round(impact_param_fm, 2),
        "head_on_closest_approach_fm": round(d0_fm, 2),
        "actual_closest_approach_fm": round(r_min_fm, 2),
        "scattering_angle_deg": round(theta_deg, 2),
        "scattering_angle_rad": round(theta_rad, 4),
        "relative_cross_section": round(cross_section_factor, 4),
    }


@app.context_processor
def inject_navigation_units():
    """Provide the 9 AP Chemistry units to the global sidebar navigation across all pages."""
    payload = quiz_engine.get_all_payload()
    return {
        "nav_units": payload["units"],
    }


@app.route("/")
def index():
    """Render the interactive Rutherford Gold Leaf Experiment web application."""
    return render_template(
        "index.html",
        parts=EXPERIMENT_PARTS,
        targets=TARGET_ELEMENTS,
        active_page="index",
    )


@app.route("/api/experiment-info", methods=["GET"])
def experiment_info():
    """Return metadata for labeled parts and target materials."""
    return jsonify({
        "parts": EXPERIMENT_PARTS,
        "targets": TARGET_ELEMENTS,
    })


@app.route("/api/scattering", methods=["POST"])
def api_scattering():
    """Calculate Rutherford scattering metrics for given target Z, energy, and impact parameter."""
    data = request.get_json(silent=True) or {}
    target_key = data.get("target", "Au")
    target = TARGET_ELEMENTS.get(target_key, TARGET_ELEMENTS["Au"])
    energy_mev = float(data.get("energy_mev", 5.5))
    impact_param_fm = float(data.get("impact_parameter_fm", 25.0))

    result = compute_rutherford_scattering(
        z_target=target["Z"],
        energy_mev=energy_mev,
        impact_param_fm=impact_param_fm,
    )
    result["target_name"] = target["name"]
    result["target_symbol"] = target["symbol"]
    return jsonify(result)


@app.route("/orbitals")
def orbitals():
    """Render the Atomic Orbitals & Quantum Mechanics section (Modules A, B, C)."""
    return render_template(
        "orbitals.html",
        elements=quantum_engine.all_elements(),
        madelung=quantum_engine.madelung_sequence(),
    )


@app.route("/api/elements", methods=["GET"])
def api_elements():
    """Return periodic-table metadata for Z = 1..118 plus the Madelung sequence."""
    return jsonify({
        "elements": quantum_engine.all_elements(),
        "madelung_order": quantum_engine.madelung_sequence(),
    })


@app.route("/api/element/<int:z>", methods=["GET"])
def api_element(z: int):
    """Return the ground-state electron configuration and orbital-box data for element Z."""
    if not 1 <= z <= 118:
        return jsonify({"error": "Atomic number must be between 1 and 118"}), 404
    return jsonify(quantum_engine.element_details(z))


@app.route("/reactions")
def reactions():
    """Render the Essential Chemical & Ionic Equations section with Virtual Lab Simulator."""
    payload = reactions_engine.get_all_payload()
    return render_template(
        "reactions.html",
        payload=payload,
        categories=payload["categories"],
        total_reactions=payload["total_reactions"],
        spec_reactions=payload["spec_reactions"],
        added_reactions=payload["added_reactions"],
        canonical_summary=payload["canonical_summary"],
    )


@app.route("/api/reactions", methods=["GET"])
def api_reactions():
    """Return all 206 categorized chemical reactions, chemical specimens, and summary table."""
    return jsonify(reactions_engine.get_all_payload())


@app.route("/api/reaction/<int:rxn_id>", methods=["GET"])
def api_reaction(rxn_id: int):
    """Return a single chemical reaction with resolved chemical specimens and lab apparatus metadata."""
    rxn = reactions_engine.get_reaction_by_id(rxn_id)
    if rxn is None:
        return jsonify({"error": f"Reaction {rxn_id} not found"}), 404
    return jsonify(rxn)


@app.route("/quiz")
def quiz():
    """Render the AP Chemistry Practice & Exam Quiz section (Units 1–9, 570 questions)."""
    payload = quiz_engine.get_all_payload()
    return render_template(
        "quiz.html",
        payload=payload,
        units=payload["units"],
        total_units=payload["total_units"],
        total_questions=payload["total_questions"],
        reference_sheet=payload["reference_sheet"],
    )


@app.route("/dashboard")
def dashboard():
    """Render the dedicated AP Chemistry Performance & Analytics Dashboard section."""
    payload = quiz_engine.get_all_payload()
    return render_template(
        "dashboard.html",
        payload=payload,
        units=payload["units"],
        total_units=payload["total_units"],
        total_questions=payload["total_questions"],
    )



@app.route("/api/quiz/units", methods=["GET"])
def api_quiz_units():
    """Return metadata for all 9 AP Chemistry units."""
    payload = quiz_engine.get_all_payload()
    return jsonify({
        "total_units": payload["total_units"],
        "total_questions": payload["total_questions"],
        "units": payload["units"],
    })


@app.route("/api/quiz/unit/<int:unit_id>", methods=["GET"])
def api_quiz_unit(unit_id: int):
    """Return metadata and all 50 practice questions for a specific AP Chemistry unit (1..9)."""
    unit_data = quiz_engine.get_unit_by_id(unit_id)
    if unit_data is None:
        return jsonify({"error": f"AP Chemistry Unit {unit_id} not found (must be 1–9)"}), 404
    return jsonify(unit_data)


@app.route("/api/quiz/question/<int:q_id>", methods=["GET"])
def api_quiz_question(q_id: int):
    """Return a single enriched AP Chemistry question by global ID (1..450)."""
    q = quiz_engine.get_question_by_id(q_id)
    if q is None:
        return jsonify({"error": f"Question {q_id} not found"}), 404
    return jsonify(q)


@app.route("/api/user/<username>", methods=["GET"])
def api_get_user_data(username: str):
    """Retrieve a user's saved quiz progress and attempt history from Cloud Storage (haren-agent-storage)."""
    norm = cloud_storage.normalize_username(username)
    if not norm:
        return jsonify({"error": "Invalid username. Please enter 1–64 letters, numbers, or hyphens."}), 400
    try:
        result = cloud_storage.get_user_data(username)
        return jsonify(result)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


@app.route("/api/user/<username>", methods=["POST"])
def api_save_user_data(username: str):
    """Save and sync a user's quiz progress and attempt history to Cloud Storage (haren-agent-storage)."""
    norm = cloud_storage.normalize_username(username)
    if not norm:
        return jsonify({"error": "Invalid username. Please enter 1–64 letters, numbers, or hyphens."}), 400
    payload = request.get_json(silent=True) or {}
    merge = bool(payload.get("merge", True))
    try:
        result = cloud_storage.save_user_data(username, payload, merge=merge)
        return jsonify(result)
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    host = os.environ.get("HOST", "0.0.0.0" if "PORT" in os.environ else "127.0.0.1")
    debug = os.environ.get("FLASK_DEBUG", "0" if "PORT" in os.environ else "1") == "1"
    app.run(host=host, port=port, debug=debug)


