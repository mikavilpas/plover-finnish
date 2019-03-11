from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb73Salata(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        s = self.s
        gradate = self.gradation_fn

        # Verbs ending with -ata/-ätä; inverse consonant gradation possible.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/salata

        # karata is the example word
        [kar, a, t, a] = reverse_parse(self.word, root_and_vcv_ending)
        [kark, *_]     = reverse_parse(gradate(self.word), root_and_vcv_ending)
        karan          = kar + a + "n"
        karka          = kark + a
        karkaa         = karka + a
        karkas         = karka + "s"
        karat          = kar + a + t
        karkaa         = karka + a

        return VerbRoots(root_strong        = karan,
                         root_weak          = karkaa,
                         root_passive       = karat,
                         singular3          = karkaa,
                         plural3            = karkaa,
                         singular1_past     = [karkas],
                         singular3_past     = [karkas],
                         conditional_strong = karka,
                         participle_root    = karkaa,
                         potential_root     = karan + "n",
                         infinitive_root    = karat,
                         imperative_root    = karat,
                         passive_weak_root  = karat,
                         present_root       = karkaa)
