from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_vowel_vowel_ending

class KotusVerb52Sanoa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)
        # all words in this class end in "ua" or "yä"
        [root, v, v2]     = reverse_parse(self.word, root_and_vowel_vowel_ending)
        [root_alt, v_alt] = reverse_parse(word_alt, root_and_end_vowel)

        return VerbRoots(root_weak = root + v,
                         root_strong = root_alt,
                         root_weak_passive = root + v,
                         singular3 = root + v + v)
