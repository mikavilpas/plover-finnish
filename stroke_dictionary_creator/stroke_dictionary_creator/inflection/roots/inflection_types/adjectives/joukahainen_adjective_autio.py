from .adjective import inflect_as, inflect_with, Adjective
from .. import base

def joukahainen_adjective_autio(word, gradation_fn = base.identity) -> Adjective:
    riiviömpi = word + "mpi"
    riiviöin  = word + "in"

    return Adjective(positive    = inflect_with(word, "autio", gradation_fn),
                     comparative = inflect_as(riiviömpi, "suurempi"),
                     superlative = inflect_as(riiviöin, "sisin"))
