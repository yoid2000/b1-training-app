"""Offline German practice server. Run with: python app.py"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
from http.cookies import CookieError, SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import sqlite3
from urllib.parse import urlsplit

from content import QUESTION_BANK, UNIT_DETAILS

ROOT = Path(__file__).resolve().parent
CATALOG = json.loads((ROOT / "data" / "syllabus.json").read_text(encoding="utf-8"))
UNITS = {unit["id"]: unit for unit in CATALOG}
for unit_id, (title, goal_en, goal_de) in UNIT_DETAILS.items():
    UNITS[unit_id].update(title=title, goal_en=goal_en, goal_de=goal_de)
QUESTIONS = {q["id"]: q for questions in QUESTION_BANK.values() for q in questions}
TRANSLATIONS = json.loads((ROOT / "data" / "question_translations.json").read_text(encoding="utf-8"))
if set(TRANSLATIONS) != set(QUESTIONS) or any(
    t["de"] != QUESTIONS[qid]["prompt"] or not isinstance(t["en"], str) or not t["en"].strip()
    for qid, t in TRANSLATIONS.items()
):
    raise ValueError("Every question must have an English translation matching its current prompt.")
TUTORIALS = {tutorial["unit_id"]: tutorial for tutorial in json.loads(
    (ROOT / "data" / "tutorials.json").read_text(encoding="utf-8"))}
if set(TUTORIALS) != set(UNITS):
    raise ValueError("Every syllabus unit must have a grammar tutorial.")


class AppError(Exception):
    def __init__(self, message, status=400):
        self.message, self.status = message, status


class Store:
    def __init__(self, path):
        self.path = str(path)
        with self.connect() as db:
            db.execute("PRAGMA journal_mode=WAL")
            db.executescript("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY, name TEXT NOT NULL COLLATE NOCASE UNIQUE,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS browser_sessions (
                    token TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id),
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
                CREATE TABLE IF NOT EXISTS practice (
                    id TEXT PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id),
                    unit_id INTEGER, mode TEXT NOT NULL, question_ids TEXT NOT NULL,
                    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, completed_at TEXT
                );
                CREATE TABLE IF NOT EXISTS answers (
                    practice_id TEXT NOT NULL REFERENCES practice(id),
                    question_id TEXT NOT NULL, choice INTEGER NOT NULL, correct INTEGER NOT NULL,
                    answered_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (practice_id, question_id)
                );
                CREATE TABLE IF NOT EXISTS question_state (
                    user_id INTEGER NOT NULL REFERENCES users(id), question_id TEXT NOT NULL,
                    correct INTEGER NOT NULL, updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (user_id, question_id)
                );
                CREATE INDEX IF NOT EXISTS practice_user ON practice(user_id, unit_id);
            """)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=15)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys=ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    def dashboard(self, db, user):
        units = []
        completed = set()
        for unit_id, questions in QUESTION_BANK.items():
            history = db.execute("""
                SELECT p.id, p.completed_at, COUNT(a.question_id) answered,
                       COALESCE(SUM(a.correct), 0) score
                FROM practice p LEFT JOIN answers a ON p.id=a.practice_id
                WHERE p.user_id=? AND p.unit_id=? AND p.mode='unit'
                GROUP BY p.id ORDER BY p.rowid DESC
            """, (user["id"], unit_id)).fetchall()
            done = [p for p in history if p["completed_at"]]
            if done:
                completed.add(unit_id)
            unit = UNITS[unit_id]
            units.append({"id": unit_id, "title": unit["title"], "stage": unit["stage"],
                          "completed": bool(done), "started": bool(history),
                          "answered": history[0]["answered"] if history else 0,
                          "best": max((p["score"] for p in done), default=None),
                          "total": len(questions)})
        next_id = next((i for i in QUESTION_BANK if i not in completed), None)
        for unit in units:
            unit["available"] = unit["completed"] or unit["id"] == next_id
        stats = db.execute("""
            SELECT COUNT(*) attempts, COALESCE(SUM(a.correct),0) correct
            FROM answers a JOIN practice p ON p.id=a.practice_id WHERE p.user_id=?
        """, (user["id"],)).fetchone()
        mistakes = db.execute("SELECT COUNT(*) FROM question_state WHERE user_id=? AND correct=0",
                              (user["id"],)).fetchone()[0]
        active_review = db.execute("""
            SELECT id FROM practice WHERE user_id=? AND mode='review' AND completed_at IS NULL
            ORDER BY rowid DESC LIMIT 1
        """, (user["id"],)).fetchone()
        return {"user": dict(user), "units": units, "next_unit": next_id,
                "completed": len(completed), "prepared": len(QUESTION_BANK), "syllabus_total": len(UNITS),
                "attempts": stats["attempts"], "correct": stats["correct"], "mistakes": mistakes,
                "active_review": active_review["id"] if active_review else None}

    def start(self, db, user, body):
        # Serialize starts and answers so concurrent browser tabs cannot duplicate a run.
        db.execute("BEGIN IMMEDIATE")
        mode = body.get("mode", "unit")
        if mode == "review":
            existing = db.execute("""
                SELECT id FROM practice WHERE user_id=? AND mode='review' AND completed_at IS NULL
                ORDER BY rowid DESC LIMIT 1
            """, (user["id"],)).fetchone()
            if existing:
                return {"id": existing["id"]}
            ids = [r[0] for r in db.execute("""
                SELECT question_id FROM question_state WHERE user_id=? AND correct=0
                ORDER BY RANDOM() LIMIT 20
            """, (user["id"],))]
            if not ids:
                raise AppError("No mistakes to review yet.")
            unit_id = None
        elif mode == "unit":
            unit_id = body.get("unit_id")
            if type(unit_id) is not int or unit_id not in QUESTION_BANK:
                raise AppError("This unit is not available yet.", 404)
            summary = self.dashboard(db, user)
            unit = next(u for u in summary["units"] if u["id"] == unit_id)
            if not unit["available"]:
                raise AppError("Finish the preceding units first.", 403)
            existing = db.execute("""
                SELECT id FROM practice WHERE user_id=? AND unit_id=? AND mode='unit'
                AND completed_at IS NULL ORDER BY rowid DESC LIMIT 1
            """, (user["id"], unit_id)).fetchone()
            if existing:
                return {"id": existing["id"]}
            ids = [q["id"] for q in QUESTION_BANK[unit_id]]
        else:
            raise AppError("Unknown practice mode.")
        practice_id = secrets.token_urlsafe(18)
        db.execute("INSERT INTO practice(id,user_id,unit_id,mode,question_ids) VALUES(?,?,?,?,?)",
                   (practice_id, user["id"], unit_id, mode, json.dumps(ids)))
        return {"id": practice_id}

    def practice(self, db, user, practice_id):
        row = db.execute("SELECT * FROM practice WHERE id=? AND user_id=?",
                         (practice_id, user["id"])).fetchone()
        if not row:
            raise AppError("Practice session not found.", 404)
        answers = {r["question_id"]: dict(r) for r in db.execute(
            "SELECT question_id, choice, correct FROM answers WHERE practice_id=?", (practice_id,))}
        questions = []
        for qid in json.loads(row["question_ids"]):
            q = QUESTIONS[qid]
            public = {k: q[k] for k in ("id", "prompt", "options", "instruction", "unit_id")}
            public["translation_en"] = TRANSLATIONS[qid]["en"]
            public["answer"] = answers.get(qid)
            if qid in answers:
                public.update(correct_index=q["correct_index"], explanation=q["explanation"])
            questions.append(public)
        return {"id": row["id"], "mode": row["mode"], "unit": UNITS.get(row["unit_id"]),
                "questions": questions, "completed": bool(row["completed_at"]),
                "score": sum(a["correct"] for a in answers.values())}

    def answer(self, db, user, body):
        db.execute("BEGIN IMMEDIATE")
        practice_id = body.get("practice_id")
        if not isinstance(practice_id, str) or not practice_id:
            raise AppError("A practice session is required.")
        practice = self.practice(db, user, practice_id)
        qid, choice = body.get("question_id"), body.get("choice")
        if not isinstance(qid, str) or qid not in {q["id"] for q in practice["questions"]}:
            raise AppError("Question not found in this session.", 404)
        q = QUESTIONS[qid]
        if type(choice) is not int or not 0 <= choice < len(q["options"]):
            raise AppError("Choose one of the answers.")
        correct = int(choice == q["correct_index"])
        inserted = db.execute("""
            INSERT OR IGNORE INTO answers(practice_id,question_id,choice,correct) VALUES(?,?,?,?)
        """, (practice["id"], qid, choice, correct)).rowcount
        if inserted:
            db.execute("""
                INSERT INTO question_state(user_id,question_id,correct) VALUES(?,?,?)
                ON CONFLICT(user_id,question_id) DO UPDATE SET
                    correct=excluded.correct, updated_at=CURRENT_TIMESTAMP
            """, (user["id"], qid, correct))
        count = db.execute("SELECT COUNT(*) FROM answers WHERE practice_id=?", (practice["id"],)).fetchone()[0]
        if count == len(practice["questions"]):
            db.execute("UPDATE practice SET completed_at=COALESCE(completed_at,CURRENT_TIMESTAMP) WHERE id=?",
                       (practice["id"],))
        first = db.execute("SELECT choice,correct FROM answers WHERE practice_id=? AND question_id=?",
                           (practice["id"], qid)).fetchone()
        return {"correct": bool(correct), "correct_index": q["correct_index"],
                "explanation": q["explanation"], "first_answer": dict(first),
                "saved": bool(inserted), "completed": count == len(practice["questions"])}


