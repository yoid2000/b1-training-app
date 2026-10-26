"""End-to-end HTTP and persistence tests; standard library only."""

from concurrent.futures import ThreadPoolExecutor
from http.cookiejar import CookieJar
import hashlib
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import build_opener, HTTPCookieProcessor, Request

from app import CATALOG, QUESTIONS, QUESTION_BANK, TRANSLATIONS, TUTORIALS, UNIT_DETAILS, Store, create_server


class Client:
    def __init__(self, base):
        self.base = base
        self.opener = build_opener(HTTPCookieProcessor(CookieJar()))

    def request(self, path, body=None, *, headers=None, method=None):
        data = None if body is None else json.dumps(body).encode()
        request = Request(self.base + path, data=data, headers=headers or {}, method=method)
        if body is not None:
            request.add_header("Content-Type", "application/json")
        try:
            response = self.opener.open(request, timeout=10)
        except HTTPError as error:
            response = error
        with response:
            raw = response.read()
            result = json.loads(raw) if "application/json" in response.headers.get("Content-Type", "") else raw
            return response.status, result, response.headers

    def get(self, path):
        status, data, _ = self.request("/api/" + path)
        if status != 200:
            raise AssertionError((path, status, data))
        return data

    def post(self, path, body):
        status, data, _ = self.request("/api/" + path, body)
        if status != 200:
            raise AssertionError((path, status, data))
        return data


