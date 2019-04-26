from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_loppu(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "pikku;adjective-loppu"
    (pik, u) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    # no need for umlauts (only one word in this class)
    pikumpi = pik + u + "mpi"
    pikuin  = pik + u + "in"

    return Adjective(positive    = inflect_with(word, "loppu", gradation_fn),
                     comparative = inflect_as(pikumpi , "suurempi"),
                     superlative = inflect_as(pikuin, "sisin"))
