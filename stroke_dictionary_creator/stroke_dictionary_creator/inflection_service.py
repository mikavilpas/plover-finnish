# -*- coding: utf-8 -*-

from voikko import inflect_word
from parsy import *

not_available = lambda inflections: inflections == {}

word_char = letter | whitespace | digit | char_from(".,-_")

no_inflection = None

# the classes require a specific format in Finnish that must be honored
noun      = string("noun").result("subst")
adjective = string("adjective").result("subst") # some forms are handled as nouns in the inflector
verb      = string("verb").result("verbi")

pronoun_fst   = string("pnoun_firstname").result("subst")
pronoun_lst   = string("pnoun_lastname").result("subst")
pronoun_misc  = string("pnoun_misc").result("subst")
pronoun_place = string("pnoun_place").result("subst")

pronoun = pronoun_fst | pronoun_lst | pronoun_misc

class_with_no_inflection = string_from("abbreviation",
                                       "adverb",
                                       "conjunction",
                                       "interjection").result(no_inflection)

word_class = noun | adjective | verb | pronoun | class_with_no_inflection

@generate
def word_and_class():
    word = yield word_char.at_least(1).concat()
    yield string(";")
    klass = yield word_class
    yield string("-")
    reference_word = yield word_char.at_least(1).concat()

    return [word, klass + "-" + reference_word]

def inflected_forms(word_and_infclass):
    (word, infclass) = word_and_class.parse(word_and_infclass)
    print(word, infclass)
    inflections = inflect_word.inflect_word(word, infclass)

    # The inflections for all words cannot be retrieved. Some words have very
    # irregular forms that the inflector can only parse, not produce.
    #
    # An example: yö (night) - yön (the night's), öin (with nights) - öiden
    # (nights')
    return None if not_available(inflections) else inflections
