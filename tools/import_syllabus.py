"""Regenerate bundled curriculum metadata from the original local text file."""

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def import_syllabus(source):
    text = source.read_text(encoding="utf-8")
    blocks = re.findall(r"^UNIT (\d{3}) - ([^\n]+)\n(.*?)(?=^UNIT \d{3} - |\Z)", text, re.M | re.S)
    units = []
    for number, heading, block in blocks:
        stage = re.search(r"Stage: (\S+)\s+Grammar mode: (\S+)", block)
        learn = re.search(r"Learn: (.*?)\nExample:", block, re.S)
        example = re.search(r"Example: (.*?)\nCompletion task:", block, re.S)
        vocab_text = block.split("Assigned vocabulary", 1)[1].split("Progress:", 1)[0]
        vocabulary = []
        for entry in re.split(r"\n  (?=V\d{4} )", "\n" + vocab_text)[1:]:
            entry = entry.strip()
            main, _, note = entry.partition("\n    Note:")
            main = " ".join(main.split())
            vocab_id, main = main.split(" ", 1)
            term, _, reference = main.rpartition(" - ")
            vocabulary.append({"id": vocab_id, "term": term, "source": reference,
                               "note": " ".join(note.split())})
        units.append({"id": int(number), "title": heading.capitalize(), "source_title": heading,
                      "stage": stage[1], "mode": stage[2], "goal_en": " ".join(learn[1].split()),
                      "example": " ".join(example[1].split()), "vocabulary": vocabulary})
    assert len(units) == 170, f"Expected 170 units, found {len(units)}"
    assert sum(len(u["vocabulary"]) for u in units) == 2050
    destination = ROOT / "data" / "syllabus.json"
    destination.parent.mkdir(exist_ok=True)
    destination.write_text(json.dumps(units, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Bundled {len(units)} units and 2050 vocabulary entries: {destination}")


if __name__ == "__main__":
    import_syllabus(ROOT / "resources" / "German_telc_B1_complete_syllabus_after_A1.txt")
