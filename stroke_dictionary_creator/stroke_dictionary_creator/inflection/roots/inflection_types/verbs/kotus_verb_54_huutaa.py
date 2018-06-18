from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_cvv_ending, change_to_same_vowel_group_prefer_umlauts

class KotusVerb54Huutaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # The examples use the word vääntää (gradation j: vääntää-väännän).
        # All the words in this class end in "aa" or "ää"
        [vään, t, ä] = reverse_parse(self.word, root_and_cvv_ending)
        [väänn, _] = reverse_parse(word_alt, root_and_double_end_vowel)

        return VerbRoots(root_strong        = vään + t + ä,
                         root_weak          = väänn + ä,
                         root_passive       = väänn + self.s("e"),
                         singular3          = vään + t + ä + ä,
                         plural3            = vään + t + ä,
                         singular1_past     = [vään + self.s("s")],
                         singular3_past     = [vään + self.s("s")],
                         conditional_strong = vään + t + ä,
                         participle_root    = vään + t + ä)
