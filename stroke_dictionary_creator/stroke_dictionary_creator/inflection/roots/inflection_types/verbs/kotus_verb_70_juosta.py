from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb70Juosta(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # A very small number of verbs ending with -sta/-stä; no consonant
        # gradation, but irregular mutations.
        #
        # These words decline roughly as rohkaista, except that their
        # inflectional stem ends with -ks-, which reduces to -s- before a
        # consonant. Present personal endings are attached by -e-.
        #
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/juosta

        # piestä is the example word
        [pie, s, t, ä] = reverse_parse(self.word, root_and_ccv_ending)
        pies           = pie + "s"
        piest          = pies + "t"
        pieks          = pie + "ks"
        piekse         = pieks + "e"

        return VerbRoots(root_strong        = pies,
                         root_weak          = piekse,
                         root_passive       = pies,
                         singular3          = piekse + "e",
                         plural3            = piekse,
                         singular1_past     = [pieks],
                         singular3_past     = [pieks],
                         conditional_strong = pieks,
                         participle_root    = piekse,
                         potential_root     = pieks,
                         infinitive_root    = piest,
                         imperative_root    = pies,
                         passive_weak_root  = piest,
                         present_root       = piekse,
                         suffix_ut          = "syt",
                         suffix_eet         = "seet")
