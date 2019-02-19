from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb65Käydä(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # The word käydä only; no consonant gradation.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/k%C3%A4yd%C3%A4

        [kä, y, d, ä] = reverse_parse(self.word, root_and_vcv_ending)
        käy           = kä + y
        käyd          = käy + d
        käv           = kä + "v"

        return VerbRoots(root_strong        = käy,
                         root_weak          = käy,
                         root_passive       = käy,
                         singular3          = käy,
                         plural3            = käy,
                         singular1_past     = [käv],
                         singular3_past     = [käv],
                         conditional_strong = käv,
                         participle_root    = käy,
                         infinitive_root    = käyd,
                         passive_weak_root  = käyd)
