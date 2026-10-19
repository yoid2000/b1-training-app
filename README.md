# Schritt · German B1 practice

A small, offline web app for a shared Linux machine and devices on a trusted WLAN.
Separate learner profiles, saved progress, grammar practice, and random mistake review.

For a Linux installation that starts automatically on reboot, see the [Linux installation and maintenance guide](docs/linux-installation.md). It includes shell scripts for installation, updates from Git or local edits, curriculum rebuilds, service control, and database backup/restore. Run these as your normal user; they request `sudo` only where needed.

## Run

Requires **Python 3.10 or newer**. No third-party packages, build step, API keys, or internet connection are needed.

```bash
python3 app.py
```

Open **http://localhost:8000** on the server, or **http://YOUR-LINUX-IP:8000** on other devices on the same WLAN. Run `hostname -I` on Linux to find the machine's address. The server listens on all network interfaces by default. If the machine has a firewall, allow TCP port 8000 from your trusted WLAN only.

On Windows, use `python app.py`. Stop the server with **Ctrl+C**.

Optional settings:

```bash
python3 app.py --host 127.0.0.1 --port 8080
python3 app.py --database /path/to/learner-progress.sqlite3
```

The default database is `instance/practice.sqlite3`, relative to the app directory. It is created automatically and excluded from Git. The server can be launched from any working directory. Back up the database while the app is stopped; restore it to the same location to recover profiles and progress.

## Learning flow

- Choose an existing profile or create one by name. Each browser remembers its selected profile. Switch profiles from the sidebar; different devices can choose different learners simultaneously.
- Work through all **170 units** in syllabus order. Every unit contains a short German and English grammar goal, the original syllabus example, assigned vocabulary, and **20 multiple-choice questions with English explanations**: **3,400 questions** in total.
- Open **Grammar tutorial** on a unit's introduction, question/answer pages, or results to read its rules, sentence pattern, two German examples with English translations, and a common pitfall. All **170 tutorials** stay hidden until requested. In mistake review, the button follows the current question's unit. Close the tutorial or press **Escape** to return to the same question; reading it does not affect scores or progress.
- Click an answer for immediate feedback and the correct answer. Use **Why this answer?** for a short English explanation. Other options remain clickable so you can explore them.
- The **first choice per question per attempt** counts. Clicking another option afterward never changes the saved result. Progress saves after each answer; returning to a unit resumes the unfinished attempt.
- Answer all 20 questions to complete a unit and unlock the next, regardless of score. No invented exam pass mark.
- **My units** lists started and completed units with brief titles. Open a completed unit to retake it. Previous attempt history and the best completed score remain saved.
- **Review mistakes** selects a random set of up to 20 questions whose latest recorded attempt was incorrect. A correct first choice in a later review or retake clears that question from the review list. Interrupted reviews resume their original selection.
- Home accuracy includes first choices across unit attempts, retakes, and reviews. A unit's best score includes completed unit attempts only.

All **170 units and 2,050 assigned vocabulary entries** are bundled in `data/syllabus.json`. All units now have practice questions and unlock sequentially. The full syllabus is visible under **My units → Full syllabus**. Vocabulary entries preserve the syllabus wording and notes, rather than inventing dictionary definitions.

Questions include sentence completion, grammatical forms, clause analysis, and interpretation. Later recognition units practise understanding constructions such as passive forms, reported speech, and regional variation. The original 400 questions, their options, and their IDs are unchanged, so existing progress remains compatible. Existing learners who finished unit 20 can continue directly to unit 21.

## Local network model

Profiles are a convenient learner selector, **without passwords**. Anyone with access to the app can select any profile. Browser sessions keep simultaneous users' selected profiles separate, and session ownership is checked for every practice and answer request. This app is intended for the trusted WLAN described above. Keep it off the public internet; use authentication and HTTPS if deploying beyond that setting.

SQLite uses WAL mode, a connection per request, and transactional writes. The threaded server supports simultaneous learners. There are no external fonts, analytics, CDNs, AI calls, or remote services.

This is grammar practice based on the supplied syllabus, not an official telc product or a complete listening, speaking, reading, and writing exam course.

## Add or revise curriculum

`content.py` retains the original 400 questions for units 1–20 and loads the additional 3,000 concrete questions from `data/questions_021_170.json`. The later units' authoring sources are grouped under `tools/curriculum/`, with German titles and goals in `metadata.py` and English goals from the bundled syllabus. Local helpers expand explicit paradigms and sentence tables, supply authored explanations, and assign stable IDs and deterministic option positions. There is no runtime question generation or AI dependency.

To rebuild the later units after editing their authoring sources:

```bash
python3 tools/build_question_bank.py
```

Commit both the source edits and the regenerated JSON. Normal app startup reads the bundled JSON and does not import the authoring tools. First-choice answer positions in each new unit are balanced across A, B, C and D. Rebuilding identical sources produces identical output.

Grammar tutorials are authored in `tools/curriculum/tutorials_*.txt` and bundled in `data/tutorials.json`. Each row contains a unit number, sentence pattern, rules separated by `~`, two `German => English` examples separated by `~`, and a reminder, with the five fields separated by `|`. After editing, rebuild and commit the source and JSON:

```bash
python3 tools/build_tutorials.py
```

The builder checks that all 170 syllabus units have a tutorial. Tutorials load locally when requested and require no additional packages or services.

The original unit 1–20 question rows have six pipe-separated fields:

```text
Prompt | Correct option | Distractor 1 | Distractor 2 | Distractor 3 | English explanation
```

Keep existing IDs, question meanings, and option ordering stable once learners have answered them. For a materially different question, use a new ID and migrate existing data deliberately. Restart the server after deploying curriculum changes.

The original source remains excluded from Git under `resources/`. To regenerate the bundled metadata after editing the source:

```bash
python3 tools/import_syllabus.py
```

The import expects `resources/German_telc_B1_complete_syllabus_after_A1.txt`. Normal app startup only needs the bundled JSON and does not read the resources directory.

## Verify

```bash
python3 -m unittest discover -s tests -v
```

The tests exercise HTTP requests, independent profiles, saved attempts, sequential unlocking through all 170 units and 3,400 answers, retakes, review selection and clearing, concurrent starts and answers, request validation, persistence, complete bilingual metadata, and curriculum integrity. They also check all 170 tutorials, reproducible tutorial builds, and that reading tutorials leaves progress unchanged. A fingerprint check protects the original 400 questions from accidental changes.

Deployment-helper checks cover live SQLite WAL backups, imports/restores, saved progress, service settings, installation ownership, and HTTP startup checks. They use temporary files and do not invoke sudo or systemd. Bash syntax and a real Linux service/reboot check are separate from the Python suite.

An optional client check, if Node.js is installed, runs without browser dependencies:

```bash
node tests/client.mjs
```

It checks rendering and client state with a DOM stub, including answer feedback, explanations, saved first choices, navigation, results, escaped content, and optional tutorials on unit and review pages. It does not replace visual browser testing.

## Language references

The learning sequence and English goals follow the supplied syllabus. Targeted reference checks for the new spelling and regional-recognition material used the [official comma rules, §73](https://grammis.ids-mannheim.de/rechtschreibung/6203), [IDS guidance on regional perfect auxiliaries](https://grammis.ids-mannheim.de/kontrastive-grammatik/4173), and [Duden's Joghurt entry](https://www.duden.de/rechtschreibung/Joghurt). These links are developer references; using the app requires no network access.
