from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb72Vanheta(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        s = self.s
        gradate = self.gradation_fn

        # Usually verbs ending with -eta/-etä, but also a few with -ata/-ätä
        # and -ota; inverse consonant gradation possible. Most verbs of this
        # type are derived from adjectives with the suffix -ta/-tä.
        #
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/vanheta

        # edetä is the example word
        [ed, e, t, ä] = reverse_parse(self.word, root_and_vcv_ending)
        [et, *_]      = reverse_parse(gradate(self.word), root_and_vcv_ending)
        eden         = ed + e + "n"
        edet          = ed + e + t
        eten          = et + e + "n"
        etene         = eten + "e"

        return VerbRoots(root_strong        = eden,
                         root_weak          = etene,
                         root_passive       = edet,
                         singular3          = etene + "e",
                         plural3            = etene,
                         singular1_past     = [eten],
                         singular3_past     = [eten],
                         conditional_strong = eten,
                         participle_root    = etene,
                         potential_root     = eden + "n",
                         infinitive_root    = edet,
                         imperative_root    = edet,
                         passive_weak_root  = edet,
                         present_root       = etene)
