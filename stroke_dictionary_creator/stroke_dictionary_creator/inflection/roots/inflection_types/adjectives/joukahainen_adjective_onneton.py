from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_onneton(word, gradation_fn = base.identity) -> Adjective:

    # suffix
    def s(text):
        return base.change_to_same_vowel_group_prefer_umlauts(word, text)

    # The example word is "hervoton;adjective-onneton"
    (alas, t, o, n) = base.reverse_parse(gradation_fn(word), base.root_and_cvc_ending)
    alastomampi     = alas + t + o + s("mampi")
    alastomin       = alas + t + o + "min"

    return Adjective(positive    = inflect_with(word, "onneton", gradation_fn),
                     comparative = inflect_as(alastomampi, "suurempi"),
                     superlative = inflect_as(alastomin, "sisin"))
