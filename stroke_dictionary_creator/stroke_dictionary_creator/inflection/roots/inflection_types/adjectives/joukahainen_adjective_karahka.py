from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_karahka(word, gradation_fn = base.identity) -> Adjective:
    # adjectives ending in -kkA, all use av1 gradation

    # suffix
    def s(text):
        return base.change_to_same_vowel_group_prefer_umlauts(word, text)

    (sutja, k, a) = base.reverse_parse(gradation_fn(word), base.root_and_cv_ending)
    sutjak        = sutja + k

    sutjakampi = sutjak + a + "mpi"
    sutjakoin  = sutjak + s("oin")

    return Adjective(positive    = inflect_with(word, "karahka", gradation_fn),
                     comparative = inflect_as(sutjakampi, "suurempi"),
                     superlative = inflect_as(sutjakoin, "sisin"))
