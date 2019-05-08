from .. import base
from .adjective import AdjectiveNotComparable, inflect_as, inflect_with


def joukahainen_adjective_loppu(word, gradation_fn = base.identity) -> AdjectiveNotComparable:

    # The example word is "pikku;adjective-loppu"
    (pik, u) = base.reverse_parse(gradation_fn(word), base.root_and_end_vowel)

    return AdjectiveNotComparable(word = inflect_with(word, "loppu", gradation_fn))
