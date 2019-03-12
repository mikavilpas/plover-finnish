from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb76Taitaa(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        s = self.s
        gradate = self.gradation_fn

        # The verbs taitaa and tietää only. Conjugation is the same as huutaa,
        # except for alternative irregular forms of the active past participles
        # and third-person present potential, where -tan-/-tän- contracts to
        # -nn-.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/taitaa

        # taitaa is the example word
        [tai, t, a] = reverse_parse(self.word, root_and_cvv_ending)
        taid        = tai + "d"
        taida       = taid + a
        taide       = taid + "e"
        taita       = tai + t + a
        taito       = tai + t + s("o")
        taido       = taid + s("o")

        return VerbRoots(root_strong        = taita,
                         root_weak          = taida,
                         root_passive       = taide + t,
                         singular3          = taita + s("a"),
                         plural3            = taida,
                         singular1_past     = [tai + "s"],
                         singular3_past     = [tai + "s"],
                         conditional_strong = taita,
                         participle_root    = taita,
                         passive_weak_root  = taid + "et")
