from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb64Juoda(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with -uoda/-iedä/-yödä; no consonant gradation.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/juoda

        [j, u, o, d, a] = reverse_parse(self.word, root_and_vvcv_ending)
        jo              = j + o
        juo             = j + u + o
        juod            = juo + d

        return VerbRoots(root_strong        = juo,
                         root_weak          = juo,
                         root_passive       = juo,
                         singular3          = juo,
                         plural3            = juo,
                         singular1_past     = [jo],
                         singular3_past     = [jo],
                         conditional_strong = jo,
                         participle_root    = juo,
                         infinitive_root    = juod,
                         passive_weak_root  = juod)
