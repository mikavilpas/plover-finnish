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
    reference_word = yield character.at_least(1).concat()

    yield string("-av").optional()
    gradation_class = (yield number.optional()) or ""

    return [word, klass, reference_word, "av" + gradation_class or ""]
