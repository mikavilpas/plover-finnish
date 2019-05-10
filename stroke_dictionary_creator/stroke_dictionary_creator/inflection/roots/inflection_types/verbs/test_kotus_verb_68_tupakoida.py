import unittest
from ensure import ensure
from .kotus_verb_68_tupakoida import KotusVerb68Tupakoida, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb68Tupakoida("elämöidä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'elämöin',
                                     singular1_negative = 'elämöi',
                                     singular2          = 'elämöit',
                                     singular2_negative = 'elämöi',
                                     singular3          = 'elämöi',
                                     singular3_negative = 'elämöi',
                                     plural1            = 'elämöimme',
                                     plural1_negative   = 'elämöi',
                                     plural2            = 'elämöitte',
                                     plural2_negative   = 'elämöi',
                                     plural3            = 'elämöivät',
                                     plural3_negative   = 'elämöi',
                                     passive            = 'elämöidään',
                                     passive_negative   = 'elämöidä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['elämöin'],
                                                  singular1_negative = 'elämöinyt',
                                                  singular2s         = ['elämöit'],
                                                  singular2_negative = 'elämöinyt',
                                                  singular3s         = ['elämöi'],
                                                  singular3_negative = 'elämöinyt',
                                                  plural1s           = ['elämöimme'],
                                                  plural1_negative   = 'elämöineet',
                                                  plural2s           = ['elämöitte'],
                                                  plural2_negative   = 'elämöineet',
                                                  plural3s           = ['elämöivät'],
                                                  plural3_negative   = 'elämöineet',
                                                  passive            = 'elämöitiin',
                                                  passive_negative   = 'elämöity')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'elämöinyt',
                                     singular1_negative = 'elämöinyt',
                                     singular2          = 'elämöinyt',
                                     singular2_negative = 'elämöinyt',
                                     singular3          = 'elämöinyt',
                                     singular3_negative = 'elämöinyt',
                                     plural1            = 'elämöineet',
                                     plural1_negative   = 'elämöineet',
                                     plural2            = 'elämöineet',
                                     plural2_negative   = 'elämöineet',
                                     plural3            = 'elämöineet',
                                     plural3_negative   = 'elämöineet',
                                     passive            = 'elämöity',
                                     passive_negative   = 'elämöity')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'elämöisin',
                                     singular1_negative = 'elämöisi',
                                     singular2          = 'elämöisit',
                                     singular2_negative = 'elämöisi',
                                     singular3          = 'elämöisi',
                                     singular3_negative = 'elämöisi',
                                     plural1            = 'elämöisimme',
                                     plural1_negative   = 'elämöisi',
                                     plural2            = 'elämöisitte',
                                     plural2_negative   = 'elämöisi',
                                     plural3            = 'elämöisivät',
                                     plural3_negative   = 'elämöisi',
                                     passive            = 'elämöitäisiin',
                                     passive_negative   = 'elämöitäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'elämöinen',
                                     singular1_negative = 'elämöine',
                                     singular2          = 'elämöinet',
                                     singular2_negative = 'elämöine',
                                     singular3          = 'elämöinee',
                                     singular3_negative = 'elämöine',
                                     plural1            = 'elämöinemme',
                                     plural1_negative   = 'elämöine',
                                     plural2            = 'elämöinette',
                                     plural2_negative   = 'elämöine',
                                     plural3            = 'elämöinevät',
                                     plural3_negative   = 'elämöine',
                                     passive            = 'elämöitäneen',
                                     passive_negative   = 'elämöitäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'elämöi',
            singular2_negative = 'elämöi',
            singular3          = 'elämöiköön',
            singular3_negative = 'elämöikö',
            plural1            = 'elämöikäämme',
            plural1_negative   = 'elämöikö',
            plural2            = 'elämöikää',
            plural2_negative   = 'elämöikö',
            plural3            = 'elämöikööt',
            plural3_negative   = 'elämöikö',
            passive            = 'elämöitäköön',
            passive_negative   = 'elämöitäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb68Tupakoida("urakoida").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("urakoiva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("urakoinut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("urakoima")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("urakoitava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("urakoitu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("urakoimaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb68Tupakoida("tupakoida").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='tupakoida',
            translative='tupakoidakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "tupakoidessa",
            inessive_passive = "tupakoitaessa",
            instructive      = "tupakoiden",
            elative          = "tupakoidesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "tupakoitaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("tupakoiminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "tupakoimaisilla")

        ensure_inflections_equal(expected, data)
