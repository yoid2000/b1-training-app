"""Bundle the authored rule guides for all 170 syllabus units."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "tools" / "curriculum"


def build(destination=None):
    tutorials = {}
    for source in sorted(SOURCES.glob("tutorials_*.txt")):
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip() or line.startswith("#"):
                continue
            try:
                number, pattern, rules, examples, remember = [part.strip() for part in line.split("|")]
                unit_id = int(number)
                if unit_id in tutorials:
                    raise ValueError(f"Duplicate unit {unit_id}")
                examples = [dict(zip(("de", "en"), [part.strip() for part in example.split("=>")], strict=True))
                            for example in examples.split("~")]
                tutorial = {"unit_id": unit_id, "pattern": pattern,
                            "rules": [rule.strip() for rule in rules.split("~")],
                            "examples": examples, "remember": remember}
                assert 2 <= len(tutorial["rules"]) <= 4
                assert len(examples) == 2
                assert all(tutorial["rules"]) and pattern and remember
                assert all(example["de"] and example["en"] for example in examples)
                tutorials[unit_id] = tutorial
            except (AssertionError, ValueError) as exc:
                raise ValueError(f"Invalid tutorial in {source.name}:{line_number}") from exc
    syllabus_ids = {unit["id"] for unit in json.loads((ROOT / "data" / "syllabus.json").read_text(encoding="utf-8"))}
    if set(tutorials) != syllabus_ids:
        raise ValueError(f"Missing tutorials: {sorted(syllabus_ids - tutorials.keys())}; extra: {sorted(tutorials.keys() - syllabus_ids)}")
    target = Path(destination) if destination else ROOT / "data" / "tutorials.json"
    target.write_text(json.dumps([tutorials[i] for i in sorted(tutorials)], ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    print(f"Bundled {len(tutorials)} tutorials with {sum(len(t['examples']) for t in tutorials.values())} translated examples.")


if __name__ == "__main__":
    build()
