"""
AP Chemistry Practice & Exam Quiz Engine
========================================
Organizes AP Exam-level multiple-choice questions across all 9 College Board
AP Chemistry units, aligned to the AP Chemistry Course and Exam Description
(CED) effective Fall 2024 (units/topics/titles as in the official CED), served in
sets of 10 questions, plus the official "AP Chemistry Equations and Constants,
Effective 2025" reference sheet.

Question counts are not fixed: each unit file in ``quiz_data`` may hold any number
of questions; counts, topic tallies and set counts are derived at load time.
"""

from __future__ import annotations

import hashlib
import importlib
from typing import Any

OPTION_LETTERS = ("A", "B", "C", "D")

# Mirrors the official College Board sheet "AP Chemistry Equations and Constants,
# Effective 2025" (CED Appendix, pp. 228-229). Do not add relations that are not on
# the official sheet (questions must supply any other relation in the stem).
AP_REFERENCE_SHEET = {
    "title": "AP Chemistry Equations and Constants, Effective 2025",
    "constants": [
        {"symbol": r"h", "name": "Planck's constant", "value": r"6.626 \times 10^{-34}\text{ J s}"},
        {"symbol": r"c", "name": "Speed of light", "value": r"2.998 \times 10^{8}\text{ m s}^{-1}"},
        {"symbol": r"N_A", "name": "Avogadro's number", "value": r"6.022 \times 10^{23}\text{ mol}^{-1}"},
        {"symbol": r"R", "name": "Gas constant",
         "value": r"8.314\text{ J mol}^{-1}\text{ K}^{-1} = 0.08206\text{ L atm K}^{-1}\text{ mol}^{-1}"},
        {"symbol": r"F", "name": "Faraday's constant", "value": r"96{,}485\text{ coulombs / 1 mol } e^-"},
        {"symbol": r"\text{STP}", "name": "Standard temperature and pressure", "value": r"273.15\text{ K and } 1.0\text{ atm}"},
        {"symbol": r"\text{STP}", "name": "Ideal gas at STP", "value": r"22.4\text{ L mol}^{-1}"},
    ],
    "unit_conversions": [
        r"1\text{ hertz} = 1\text{ s}^{-1}",
        r"1\text{ atm} = 760\text{ mm Hg} = 760\text{ torr}",
        r"\text{K} = {}^\circ\text{C} + 273.15",
        r"1\text{ volt} = \dfrac{1\text{ joule}}{1\text{ coulomb}}",
        r"1\text{ ampere} = \dfrac{1\text{ coulomb}}{1\text{ second}}",
    ],
    "metric_prefixes": [
        {"factor": r"10^{9}", "prefix": "giga", "symbol": "G"},
        {"factor": r"10^{6}", "prefix": "mega", "symbol": "M"},
        {"factor": r"10^{3}", "prefix": "kilo", "symbol": "k"},
        {"factor": r"10^{-2}", "prefix": "centi", "symbol": "c"},
        {"factor": r"10^{-3}", "prefix": "milli", "symbol": "m"},
        {"factor": r"10^{-6}", "prefix": "micro", "symbol": "μ"},
        {"factor": r"10^{-9}", "prefix": "nano", "symbol": "n"},
        {"factor": r"10^{-12}", "prefix": "pico", "symbol": "p"},
    ],
    "unit_symbols": [
        ("gram", "g"), ("mole", "mol"), ("liter", "L"), ("meter", "m"), ("second", "s"), ("hertz", "Hz"),
        ("atmosphere", "atm"), ("millimeter of mercury", "mm Hg"), ("degree Celsius", "°C"), ("kelvin", "K"),
        ("joule", "J"), ("volt", "V"), ("coulomb", "C"), ("ampere", "A"),
    ],
    "equations": [
        {
            "category": "Atomic Structure",
            "items": [
                r"E = h\nu",
                r"c = \lambda\nu",
                r"F_{\text{coulombic}} \propto \dfrac{q_1 q_2}{r^2}",
            ],
            "legend": [
                (r"E", "energy"), (r"\nu", "frequency"), (r"\lambda", "wavelength"),
                (r"F", "force"), (r"q", "charge"), (r"r", "separation"),
            ],
        },
        {
            "category": "Gases, Liquids, and Solutions",
            "items": [
                r"\dfrac{P_1V_1}{T_1} = \dfrac{P_2V_2}{T_2}",
                r"PV = nRT",
                r"P_A = P_{\text{total}} \times X_A,\ \text{where } X_A = \dfrac{\text{moles A}}{\text{total moles}}",
                r"P_{\text{total}} = P_A + P_B + P_C + \dots",
                r"n = \dfrac{m}{\boldsymbol{M}}",
                r"D = \dfrac{m}{V}",
                r"KE = \tfrac{1}{2}mv^2",
                r"M = \dfrac{n_{\text{solute}}}{\text{L}_{\text{solution}}}",
                r"A = \varepsilon b c",
            ],
            "legend": [
                (r"P", "pressure"), (r"V", "volume"), (r"T", "temperature"), (r"n", "number of moles"),
                (r"X", "mole fraction"), (r"m", "mass"), (r"\boldsymbol{M}", "molar mass"), (r"D", "density"),
                (r"KE", "kinetic energy"), (r"v", "velocity"), (r"M", "molarity"), (r"A", "absorbance"),
                (r"\varepsilon", "molar absorptivity"), (r"b", "path length"), (r"c", "concentration"),
            ],
        },
        {
            "category": "Kinetics",
            "items": [
                r"[\text{A}]_t - [\text{A}]_0 = -kt",
                r"\ln[\text{A}]_t - \ln[\text{A}]_0 = -kt",
                r"\dfrac{1}{[\text{A}]_t} - \dfrac{1}{[\text{A}]_0} = kt",
                r"t_{1/2} = \dfrac{0.693}{k}",
            ],
            "legend": [(r"k", "rate constant"), (r"t", "time"), (r"t_{1/2}", "half-life")],
        },
        {
            "category": "Equilibrium",
            "items": [
                r"K_c = \dfrac{[\text{C}]^c[\text{D}]^d}{[\text{A}]^a[\text{B}]^b},\ \text{where } a\,\text{A} + b\,\text{B} \rightleftarrows c\,\text{C} + d\,\text{D}",
                r"K_p = \dfrac{(P_{\text{C}})^c(P_{\text{D}})^d}{(P_{\text{A}})^a(P_{\text{B}})^b}",
                r"K_w = [\text{H}_3\text{O}^+][\text{OH}^-] = 1.0 \times 10^{-14}\text{ at }25^\circ\text{C}",
                r"\text{p}K_w = 14 = \text{pH} + \text{pOH}\text{ at }25^\circ\text{C}",
                r"\text{pH} = -\log[\text{H}_3\text{O}^+],\quad \text{pOH} = -\log[\text{OH}^-]",
                r"K_a = \dfrac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]},\quad K_b = \dfrac{[\text{OH}^-][\text{HB}^+]}{[\text{B}]}",
                r"\text{p}K_a = -\log K_a,\quad \text{p}K_b = -\log K_b",
                r"K_w = K_a \times K_b,\quad \text{p}K_w = \text{p}K_a + \text{p}K_b",
                r"\text{pH} = \text{p}K_a + \log\dfrac{[\text{A}^-]}{[\text{HA}]}",
            ],
            "legend": [
                (r"K_c", "molar concentrations"), (r"K_p", "gas pressures"), (r"K_w", "water"),
                (r"K_a", "acid"), (r"K_b", "base"),
            ],
        },
        {
            "category": "Thermodynamics / Electrochemistry",
            "items": [
                r"q = mc\Delta T",
                r"\Delta H^\circ_{\text{reaction}} = \textstyle\sum \Delta H^\circ_{f\ \text{products}} - \sum \Delta H^\circ_{f\ \text{reactants}}",
                r"\Delta S^\circ_{\text{reaction}} = \textstyle\sum S^\circ_{\text{products}} - \sum S^\circ_{\text{reactants}}",
                r"\Delta G^\circ_{\text{reaction}} = \textstyle\sum \Delta G^\circ_{f\ \text{products}} - \sum \Delta G^\circ_{f\ \text{reactants}}",
                r"\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = -RT\ln K = -nFE^\circ",
                r"I = \dfrac{q}{t}",
                r"E_{\text{cell}} = E^\circ_{\text{cell}} - \dfrac{RT}{nF}\ln Q",
            ],
            "legend": [
                (r"q", "heat"), (r"m", "mass"), (r"c", "specific heat capacity"), (r"T", "temperature"),
                (r"S^\circ", "standard entropy"), (r"H^\circ", "standard enthalpy"),
                (r"G^\circ", "standard Gibbs free energy"), (r"R", "gas constant"), (r"K", "equilibrium constant"),
                (r"n", "number of moles of electrons"), (r"E^\circ", "standard potential"),
                (r"I", "current (amperes)"), (r"q", "charge (coulombs)"), (r"t", "time (seconds)"),
                (r"Q", "reaction quotient"),
            ],
        },
    ],
}


