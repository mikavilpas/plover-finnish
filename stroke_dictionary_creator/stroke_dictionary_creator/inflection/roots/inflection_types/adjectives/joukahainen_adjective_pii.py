from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_pii(word, gradation_fn = base.identity) -> Adjective:
    # the word peeaa only

    (peea, _) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    # The example word is "peeaa;adjective-pii"
    peeaampi = word + "mpi"
    peeain   = peea + "in"

    return Adjective(positive    = inflect_with(word, "pii", gradation_fn),
                     comparative = inflect_as(peeaampi, "suurempi"),
                     superlative = inflect_as(peeain, "sisin"))
