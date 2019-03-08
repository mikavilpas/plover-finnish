import unittest
from ensure import ensure
from .kotus_verb_71_nähdä import KotusVerb71Nähdä, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb71Nähdä("tehdä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'teen',
                                     singular1_negative = 'tee',
                                     singular2          = 'teet',
                                     singular2_negative = 'tee',
                                     singular3          = 'tekee',
                                     singular3_negative = 'tee',
                                     plural1            = 'teemme',
                                     plural1_negative   = 'tee',
                                     plural2            = 'teette',
                                     plural2_negative   = 'tee',
                                     plural3            = 'tekevät',
                                     plural3_negative   = 'tee',
                                     passive            = 'tehdään',
                                     passive_negative   = 'tehdä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['tein'],
                                                  singular1_negative = 'tehnyt',
                                                  singular2s         = ['teit'],
                                                  singular2_negative = 'tehnyt',
                                                  singular3s         = ['teki'],
                                                  singular3_negative = 'tehnyt',
                                                  plural1s           = ['teimme'],
                                                  plural1_negative   = 'tehneet',
                                                  plural2s           = ['teitte'],
                                                  plural2_negative   = 'tehneet',
                                                  plural3s           = ['tekivät'],
                                                  plural3_negative   = 'tehneet',
                                                  passive            = 'tehtiin',
                                                  passive_negative   = 'tehty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'tehnyt',
                                     singular1_negative = 'tehnyt',
                                     singular2          = 'tehnyt',
                                     singular2_negative = 'tehnyt',
                                     singular3          = 'tehnyt',
                                     singular3_negative = 'tehnyt',
                                     plural1            = 'tehneet',
                                     plural1_negative   = 'tehneet',
                                     plural2            = 'tehneet',
                                     plural2_negative   = 'tehneet',
                                     plural3            = 'tehneet',
                                     plural3_negative   = 'tehneet',
                                     passive            = 'tehty',
                                     passive_negative   = 'tehty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'tekisin',
                                     singular1_negative = 'tekisi',
                                     singular2          = 'tekisit',
                                     singular2_negative = 'tekisi',
                                     singular3          = 'tekisi',
                                     singular3_negative = 'tekisi',
                                     plural1            = 'tekisimme',
                                     plural1_negative   = 'tekisi',
                                     plural2            = 'tekisitte',
                                     plural2_negative   = 'tekisi',
                                     plural3            = 'tekisivät',
                                     plural3_negative   = 'tekisi',
                                     passive            = 'tehtäisiin',
                                     passive_negative   = 'tehtäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'teen',
                                     singular1_negative = 'tee',
                                     singular2          = 'teet',
                                     singular2_negative = 'tee',
                                     singular3          = 'tee',
                                     singular3_negative = 'tee',
                                     plural1            = 'teemme',
                                     plural1_negative   = 'tee',
                                     plural2            = 'teette',
                                     plural2_negative   = 'tee',
                                     plural3            = 'tekevät',
                                     plural3_negative   = 'tee',
                                     passive            = 'tehtäneen',
                                     passive_negative   = 'tehtäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2          = 'tee',
                                                      singular2_negative = 'tee',
                                                      singular3          = 'tehköön',
                                                      singular3_negative = 'tehkö',
                                                      plural1            = 'tehkäämme',
                                                      plural1_negative   = 'tehkö',
                                                      plural2            = 'tehkää',
                                                      plural2_negative   = 'tehkö',
                                                      plural3            = 'tehkööt',
                                                      plural3_negative   = 'tehkö',
                                                      passive            = 'tehtäköön',
                                                      passive_negative   = 'tehtäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb71Nähdä("nähdä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("näkevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("nähnyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("näkemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("nähtävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("nähty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("näkemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb71Nähdä("tehdä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'tehdä',
            translative = 'tehdäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "tehdessä",
            inessive_passive = "tehtäessä",
            instructive      = "tehden",
            elative          = "tehdestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "tehtämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("tekeminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "tekemäisillä")

        ensure_inflections_equal(expected, data)
