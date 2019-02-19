from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb62Voida(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with -aida/-oida/-öidä/-uida; no consonant gradation.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/voida

        # NOTE: I don't understand why, but the joukahainen wordlist lists all
        # "voida" and "kanavoida" like verbs as having the $gradation av2
        # (gradate_kotus_f_keidas_keitaan).
        #
        # The page above says there is no gradation, so I'm sticking with that,
        # and _silently ignoring_ the given gradation function.

        [vo, i, d, a] = reverse_parse(self.word, root_and_vcv_ending)
        voi           = vo + i
        void          = voi + d

        return VerbRoots(root_strong        = voi,
                         root_weak          = voi,
                         root_passive       = voi,
                         singular3          = voi,
                         plural3            = voi,
                         singular1_past     = [vo],
                         singular3_past     = [vo],
                         conditional_strong = vo,
                         participle_root    = voi,
                         infinitive_root    = void,
                         passive_weak_root  = void)
