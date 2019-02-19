from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb61Sallia(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        [so, p, i, a]   = reverse_parse(self.word, root_and_cvv_ending_different_vowels)
        [so_alt, v, *_] = reverse_parse(word_alt, root_and_cvv_ending_different_vowels)

        sop  = so + p
        sov  = so_alt + v
        sopi = sop + i
        sovi = sov + i

        return VerbRoots(root_strong        = sopi,
                         root_weak          = sovi,
                         root_passive       = sovi,
                         singular3          = sopi + "i",
                         plural3            = sopi,
                         singular1_past     = [sov],
                         singular3_past     = [sop],
                         conditional_strong = sop,
                         participle_root    = sopi,
                         infinitive_root    = sopi)
