from collections import namedtuple
from typing import Dict

from .. import base

Adjective = namedtuple("Adjective",
                       ["positive", "comparative", "superlative"])

AdjectiveNoPositive = namedtuple("AdjectiveNoPositive",
                                 ["comparative", "superlative"])

AdjectiveNotComparable = namedtuple("AdjectiveNotComparable",
                                    ["word"])

# have an overload just to make the calls more readable
def inflect_as(word,
               refword: str) -> base.InflectionInfo:
    return inflect_with(word, refword, gradation_fn = None)

def inflect_with(word, refword: str, gradation_fn) -> base.InflectionInfo:
    # This can't be a top level import, otherwise there will be a circular
    # dependency error. Might need a bit of re-thinking later on to have a
    # better design.
    from stroke_dictionary_creator\
        .stroke_dictionary_creator.inflection.roots.joukahainen_kotus_mapping import \
        NominalInflection, nominals

    info: NominalInflection = nominals[refword]
    inflect                 = info.inflection_fn
    grad                    = gradation_fn or info.gradation_fn or base.identity

    return inflect(word, grad)
