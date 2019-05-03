from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_paperi(word, gradation_fn = base.identity) -> Adjective:
    # adjectives that end in "Ci" (consonant + i)

    # The example word is "immuuni;adjective-paperi"
    (immuun, i) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)
    immuunimpi      = immuun + "impi"
    immuunein       = immuun + "ein"

    return Adjective(positive    = inflect_with(word, "paperi", gradation_fn),
                     comparative = inflect_as(immuunimpi, "suurempi"),
                     superlative = inflect_as(immuunein, "sisin"))
