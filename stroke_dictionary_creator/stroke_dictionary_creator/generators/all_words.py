from parsy import *
from .short_words import short_word
from .two_stroke_words import two_strokes

all_words = two_strokes | short_word
