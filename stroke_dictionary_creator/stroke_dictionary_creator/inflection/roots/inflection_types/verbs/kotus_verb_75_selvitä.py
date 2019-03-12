from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *
class KotusVerb75Selvitä(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        s = self.s
        gradate = self.gradation_fn

        # Verbs ending with -ta/-tä; inverse consonant gradation possible.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/selvit%C3%A4

        # peitota is the example word
        [peito, t, a] = reverse_parse(self.word, root_and_cv_ending)
        [peitto, *_]  = reverse_parse(gradate(self.word), root_and_cv_ending)
        peiton        = peito + "n"
        peitot        = peito + t
        peittoa       = peitto + s("a")
        peittos       = peitto + "s"

        return VerbRoots(root_strong        = peiton,
                         root_weak          = peittoa,
                         root_passive       = peitot,
                         singular3          = peittoa + s("a"),
                         plural3            = peittoa,
                         singular1_past     = [peittos],
                         singular3_past     = [peittos],
                         conditional_strong = peittoa,
                         participle_root    = peittoa,
                         potential_root     = peiton + "n",
                         infinitive_root    = peitot,
                         imperative_root    = peitot,
                         passive_weak_root  = peitot,
                         present_root       = peittoa)
