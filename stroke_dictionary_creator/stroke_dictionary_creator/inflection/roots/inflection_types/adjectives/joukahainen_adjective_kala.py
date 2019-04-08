from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_kala(word, gradation_fn = base.identity) -> Adjective:

    # arka is the example word
    (ar, a) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)
    arempi  = ar + "empi"
    arin    = ar + "in"

    return Adjective(positive    = inflect_with(word, "kala", gradation_fn),
                     comparative = inflect_as(arempi, "suurempi"),
                     superlative = inflect_as(arin, "sisin"))
