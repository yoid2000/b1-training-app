"""Small authoring helpers; no network or language model is used at build/runtime."""
import random

LESSONS = {}


def question(prompt, correct, wrong, explanation, instruction="Choose the correct answer."):
    options = [correct, *wrong]
    if len(options) != 4 or len(set(options)) != 4:
        raise ValueError((prompt, options))
    if not all(isinstance(x, str) and x.strip() for x in [prompt, *options, explanation]):
        raise ValueError(prompt)
    return dict(prompt=prompt, options=options, correct_index=0, explanation=explanation, instruction=instruction)


def gaps(unit, choices, text, reasons):
    """Rows contain a sentence, its answer, and optionally a specific explanation."""
    questions = LESSONS.setdefault(unit, [])
    for line in text.strip().splitlines():
        row = [x.strip() for x in line.split("|")]
        prompt, correct = row[:2]
        why = row[2] if len(row) > 2 else reasons[correct] if isinstance(reasons, dict) else reasons.format(answer=correct)
        pool = [x for x in choices.split("|") if x != correct and (unit == 126 or x.casefold() != correct.casefold())]
        if unit != 126 and correct[0].isupper():
            pool = [x[0].upper()+x[1:] for x in pool]
        random.Random(f"distractors-{unit}-{len(questions)}").shuffle(pool)
        questions.append(question(prompt, correct, pool[:3], why, "Complete the sentence in standard written German."))


def meanings(unit, text, labels, instruction="What does the highlighted construction express?"):
    """Explicit scenario/category pairs, with authored interpretations and explanations."""
    questions = LESSONS.setdefault(unit, [])
    for line in text.strip().splitlines():
        sentence, key = [x.strip() for x in line.rsplit("|", 1)]
        correct, why = labels[key]
        wrong = [v[0] for k, v in labels.items() if k != key]
        random.Random(f"meaning-{unit}-{len(questions)}").shuffle(wrong)
        questions.append(question(sentence, correct, wrong[:3], why, instruction))


def explicit(unit, text, instruction="Choose the correct answer."):
    for line in text.strip().splitlines():
        prompt, correct, a, b, c, why = [x.strip() for x in line.split("|")]
        LESSONS.setdefault(unit, []).append(question(prompt, correct, [a, b, c], why, instruction))


def clauses(unit, connector, contexts):
    """Twenty authored clause contexts: prefix | subject | middle | finite verb | infinitive."""
    for row in contexts.strip().splitlines():
        prefix, subject, middle, verb, infinitive = [x.strip() for x in row.split("|")]
        correct = f"{subject} {middle} {verb}".replace("  ", " ")
        wrong = [f"{subject} {verb} {middle}", f"{verb} {subject} {middle}", f"{subject} {middle} zu {infinitive}"]
        LESSONS.setdefault(unit, []).append(question(f"{prefix} {connector} ___. (Wörter: {infinitive}; {subject}; {middle})", correct, wrong,
            f"{connector.capitalize()} introduces a subordinate clause, so the finite verb '{verb}' comes last.",
            "Choose the correctly ordered subordinate clause in standard written German."))
