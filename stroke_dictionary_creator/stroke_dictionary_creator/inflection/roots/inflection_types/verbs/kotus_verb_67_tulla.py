from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb67Tulla(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with a double consonant and -a/-ä; inverse consonant
        # gradation possible.
        # The basic "type II" Finnish verb. The stem is obtained by removing
        # the second consonant and a/ä. Present personal endings are attached
        # by -e-.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/tulla

        gradate = self.gradation_fn

        # otella is the example word
        [otel, l, a] = reverse_parse(self.word, root_and_cv_ending)
        [ottel, *_]  = reverse_parse(gradate(self.word), root_and_cv_ending)
        otell        = otel + l
        ottele       = ottel + "e"

        return VerbRoots(root_strong        = otel,
                         root_weak          = ottele,
                         root_passive       = otel,
                         passive_weak_root  = otell,
                         singular3          = ottele + "e",
                         plural3            = ottele,
                         singular1_past     = [ottel],
                         singular3_past     = [ottel],
                         conditional_strong = ottel,
                         participle_root    = ottele,
                         potential_root     = otell,
                         infinitive_root    = otell,
                         present_root       = ottele,
                         suffix_ut          = "lut",
                         suffix_eet         = "leet")
