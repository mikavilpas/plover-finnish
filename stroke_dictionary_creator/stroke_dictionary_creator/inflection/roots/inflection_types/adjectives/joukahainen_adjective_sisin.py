from .. import base
from .adjective import AdjectiveNoPositive, inflect_as, inflect_with


def joukahainen_adjective_sisin(word,
                                gradation_fn = base.identity) -> AdjectiveNoPositive:
    """Special adjectives that are missing the positive form, but behave like
    normal adjectives otherwise."""

    # The example word is "ylin;adjective-sisin"
    (yl, i, n) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)
    ylempi     = yl + "empi"

    return AdjectiveNoPositive(comparative = inflect_as(ylempi, "suurempi"),
                               superlative = inflect_as(word, "sisin"))
