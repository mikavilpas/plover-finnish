from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts, root_and_double_end_vowel, identity
from ...noun_inflection_info import InflectionInfo
from ...gradation import gradate_kotus_c_tyttö_tytön, gradate_kotus_c_kate_katteen

from ..kotus_noun_1_valo import kotus_noun_1_valo
from ..kotus_noun_10_koira import kotus_noun_10_koira
from ..kotus_noun_34_onneton import kotus_noun_34_onneton
from ..kotus_noun_47_kuollut import kotus_noun_47_kuollut

class VerbParticiples():
    # Participles are verbs that are made into adjectives.
    # For example, draw -> drawn: piirtää -> piirretty

    def __init__(self, word, roots, moduses):
        self.word = word
        self.roots = roots
        self.moduses = moduses

    def group_1_VA(self) -> InflectionInfo:
        word_va = self.roots.participle_root + self.s("va")
        return kotus_noun_10_koira(word_va)

    def group_2_NUT(self) -> InflectionInfo:
        word_nut = self.moduses.indicative_perfect().singular1
        return kotus_noun_47_kuollut(word_nut)

    def group_3_MA_agent_participle(self) -> InflectionInfo:
        word_va = self.roots.participle_root + self.s("ma")
        return kotus_noun_10_koira(word_va)

    def group_4_VA_passive(self) -> InflectionInfo:
        word_va = self.roots.root_passive + self.s("ttava")
        return kotus_noun_10_koira(word_va)

    def group_5_TU_passive(self) -> InflectionInfo:
        word_passive = self.moduses.indicative_perfect().passive
        return kotus_noun_1_valo(word_passive,
                                 gradate_kotus_c_tyttö_tytön)

    def group_6_negation(self) -> InflectionInfo:
        word_maton = self.roots.participle_root + self.s("maton")
        return kotus_noun_34_onneton(word_maton,
                                     gradate_kotus_c_kate_katteen)

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.roots.participle_root, text)
