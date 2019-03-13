import unittest
from ensure import ensure
from .kotus_verb_75_selvitä import KotusVerb75Selvitä, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb75Selvitä("hellitä",
                                 g.gradate_kotus_i_sivellin_siveltimen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'heltiän',
                                     singular1_negative = 'heltiä',
                                     singular2          = 'heltiät',
                                     singular2_negative = 'heltiä',
                                     singular3          = 'heltiää',
                                     singular3_negative = 'heltiä',
                                     plural1            = 'heltiämme',
                                     plural1_negative   = 'heltiä',
                                     plural2            = 'heltiätte',
                                     plural2_negative   = 'heltiä',
                                     plural3            = 'heltiävät',
                                     plural3_negative   = 'heltiä',
                                     passive            = 'hellitään',
                                     passive_negative   = 'hellitä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['heltisin'],
                                                  singular1_negative = 'hellinnyt',
                                                  singular2s         = ['heltisit'],
                                                  singular2_negative = 'hellinnyt',
                                                  singular3s         = ['heltisi'],
                                                  singular3_negative = 'hellinnyt',
                                                  plural1s           = ['heltisimme'],
                                                  plural1_negative   = 'hellinneet',
                                                  plural2s           = ['heltisitte'],
                                                  plural2_negative   = 'hellinneet',
                                                  plural3s           = ['heltisivät'],
                                                  plural3_negative   = 'hellinneet',
                                                  passive            = 'hellittiin',
                                                  passive_negative   = 'hellitty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'hellinnyt',
                                     singular1_negative = 'hellinnyt',
                                     singular2          = 'hellinnyt',
                                     singular2_negative = 'hellinnyt',
                                     singular3          = 'hellinnyt',
                                     singular3_negative = 'hellinnyt',
                                     plural1            = 'hellinneet',
                                     plural1_negative   = 'hellinneet',
                                     plural2            = 'hellinneet',
                                     plural2_negative   = 'hellinneet',
                                     plural3            = 'hellinneet',
                                     plural3_negative   = 'hellinneet',
                                     passive            = 'hellitty',
                                     passive_negative   = 'hellitty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'heltiäisin',
                                     singular1_negative = 'heltiäisi',
                                     singular2          = 'heltiäisit',
                                     singular2_negative = 'heltiäisi',
                                     singular3          = 'heltiäisi',
                                     singular3_negative = 'heltiäisi',
                                     plural1            = 'heltiäisimme',
                                     plural1_negative   = 'heltiäisi',
                                     plural2            = 'heltiäisitte',
                                     plural2_negative   = 'heltiäisi',
                                     plural3            = 'heltiäisivät',
                                     plural3_negative   = 'heltiäisi',
                                     passive            = 'hellittäisiin',
                                     passive_negative   = 'hellittäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'hellinnen',
                                     singular1_negative = 'hellinne',
                                     singular2          = 'hellinnet',
                                     singular2_negative = 'hellinne',
                                     singular3          = 'hellinnee',
                                     singular3_negative = 'hellinne',
                                     plural1            = 'hellinnemme',
                                     plural1_negative   = 'hellinne',
                                     plural2            = 'hellinnette',
                                     plural2_negative   = 'hellinne',
                                     plural3            = 'hellinnevät',
                                     plural3_negative   = 'hellinne',
                                     passive            = 'hellittäneen',
                                     passive_negative   = 'hellittäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'heltiä',
            singular2_negative = 'heltiä',
            singular3          = 'hellitköön',
            singular3_negative = 'hellitkö',
            plural1            = 'hellitkäämme',
            plural1_negative   = 'hellitkö',
            plural2            = 'hellitkää',
            plural2_negative   = 'hellitkö',
            plural3            = 'hellitkööt',
            plural3_negative   = 'hellitkö',
            passive            = 'hellittäköön',
            passive_negative   = 'hellittäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb75Selvitä("keritä",
                                     g.gradate_kotus_d_joukahainen_av6_aie_aikeen)\
                                     .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("kerkiävä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("kerinnyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("kerkiämä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("kerittävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("keritty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("kerkiämätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb75Selvitä("höyrytä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'höyrytä',
            translative = 'höyrytäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "höyrytessä",
            inessive_passive = "höyryttäessä",
            instructive      = "höyryten",
            elative          = "höyrytestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "höyryttämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("höyryäminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "höyryämäisillä")

        ensure_inflections_equal(expected, data)
