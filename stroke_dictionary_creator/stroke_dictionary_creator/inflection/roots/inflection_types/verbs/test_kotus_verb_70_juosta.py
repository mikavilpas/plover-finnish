import unittest
from ensure import ensure
from .kotus_verb_70_juosta import KotusVerb70Juosta, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb70Juosta("piestä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'pieksen',
                                     singular1_negative = 'piekse',
                                     singular2          = 'piekset',
                                     singular2_negative = 'piekse',
                                     singular3          = 'pieksee',
                                     singular3_negative = 'piekse',
                                     plural1            = 'pieksemme',
                                     plural1_negative   = 'piekse',
                                     plural2            = 'pieksette',
                                     plural2_negative   = 'piekse',
                                     plural3            = 'pieksevät',
                                     plural3_negative   = 'piekse',
                                     passive            = 'piestään',
                                     passive_negative   = 'piestä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['pieksin'],
                                                  singular1_negative = 'piessyt',
                                                  singular2s         = ['pieksit'],
                                                  singular2_negative = 'piessyt',
                                                  singular3s         = ['pieksi'],
                                                  singular3_negative = 'piessyt',
                                                  plural1s           = ['pieksimme'],
                                                  plural1_negative   = 'piesseet',
                                                  plural2s           = ['pieksitte'],
                                                  plural2_negative   = 'piesseet',
                                                  plural3s           = ['pieksivät'],
                                                  plural3_negative   = 'piesseet',
                                                  passive            = 'piestiin',
                                                  passive_negative   = 'piesty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'piessyt',
                                     singular1_negative = 'piessyt',
                                     singular2          = 'piessyt',
                                     singular2_negative = 'piessyt',
                                     singular3          = 'piessyt',
                                     singular3_negative = 'piessyt',
                                     plural1            = 'piesseet',
                                     plural1_negative   = 'piesseet',
                                     plural2            = 'piesseet',
                                     plural2_negative   = 'piesseet',
                                     plural3            = 'piesseet',
                                     plural3_negative   = 'piesseet',
                                     passive            = 'piesty',
                                     passive_negative   = 'piesty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'pieksisin',
                                     singular1_negative = 'pieksisi',
                                     singular2          = 'pieksisit',
                                     singular2_negative = 'pieksisi',
                                     singular3          = 'pieksisi',
                                     singular3_negative = 'pieksisi',
                                     plural1            = 'pieksisimme',
                                     plural1_negative   = 'pieksisi',
                                     plural2            = 'pieksisitte',
                                     plural2_negative   = 'pieksisi',
                                     plural3            = 'pieksisivät',
                                     plural3_negative   = 'pieksisi',
                                     passive            = 'piestäisiin',
                                     passive_negative   = 'piestäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'piessen',
                                     singular1_negative = 'piesse',
                                     singular2          = 'piesset',
                                     singular2_negative = 'piesse',
                                     singular3          = 'piessee',
                                     singular3_negative = 'piesse',
                                     plural1            = 'piessemme',
                                     plural1_negative   = 'piesse',
                                     plural2            = 'piessette',
                                     plural2_negative   = 'piesse',
                                     plural3            = 'piessevät',
                                     plural3_negative   = 'piesse',
                                     passive            = 'piestäneen',
                                     passive_negative   = 'piestäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'piekse',
            singular2_negative = 'piekse',
            singular3          = 'piesköön',
            singular3_negative = 'pieskö',
            plural1            = 'pieskäämme',
            plural1_negative   = 'pieskö',
            plural2            = 'pieskää',
            plural2_negative   = 'pieskö',
            plural3            = 'pieskööt',
            plural3_negative   = 'pieskö',
            passive            = 'piestäköön',
            passive_negative   = 'piestäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb70Juosta("piestä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("pieksevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("piessyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("pieksemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("piestävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("piesty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("pieksemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb70Juosta("piestä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'piestä',
            translative = 'piestäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "piestessä",
            inessive_passive = "piestäessä",
            instructive      = "piesten",
            elative          = "piestestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "piestämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("piekseminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "pieksemäisillä")

        ensure_inflections_equal(expected, data)
