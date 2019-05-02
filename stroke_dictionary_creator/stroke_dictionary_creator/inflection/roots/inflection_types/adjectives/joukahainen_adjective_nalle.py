from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_nalle(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "söde;adjective-nalle"
    söde    = word
    södempi = söde + "mpi"
    södein  = söde + "in"

    return Adjective(positive    = inflect_with(söde, "nalle", gradation_fn),
                     comparative = inflect_as(södempi, "suurempi"),
                     superlative = inflect_as(södein, "sisin"))
