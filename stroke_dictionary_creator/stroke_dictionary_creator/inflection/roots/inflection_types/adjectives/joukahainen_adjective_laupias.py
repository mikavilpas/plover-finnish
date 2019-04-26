from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_laupias(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "laupias;adjective-laupias"
    (laupi, a, _s) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)
    laupia         = laupi + a

    # no need for umlauts (only one word in this class)
    vastasyntyneempi = laupia + "ampi"
    vastasyntynein   = laupia + "in"

    return Adjective(positive    = inflect_with(word, "laupias", gradation_fn),
                     comparative = inflect_as(vastasyntyneempi, "suurempi"),
                     superlative = inflect_as(vastasyntynein, "sisin"))
