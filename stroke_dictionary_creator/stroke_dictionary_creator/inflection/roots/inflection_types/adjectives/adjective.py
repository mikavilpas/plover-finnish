from collections import namedtuple
from ...joukahainen_kotus_mapping import nominals, NominalInflection
from typing import Dict
from .. import base

Adjective = namedtuple("Adjective",
                       ["positive", "comparative", "superlative"])

def inflect_as(word,
               refword: str,
               gradation_fn) -> base.InflectionInfo:

    info: NominalInflection = nominals[refword]
    inflect                 = info.inflection_fn
    grad                    = gradation_fn or info.gradation_fn or base.identity

    return inflect(word, grad)
