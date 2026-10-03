import math
import re
import unittest

from quiz_engine import (
    AP_REFERENCE_SHEET,
    get_all_payload,
    get_units_summary,
    get_unit_by_id,
    get_question_by_id,
)

# Question bank size per unit after the 2026-10-03 CED review (blind-spot additions).
EXPECTED_COUNTS = {1: 60, 2: 60, 3: 80, 4: 60, 5: 60, 6: 60, 7: 60, 8: 70, 9: 60}
EXPECTED_TOTAL = sum(EXPECTED_COUNTS.values())  # 570

# Official AP Chemistry Course and Exam Description (Effective Fall 2024) unit and topic titles.
CED_FALL_2024 = {
    1: ("Unit 1: Atomic Structure and Properties", [
        ("1.1", "Moles and Molar Mass"), ("1.2", "Mass Spectra of Elements"),
        ("1.3", "Elemental Composition of Pure Substances"), ("1.4", "Composition of Mixtures"),
        ("1.5", "Atomic Structure and Electron Configuration"), ("1.6", "Photoelectron Spectroscopy"),
        ("1.7", "Periodic Trends"), ("1.8", "Valence Electrons and Ionic Compounds")]),
    2: ("Unit 2: Compound Structure and Properties", [
        ("2.1", "Types of Chemical Bonds"), ("2.2", "Intramolecular Force and Potential Energy"),
        ("2.3", "Structure of Ionic Solids"), ("2.4", "Structure of Metals and Alloys"),
        ("2.5", "Lewis Diagrams"), ("2.6", "Resonance and Formal Charge"), ("2.7", "VSEPR and Hybridization")]),
    3: ("Unit 3: Properties of Substances and Mixtures", [
        ("3.1", "Intermolecular and Interparticle Forces"), ("3.2", "Properties of Solids"),
        ("3.3", "Solids, Liquids, and Gases"), ("3.4", "Ideal Gas Law"), ("3.5", "Kinetic Molecular Theory"),
        ("3.6", "Deviation from Ideal Gas Law"), ("3.7", "Solutions and Mixtures"),
        ("3.8", "Representations of Solutions"), ("3.9", "Separation of Solutions and Mixtures"),
        ("3.10", "Solubility"), ("3.11", "Spectroscopy and the Electromagnetic Spectrum"),
        ("3.12", "Properties of Photons"), ("3.13", "Beer-Lambert Law")]),
    4: ("Unit 4: Chemical Reactions", [
        ("4.1", "Introduction for Reactions"), ("4.2", "Net Ionic Equations"), ("4.3", "Representations of Reactions"),
        ("4.4", "Physical and Chemical Changes"), ("4.5", "Stoichiometry"), ("4.6", "Introduction to Titration"),
        ("4.7", "Types of Chemical Reactions"), ("4.8", "Introduction to Acid-Base Reactions"),
        ("4.9", "Oxidation-Reduction (Redox) Reactions")]),
    5: ("Unit 5: Kinetics", [
        ("5.1", "Reaction Rates"), ("5.2", "Introduction to Rate Law"), ("5.3", "Concentration Changes Over Time"),
        ("5.4", "Elementary Reactions"), ("5.5", "Collision Model"), ("5.6", "Reaction Energy Profile"),
        ("5.7", "Introduction to Reaction Mechanisms"), ("5.8", "Reaction Mechanism and Rate Law"),
        ("5.9", "Pre-Equilibrium Approximation"), ("5.10", "Multistep Reaction Energy Profile"), ("5.11", "Catalysis")]),
    6: ("Unit 6: Thermochemistry", [
        ("6.1", "Endothermic and Exothermic Processes"), ("6.2", "Energy Diagrams"),
        ("6.3", "Heat Transfer and Thermal Equilibrium"), ("6.4", "Heat Capacity and Calorimetry"),
        ("6.5", "Energy of Phase Changes"), ("6.6", "Introduction to Enthalpy of Reaction"),
        ("6.7", "Bond Enthalpies"), ("6.8", "Enthalpy of Formation"), ("6.9", "Hess's Law")]),
    7: ("Unit 7: Equilibrium", [
        ("7.1", "Introduction to Equilibrium"), ("7.2", "Direction of Reversible Reactions"),
        ("7.3", "Reaction Quotient and Equilibrium Constant"), ("7.4", "Calculating the Equilibrium Constant"),
        ("7.5", "Magnitude of the Equilibrium Constant"), ("7.6", "Properties of the Equilibrium Constant"),
        ("7.7", "Calculating Equilibrium Concentrations"), ("7.8", "Representations of Equilibrium"),
        ("7.9", "Introduction to Le Châtelier's Principle"), ("7.10", "Reaction Quotient and Le Châtelier's Principle"),
        ("7.11", "Introduction to Solubility Equilibria"), ("7.12", "Common-Ion Effect")]),
    8: ("Unit 8: Acids and Bases", [
        ("8.1", "Introduction to Acids and Bases"), ("8.2", "pH and pOH of Strong Acids and Bases"),
        ("8.3", "Weak Acid and Base Equilibria"), ("8.4", "Acid-Base Reactions and Buffers"),
        ("8.5", "Acid-Base Titrations"), ("8.6", "Molecular Structure of Acids and Bases"), ("8.7", "pH and pKa"),
        ("8.8", "Properties of Buffers"), ("8.9", "Henderson-Hasselbalch Equation"), ("8.10", "Buffer Capacity"),
        ("8.11", "pH and Solubility")]),
    9: ("Unit 9: Thermodynamics and Electrochemistry", [
        ("9.1", "Introduction to Entropy"), ("9.2", "Absolute Entropy and Entropy Change"),
        ("9.3", "Gibbs Free Energy and Thermodynamic Favorability"), ("9.4", "Thermodynamic and Kinetic Control"),
        ("9.5", "Free Energy and Equilibrium"), ("9.6", "Free Energy of Dissolution"), ("9.7", "Coupled Reactions"),
        ("9.8", "Galvanic (Voltaic) and Electrolytic Cells"), ("9.9", "Cell Potential and Free Energy"),
        ("9.10", "Cell Potential Under Nonstandard Conditions"), ("9.11", "Electrolysis and Faraday's Law")]),
}

