from .moduses import *
from ...gradation import identity
from .verb import VerbBase

class KotusVerb52Sanoa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)
        # all words in this class end in "ua" or "yä"
        [root, v]         = reverse_parse(self.word, root_and_end_vowel)
        [root_alt, v_alt] = reverse_parse(word_alt, root_and_end_vowel)

        return VerbRoots(present = root,
                         present_passive = root_alt)
