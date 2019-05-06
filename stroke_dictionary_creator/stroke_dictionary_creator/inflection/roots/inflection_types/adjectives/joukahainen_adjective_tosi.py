from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_tosi(word, gradation_fn = base.identity) -> Adjective:
    # the word täysi only

    (täy, s, i) = base.reverse_parse(gradation_fn(word), base.root_and_cv_ending)

    # The example word is "täysi;adjective-tosi"
    täydempi = täy + "dempi"
    täysin   = täy + s + i + "n"

    return Adjective(positive    = inflect_with(word, "tosi", gradation_fn),
                     comparative = inflect_as(täydempi, "suurempi"),
                     superlative = inflect_as(täysin, "sisin"))
