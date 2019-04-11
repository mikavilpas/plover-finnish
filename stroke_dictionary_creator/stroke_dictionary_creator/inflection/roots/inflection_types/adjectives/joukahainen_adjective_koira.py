from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_koira(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "märkä;adjective-koira-av5"
    (mä, r, _ä) = base.reverse_parse(gradation_fn(word), base.root_and_cv_ending)

    märempi = mä + r + "empi"
    märin   = mä + r + "in"

    return Adjective(positive    = inflect_with(word, "koira", gradation_fn),
                     comparative = inflect_as(märempi, "suurempi"),
                     superlative = inflect_as(märin, "sisin"))
