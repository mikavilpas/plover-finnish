from .adjective import inflect_as, Adjective
from .. import base

def joukahainen_adjective_autio(word, gradation_fn = base.identity) -> Adjective:
    riiviömpi = word + "mpi"
    riiviöin  = word + "in"

    return Adjective(positive    = inflect_as(word, "autio", gradation_fn),
                     comparative = inflect_as(riiviömpi, "suurempi", None),
                     superlative = inflect_as(riiviöin, "sisin", None))
