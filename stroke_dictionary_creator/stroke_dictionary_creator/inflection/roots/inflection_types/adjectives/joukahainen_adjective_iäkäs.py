from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_iäkäs(word, gradation_fn = base.identity) -> Adjective:

    # all words in this group are av2 and end with "kas"/"käs"
    (hapokk, a, s) = base.reverse_parse(gradation_fn(word), base.root_and_vc_ending)
    hapokkaampi    = hapokk + a + a + "mpi"
    hapokkain      = hapokk + a + "in"

    return Adjective(positive    = inflect_with(word, "iäkäs", gradation_fn),
                     comparative = inflect_as(hapokkaampi, "suurempi"),
                     superlative = inflect_as(hapokkain, "sisin"))
