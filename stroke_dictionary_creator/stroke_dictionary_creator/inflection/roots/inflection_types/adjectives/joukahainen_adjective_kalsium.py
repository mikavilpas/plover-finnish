from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_kalsium(word, gradation_fn = base.identity) -> Adjective:

    kosher     = word
    kosherimpi = kosher + "impi"
    kosherein  = kosher + "ein"

    return Adjective(positive    = inflect_with(word, "kalsium", gradation_fn),
                     comparative = inflect_as(kosherimpi, "suurempi"),
                     superlative = inflect_as(kosherein, "sisin"))
