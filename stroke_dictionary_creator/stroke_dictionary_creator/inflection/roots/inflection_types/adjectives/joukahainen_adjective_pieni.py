from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_pieni(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "tyyni;adjective-pieni"
    (tyyn, i) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)
    tyynempi  = tyyn + "empi"
    tyynein   = tyyn + "in"

    return Adjective(positive    = inflect_with(word, "pieni", gradation_fn),
                     comparative = inflect_as(tyynempi, "suurempi"),
                     superlative = inflect_as(tyynein, "sisin"))