CTRL_CHARS = re.compile(r"[\x00-\x09\x0b\x0c\x0e-\x1f\x7f]")


def _norm_title(s: str) -> str:
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s*\([^)]*\)\s*$", "", s).strip().lower()


class TestQuizEngine(unittest.TestCase):
    def test_nine_units_and_question_totals(self):
        payload = get_all_payload()
        self.assertEqual(payload["total_units"], 9)
        self.assertEqual(payload["total_questions"], EXPECTED_TOTAL)
        self.assertEqual(payload["questions_per_set"], 10)

        units = get_units_summary()
        self.assertEqual(len(units), 9)

        expected_weights = {
            1: "7–9%",
            2: "7–9%",
            3: "18–22%",
            4: "7–9%",
            5: "7–9%",
            6: "7–9%",
            7: "7–9%",
            8: "11–15%",
            9: "7–9%",
        }
        for u in units:
            uid = u["id"]
            self.assertEqual(u["question_count"], EXPECTED_COUNTS[uid], f"Unit {uid} question count")
            self.assertEqual(u["set_count"], math.ceil(EXPECTED_COUNTS[uid] / 10), f"Unit {uid} set count")
            self.assertEqual(u["exam_weight"], expected_weights[uid])

        # The highest-weighted units carry the most practice questions.
        counts = {u["id"]: u["question_count"] for u in units}
        self.assertEqual(max(counts, key=counts.get), 3)
        self.assertGreater(counts[8], max(counts[i] for i in (1, 2, 4, 5, 6, 7, 9)))

    def test_units_and_topics_match_fall_2024_ced(self):
        units = get_units_summary()
        total_topics = 0
        for u in units:
            official_title, official_topics = CED_FALL_2024[u["id"]]
            self.assertEqual(u["title"], official_title)
            self.assertEqual([t["code"] for t in u["topics"]], [c for c, _ in official_topics])
            for t, (_, official) in zip(u["topics"], official_topics):
                self.assertEqual(_norm_title(t["title"]), _norm_title(official), f"Topic {t['code']} title")
            total_topics += len(u["topics"])
        self.assertEqual(total_topics, 91)

    def test_every_question_schema_and_explanations(self):
        payload = get_all_payload()
        questions = payload["questions"]
        self.assertEqual(len(questions), EXPECTED_TOTAL)
        self.assertEqual([q["id"] for q in questions], list(range(1, EXPECTED_TOTAL + 1)))

        uids = [q["uid"] for q in questions]
        self.assertEqual(len(uids), len(set(uids)), "question uids must be unique")

        topics_by_unit = {u["id"]: {t["code"]: t["title"] for t in u["topics"]} for u in payload["units"]}
        per_unit_nums: dict[int, list[int]] = {}
        for q in questions:
            qid = q["id"]
            self.assertIn(q["unit_id"], range(1, 10))
            per_unit_nums.setdefault(q["unit_id"], []).append(q["unit_q_num"])
            self.assertEqual(q["uid"], f"u{q['unit_id']}q{q['unit_q_num']}")
            self.assertRegex(q["rev"], r"^[0-9a-f]{10}$")
            self.assertEqual(q["set_number"], (q["unit_q_num"] - 1) // 10 + 1)
            self.assertIn(q["topic_code"], topics_by_unit[q["unit_id"]], f"Q#{qid} unknown topic")
            self.assertEqual(q["topic_title"], topics_by_unit[q["unit_id"]][q["topic_code"]], f"Q#{qid} topic title")
            self.assertIn(q["difficulty"], ("AP Exam Level", "Challenging"))
            self.assertTrue(len(q["question"]) > 15, f"Q#{qid} question stem too short")
            self.assertEqual(len(q["options"]), 4, f"Q#{qid} must have 4 options")
            self.assertEqual(len(set(map(str, q["options"]))), 4, f"Q#{qid} has duplicate options")
            for opt in q["options"]:
                self.assertTrue(len(str(opt).strip()) > 0, f"Q#{qid} has empty option")
            self.assertIn(q["correct_index"], (0, 1, 2, 3), f"Q#{qid} invalid correct_index")
            self.assertEqual(q["correct_letter"], "ABCD"[q["correct_index"]])
            self.assertTrue(len(q["explanation"]) > 40, f"Q#{qid} explanation too short")

        for unit_id, nums in per_unit_nums.items():
            self.assertEqual(nums, list(range(1, len(nums) + 1)), f"Unit {unit_id} numbering must be 1..N")

    def test_topic_coverage_minimums(self):
        for u in get_units_summary():
            minimum = 5 if u["id"] == 3 else 4
            for t in u["topics"]:
                self.assertGreaterEqual(t["count"], minimum, f"Topic {t['code']} has only {t['count']} questions")

    def test_answer_key_balance_per_unit(self):
        payload = get_all_payload()
        for u in payload["units"]:
            keys = [q["correct_letter"] for q in payload["questions"] if q["unit_id"] == u["id"]]
            for letter in "ABCD":
                share = keys.count(letter) / len(keys)
                self.assertTrue(0.18 <= share <= 0.32,
                                f"Unit {u['id']}: key {letter} is {share:.0%} of answers (keep within 18-32%)")

    def test_no_corrupted_escapes_or_math_inside_svg(self):
        """Regression: non-raw strings once turned '\\a'/'\\t' into control characters."""
        for q in get_all_payload()["questions"]:
            fields = [q["stimulus"], q["question"], q["explanation"], *q["options"]]
            for text in fields:
                self.assertIsNone(CTRL_CHARS.search(str(text)), f"Q#{q['id']} contains a control character")
            for svg in re.findall(r"<svg\b.*?</svg>", q["stimulus"], re.S):
                self.assertNotIn("$", svg, f"Q#{q['id']}: '$' inside <svg> would be mangled by KaTeX")
                self.assertIn('role="img"', svg, f"Q#{q['id']}: SVG figure needs role=img")
                self.assertIn("aria-label=", svg, f"Q#{q['id']}: SVG figure needs an aria-label")

    def test_reference_sheet_matches_official_2025_sheet(self):
        sheet = AP_REFERENCE_SHEET
        self.assertIn("Effective 2025", sheet["title"])
        all_tex = " ".join(item for grp in sheet["equations"] for item in grp["items"])
        all_tex += " " + " ".join(c["value"] for c in sheet["constants"])
        # On the official sheet
        for needle in (r"F_{\text{coulombic}}", r"\dfrac{P_1V_1}{T_1}", r"K_a =", r"K_b =",
                       r"\text{p}K_w = \text{p}K_a + \text{p}K_b", r"I = \dfrac{q}{t}", "22.4", "0.08206"):
            self.assertIn(needle, all_tex)
        # Not on the official sheet (must not be presented as official reference data)
        for needle in (r"\sqrt{\frac{M_2}{M_1}}", "M_1V_1", "62.36", "101.325", "1.602"):
            self.assertNotIn(needle, all_tex)
        self.assertEqual(len(sheet["metric_prefixes"]), 8)
        self.assertEqual(len(sheet["unit_conversions"]), 5)
        self.assertEqual([g["category"] for g in sheet["equations"]],
                         ["Atomic Structure", "Gases, Liquids, and Solutions", "Kinetics", "Equilibrium",
                          "Thermodynamics / Electrochemistry"])

    def test_unit_and_question_lookup(self):
        u3 = get_unit_by_id(3)
        self.assertIsNotNone(u3)
        self.assertEqual(u3["unit"]["id"], 3)
        self.assertEqual(len(u3["questions"]), EXPECTED_COUNTS[3])
        self.assertIsNone(get_unit_by_id(0))
        self.assertIsNone(get_unit_by_id(10))

        q1 = get_question_by_id(1)
        self.assertIsNotNone(q1)
        self.assertEqual(q1["unit_id"], 1)
        q_last = get_question_by_id(EXPECTED_TOTAL)
        self.assertIsNotNone(q_last)
        self.assertEqual(q_last["unit_id"], 9)
        self.assertIsNone(get_question_by_id(9999))

    def test_flask_quiz_routes(self):
        from app import app
        client = app.test_client()

        resp_page = client.get("/quiz")
        self.assertEqual(resp_page.status_code, 200)
        self.assertIn(b"AP Chemistry", resp_page.data)
        self.assertIn(b'id="btn-toggle-timed-mode"', resp_page.data)
        self.assertIn(b"Timed Mode", resp_page.data)
        self.assertIn(b'id="btn-revert-instant-mode"', resp_page.data)
        self.assertNotIn(b'class="quiz-mode-bar"', resp_page.data)
        self.assertNotIn(b'class="catalog-sidebar quiz-sidebar"', resp_page.data)
        self.assertIn(b"Equations and Constants, Effective 2025", resp_page.data)
        self.assertNotIn(b'id="quiz-performance-dashboard"', resp_page.data)
        self.assertIn(b"btn-batch-timer-start", resp_page.data)
        self.assertIn(b"btn-batch-timer-pause", resp_page.data)
        self.assertIn(b"btn-batch-timer-resume", resp_page.data)
        self.assertIn(b"btn-single-timer-start", resp_page.data)
        self.assertIn(b"btn-single-timer-pause", resp_page.data)
        self.assertIn(b"btn-single-timer-resume", resp_page.data)
        self.assertIn(b"quiz-timer-gate-banner", resp_page.data)
        self.assertIn(b"btn-retake-unit-batch", resp_page.data)
        self.assertIn(b"btn-retake-unit-single", resp_page.data)
        self.assertNotIn(b"btn-reset-progress", resp_page.data)

        resp_dash = client.get("/dashboard")
        self.assertEqual(resp_dash.status_code, 200)
        self.assertIn(b"AP Chemistry Performance", resp_dash.data)
        self.assertIn(b"chart-accuracy-trend", resp_dash.data)
        self.assertIn(b"chart-bank-donut", resp_dash.data)
        self.assertIn(b"chart-unit-bars", resp_dash.data)
        self.assertIn(b"chart-unit-pace", resp_dash.data)
        self.assertIn(b"dash-paused-table-wrap", resp_dash.data)
        self.assertIn(b"dash-unit-summary-table-wrap", resp_dash.data)
        self.assertIn(b"dash-attempts-table-wrap", resp_dash.data)

        resp_units = client.get("/api/quiz/units")
        self.assertEqual(resp_units.status_code, 200)
        units_json = resp_units.get_json()
        self.assertEqual(units_json["total_units"], 9)
        self.assertEqual(units_json["total_questions"], EXPECTED_TOTAL)

        resp_u8 = client.get("/api/quiz/unit/8")
        self.assertEqual(resp_u8.status_code, 200)
        self.assertEqual(len(resp_u8.get_json()["questions"]), EXPECTED_COUNTS[8])

        resp_u_404 = client.get("/api/quiz/unit/99")
        self.assertEqual(resp_u_404.status_code, 404)

        resp_q = client.get("/api/quiz/question/250")
        self.assertEqual(resp_q.status_code, 200)
        self.assertEqual(resp_q.get_json()["id"], 250)

        resp_q_404 = client.get("/api/quiz/question/9999")
        self.assertEqual(resp_q_404.status_code, 404)

    def test_user_cloud_storage_api_and_merge(self):
        import os
        import cloud_storage
        from app import app

        prev_disable = os.environ.get("DISABLE_GCS_SYNC")
        os.environ["DISABLE_GCS_SYNC"] = "1"
        test_user = "test_unit_student_01"
        local_path = cloud_storage._local_cache_path(test_user)
        if os.path.exists(local_path):
            os.remove(local_path)

        try:
            client = app.test_client()

            # Verify user_sync.js is loaded on all 5 screens
            for route in ("/", "/orbitals", "/reactions", "/quiz", "/dashboard"):
                r = client.get(route)
                self.assertEqual(r.status_code, 200)
                self.assertIn(b"user_sync.js", r.data)

            # 1. Initial GET for a new user
            r_get_new = client.get(f"/api/user/{test_user}")
            self.assertEqual(r_get_new.status_code, 200)
            new_json = r_get_new.get_json()
            self.assertEqual(new_json["username"], test_user)
            self.assertEqual(new_json["bucket"], "haren-agent-storage")
            self.assertFalse(new_json["found"])
            self.assertEqual(new_json["data"]["attempts"], [])

            # 2. Save first attempt and history via POST
            payload_1 = {
                "display_name": "Test Student 01",
                "history": {"u1q1": {"selected": 2, "correct": True, "rev": "abc1234567"}},
                "attempts": [
                    {
                        "id": "att_1001",
                        "timestamp": "2026-10-03T10:00:00Z",
                        "unitId": 1,
                        "unitTitle": "Unit 1: Atomic Structure and Properties",
                        "mode": "batch",
                        "setIndex": 0,
                        "scopeKey": "u1_set1",
                        "scopeLabel": "Set 1 (Q1–Q10)",
                        "correct": 8,
                        "answered": 10,
                        "total": 10,
                        "pct": 80,
                        "durationSec": 125,
                    }
                ],
                "sessions": {
                    "batchByUnitSet": {
                        "1:0": {
                            "answers": {"u1q1": {"selected": 2, "rev": "abc1234567"}},
                            "submitted": True,
                            "elapsedSec": 125,
                            "timerState": "completed",
                        }
                    },
                    "singleByUnit": {},
                    "lastLocation": {
                        "mode": "batch",
                        "unitId": 3,
                        "batchSetIndex": 1,
                        "updatedAt": "2026-10-03T10:05:00Z",
                    },
                },
                "merge": True,
            }
            r_post_1 = client.post(f"/api/user/{test_user}", json=payload_1)
            self.assertEqual(r_post_1.status_code, 200)
            saved_1 = r_post_1.get_json()
            self.assertEqual(len(saved_1["data"]["attempts"]), 1)
            self.assertEqual(saved_1["data"]["attempts"][0]["attemptNumber"], 1)
            self.assertEqual(saved_1["data"]["sessions"]["lastLocation"]["unitId"], 3)
            self.assertEqual(saved_1["data"]["sessions"]["lastLocation"]["batchSetIndex"], 1)

            # 3. Merge second attempt on same unit/mode/set and verify sequential attemptNumber
            payload_2 = {
                "display_name": "Test Student 01",
                "history": {"u1q2": {"selected": 1, "correct": True, "rev": "def1234567"}},
                "attempts": [
                    {
                        "id": "att_1002",
                        "timestamp": "2026-10-03T10:15:00Z",
                        "unitId": 1,
                        "unitTitle": "Unit 1: Atomic Structure and Properties",
                        "mode": "batch",
                        "setIndex": 0,
                        "scopeKey": "u1_set1",
                        "scopeLabel": "Set 1 (Q1–Q10)",
                        "correct": 10,
                        "answered": 10,
                        "total": 10,
                        "pct": 100,
                        "durationSec": 95,
                    }
                ],
                "sessions": {"batchByUnitSet": {}, "singleByUnit": {}},
                "merge": True,
            }
            r_post_2 = client.post(f"/api/user/{test_user}", json=payload_2)
            self.assertEqual(r_post_2.status_code, 200)

            # 4. Retrieve via GET and confirm both attempts, history entries, and lastLocation are returned
            r_get_after = client.get(f"/api/user/{test_user}")
            self.assertEqual(r_get_after.status_code, 200)
            after_json = r_get_after.get_json()
            self.assertTrue(after_json["found"])
            self.assertIn("u1q1", after_json["data"]["history"])
            self.assertIn("u1q2", after_json["data"]["history"])
            self.assertEqual(len(after_json["data"]["attempts"]), 2)
            self.assertEqual(after_json["data"]["attempts"][0]["attemptNumber"], 1)
            self.assertEqual(after_json["data"]["attempts"][1]["attemptNumber"], 2)
            self.assertEqual(after_json["data"]["attempts"][1]["pct"], 100)
            self.assertEqual(after_json["data"]["sessions"]["lastLocation"]["unitId"], 3)
        finally:
            if os.path.exists(local_path):
                os.remove(local_path)
            if prev_disable is None:
                os.environ.pop("DISABLE_GCS_SYNC", None)
            else:
                os.environ["DISABLE_GCS_SYNC"] = prev_disable

    def test_all_pages_render_retractable_sidebar(self):
        from app import app
        client = app.test_client()
        for route in ("/", "/orbitals", "/reactions", "/quiz", "/dashboard"):
            resp = client.get(route)
            self.assertEqual(resp.status_code, 200, f"Expected 200 on {route}")
            html = resp.get_data(as_text=True)
            self.assertIn('class="site-sidebar"', html, f"Missing .site-sidebar on {route}")
            self.assertIn('class="sidebar-atom-svg"', html, f"Missing Atom SVG in sidebar top on {route}")
            self.assertNotIn("AP &amp; Quantum Lab", html, f"Removed brand text still present on {route}")
            self.assertNotIn('class="sidebar-page-context"', html, f"Removed sidebar page context still present on {route}")
            self.assertIn('id="sidebar-group-topics"', html, f"Missing Chemistry Topics group on {route}")
            self.assertIn("Chemistry Topics", html, f"Missing Chemistry Topics label on {route}")
            self.assertIn('id="sidebar-group-quiz"', html, f"Missing AP Chemistry Quiz group on {route}")
            self.assertIn('id="quiz-unit-sidebar"', html, f"Missing quiz unit submenu in sidebar on {route}")
            self.assertIn('id="btn-toggle-sidebar"', html, f"Missing #btn-toggle-sidebar on {route}")
            self.assertIn('id="sidebar-user-mount"', html, f"Missing #sidebar-user-mount on {route}")
            self.assertIn('class="site-header"', html, f"Missing compact top .site-header on {route}")
            self.assertIn('class="header-lab-svgs"', html, f"Missing lab equipment SVGs in header on {route}")


if __name__ == "__main__":
    unittest.main()



