from .. import base
from .adjective import AdjectiveNotComparable, inflect_as, inflect_with


def joukahainen_adjective_suurempi(
        word,
        gradation_fn = base.identity) -> AdjectiveNotComparable:
    """Adjectives that cannot be compared. Only the comparative forms are
    included in the worldist. For the superlative forms use the 'sisin'
    class."""
    return AdjectiveNotComparable(word = inflect_as(word, "suurempi"))
