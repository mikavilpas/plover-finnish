# -*- coding: utf-8 -*-

from voikko import inflect_word
from parsy import *
from operator import concat

compound_word_separator = string("=")

# E.g. "Ruthenberg" is defined as Ruthen|berg, showing the morpheme boundary of
# the Swedish word "berg". This holds no meaning in Finnish, so this is best
# ignored.
empty_char = char_from("|").result("")
word_char =   letter | whitespace | digit | char_from(".,-_'") \
            | compound_word_separator | empty_char

# the classes require a specific format in Finnish that must be honored
noun      = string("noun").result("subst")
adjective = string("adjective").result("subst") # some forms are handled as nouns in the inflector
verb      = string("verb").result("verbi")

pronoun_fst   = string("pnoun_firstname").result("subst")
pronoun_lst   = string("pnoun_lastname").result("subst")
pronoun_misc  = string("pnoun_misc").result("subst")
pronoun_place = string("pnoun_place").result("subst")

pronoun = pronoun_fst | pronoun_lst | pronoun_misc | pronoun_place

class_with_no_inflection = string_from("abbreviation",
                                       "adverb",
                                       "conjunction",
                                       "interjection",
                                       "prefix")

word_class = noun | adjective | verb | pronoun | class_with_no_inflection

@generate
def word_and_class():
    word = yield word_char.at_least(1).concat()
    yield string(";")
    klass = yield word_class
    yield string("-")
    reference_word = yield word_char.at_least(1).concat()

    return [word, klass + "-" + reference_word]

def is_custom_compound_noun(word):
    return "=" in word

def not_inflectable(word, infclass):
    no_inflectable_reference_word = infclass.endswith("None")

    # this could be allowed later, since they actually technically can be
    # inflected
    custom_compound_noun = is_custom_compound_noun(word)

    return no_inflectable_reference_word or custom_compound_noun

def inflected_forms(word_and_infclass):
    (word, infclass) = word_and_class.parse(word_and_infclass)

    # The inflections for all words cannot be retrieved. Some words have very
    # irregular forms that the inflector can only parse, not produce.
    #
    # An example: yö (night) - yön (the night's), öin (with nights) - öiden
    # (nights')
    if not_inflectable(word, infclass):
        # this could be allowed later, since they actually technically can be
        # inflected
        if is_custom_compound_noun(word):
            print("    skipping custom compound word {}".format(word))
            return set()
        return set([word])
    else:
        inflections = inflect_word.inflect_word(word, infclass).values()
        return set(inflections)
