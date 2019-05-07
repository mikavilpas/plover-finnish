from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_vieras(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "ahdas;adjective-vieras-av2"
    (aht, a, s) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)

    ahtaampi = aht + a + a + "mpi"
    ahtain   = aht + a + "in"

    return Adjective(positive    = inflect_with(word, "vieras", gradation_fn),
                     comparative = inflect_as(ahtaampi, "suurempi"),
                     superlative = inflect_as(ahtain, "sisin"))
