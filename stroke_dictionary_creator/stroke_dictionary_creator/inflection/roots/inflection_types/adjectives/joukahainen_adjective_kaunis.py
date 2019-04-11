from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_kaunis(word, gradation_fn = base.identity) -> Adjective:
    # the adjectives kallis, kaunis only

    (kall, i, _s) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)

    kalliimpi = kall + i + i + "mpi"
    kallein   = kall + "ein"

    return Adjective(positive    = inflect_with(word, "kaunis", gradation_fn),
                     comparative = inflect_as(kalliimpi, "suurempi"),
                     superlative = inflect_as(kallein, "sisin"))
