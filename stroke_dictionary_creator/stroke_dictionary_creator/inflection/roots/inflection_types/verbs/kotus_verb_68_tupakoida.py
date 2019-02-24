from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb68Tupakoida(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with -oida/-öidä; no consonant gradation.
        # The stem for inflection is obtained by removing the -da/-dä.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/tupakoida

        gradate = self.gradation_fn

        # otella is the example word
        [tupako, i, d, a] = reverse_parse(self.word, root_and_vcv_ending)
        tupakoi           = tupako + i
        tupakoid          = tupakoi + d

        return VerbRoots(root_strong        = tupakoi,
                         root_weak          = tupakoi,
                         root_passive       = tupakoi,
                         passive_weak_root  = tupakoid,
                         singular3          = tupakoi,
                         plural3            = tupakoi,
                         singular1_past     = [tupako],
                         singular3_past     = [tupako],
                         infinitive_root    = tupakoid,
                         conditional_strong = tupako,
                         participle_root    = tupakoi)
