from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts, root_and_double_end_vowel, identity
from ...noun_inflection_info import InflectionInfo
from ...gradation import gradate_kotus_c_tyttö_tytön_kate_katteen
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses

VerbInfinitive_1_A = namedtuple("VerbInfinitive_1_A",
                                # this is also sometimes called the lemma or headword
                                [ "basic_form",
                                  # VerbInfinitiveAPersonalForms
                                  "translative",])

VerbInfinitiveAPersonalForms = namedtuple("VerbInfinitiveAPersonalForms",
                                          ["singular1", "singular2", "singular3",
                                           "plural1", "plural2", "plural3", ])

class VerbInfinitives():

    def __init__(self, word, roots: VerbRoots, moduses: VerbModuses):
        self.word = word
        self.roots = roots
        self.moduses = moduses

    def group_1_A(self) -> VerbInfinitive_1_A:
        s = self.s

        translative = VerbInfinitiveAPersonalForms\
                      (singular1 = self.word + s("kseni"),
                       singular2 = self.word + s("ksesi"),
                       singular3 = self.word + s("kseen"),
                       plural1   = self.word + s("ksemme"),
                       plural2   = self.word + s("ksenne"),
                       plural3   = self.word + s("kseen"),)

        return VerbInfinitive_1_A(basic_form = self.word,
                                  translative = translative)

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.roots.present, text)
