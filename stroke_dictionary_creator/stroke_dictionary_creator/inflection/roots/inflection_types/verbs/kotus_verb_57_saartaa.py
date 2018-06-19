from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_cvv_ending

class KotusVerb57Saartaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # only 3 words in this group.

        # the examples use the word saartaa (gradation k: saartaa-saarran)
        [saar, t, a] = reverse_parse(self.word, root_and_cvv_ending)
        [saar, r, _]  = reverse_parse(word_alt, root_and_cvv_ending)

        saart = saar + t
        saarr = saar + r

        return VerbRoots(root_strong        = saart + a,
                         root_weak          = saarr + a,
                         root_passive       = saarr + self.s("e"),
                         singular3          = saart + a + a,
                         plural3            = saart + a,
                         singular1_past     = [saar + self.s("s"),
                                               saarr + self.s("o")],
                         singular3_past     = [saar + self.s("s"),
                                               saart + self.s("o")],
                         conditional_strong = saart + a,
                         participle_root    = saart + a)
