from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_ohut(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "ohut;adjective-ohut"
    (oh, u, _t) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)
    ohuempi     = oh + u + "empi"
    ohuin       = oh + u + "in"

    return Adjective(positive    = inflect_with(word, "ohut", gradation_fn),
                     comparative = inflect_as(ohuempi, "suurempi"),
                     superlative = inflect_as(ohuin, "sisin"))
