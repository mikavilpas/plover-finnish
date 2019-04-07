from .adjective import inflect_as, inflect_with, Adjective
from .. import base

def joukahainen_adjective_asema(word, gradation_fn = base.identity) -> Adjective:

    (kiper, ä) = base.reverse_parse(word, base.root_and_end_vowel)

    kiperämpi = kiper + ä + "mpi"
    kiperin   = kiper + "in"

    return Adjective(positive    = inflect_with(word, "asema", gradation_fn),
                     comparative = inflect_as(kiperämpi, "suurempi"),
                     superlative = inflect_as(kiperin, "sisin"))
