from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_ccvv_ending, root_and_vowel_vowel_ending

class KotusVerb60Lähteä(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # there is only one word in this class, "lähteä"!
        # So that is what we'll use is the example too.
        [lä, h, t, e, ä] = reverse_parse(self.word, root_and_ccvv_ending)
        # no known gradation is used for this class (word)

        läht  = lä + h + t
        lähd  = lä + h + self.s("d")
        lähde = lähd + e
        lähte = läht + e
        lähti = läht + self.s("i")
        läks  = lä + self.s("ks")

        return VerbRoots(root_strong        = lähte,
                         root_weak          = lähde,
                         root_passive       = lähde,
                         singular3          = lähte + e,
                         plural3            = lähte,
                         singular1_past     = [lähd, läks],
                         singular3_past     = [läht, läks],
                         conditional_strong = läht,
                         participle_root    = lähte,
                         infinitive_root    = lähti)
