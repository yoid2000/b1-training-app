"""Build all 3,000 additional questions from reviewed local authoring tables."""
import json
from copy import deepcopy
from pathlib import Path
import random
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.curriculum.core import LESSONS
from tools.curriculum.metadata import METADATA
from tools.curriculum import units021_050, units051_080, units081_106, units107_128, units129_144, units145_158, units159_170

ROOT = Path(__file__).resolve().parents[1]


def build(destination=None):
    syllabus = {u['id']: u for u in json.loads((ROOT/'data/syllabus.json').read_text(encoding='utf-8'))}
    if set(LESSONS) != set(range(21,171)) or set(METADATA) != set(LESSONS):
        raise ValueError('Missing or extra units')
    result = []
    for unit_id in range(21,171):
        title, goal_de = METADATA[unit_id]
        questions = deepcopy(LESSONS[unit_id])
        if len(questions)!=20 or len(title.split()) not in (3,4):
            raise ValueError((unit_id, len(questions), title))
        seen=set()
        positions = list(range(4))*5
        random.Random(f'positions-{unit_id}').shuffle(positions)
        for i,q in enumerate(questions,1):
            key=(q['prompt'],tuple(q['options']),q['instruction'])
            if key in seen:
                raise ValueError(('Duplicate question',unit_id,i))
            seen.add(key)
            correct=q['options'].pop(0)
            random.Random(f'{unit_id}-{i}').shuffle(q['options'])
            q['options'].insert(positions[i-1], correct)
            q.update(id=f'u{unit_id:03d}-q{i:02d}',unit_id=unit_id,correct_index=positions[i-1])
        result.append(dict(id=unit_id,title=title,goal_en=syllabus[unit_id]['goal_en'],goal_de=goal_de,questions=questions))
    target=Path(destination) if destination else ROOT/'data/questions_021_170.json'
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f'Built {len(result)} units with {sum(len(u["questions"]) for u in result):,} questions.')


if __name__=='__main__':
    build()
