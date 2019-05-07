from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_vastaus(word, gradation_fn = base.identity) -> Adjective:
    """The words 'symppis' and 'veres' only."""

    # The example word is "symppis;adjective-vastaus"
    (sympp, i, s) = base.reverse_parse(word, base.root_and_vc_ending)
    symppiksempi  = sympp + i + "ksempi"
    syppiksin     = sympp + i + "ksin"

    return Adjective(positive    = inflect_with(word, "vastaus", gradation_fn),
                     comparative = inflect_as(symppiksempi, "suurempi"),
                     superlative = inflect_as(syppiksin, "sisin"))
