from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_korkea(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "hilpeä;adjective-korkea"
    (hilpe, ä) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    hilpeämpi = hilpe + ä + "mpi"
    hilpein   = hilpe + "in"

    return Adjective(positive    = inflect_with(word, "korkea", gradation_fn),
                     comparative = inflect_as(hilpeämpi, "suurempi"),
                     superlative = inflect_as(hilpein, "sisin"))
