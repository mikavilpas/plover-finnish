from .base import *

from parsy import *
from ..tokens import *
from .kotus_noun_41_vieras import kotus_noun_41_vieras

def kotus_noun_44_kevät(word, gradation_fn = identity):
    # A very small number of nominals ending with -Vt (V = vowel; in the little
    # amount of examples, V is either ä or u); those words do not have
    # consonant gradation.
    #
    # These words decline like vieras, differing only in that the nominative
    # and partitive singular end with -t instead of -s.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/kev%C3%A4t

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    kevät         = word
    (ke, v, ä, t) = reverse_parse(word, root_and_cvc_ending)
    kevätt        = ke + v + ä + t + t

    reference = kotus_noun_41_vieras(word, gradation_fn)
    return reference._replace(partitives = [kevätt + s("a")])
