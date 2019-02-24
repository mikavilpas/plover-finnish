from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts, root_and_double_end_vowel, identity
from ...noun_inflection_info import InflectionInfo
from ...gradation import gradate_kotus_c_tyttö_tytön
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses
from ..kotus_noun_38_nainen import kotus_noun_38_nainen

VerbInfinitiveAPersonalForms = namedtuple("VerbInfinitiveAPersonalForms",
                                          ["singular1", "singular2", "singular3",
                                           "plural1", "plural2", "plural3", ])

VerbInfinitive_1_A = namedtuple("VerbInfinitive_1_A",
                                # this is also sometimes called the lemma or headword
                                [ "basic_form",
                                  # VerbInfinitiveAPersonalForms
                                  "translative",])

VerbInfinitive_2_E = namedtuple("VerbInfinitive_2_E",
                                ["inessive",
                                 "inessive_passive",
                                 "instructive",
                                 "elative",])

VerbInfinitive_3_MA = namedtuple("VerbInfinitive_3_MA",
                                 # This has the forms that are also present in
                                 # the participle 3 (the agent participle).
                                 # They are not repeated here, however.
                                 #
                                 # This is the one extra form that is not
                                 # present in the participle 3.
                                 ["instructive_passive"])

VerbInfinitive_5_MAINEN = namedtuple("VerbInfinitive_5_MAINEN",
                                     ["adessive"])

class VerbInfinitives():

    def __init__(self, word, roots: VerbRoots, moduses: VerbModuses):
        self.word = word
        self.roots = roots
        self.moduses = moduses

    def group_1_A(self) -> VerbInfinitive_1_A:
        return VerbInfinitive_1_A(
            basic_form = self.word,
            translative = self.word + self.s("kse"))

    def group_2_E(self) -> VerbInfinitive_2_E:
        s = self.s

        # TODO also also the third forms can be -ssansa

        return VerbInfinitive_2_E(
            inessive         = self.roots.infinitive_root + s("essa"),
            inessive_passive = self.roots.root_passive    + s("taessa"),
            instructive      = self.roots.infinitive_root + s("en"),
            elative          = self.roots.infinitive_root + s("esta"))

    def group_3_MA(self) -> VerbInfinitive_3_MA:
        return VerbInfinitive_3_MA(
            instructive_passive = self.roots.root_passive + self.s("taman"))

    def group_4_MINEN(self) -> InflectionInfo:
        word_minen = self.roots.present_root + self.s("minen")
        return kotus_noun_38_nainen(word_minen)

    def group_5_MAINEN(self) -> VerbInfinitive_5_MAINEN:
        return VerbInfinitive_5_MAINEN(
            adessive = self.roots.present_root + self.s("maisilla"))

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.roots.root_weak, text)
