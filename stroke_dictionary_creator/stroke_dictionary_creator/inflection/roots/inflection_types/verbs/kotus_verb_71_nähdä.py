from .moduses import *
from ...gradation import identity
from .verb import VerbBase
from ..base import *

class KotusVerb71Nähdä(VerbBase):
    def __init__(self, word, gradation_fn = identity):
        super().__init__(word, gradation_fn)

    def _roots(self) -> VerbRoots:
        # The verbs nähdä and tehdä only.
        # https://en.wiktionary.org/wiki/Appendix:Finnish_conjugation/n%C3%A4hd%C3%A4

        # tehdä is the example word
        [te, h, d, ä] = reverse_parse(self.word, root_and_ccv_ending)
        teh           = te + h
        tek           = te + "k"
        teke          = tek + "e"
        tehd          = teh + d
        tee           = te + "e"

        return VerbRoots(root_strong        = teh,
                         root_weak          = tee,
                         root_passive       = teh,
                         singular3          = teke + "e",
                         plural3            = teke,
                         singular1_past     = [te],
                         singular3_past     = [tek],
                         conditional_strong = tek,
                         participle_root    = teke,
                         potential_root     = te,
                         potential_s3_root  = te,
                         potential_p3_root  = teke,
                         infinitive_root    = tehd,
                         imperative_root    = teh,
                         passive_weak_root  = tehd,
                         present_root       = tee)
