from parsy import *

from .generators import *
from .short_words import short_word
from .generators import morpheme
from functools import reduce
from operator import ior

def join_strokes(*strokes):
    return "/".join(strokes)

#
#
#
# Reduce the size of the word list by omitting very common suffices from it
# keep manually in sync with 10_suffixes.yaml
suffix = string_from(
    # the implementation of string_from will sort these longest first as well
    "nsa", "nsä", "mme", "nne"
    "sta", "stä", "ssa", "ssä",
    "lla", "llä", "lta", "ltä",
    "tta", "ttä", "ksi", "ine"
    "lle",
    "ni", "si", "na", "nä",
    "n", "t", "a,", "ä",
).result(None)

second_chord      = suffix << any_char.should_fail("end of word") | short_word
stroke_and_suffix = seq(short_word, second_chord)

def two_strokes(word):
    @generate("two stroke word")
    def two_strokes_parser():
        (s1, s2) = yield seq(short_word, second_chord)

        is_suffix_stroke = s2 is None
        if is_suffix_stroke:
            return [word, s1]
        else:
            return [word, join_strokes(s1, s2)]

    return two_strokes_parser.parse(word)
