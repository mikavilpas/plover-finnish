from .moduses import *
from ...gradation import identity
from .verb import VerbBase

class KotusVerb56Laulaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # the examples use the word tappaa (gradation b: tappaa-tapan)
        [tapp, a] = reverse_parse(self.word, root_and_double_end_vowel)
        [tap, _]  = reverse_parse(word_alt, root_and_double_end_vowel)

        return VerbRoots(root_strong        = tapp + a,
                         root_weak          = tap + a,
                         root_passive       = tap + self.s("e"),
                         singular1_past     = tap + self.s("o"),
                         singular3          = tapp + a + a,
                         singular3_past     = tapp + self.s("o"),
                         plural3            = tapp + a,
                         conditional_strong = tapp + a,
                         participle_root    = tapp + a)