class Handler(BaseHTTPRequestHandler):
    server_version = "DeutschPractice/1.0"

    def reply(self, status, data, *, cookie=None):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.headers_common()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        if cookie:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()
        self.wfile.write(payload)

    def headers_common(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "same-origin")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")

    def current_user(self, db):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
            token = cookie["practice_session"].value
        except (KeyError, ValueError, CookieError):
            raise AppError("Choose your profile to continue.", 401)
        user = db.execute("SELECT u.id,u.name FROM users u JOIN browser_sessions s ON u.id=s.user_id WHERE s.token=?",
                          (token,)).fetchone()
        if not user:
            raise AppError("Choose your profile to continue.", 401)
        return user

    def do_GET(self):
        try:
            path = urlsplit(self.path).path
            if path.startswith("/api/"):
                with self.server.store.connect() as db:
                    if path == "/api/users":
                        data = {"users": [dict(r) for r in db.execute("SELECT id,name FROM users ORDER BY name COLLATE NOCASE")],
                                "prepared": len(QUESTION_BANK), "questions": len(QUESTIONS)}
                    elif path == "/api/me":
                        data = self.server.store.dashboard(db, self.current_user(db))
                    elif path == "/api/syllabus":
                        self.current_user(db)
                        data = {"units": [{"id": u["id"], "title": u["title"], "stage": u["stage"],
                                            "prepared": u["id"] in QUESTION_BANK} for u in CATALOG]}
                    elif path.startswith("/api/tutorial/"):
                        self.current_user(db)
                        raw_id = path.removeprefix("/api/tutorial/")
                        if not raw_id.isascii() or not raw_id.isdecimal() or len(raw_id) > 3 or int(raw_id) not in TUTORIALS:
                            raise AppError("Tutorial not found.", 404)
                        unit_id = int(raw_id)
                        data = {"unit_id": unit_id, "title": UNITS[unit_id]["title"], "tutorial": TUTORIALS[unit_id]}
                    elif path.startswith("/api/practice/"):
                        data = self.server.store.practice(db, self.current_user(db), path.removeprefix("/api/practice/"))
                    else:
                        raise AppError("Page not found.", 404)
                self.reply(200, data)
            else:
                files = {"/": ("index.html", "text/html"), "/app.js": ("app.js", "text/javascript"),
                         "/style.css": ("style.css", "text/css"), "/favicon.svg": ("favicon.svg", "image/svg+xml")}
                if path not in files:
                    raise AppError("Page not found.", 404)
                name, mime = files[path]
                payload = (ROOT / "static" / name).read_bytes()
                self.send_response(200)
                self.headers_common()
                self.send_header("Content-Type", mime + "; charset=utf-8")
                self.send_header("Cache-Control", "no-cache")
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
        except AppError as exc:
            self.reply(exc.status, {"error": exc.message})
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception:
            import traceback
            traceback.print_exc()
            self.reply(500, {"error": "Something went wrong. Please try again."})

    def do_POST(self):
        try:
            # Only app-origin JSON requests can mutate state. No cross-origin CORS is enabled.
            if self.headers.get("Sec-Fetch-Site") == "cross-site":
                raise AppError("Cross-site requests are not allowed.", 403)
            origin = self.headers.get("Origin")
            if origin and origin != "http://" + self.headers.get("Host", ""):
                raise AppError("Request origin does not match this server.", 403)
            if self.headers.get("Content-Type", "").split(";")[0].strip() != "application/json":
                raise AppError("JSON is required.", 415)
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 8192:
                    raise ValueError
                body = json.loads(self.rfile.read(length))
                if not isinstance(body, dict):
                    raise ValueError
            except (ValueError, UnicodeDecodeError):
                raise AppError("Invalid request body.")
            cookie = None
            path = urlsplit(self.path).path
            with self.server.store.connect() as db:
                if path in ("/api/users", "/api/select-user"):
                    if path == "/api/users":
                        name = body.get("name", "")
                        if not isinstance(name, str) or not 1 <= len(name.strip()) <= 40 or any(ord(c) < 32 for c in name):
                            raise AppError("Use a name between 1 and 40 characters.")
                        try:
                            cursor = db.execute("INSERT INTO users(name) VALUES(?)", (name.strip(),))
                        except sqlite3.IntegrityError:
                            raise AppError("That profile already exists. Choose it from the list.", 409)
                        user_id = cursor.lastrowid
                    else:
                        user_id = body.get("user_id")
                        if type(user_id) is not int or not db.execute("SELECT id FROM users WHERE id=?", (user_id,)).fetchone():
                            raise AppError("Profile not found.", 404)
                    token = secrets.token_urlsafe(32)
                    db.execute("INSERT INTO browser_sessions(token,user_id) VALUES(?,?)", (token, user_id))
                    cookie = f"practice_session={token}; Path=/; HttpOnly; SameSite=Strict; Max-Age=31536000"
                    data = {"ok": True}
                elif path == "/api/logout":
                    user = self.current_user(db)
                    raw = SimpleCookie(self.headers.get("Cookie", ""))
                    db.execute("DELETE FROM browser_sessions WHERE token=? AND user_id=?",
                               (raw["practice_session"].value, user["id"]))
                    cookie = "practice_session=; Path=/; HttpOnly; SameSite=Strict; Max-Age=0"
                    data = {"ok": True}
                elif path == "/api/start":
                    data = self.server.store.start(db, self.current_user(db), body)
                elif path == "/api/answer":
                    data = self.server.store.answer(db, self.current_user(db), body)
                else:
                    raise AppError("Page not found.", 404)
            self.reply(200, data, cookie=cookie)
        except AppError as exc:
            self.reply(exc.status, {"error": exc.message})
        except (BrokenPipeError, ConnectionResetError):
            pass
        except Exception:
            import traceback
            traceback.print_exc()
            self.reply(500, {"error": "Something went wrong. Please try again."})


def create_server(host="0.0.0.0", port=8188, database=None):
    path = Path(database) if database else ROOT / "instance" / "practice.sqlite3"
    path.parent.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((host, port), Handler)
    server.daemon_threads = True
    server.store = Store(path)
    return server


def main():
    parser = argparse.ArgumentParser(description="Offline German B1 practice for a trusted local network.")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8188)
    parser.add_argument("--database", type=Path)
    args = parser.parse_args()
    server = create_server(args.host, args.port, args.database)
    print(f"Deutsch practice is running at http://localhost:{server.server_port}", flush=True)
    print(f"WLAN: open http://<this-machine-IP>:{server.server_port} on each device. Ctrl+C to stop.", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
