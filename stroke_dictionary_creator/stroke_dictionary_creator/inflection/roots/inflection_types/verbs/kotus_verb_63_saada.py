from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb63Saada(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with a long vowel followed by -da/-dä; no consonant
        # gradation. The stem is found by removing the -da/-dä.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/saada

        [s, a, d, _] = reverse_parse(self.word, root_and_double_vowel_cv)
        sa           = s + a
        saa          = sa + a
        saad         = saa + "d"
        sai          = s + a + "i"

        return VerbRoots(root_strong        = saa,
                         root_weak          = saa,
                         root_passive       = saa,
                         singular3          = saa,
                         plural3            = saa,
                         singular1_past     = [sa],
                         singular3_past     = [sa],
                         conditional_strong = sa,
                         participle_root    = saa,
                         infinitive_root    = saad,
                         passive_weak_root  = saad)
