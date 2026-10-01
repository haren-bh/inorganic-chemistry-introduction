import unittest
from reactions_engine import (
    CHEMICALS,
    CATEGORIES,
    REACTIONS,
    CANONICAL_SUMMARY,
    get_all_payload,
    get_reaction_by_id,
)


class TestReactionsEngine(unittest.TestCase):
    def test_counts_and_ids(self):
        payload = get_all_payload()
        self.assertEqual(payload["spec_reactions"], 187)
        self.assertEqual(payload["added_reactions"], 19)
        self.assertEqual(payload["total_reactions"], 206)
        self.assertEqual(len(CATEGORIES), 12)
        self.assertEqual(len(CANONICAL_SUMMARY), 9)

        ids = [r["id"] for r in REACTIONS]
        self.assertEqual(ids, list(range(1, 207)))

    def test_every_reaction_has_explanation_and_lab(self):
        payload = get_all_payload()
        for r in payload["reactions"]:
            self.assertTrue(r["name"], f"Reaction {r['id']} missing name")
            self.assertTrue(r["equation"], f"Reaction {r['id']} missing equation")
            self.assertTrue(len(r["explanation"]) > 40, f"Reaction {r['id']} explanation too short")
            self.assertIn("lab", r)
            self.assertTrue(r["lab"]["apparatus"], f"Reaction {r['id']} missing lab apparatus")
            self.assertTrue(len(r["chemical_details"]) >= 1, f"Reaction {r['id']} has no chemicals")
            # Ensure every chemical key in reactions is explicitly defined in CHEMICALS
            for c_key in r["chemicals"]:
                self.assertIn(c_key, CHEMICALS, f"Chemical key '{c_key}' in reaction #{r['id']} not in CHEMICALS")

    def test_get_reaction_by_id(self):
        r1 = get_reaction_by_id(1)
        self.assertIsNotNone(r1)
        self.assertIn("Formation of Water", r1["name"])
        r2 = get_reaction_by_id(2)
        self.assertIsNotNone(r2)
        self.assertIn("Haber-Bosch", r2["name"])
        self.assertIsNone(get_reaction_by_id(9999))

    def test_flask_routes(self):
        from app import app
        client = app.test_client()

        resp_page = client.get("/reactions")
        self.assertEqual(resp_page.status_code, 200)
        self.assertIn(b"Essential Chemical", resp_page.data)

        resp_api = client.get("/api/reactions")
        self.assertEqual(resp_api.status_code, 200)
        data = resp_api.get_json()
        self.assertEqual(data["total_reactions"], 206)

        resp_single = client.get("/api/reaction/155")
        self.assertEqual(resp_single.status_code, 200)
        self.assertEqual(resp_single.get_json()["title"], "Thermite Reaction")

        resp_404 = client.get("/api/reaction/9999")
        self.assertEqual(resp_404.status_code, 404)


if __name__ == "__main__":
    unittest.main()

