from parsy import *

from .generators import *
from . import short_words as short

def strokes(*parsers):
    @generate
    def strokeify():
        result_strokes = yield seq(*parsers)
        return "/".join(result_strokes)

    return strokeify

two_strokes = strokes(short.short_word, short.short_word)
