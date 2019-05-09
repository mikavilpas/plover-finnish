from .. import base
from .adjective import AdjectiveNotComparable, inflect_as, inflect_with


def joukahainen_adjective_sisin(word,
                                gradation_fn = base.identity) -> AdjectiveNotComparable:
    """Adjectives that cannot be compared. Only the superlative forms are
    included in the worldist. For the comparative forms use the 'suurempi'
    class."""

    return AdjectiveNotComparable(word = inflect_as(word, "sisin"))
