from collections import namedtuple

from ..base import change_to_same_vowel_group_prefer_umlauts
from ...gradation import (gradate_kotus_c_kate_katteen, gradate_kotus_c_tyttö_tytön)
from ..adjectives.adjective import Adjective
from ..adjectives.joukahainen_adjective_onneton import joukahainen_adjective_onneton
from ..adjectives.joukahainen_adjective_kuollut import joukahainen_adjective_kuollut
from ..adjectives.joukahainen_adjective_valo import joukahainen_adjective_valo
from ..adjectives.joukahainen_adjective_koira import joukahainen_adjective_koira


class VerbParticiples():
    """Participles are verbs that are made into adjectives.
    For example, draw -> drawn: piirtää -> piirretty"""

    def __init__(self, word, roots, moduses):
        self.word = word
        self.roots = roots
        self.moduses = moduses

    def group_1_VA(self) -> Adjective:
        word_va = self.roots.participle_root + self.s("va")
        # return kotus_noun_10_koira(word_va)
        return joukahainen_adjective_koira(word_va)

    def group_2_NUT(self) -> Adjective:
        word_nut = self.moduses.indicative_perfect().singular1
        # return kotus_noun_47_kuollut(word_nut)
        return joukahainen_adjective_kuollut(word_nut)

    def group_3_MA_agent_participle(self) -> Adjective:
        word_va = self.roots.participle_root + self.s("ma")
        return joukahainen_adjective_koira(word_va)

    def group_4_VA_passive(self) -> Adjective:
        word_va = self.roots.root_passive + self.s("tava")
        return joukahainen_adjective_koira(word_va)

    def group_5_TU_passive(self) -> Adjective:
        word_passive = self.moduses.indicative_perfect().passive
        return joukahainen_adjective_valo(word_passive,
                                          gradate_kotus_c_tyttö_tytön)

    def group_6_negation(self) -> Adjective:
        word_maton = self.roots.participle_root + self.s("maton")
        return joukahainen_adjective_onneton(word_maton,
                                             gradate_kotus_c_kate_katteen)

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.roots.participle_root, text)
