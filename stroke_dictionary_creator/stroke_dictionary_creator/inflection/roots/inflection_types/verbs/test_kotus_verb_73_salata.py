import unittest
from ensure import ensure
from .kotus_verb_73_salata import KotusVerb73Salata, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb73Salata("hyljätä",
                                g.gradate_kotus_l_hylje_hylkeen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'hylkään',
                                     singular1_negative = 'hylkää',
                                     singular2          = 'hylkäät',
                                     singular2_negative = 'hylkää',
                                     singular3          = 'hylkää',
                                     singular3_negative = 'hylkää',
                                     plural1            = 'hylkäämme',
                                     plural1_negative   = 'hylkää',
                                     plural2            = 'hylkäätte',
                                     plural2_negative   = 'hylkää',
                                     plural3            = 'hylkäävät',
                                     plural3_negative   = 'hylkää',
                                     passive            = 'hyljätään',
                                     passive_negative   = 'hyljätä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['hylkäsin'],
                                                  singular1_negative = 'hyljännyt',
                                                  singular2s         = ['hylkäsit'],
                                                  singular2_negative = 'hyljännyt',
                                                  singular3s         = ['hylkäsi'],
                                                  singular3_negative = 'hyljännyt',
                                                  plural1s           = ['hylkäsimme'],
                                                  plural1_negative   = 'hyljänneet',
                                                  plural2s           = ['hylkäsitte'],
                                                  plural2_negative   = 'hyljänneet',
                                                  plural3s           = ['hylkäsivät'],
                                                  plural3_negative   = 'hyljänneet',
                                                  passive            = 'hyljättiin',
                                                  passive_negative   = 'hyljätty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'hyljännyt',
                                     singular1_negative = 'hyljännyt',
                                     singular2          = 'hyljännyt',
                                     singular2_negative = 'hyljännyt',
                                     singular3          = 'hyljännyt',
                                     singular3_negative = 'hyljännyt',
                                     plural1            = 'hyljänneet',
                                     plural1_negative   = 'hyljänneet',
                                     plural2            = 'hyljänneet',
                                     plural2_negative   = 'hyljänneet',
                                     plural3            = 'hyljänneet',
                                     plural3_negative   = 'hyljänneet',
                                     passive            = 'hyljätty',
                                     passive_negative   = 'hyljätty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'hylkäisin',
                                     singular1_negative = 'hylkäisi',
                                     singular2          = 'hylkäisit',
                                     singular2_negative = 'hylkäisi',
                                     singular3          = 'hylkäisi',
                                     singular3_negative = 'hylkäisi',
                                     plural1            = 'hylkäisimme',
                                     plural1_negative   = 'hylkäisi',
                                     plural2            = 'hylkäisitte',
                                     plural2_negative   = 'hylkäisi',
                                     plural3            = 'hylkäisivät',
                                     plural3_negative   = 'hylkäisi',
                                     passive            = 'hyljättäisiin',
                                     passive_negative   = 'hyljättäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'hyljännen',
                                     singular1_negative = 'hyljänne',
                                     singular2          = 'hyljännet',
                                     singular2_negative = 'hyljänne',
                                     singular3          = 'hyljännee',
                                     singular3_negative = 'hyljänne',
                                     plural1            = 'hyljännemme',
                                     plural1_negative   = 'hyljänne',
                                     plural2            = 'hyljännette',
                                     plural2_negative   = 'hyljänne',
                                     plural3            = 'hyljännevät',
                                     plural3_negative   = 'hyljänne',
                                     passive            = 'hyljättäneen',
                                     passive_negative   = 'hyljättäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'hylkää',
            singular2_negative = 'hylkää',
            singular3          = 'hyljätköön',
            singular3_negative = 'hyljätkö',
            plural1            = 'hyljätkäämme',
            plural1_negative   = 'hyljätkö',
            plural2            = 'hyljätkää',
            plural2_negative   = 'hyljätkö',
            plural3            = 'hyljätkööt',
            plural3_negative   = 'hyljätkö',
            passive            = 'hyljättäköön',
            passive_negative   = 'hyljättäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb73Salata("salata").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("salaava")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("salannut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("salaama")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("salattava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("salattu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("salaamaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb73Salata("salata").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'salata',
            translative = 'salatakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "salatessa",
            inessive_passive = "salattaessa",
            instructive      = "salaten",
            elative          = "salatesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "salattaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("salaaminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "salaamaisilla")

        ensure_inflections_equal(expected, data)