class AppTests(unittest.TestCase):
    def setUp(self):
        self.quiet = patch("app.Handler.log_message")
        self.quiet.start()
        self.temp = tempfile.TemporaryDirectory()
        self.database = Path(self.temp.name) / "test.sqlite3"
        self.server = create_server("127.0.0.1", 0, self.database)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"
        self.alice = Client(self.base)
        self.bob = Client(self.base)
        self.alice.post("users", {"name": "Alice"})
        self.bob.post("users", {"name": "Bob"})

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.temp.cleanup()
        self.quiet.stop()

    def start(self, client, unit=1, **kwargs):
        result = client.post("start", {"unit_id": unit, **kwargs})
        return client.get("practice/" + result["id"])

    def answer(self, client, practice, question, correct=True):
        index = QUESTIONS[question["id"]]["correct_index"]
        choice = index if correct else (index + 1) % 4
        return client.post("answer", {"practice_id": practice["id"], "question_id": question["id"], "choice": choice})

    def finish(self, client, practice, correct=True):
        for question in practice["questions"]:
            self.answer(client, practice, question, correct)

    def test_user_isolation_and_no_answer_leak(self):
        practice = self.start(self.alice)
        first = practice["questions"][0]
        self.assertNotIn("correct_index", first)
        self.assertNotIn("explanation", first)
        status, _, _ = self.bob.request("/api/practice/" + practice["id"])
        self.assertEqual(status, 404)
        status, _, _ = self.bob.request("/api/answer", {"practice_id": practice["id"], "question_id": first["id"], "choice": 0})
        self.assertEqual(status, 404)
        self.answer(self.alice, practice, first, False)
        self.assertEqual(self.alice.get("me")["mistakes"], 1)
        self.assertEqual(self.bob.get("me")["mistakes"], 0)
        self.assertEqual(self.bob.get("me")["attempts"], 0)

    def test_first_choice_is_immutable_and_progress_resumes(self):
        practice = self.start(self.alice)
        question = practice["questions"][0]
        result = self.answer(self.alice, practice, question, False)
        self.assertFalse(result["correct"])
        self.assertTrue(result["saved"])
        result = self.answer(self.alice, practice, question, True)
        self.assertTrue(result["correct"])
        self.assertFalse(result["saved"])
        self.assertFalse(result["first_answer"]["correct"])
        self.assertEqual(self.alice.get("me")["attempts"], 1)
        resumed = self.start(self.alice)
        self.assertEqual(resumed["id"], practice["id"])
        self.assertFalse(resumed["questions"][0]["answer"]["correct"])
        self.assertIn("explanation", resumed["questions"][0])
        self.assertIn("correct_index", resumed["questions"][0])

    def test_translations_in_practice_and_review_preserve_progress(self):
        practice = self.start(self.alice)
        before = self.alice.get("me")
        for question in practice["questions"]:
            self.assertEqual(question["translation_en"], TRANSLATIONS[question["id"]]["en"])
            self.assertIsNone(question["answer"])
            self.assertNotIn("correct_index", question)
            self.assertNotIn("explanation", question)
        self.assertEqual(self.alice.get("me"), before)
        self.answer(self.alice, practice, practice["questions"][0], False)
        review = self.start(self.alice, mode="review")
        before = self.alice.get("me")
        loaded = self.alice.get("practice/" + review["id"])
        self.assertEqual(loaded["questions"][0]["translation_en"], practice["questions"][0]["translation_en"])
        self.assertIsNone(loaded["questions"][0]["answer"])
        self.assertEqual(self.alice.get("me"), before)

    def test_sequential_unlock_completion_and_retake(self):
        status, _, _ = self.alice.request("/api/start", {"unit_id": 2})
        self.assertEqual(status, 403)
        first = self.start(self.alice)
        self.finish(self.alice, first, False)
        d = self.alice.get("me")
        self.assertEqual(d["completed"], 1)
        self.assertEqual(d["next_unit"], 2)
        self.assertEqual(d["units"][0]["best"], 0)
        self.assertEqual(d["mistakes"], 20)
        second = self.start(self.alice, 2)
        self.assertEqual(second["unit"]["id"], 2)
        retake = self.start(self.alice)
        self.assertNotEqual(first["id"], retake["id"])
        self.assertTrue(all(q["answer"] is None for q in retake["questions"]))
        self.finish(self.alice, retake)
        d = self.alice.get("me")
        self.assertEqual(d["completed"], 1)
        self.assertEqual(d["units"][0]["best"], 20)
        self.assertEqual(d["mistakes"], 0)
        self.assertEqual(d["attempts"], 40)

    def test_random_review_snapshot_resume_and_correction(self):
        first = self.start(self.alice)
        self.finish(self.alice, first, False)
        second = self.start(self.alice, 2)
        self.finish(self.alice, second, False)
        review = self.start(self.alice, mode="review")
        self.assertEqual(review["mode"], "review")
        self.assertEqual(len(review["questions"]), 20)
        ids = {q["id"] for q in review["questions"]}
        self.assertEqual(len(ids), 20)
        self.assertTrue(ids.issubset({q["id"] for q in first["questions"] + second["questions"]}))
        self.assertEqual(self.start(self.alice, mode="review")["id"], review["id"])
        self.answer(self.alice, review, review["questions"][0])
        self.assertEqual(self.alice.get("me")["mistakes"], 39)
        resumed = self.start(self.alice, mode="review")
        self.assertEqual([q["id"] for q in review["questions"]], [q["id"] for q in resumed["questions"]])
        self.finish(self.alice, review)
        self.assertEqual(self.alice.get("me")["mistakes"], 20)
        next_review = self.start(self.alice, mode="review")
        self.assertNotEqual(next_review["id"], review["id"])
        self.assertTrue(ids.isdisjoint({q["id"] for q in next_review["questions"]}))

    def test_database_persists_and_profiles_switch_independently(self):
        practice = self.start(self.alice)
        self.answer(self.alice, practice, practice["questions"][0])
        store = Store(self.database)
        with store.connect() as db:
            user = db.execute("SELECT id,name FROM users WHERE name='Alice'").fetchone()
            self.assertEqual(store.dashboard(db, user)["attempts"], 1)
        users = self.alice.get("users")["users"]
        another_device = Client(self.base)
        another_device.post("select-user", {"user_id": users[0]["id"]})
        self.assertEqual(another_device.get("me")["attempts"], 1)
        self.alice.post("select-user", {"user_id": users[1]["id"]})
        self.assertEqual(self.alice.get("me")["user"]["name"], "Bob")
        self.assertEqual(another_device.get("me")["user"]["name"], "Alice")

    def test_concurrent_starts_and_answers(self):
        user_id = self.alice.get("me")["user"]["id"]
        clients = [Client(self.base) for _ in range(8)]
        for client in clients:
            client.post("select-user", {"user_id": user_id})
        with ThreadPoolExecutor(max_workers=8) as pool:
            runs = list(pool.map(lambda client: client.post("start", {"unit_id": 1}), clients))
        self.assertEqual(len({p["id"] for p in runs}), 1)
        practice = self.alice.get("practice/" + runs[0]["id"])
        with ThreadPoolExecutor(max_workers=8) as pool:
            results = list(pool.map(lambda client: self.answer(client, practice, practice["questions"][0]), clients))
        self.assertEqual(sum(r["saved"] for r in results), 1)
        self.assertEqual(self.alice.get("me")["attempts"], 1)

    def test_validation_request_protection_and_static_routes(self):
        anon = Client(self.base)
        self.assertEqual(anon.request("/api/me")[0], 401)
        self.assertEqual(self.alice.request("/api/users", {"name": " alice "})[0], 409)
        for name in ("", "  ", "a" * 41, 7, "bad\nname"):
            self.assertEqual(self.alice.request("/api/users", {"name": name})[0], 400)
        for unit in (0, -1, 171, "1", True):
            self.assertEqual(self.alice.request("/api/start", {"unit_id": unit})[0], 404)
        self.assertEqual(self.alice.request("/api/start", {"mode": "unknown"})[0], 400)
        self.assertEqual(self.alice.request("/api/start", {"mode": "review"})[0], 400)
        self.assertEqual(self.alice.request("/api/users", {"name": "Mallory"}, headers={"Origin": "http://evil.example"})[0], 403)
        self.assertEqual(self.alice.request("/api/users", {"name": "Mallory"}, headers={"Sec-Fetch-Site": "cross-site"})[0], 403)
        self.assertEqual(self.alice.request("/api/start", method="POST")[0], 415)
        practice = self.start(self.alice)
        question = practice["questions"][0]
        for choice in (-1, 4, True, "0", None):
            self.assertEqual(self.alice.request("/api/answer", {"practice_id": practice["id"], "question_id": question["id"], "choice": choice})[0], 400)
        self.assertEqual(self.alice.request("/api/answer", {"practice_id": practice["id"], "question_id": "u002-q01", "choice": 0})[0], 404)
        for path in ("/", "/style.css", "/app.js", "/favicon.svg"):
            status, data, headers = self.alice.request(path)
            self.assertEqual(status, 200)
            self.assertTrue(data)
            self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
        for path in ("/app.py", "/data/syllabus.json", "/instance/practice.sqlite3", "/../app.py"):
            self.assertEqual(self.alice.request(path)[0], 404)
        self.alice.post("logout", {})
        self.assertEqual(self.alice.request("/api/me")[0], 401)

    def test_all_prepared_units_end_at_boundary(self):
        for unit in range(1, 171):
            practice = self.start(self.alice, unit)
            self.assertTrue(practice["unit"]["goal_de"])
            self.assertTrue(practice["unit"]["vocabulary"])
            self.finish(self.alice, practice)
        d = self.alice.get("me")
        self.assertEqual((d["completed"], d["attempts"], d["correct"], d["mistakes"]), (170, 3400, 3400, 0))
        self.assertIsNone(d["next_unit"])
        self.assertTrue(all(u["available"] for u in d["units"]))
        self.assertEqual(len(self.alice.get("syllabus")["units"]), 170)

    def test_tutorials_for_every_unit_are_read_only(self):
        practice = self.start(self.alice)
        self.assertNotIn("tutorial", practice["unit"])
        self.answer(self.alice, practice, practice["questions"][0], False)
        before = self.alice.get("me")
        saved_practice = self.alice.get("practice/" + practice["id"])
        for unit_id in range(1, 171):
            data = self.alice.get(f"tutorial/{unit_id}")
            self.assertEqual(data["unit_id"], unit_id)
            self.assertEqual(data["title"], UNIT_DETAILS[unit_id][0])
            self.assertEqual(data["tutorial"], TUTORIALS[unit_id])
        self.assertEqual(self.alice.get("me"), before)
        self.assertEqual(self.alice.get("practice/" + practice["id"]), saved_practice)
        with Store(self.database).connect() as db:
            self.assertEqual(db.execute("SELECT COUNT(*) FROM practice").fetchone()[0], 1)
            self.assertEqual(db.execute("SELECT COUNT(*) FROM answers").fetchone()[0], 1)
        self.assertEqual(self.bob.get("me")["attempts"], 0)

    def test_tutorial_access_and_invalid_units(self):
        self.assertEqual(Client(self.base).request("/api/tutorial/1")[0], 401)
        for unit_id in ("", "0", "-1", "171", "abc", "1.0", "0001", "1/extra", "%31"):
            self.assertEqual(self.alice.request("/api/tutorial/" + unit_id)[0], 404, unit_id)


