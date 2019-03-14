from parsy import *
from operator import concat
from .roots.tokens import character, number

compound_word_separator = string("=")

# E.g. "Ruthenberg" is defined as Ruthen|berg, showing the morpheme boundary of
# the Swedish word "berg". This holds no meaning in Finnish, so this is best
# ignored.
empty_char = char_from("|").result("")
word_char  =  letter | whitespace | digit | char_from(".,-_'") \
            | compound_word_separator | empty_char

noun      = string("noun")
adjective = string("adjective")
verb      = string("verb")

pronoun_fst   = string("pnoun_firstname")
pronoun_lst   = string("pnoun_lastname")
pronoun_misc  = string("pnoun_misc")
pronoun_place = string("pnoun_place")

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
    reference_word = yield character.at_least(1).concat()

    yield string("-av").optional()
    gradation_number = (yield number.optional())
    gradation_class  = "av" + gradation_number if gradation_number else None

    return [word, klass, reference_word, gradation_class]
