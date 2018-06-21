from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import root_and_ccvv_ending, root_and_vowel_vowel_ending

class KotusVerb59Tuntea(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        word_alt = self.gradation_fn(self.word)

        # there is only one word in this class, "tuntea"!
        # So that is what we'll uses is the example too.
        [tu, n, t, e, a] = reverse_parse(self.word, root_and_ccvv_ending)
        [tunn, _, _]   = reverse_parse(word_alt, root_and_vowel_vowel_ending)

        tun   = tu + n
        tunt  = tun + t
        tuns  = tun + self.s("s")
        tunne = tunn + e
        tunte = tunt + e
        tunti = tunt + self.s("i")

        return VerbRoots(root_strong        = tunte,
                         root_weak          = tunne,
                         root_passive       = tunne,
                         singular3          = tunte + e,
                         plural3            = tunte,
                         singular1_past     = [tuns],
                         singular3_past     = [tuns],
                         conditional_strong = tunt,
                         participle_root    = tunte,
                         infinitive_root    = tunti)
