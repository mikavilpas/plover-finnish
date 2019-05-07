from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_vapaa(word, gradation_fn = base.identity) -> Adjective:
    """The word 'vakaa' only."""

    # The example word is "vakaa;adjective-vapaa"
    (vaka, a) = base.reverse_parse(word, base.root_and_end_vowel)
    vakaampi = word + "mpi"
    vakain   = vaka + "in"

    return Adjective(positive    = inflect_with(word, "vapaa", gradation_fn),
                     comparative = inflect_as(vakaampi, "suurempi"),
                     superlative = inflect_as(vakain, "sisin"))
