from toolz import itertoolz


def conflict_strokes(load_file_function) -> dict:
    raw = load_file_function("../conflicts/manually_resolved_conflicts.yaml")
    strokes = strokefy(raw)
    return strokes

def strokefy(raw_dict: dict):
    results = {}
    for stroke_base, words in raw_dict.items():
        indices_words = zip(range(len(words)), words)
        for i, word in indices_words:
            stroke = repeat_stroke(stroke_base, i + 1)
            results[stroke] = word

    return results

def repeat_stroke(stroke_base, times: int):
    strokes = itertoolz.iterate(lambda s: s, stroke_base)
    return "/".join(itertoolz.take(times, strokes))
