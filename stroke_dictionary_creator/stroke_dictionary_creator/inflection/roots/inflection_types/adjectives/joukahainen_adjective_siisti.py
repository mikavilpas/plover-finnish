from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_siisti(word, gradation_fn = base.identity) -> Adjective:
    # just the adjective "siisti" in this class

    # The example word is "siisti;adjective-siisti"
    (siist, i) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)
    siistimpi  = word + "mpi"
    siistein   = siist + "ein"

    return Adjective(positive    = inflect_with(word, "siisti", gradation_fn),
                     comparative = inflect_as(siistimpi, "suurempi"),
                     superlative = inflect_as(siistein, "sisin"))
