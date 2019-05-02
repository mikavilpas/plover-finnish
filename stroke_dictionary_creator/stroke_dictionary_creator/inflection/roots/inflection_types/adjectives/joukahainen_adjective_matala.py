from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_matala(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "littana;adjective-matala"
    (littan, a) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    littanampi = littan + a + "mpi"
    littanin   = littan + "in"

    return Adjective(positive    = inflect_with(word, "matala", gradation_fn),
                     comparative = inflect_as(littanampi, "suurempi"),
                     superlative = inflect_as(littanin, "sisin"))
