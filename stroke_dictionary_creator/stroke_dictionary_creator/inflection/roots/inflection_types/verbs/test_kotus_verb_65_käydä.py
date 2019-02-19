import unittest
from ensure import ensure
from .kotus_verb_65_käydä import KotusVerb65Käydä, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb65Käydä("käydä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'käyn',
                                     singular1_negative = 'käy',
                                     singular2          = 'käyt',
                                     singular2_negative = 'käy',
                                     singular3          = 'käy',
                                     singular3_negative = 'käy',
                                     plural1            = 'käymme',
                                     plural1_negative   = 'käy',
                                     plural2            = 'käytte',
                                     plural2_negative   = 'käy',
                                     plural3            = 'käyvät',
                                     plural3_negative   = 'käy',
                                     passive            = 'käydään',
                                     passive_negative   = 'käydä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['kävin'],
                                                  singular1_negative = 'käynyt',
                                                  singular2s         = ['kävit'],
                                                  singular2_negative = 'käynyt',
                                                  singular3s         = ['kävi'],
                                                  singular3_negative = 'käynyt',
                                                  plural1s           = ['kävimme'],
                                                  plural1_negative   = 'käyneet',
                                                  plural2s           = ['kävitte'],
                                                  plural2_negative   = 'käyneet',
                                                  plural3s           = ['kävivät'],
                                                  plural3_negative   = 'käyneet',
                                                  passive            = 'käytiin',
                                                  passive_negative   = 'käyty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'käynyt',
                                     singular1_negative = 'käynyt',
                                     singular2          = 'käynyt',
                                     singular2_negative = 'käynyt',
                                     singular3          = 'käynyt',
                                     singular3_negative = 'käynyt',
                                     plural1            = 'käyneet',
                                     plural1_negative   = 'käyneet',
                                     plural2            = 'käyneet',
                                     plural2_negative   = 'käyneet',
                                     plural3            = 'käyneet',
                                     plural3_negative   = 'käyneet',
                                     passive            = 'käyty',
                                     passive_negative   = 'käyty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'kävisin',
                                     singular1_negative = 'kävisi',
                                     singular2          = 'kävisit',
                                     singular2_negative = 'kävisi',
                                     singular3          = 'kävisi',
                                     singular3_negative = 'kävisi',
                                     plural1            = 'kävisimme',
                                     plural1_negative   = 'kävisi',
                                     plural2            = 'kävisitte',
                                     plural2_negative   = 'kävisi',
                                     plural3            = 'kävisivät',
                                     plural3_negative   = 'kävisi',
                                     passive            = 'käytäisiin',
                                     passive_negative   = 'käytäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'käynen',
                                     singular1_negative = 'käyne',
                                     singular2          = 'käynet',
                                     singular2_negative = 'käyne',
                                     singular3          = 'käynee',
                                     singular3_negative = 'käyne',
                                     plural1            = 'käynemme',
                                     plural1_negative   = 'käyne',
                                     plural2            = 'käynette',
                                     plural2_negative   = 'käyne',
                                     plural3            = 'käynevät',
                                     plural3_negative   = 'käyne',
                                     passive            = 'käytäneen',
                                     passive_negative   = 'käytäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2          = 'käy',
                                                      singular2_negative = 'käy',
                                                      singular3          = 'käyköön',
                                                      singular3_negative = 'käykö',
                                                      plural1            = 'käykäämme',
                                                      plural1_negative   = 'käykö',
                                                      plural2            = 'käykää',
                                                      plural2_negative   = 'käykö',
                                                      plural3            = 'käykööt',
                                                      plural3_negative   = 'käykö',
                                                      passive            = 'käytäköön',
                                                      passive_negative   = 'käytäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb65Käydä("käydä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("käyvä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("käynyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("käymä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("käytävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("käyty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("käymätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb65Käydä("käydä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='käydä',
            translative='käydäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "käydessä",
            inessive_passive = "käytäessä",
            instructive      = "käyden",
            elative          = "käydestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "käytämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("käyminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "käymäisillä")

        ensure_inflections_equal(expected, data)
