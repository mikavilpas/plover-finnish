from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb74Katketa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        s = self.s
        gradate = self.gradation_fn

        # Verbs ending with -ta/-tä; inverse consonant gradation possible.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/katketa

        # aueta is the example word
        [au, e, t, a] = reverse_parse(self.word, root_and_vcv_ending)
        [auk, *_]     = reverse_parse(gradate(self.word), root_and_XcX_ending)
        aue           = au + e
        auen          = aue + "n"
        auke          = auk + e
        aukea         = auke + a
        aukeaa        = aukea + a
        auet          = aue + "t"
        aukes         = auk + e + "s"

        return VerbRoots(root_strong        = auen,
                         root_weak          = aukea,
                         root_passive       = auet,
                         singular3          = aukeaa,
                         plural3            = aukea,
                         singular1_past     = [aukes],
                         singular3_past     = [aukes],
                         conditional_strong = auke,
                         participle_root    = aukea,
                         potential_root     = auen + "n",
                         infinitive_root    = auet,
                         imperative_root    = auet,
                         passive_weak_root  = auet,
                         present_root       = aukea)
