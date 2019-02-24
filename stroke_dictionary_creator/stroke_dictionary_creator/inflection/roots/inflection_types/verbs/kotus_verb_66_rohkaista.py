from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb66Rohkaista(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with -sta/-stä; inverse consonant gradation possible.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/rohkaista

        gradate = self.gradation_fn

        # vavista is the example word
        [vavi, s, t, a] = reverse_parse(self.word, root_and_ccv_ending)
        [vapi, *_]      = reverse_parse(gradate(self.word), root_and_ccv_ending)
        vapis           = vapi + s
        vavis           = vavi + s
        vaviss          = vavis + s
        vapise          = vapis + "e"
        vavist          = vavi + s + t

        return VerbRoots(root_strong        = vavis,
                         root_weak          = vapise,
                         root_passive       = vavis,
                         singular3          = vapise + "e",
                         plural3            = vapise,
                         singular1_past     = [vapis],
                         singular3_past     = [vapis],
                         conditional_strong = vapis,
                         participle_root    = vapise,
                         potential_root     = vaviss,
                         infinitive_root    = vavist,
                         passive_weak_root  = vavist,
                         present_root       = vapise,
                         # for vavissut, vavisseet etc
                         suffix_ut          = "sut",
                         suffix_eet         = "seet")
