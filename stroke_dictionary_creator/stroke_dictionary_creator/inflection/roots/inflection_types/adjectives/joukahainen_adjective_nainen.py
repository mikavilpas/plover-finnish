from .. import base
from .adjective import Adjective, inflect_as, inflect_with


def joukahainen_adjective_nainen(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "sammalinen;adjective-nainen"
    (sammali, _nen) = base.reverse_parse(gradation_fn(word), base.word_nen_ending)

    sammalisempi = sammali + "sempi"
    sammalisin   = sammali + "sin"

    return Adjective(positive    = inflect_with(word, "nainen", gradation_fn),
                     comparative = inflect_as(sammalisempi, "suurempi"),
                     superlative = inflect_as(sammalisin, "sisin"))
