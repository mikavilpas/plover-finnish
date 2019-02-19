from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_cvv_ending

class KotusVerb55Soutaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # The examples use the word yltää (gradation i: yltää-yllän).
        # All the words in this class end in "aa" or "ää"
        [yl, t, ä] = reverse_parse(self.word, root_and_cvv_ending)
        [yl, l, _] = reverse_parse(word_alt, root_and_cvv_ending)
        s = self.s("s")
        yltä = yl + t + ä

        return VerbRoots(root_strong        = yltä,
                         root_weak          = yl + l + ä,
                         root_passive       = yl + l + self.s("et"),
                         singular3          = yltä + ä,
                         plural3            = yltä,
                         singular1_past     = [yl + l,
                                               yl + s],
                         singular3_past     = [yl + t,
                                               yl + s],
                         conditional_strong = yltä,
                         participle_root    = yltä)
