from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_vowel_vowel_ending

class KotusVerb58Laskea(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # the examples use the word kulkea (gradation L: kulkea-kuljen)
        [kulk, e, a] = reverse_parse(self.word, root_and_vowel_vowel_ending)
        [kulj, _, _]  = reverse_parse(word_alt, root_and_vowel_vowel_ending)
        kulke = kulk + e
        kulje = kulj + e

        return VerbRoots(root_strong        = kulke,
                         root_weak          = kulje,
                         root_passive       = kulje + "t",
                         singular3          = kulke + e,
                         plural3            = kulke,
                         singular1_past     = [kulj],
                         singular3_past     = [kulk],
                         conditional_strong = kulk,
                         participle_root    = kulke,
                         infinitive_root    = kulk + self.s("i")) # kulkiessa