class ContentTests(unittest.TestCase):
    def test_translations_cover_current_questions_and_preserve_blanks(self):
        self.assertEqual(set(TRANSLATIONS), set(QUESTIONS))
        for qid, question in QUESTIONS.items():
            translation = TRANSLATIONS[qid]
            self.assertEqual(translation["de"], question["prompt"])
            self.assertTrue(translation["en"].strip(), qid)
            self.assertEqual(translation["en"].count("___"), question["prompt"].count("___"), qid)
            self.assertNotIn("XYZ", translation["en"], qid)

    def test_all_tutorials_are_complete_and_individual(self):
        self.assertEqual(sorted(TUTORIALS), list(range(1, 171)))
        seen = set()
        for unit_id, tutorial in TUTORIALS.items():
            self.assertEqual(tutorial["unit_id"], unit_id)
            self.assertTrue(tutorial["pattern"].strip())
            self.assertTrue(tutorial["remember"].strip())
            self.assertIn(len(tutorial["rules"]), range(2, 5))
            self.assertTrue(all(rule.strip() for rule in tutorial["rules"]))
            self.assertEqual(len(tutorial["examples"]), 2)
            self.assertTrue(all(e["de"].strip() and e["en"].strip() for e in tutorial["examples"]))
            text = json.dumps(tutorial, ensure_ascii=False)
            self.assertNotIn("TODO", text)
            self.assertGreater(len(text.split()), 60)
            self.assertLess(len(text.split()), 220)
            key = tuple(tutorial["rules"])
            self.assertNotIn(key, seen, unit_id)
            seen.add(key)

    def test_bundled_tutorials_rebuild_identically(self):
        from tools.build_tutorials import build
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "tutorials.json"
            with patch("builtins.print"):
                build(target)
            bundled = Path(__file__).resolve().parents[1] / "data" / "tutorials.json"
            self.assertEqual(target.read_bytes(), bundled.read_bytes())

    def test_bundled_questions_rebuild_identically(self):
        from tools.build_question_bank import build
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.json"
            second = Path(directory) / "second.json"
            with patch("builtins.print"):
                build(first)
                build(second)
            bundled = Path(__file__).resolve().parents[1] / "data" / "questions_021_170.json"
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(first.read_bytes(), bundled.read_bytes())

    def test_complete_content_and_stable_identifiers(self):
        self.assertEqual(list(QUESTION_BANK), list(range(1, 171)))
        self.assertEqual(len(QUESTIONS), 3400)
        self.assertEqual(len(CATALOG), 170)
        self.assertEqual(sum(len(u["vocabulary"]) for u in CATALOG), 2050)
        vocab_ids = [v["id"] for u in CATALOG for v in u["vocabulary"]]
        self.assertEqual(len(set(vocab_ids)), 2050)
        for unit_id, questions in QUESTION_BANK.items():
            self.assertEqual(len(questions), 20)
            self.assertIn(len(UNIT_DETAILS[unit_id][0].split()), (3, 4))
            self.assertTrue(UNIT_DETAILS[unit_id][1])
            self.assertTrue(UNIT_DETAILS[unit_id][2])
            for index, q in enumerate(questions, 1):
                self.assertEqual(q["id"], f"u{unit_id:03d}-q{index:02d}")
                self.assertEqual(len(set(q["options"])), 4)
                self.assertIn(q["correct_index"], range(4))
                self.assertTrue(q["explanation"])
                self.assertTrue(q["instruction"])
            # Correct answer placement should not turn into a fixed-letter exercise.
            self.assertEqual({q["correct_index"] for q in questions}, {0, 1, 2, 3})

    def test_original_questions_match_reviewed_content(self):
        original = {i: QUESTION_BANK[i] for i in range(1, 21)}
        digest = hashlib.sha256(json.dumps(original, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        self.assertEqual(digest, "4526706e3e0ea10024e7d0ec5af943711bb6ef5c534c9a6f1550fa346c2e7a20")

    def test_new_questions_are_complete_and_not_repeated_in_a_unit(self):
        for unit_id in range(21, 171):
            seen = set()
            positions = []
            for q in QUESTION_BANK[unit_id]:
                self.assertTrue(all(option.strip() for option in q["options"]))
                self.assertGreaterEqual(len(q["explanation"].split()), 4)
                self.assertNotIn("TODO", q["prompt"] + q["explanation"])
                # Capitalization itself is the target in unit 126.
                if unit_id != 126:
                    self.assertEqual(len({option.casefold().strip() for option in q["options"]}), 4, q["id"])
                key = (q["prompt"], q["instruction"], tuple(sorted(q["options"])))
                self.assertNotIn(key, seen, q["id"])
                seen.add(key)
                positions.append(q["correct_index"])
            self.assertEqual([positions.count(i) for i in range(4)], [5, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()
