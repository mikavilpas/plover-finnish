from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_uistin(word, gradation_fn = base.identity) -> Adjective:
    # the words avoin, valtoin

    # The example word is "avoin;adjective-uistin"
    (avo, i, n) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)

    avoimempi = avo + i + "mempi"
    avoimin   = avo + i + "min"

    return Adjective(positive    = inflect_with(word, "uistin", gradation_fn),
                     comparative = inflect_as(avoimempi, "suurempi"),
                     superlative = inflect_as(avoimin, "sisin"))
