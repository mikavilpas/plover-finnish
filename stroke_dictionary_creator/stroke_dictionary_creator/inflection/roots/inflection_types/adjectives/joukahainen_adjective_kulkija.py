from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_kulkija(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "kinttana;adjective-kulkija"
    (kinttan, a) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    kinttanampi = kinttan + a + "mpi"
    kinttanin   = kinttan + a + "in"

    return Adjective(positive    = inflect_with(word, "kulkija", gradation_fn),
                     comparative = inflect_as(kinttanampi, "suurempi"),
                     superlative = inflect_as(kinttanin, "sisin"))
