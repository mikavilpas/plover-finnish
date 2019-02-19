from .moduses import *
from ...gradation import identity
from ..base import root_and_cvv_ending, change_to_same_vowel_group_prefer_umlauts
from .verb import VerbBase

class KotusVerb53Muistaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)
        # all words in this class end in "aa" or "ää"

        # examples use the word "esittää"
        [esitt, ä] = reverse_parse(self.word, root_and_double_end_vowel)
        [esit, v_alt] = reverse_parse(word_alt, root_and_double_end_vowel)

        return VerbRoots(root_strong        = esitt + ä,
                         root_weak          = esit + ä,
                         root_passive       = esit + self.s("et"),
                         singular3          = esitt + ä + ä,
                         plural3            = esitt + ä,
                         singular1_past     = [esit],
                         singular3_past     = [esitt],
                         conditional_strong = esitt + ä,
                         participle_root    = esitt + ä)
