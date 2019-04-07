from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_hame(word, gradation_fn = base.identity) -> Adjective:
    (ah, n, e) = base.reverse_parse(word,
                                    base.root_and_cv_ending)

    ahne     = ah + n + e
    ahneempi = ahne + e + "mpi"
    ahnein   = ahne + "in"

    return Adjective(positive    = inflect_with(word, "hame", gradation_fn),
                     comparative = inflect_as(ahneempi, "suurempi"),
                     superlative = inflect_as(ahnein, "sisin"))
