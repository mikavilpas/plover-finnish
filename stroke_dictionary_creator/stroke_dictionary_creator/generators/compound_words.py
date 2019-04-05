from parsy import ParseError

from .two_stroke_words import join_strokes
from .short_words import short_word
from .two_stroke_words import two_strokes
from typing import List, Tuple

def safe_parse(p, text):
    try:
        return p.parse(text)
    except ParseError:
        pass

def split_compound_word(word_info: str) -> Tuple[List[str], str]:
    """Takes a word in the form 'anteeksi=antaa;verb-kaivaa-av1'"""
    parts = word_info.split("=")
    return (parts[0:-1], parts[-1])

def combine(leading_strokes: List[List[str]], trailing_strokes: List[List[str]]) -> List[Tuple[str, str]]:
    # example data:
    # leading_strokes: [['määrätyn', 'PHA*R/TAON']]
    # trailing_strokes: [['lainen', 'HRAINe'], ['laise', 'HRAISe'], ...]
    results: List[Tuple[str, str]] = []
    for (leading_word, leading) in leading_strokes:
        for (trailing_word, trailing) in trailing_strokes:
            word = leading_word + trailing_word
            word_and_stroke = (word, join_strokes(leading, trailing))
            results.append(word_and_stroke)
    return results

def strokefy_compound_word(inflection_fn, word_info: str) -> List[Tuple[str, str]]:
    def make_stroke(word):
        result = safe_parse(short_word, word)
        if result:
            return [word, result]
        return two_strokes(word)

    # for the word_info 'anteeksi=antaa;verb-kaivaa-av1',
    # - leading_parts contains ['anteeksi']
    # - last_part contains 'antaa;verb-kaivaa-av1', and thus can be inflected
    (leading_parts, last_part) = split_compound_word(word_info)

    inflections      = inflection_fn(last_part)
    leading_strokes  = [make_stroke(word) for word in leading_parts]
    trailing_strokes = [make_stroke(i) for i in inflections]
    strokes          = combine(leading_strokes, trailing_strokes)

    return strokes
