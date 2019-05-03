from .. import base
from .adjective import AdjectiveNotComparable, inflect_as, inflect_with


def joukahainen_adjective_suurempi(
        word,
        gradation_fn = base.identity) -> AdjectiveNotComparable:
    """Non-comparable adjectives."""
    return AdjectiveNotComparable(word = inflect_as(word, "suurempi"))
