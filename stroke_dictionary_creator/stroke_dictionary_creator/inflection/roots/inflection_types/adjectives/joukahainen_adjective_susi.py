from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_susi(word, gradation_fn = base.identity) -> Adjective:
    """Just the adjective 'uusi'"""

    # The example word is "uusi;adjective-susi"
    (uu, s, _) = base.reverse_parse(gradation_fn(word), base.root_and_cv_ending)
    uudempi    = uu + "dempi"
    uusin      = word + "n"

    return Adjective(positive    = inflect_with(word, "susi", gradation_fn),
                     comparative = inflect_as(uudempi, "suurempi"),
                     superlative = inflect_as(uusin, "sisin"))
