from .moduses import *
from ...gradation import identity
from ..base import root_and_ccvv_ending, change_to_same_vowel_group_prefer_umlauts
from .verb import VerbBase

class KotusVerb53Muistaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)
        # all words in this class end in "aa" or "ää"

        # examples use the word "esittää"
        [esitt, v] = reverse_parse(self.word, root_and_double_end_vowel)
        [esit, v_alt] = reverse_parse(word_alt, root_and_double_end_vowel)

        return VerbRoots(root_strong = esitt + v,
                         root_weak = esit + v,
                         root_passive = esit + self.s("e"),
                         singular1_past = esit,
                         singular3 = esitt + v + v,
                         singular3_past = esitt,
                         conditional_strong = esitt + v,
                         participle_root = esitt + v)

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.word, text)
