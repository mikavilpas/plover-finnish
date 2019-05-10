import unittest
from ensure import ensure
from .kotus_verb_76_taitaa import KotusVerb76Taitaa, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb76Taitaa("tietää").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'tiedän',
                                     singular1_negative = 'tiedä',
                                     singular2          = 'tiedät',
                                     singular2_negative = 'tiedä',
                                     singular3          = 'tietää',
                                     singular3_negative = 'tiedä',
                                     plural1            = 'tiedämme',
                                     plural1_negative   = 'tiedä',
                                     plural2            = 'tiedätte',
                                     plural2_negative   = 'tiedä',
                                     plural3            = 'tiedävät',
                                     plural3_negative   = 'tiedä',
                                     passive            = 'tiedetään',
                                     passive_negative   = 'tiedetä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['tiesin'],
                                                  singular1_negative = 'tietänyt',
                                                  singular2s         = ['tiesit'],
                                                  singular2_negative = 'tietänyt',
                                                  singular3s         = ['tiesi'],
                                                  singular3_negative = 'tietänyt',
                                                  plural1s           = ['tiesimme'],
                                                  plural1_negative   = 'tietäneet',
                                                  plural2s           = ['tiesitte'],
                                                  plural2_negative   = 'tietäneet',
                                                  plural3s           = ['tiesivät'],
                                                  plural3_negative   = 'tietäneet',
                                                  passive            = 'tiedettiin',
                                                  passive_negative   = 'tiedetty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'tietänyt',
                                     singular1_negative = 'tietänyt',
                                     singular2          = 'tietänyt',
                                     singular2_negative = 'tietänyt',
                                     singular3          = 'tietänyt',
                                     singular3_negative = 'tietänyt',
                                     plural1            = 'tietäneet',
                                     plural1_negative   = 'tietäneet',
                                     plural2            = 'tietäneet',
                                     plural2_negative   = 'tietäneet',
                                     plural3            = 'tietäneet',
                                     plural3_negative   = 'tietäneet',
                                     passive            = 'tiedetty',
                                     passive_negative   = 'tiedetty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'tietäisin',
                                     singular1_negative = 'tietäisi',
                                     singular2          = 'tietäisit',
                                     singular2_negative = 'tietäisi',
                                     singular3          = 'tietäisi',
                                     singular3_negative = 'tietäisi',
                                     plural1            = 'tietäisimme',
                                     plural1_negative   = 'tietäisi',
                                     plural2            = 'tietäisitte',
                                     plural2_negative   = 'tietäisi',
                                     plural3            = 'tietäisivät',
                                     plural3_negative   = 'tietäisi',
                                     passive            = 'tiedettäisiin',
                                     passive_negative   = 'tiedettäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'tietänen',
                                     singular1_negative = 'tietäne',
                                     singular2          = 'tietänet',
                                     singular2_negative = 'tietäne',
                                     singular3          = 'tietänee',
                                     singular3_negative = 'tietäne',
                                     plural1            = 'tietänemme',
                                     plural1_negative   = 'tietäne',
                                     plural2            = 'tietänette',
                                     plural2_negative   = 'tietäne',
                                     plural3            = 'tietänevät',
                                     plural3_negative   = 'tietäne',
                                     passive            = 'tiedettäneen',
                                     passive_negative   = 'tiedettäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'tiedä',
            singular2_negative = 'tiedä',
            singular3          = 'tietäköön',
            singular3_negative = 'tietäkö',
            plural1            = 'tietäkäämme',
            plural1_negative   = 'tietäkö',
            plural2            = 'tietäkää',
            plural2_negative   = 'tietäkö',
            plural3            = 'tietäkööt',
            plural3_negative   = 'tietäkö',
            passive            = 'tiedettäköön',
            passive_negative   = 'tiedettäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb76Taitaa("taitaa").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("taitava")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("taitanut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("taitama")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("taidettava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("taidettu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("taitamaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb76Taitaa("tietää").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'tietää',
            translative = 'tietääkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "tietäessä",
            inessive_passive = "tiedettäessä",
            instructive      = "tietäen",
            elative          = "tietäestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "tiedettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("tietäminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "tietämäisillä")

        ensure_inflections_equal(expected, data)
