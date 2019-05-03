from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_risti(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "pinkki;adjective-risti-av1"
    (pink, i) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)
    pinkimpi  = pink + i + "mpi"
    pinkein   = pink + "ein"

    return Adjective(positive    = inflect_with(word, "risti", gradation_fn),
                     comparative = inflect_as(pinkimpi, "suurempi"),
                     superlative = inflect_as(pinkein, "sisin"))
