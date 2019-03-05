from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb69Valita(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # Verbs ending with -ita/-itä; no consonant gradation.
        #
        # The inflectional stem is obtained by replacing the final -ta/-tä with
        # -tse-.
        #
        # Verbs ending with -ita/-itä are more commonly declined as selvitä,
        # although a few common words like tarvita fall into this type. Almost
        # all verbs of this type are formed with the suffix -ita.
        #
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/valita

        gradate = self.gradation_fn

        # valita is the example word
        [val, i, t, a] = reverse_parse(self.word, root_and_vcv_ending)
        valit          = val + i + t
        valits         = valit + "s"
        valin          = val + i + "n"

        return VerbRoots(root_strong        = valin,
                         root_weak          = valits + self.s("e"),
                         present_root       = valits + self.s("e"),
                         root_passive       = valit,
                         singular3          = valits + self.s("ee"),
                         plural3            = valits + self.s("e"),
                         singular1_past     = [valits],
                         singular3_past     = [valits],
                         infinitive_root    = valit,
                         potential_root     = valin + "n",
                         conditional_strong = valits,
                         imperative_root    = valit,
                         participle_root    = valits + self.s("e"),)
