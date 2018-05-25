# -*- coding: utf-8 -*-

from voikko import inflect_word
from parsy import *

not_available = lambda inflections: inflections == {}
guess = None

word_char = letter | whitespace | digit | char_from(".,-")
word_and_class = word_char.at_least(1).concat().sep_by(string(";"))

def inflected_forms(word_and_infclass):
    (word, infclass) = word_and_class.parse(word_and_infclass)
    inflections = inflect_word.inflect_word(word, infclass)

    # The inflections for all words cannot be retrieved. Some words have very
    # irregular forms that the inflector can only parse, not produce.
    #
    # An example: yö (night) - yön (the night's), öin (with nights) - öiden
    # (nights')
    return None if not_available(inflections) else inflections
