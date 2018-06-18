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

        # examples use the word "eheytyä" (gradation f: eheytyä-eheydyn)
        [eheyt, y, ä] = reverse_parse(self.word, root_and_vowel_vowel_ending)
        [eheyd, _, _] = reverse_parse(word_alt, root_and_vowel_vowel_ending)

        return VerbRoots(root_strong        = eheyt + y,
                         root_weak          = eheyd + y,
                         root_passive       = eheyd + y,
                         singular1_past     = [eheyd + y],
                         singular3_past     = [eheyt + y],
                         singular3          = eheyt + y + y,
                         plural3            = eheyt + y,
                         conditional_strong = eheyt + y,
                         participle_root    = eheyt + y)
