import unittest
from ensure import ensure
from .kotus_verb_72_vanheta import KotusVerb72Vanheta, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb72Vanheta("edetä",
                                 g.gradate_kotus_f_keidas_keitaan).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'etenen',
                                     singular1_negative = 'etene',
                                     singular2          = 'etenet',
                                     singular2_negative = 'etene',
                                     singular3          = 'etenee',
                                     singular3_negative = 'etene',
                                     plural1            = 'etenemme',
                                     plural1_negative   = 'etene',
                                     plural2            = 'etenette',
                                     plural2_negative   = 'etene',
                                     plural3            = 'etenevät',
                                     plural3_negative   = 'etene',
                                     passive            = 'edetään',
                                     passive_negative   = 'edetä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['etenin'],
                                                  singular1_negative = 'edennyt',
                                                  singular2s         = ['etenit'],
                                                  singular2_negative = 'edennyt',
                                                  singular3s         = ['eteni'],
                                                  singular3_negative = 'edennyt',
                                                  plural1s           = ['etenimme'],
                                                  plural1_negative   = 'edenneet',
                                                  plural2s           = ['etenitte'],
                                                  plural2_negative   = 'edenneet',
                                                  plural3s           = ['etenivät'],
                                                  plural3_negative   = 'edenneet',
                                                  passive            = 'edettiin',
                                                  passive_negative   = 'edetty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'edennyt',
                                     singular1_negative = 'edennyt',
                                     singular2          = 'edennyt',
                                     singular2_negative = 'edennyt',
                                     singular3          = 'edennyt',
                                     singular3_negative = 'edennyt',
                                     plural1            = 'edenneet',
                                     plural1_negative   = 'edenneet',
                                     plural2            = 'edenneet',
                                     plural2_negative   = 'edenneet',
                                     plural3            = 'edenneet',
                                     plural3_negative   = 'edenneet',
                                     passive            = 'edetty',
                                     passive_negative   = 'edetty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'etenisin',
                                     singular1_negative = 'etenisi',
                                     singular2          = 'etenisit',
                                     singular2_negative = 'etenisi',
                                     singular3          = 'etenisi',
                                     singular3_negative = 'etenisi',
                                     plural1            = 'etenisimme',
                                     plural1_negative   = 'etenisi',
                                     plural2            = 'etenisitte',
                                     plural2_negative   = 'etenisi',
                                     plural3            = 'etenisivät',
                                     plural3_negative   = 'etenisi',
                                     passive            = 'edettäisiin',
                                     passive_negative   = 'edettäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'edennen',
                                     singular1_negative = 'edenne',
                                     singular2          = 'edennet',
                                     singular2_negative = 'edenne',
                                     singular3          = 'edennee',
                                     singular3_negative = 'edenne',
                                     plural1            = 'edennemme',
                                     plural1_negative   = 'edenne',
                                     plural2            = 'edennette',
                                     plural2_negative   = 'edenne',
                                     plural3            = 'edennevät',
                                     plural3_negative   = 'edenne',
                                     passive            = 'edettäneen',
                                     passive_negative   = 'edettäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'etene',
            singular2_negative = 'etene',
            singular3          = 'edetköön',
            singular3_negative = 'edetkö',
            plural1            = 'edetkäämme',
            plural1_negative   = 'edetkö',
            plural2            = 'edetkää',
            plural2_negative   = 'edetkö',
            plural3            = 'edetkööt',
            plural3_negative   = 'edetkö',
            passive            = 'edettäköön',
            passive_negative   = 'edettäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb72Vanheta("vähetä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("vähenevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("vähennyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("vähenemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("vähettävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("vähetty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("vähenemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb72Vanheta("vanheta").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'vanheta',
            translative = 'vanhetakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "vanhetessa",
            inessive_passive = "vanhettaessa",
            instructive      = "vanheten",
            elative          = "vanhetesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "vanhettaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("vanheneminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "vanhenemaisilla")

        ensure_inflections_equal(expected, data)
