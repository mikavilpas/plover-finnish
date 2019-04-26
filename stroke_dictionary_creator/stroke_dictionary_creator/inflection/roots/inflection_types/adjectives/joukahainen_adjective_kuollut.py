from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_kuollut(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "vasta=syntynyt;adjective-kuollut"
    (vastasyntyn, _y, _t) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)

    vastasyntyneempi = vastasyntyn + "eempi"
    vastasyntynein   = vastasyntyn + "ein"

    return Adjective(positive    = inflect_with(word, "kuollut", gradation_fn),
                     comparative = inflect_as(vastasyntyneempi, "suurempi"),
                     superlative = inflect_as(vastasyntynein, "sisin"))