def _load_raw_units() -> list[tuple[dict[str, Any], list[dict[str, Any]]]]:
    """Dynamically load unit_1 through unit_9 modules from quiz_data."""
    loaded: list[tuple[dict[str, Any], list[dict[str, Any]]]] = []
    for unit_num in range(1, 10):
        mod = importlib.import_module(f"quiz_data.unit_{unit_num}")
        meta = dict(mod.UNIT_META)
        questions = [dict(q) for q in mod.QUESTIONS]
        loaded.append((meta, questions))
    return loaded


def _question_revision(q: dict[str, Any]) -> str:
    """Short fingerprint of a question's stem, options and key.

    The browser stores it with each saved answer so that progress recorded for an
    older version of a question (e.g. re-ordered options) is discarded, not mis-scored.
    """
    blob = "\x1f".join([str(q.get("question", "")), *map(str, q.get("options", [])), str(q.get("correct_index"))])
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:10]


_CACHED_PAYLOAD: dict[str, Any] | None = None


def get_all_payload() -> dict[str, Any]:
    """Return the complete enriched AP Chemistry quiz payload across all 9 units."""
    global _CACHED_PAYLOAD
    if _CACHED_PAYLOAD is not None:
        return _CACHED_PAYLOAD

    raw_units = _load_raw_units()
    units_out: list[dict[str, Any]] = []
    all_questions: list[dict[str, Any]] = []

    global_id = 1
    for meta, raw_qs in raw_units:
        unit_id = int(meta["id"])
        unit_questions: list[dict[str, Any]] = []

        # Count questions per CED topic within this unit
        topic_counts: dict[str, int] = {}

        for idx, q in enumerate(raw_qs, start=1):
            unit_q_num = int(q.get("unit_q_num", idx))
            set_number = ((unit_q_num - 1) // 10) + 1
            correct_idx = int(q["correct_index"])
            topic_code = str(q["topic_code"])
            topic_counts[topic_code] = topic_counts.get(topic_code, 0) + 1

            enriched_q = {
                "id": global_id,
                # Stable identifier (does not shift when other units gain questions)
                "uid": f"u{unit_id}q{unit_q_num}",
                "rev": _question_revision(q),
                "unit_id": unit_id,
                "unit_title": meta["title"],
                "unit_short_title": meta["short_title"],
                "exam_weight": meta["exam_weight"],
                "unit_color": meta["color"],
                "unit_q_num": unit_q_num,
                "set_number": set_number,
                "topic_code": topic_code,
                "topic_title": q["topic_title"],
                "difficulty": q.get("difficulty", "AP Exam Level"),
                "stimulus": q.get("stimulus", ""),
                "question": q["question"],
                "options": list(q["options"]),
                "correct_index": correct_idx,
                "correct_letter": OPTION_LETTERS[correct_idx],
                "explanation": q["explanation"],
            }
            unit_questions.append(enriched_q)
            all_questions.append(enriched_q)
            global_id += 1

        topics_enriched = []
        for t in meta.get("topics", []):
            code = t["code"]
            topics_enriched.append({
                "code": code,
                "title": t["title"],
                "count": topic_counts.get(code, 0),
            })

        unit_summary = {
            "id": unit_id,
            "title": meta["title"],
            "short_title": meta["short_title"],
            "exam_weight": meta["exam_weight"],
            "color": meta["color"],
            "description": meta["description"],
            "question_count": len(unit_questions),
            "set_count": (len(unit_questions) + 9) // 10,
            "topics": topics_enriched,
        }
        units_out.append(unit_summary)

    _CACHED_PAYLOAD = {
        "total_units": len(units_out),
        "total_questions": len(all_questions),
        "questions_per_set": 10,
        "units": units_out,
        "questions": all_questions,
        "reference_sheet": AP_REFERENCE_SHEET,
    }
    return _CACHED_PAYLOAD


def get_units_summary() -> list[dict[str, Any]]:
    """Return metadata for all 9 AP Chemistry units."""
    return get_all_payload()["units"]


def get_unit_by_id(unit_id: int) -> dict[str, Any] | None:
    """Return a single unit's metadata and all of its questions, or None if invalid."""
    payload = get_all_payload()
    unit_meta = next((u for u in payload["units"] if u["id"] == unit_id), None)
    if unit_meta is None:
        return None
    unit_qs = [q for q in payload["questions"] if q["unit_id"] == unit_id]
    return {
        "unit": unit_meta,
        "questions": unit_qs,
    }


def get_question_by_id(q_id: int) -> dict[str, Any] | None:
    """Return a single enriched question by its global ID (1..total_questions), or None."""
    payload = get_all_payload()
    return next((q for q in payload["questions"] if q["id"] == q_id), None)
