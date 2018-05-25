# -*- coding: utf-8 -*-

from voikko import inflect_word

not_available = lambda inflections: inflections == {}
guess = None

def inflected_forms(word, infclass = guess):
    inflections = inflect_word.inflect_word(word, infclass)

    # The inflections for all words cannot be retrieved. Some words have very
    # irregular forms that the inflector can only parse, not produce.
    #
    # An example: yö (night) - yön (the night's), öin (with nights) - öiden
    # (nights')
    return None if not_available(inflections) else inflections
