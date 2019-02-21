import unittest
from ensure import ensure
from .kotus_verb_63_saada import KotusVerb63Saada, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb63Saada("saada").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'saan',
                                     singular1_negative = 'saa',
                                     singular2          = 'saat',
                                     singular2_negative = 'saa',
                                     singular3          = 'saa',
                                     singular3_negative = 'saa',
                                     plural1            = 'saamme',
                                     plural1_negative   = 'saa',
                                     plural2            = 'saatte',
                                     plural2_negative   = 'saa',
                                     plural3            = 'saavat',
                                     plural3_negative   = 'saa',
                                     passive            = 'saadaan',
                                     passive_negative   = 'saada')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['sain'],
                                                  singular1_negative = 'saanut',
                                                  singular2s         = ['sait'],
                                                  singular2_negative = 'saanut',
                                                  singular3s         = ['sai'],
                                                  singular3_negative = 'saanut',
                                                  plural1s           = ['saimme'],
                                                  plural1_negative   = 'saaneet',
                                                  plural2s           = ['saitte'],
                                                  plural2_negative   = 'saaneet',
                                                  plural3s           = ['saivat'],
                                                  plural3_negative   = 'saaneet',
                                                  passive            = 'saatiin',
                                                  passive_negative   = 'saatu')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'saanut',
                                     singular1_negative = 'saanut',
                                     singular2          = 'saanut',
                                     singular2_negative = 'saanut',
                                     singular3          = 'saanut',
                                     singular3_negative = 'saanut',
                                     plural1            = 'saaneet',
                                     plural1_negative   = 'saaneet',
                                     plural2            = 'saaneet',
                                     plural2_negative   = 'saaneet',
                                     plural3            = 'saaneet',
                                     plural3_negative   = 'saaneet',
                                     passive            = 'saatu',
                                     passive_negative   = 'saatu')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'saisin',
                                     singular1_negative = 'saisi',
                                     singular2          = 'saisit',
                                     singular2_negative = 'saisi',
                                     singular3          = 'saisi',
                                     singular3_negative = 'saisi',
                                     plural1            = 'saisimme',
                                     plural1_negative   = 'saisi',
                                     plural2            = 'saisitte',
                                     plural2_negative   = 'saisi',
                                     plural3            = 'saisivat',
                                     plural3_negative   = 'saisi',
                                     passive            = 'saataisiin',
                                     passive_negative   = 'saataisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'saanen',
                                     singular1_negative = 'saane',
                                     singular2          = 'saanet',
                                     singular2_negative = 'saane',
                                     singular3          = 'saanee',
                                     singular3_negative = 'saane',
                                     plural1            = 'saanemme',
                                     plural1_negative   = 'saane',
                                     plural2            = 'saanette',
                                     plural2_negative   = 'saane',
                                     plural3            = 'saanevat',
                                     plural3_negative   = 'saane',
                                     passive            = 'saataneen',
                                     passive_negative   = 'saatane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2          = 'saa',
                                                      singular2_negative = 'saa',
                                                      singular3          = 'saakoon',
                                                      singular3_negative = 'saako',
                                                      plural1            = 'saakaamme',
                                                      plural1_negative   = 'saako',
                                                      plural2            = 'saakaa',
                                                      plural2_negative   = 'saako',
                                                      plural3            = 'saakoot',
                                                      plural3_negative   = 'saako',
                                                      passive            = 'saatakoon',
                                                      passive_negative   = 'saatako')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb63Saada("jäädä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("jäävä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("jäänyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("jäämä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("jäätävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("jääty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("jäämätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb63Saada("jäädä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='jäädä',
            translative='jäädäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "jäädessä",
            inessive_passive = "jäätäessä",
            instructive      = "jääden",
            elative          = "jäädestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "jäätämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("jääminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "jäämäisillä")

        ensure_inflections_equal(expected, data)
