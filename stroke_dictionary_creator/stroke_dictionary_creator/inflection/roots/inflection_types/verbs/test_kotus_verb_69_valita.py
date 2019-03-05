import unittest
from ensure import ensure
from .kotus_verb_69_valita import KotusVerb69Valita, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb69Valita("merkitä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'merkitsen',
                                     singular1_negative = 'merkitse',
                                     singular2          = 'merkitset',
                                     singular2_negative = 'merkitse',
                                     singular3          = 'merkitsee',
                                     singular3_negative = 'merkitse',
                                     plural1            = 'merkitsemme',
                                     plural1_negative   = 'merkitse',
                                     plural2            = 'merkitsette',
                                     plural2_negative   = 'merkitse',
                                     plural3            = 'merkitsevät',
                                     plural3_negative   = 'merkitse',
                                     passive            = 'merkitään',
                                     passive_negative   = 'merkitä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['merkitsin'],
                                                  singular1_negative = 'merkinnyt',
                                                  singular2s         = ['merkitsit'],
                                                  singular2_negative = 'merkinnyt',
                                                  singular3s         = ['merkitsi'],
                                                  singular3_negative = 'merkinnyt',
                                                  plural1s           = ['merkitsimme'],
                                                  plural1_negative   = 'merkinneet',
                                                  plural2s           = ['merkitsitte'],
                                                  plural2_negative   = 'merkinneet',
                                                  plural3s           = ['merkitsivät'],
                                                  plural3_negative   = 'merkinneet',
                                                  passive            = 'merkittiin',
                                                  passive_negative   = 'merkitty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'merkinnyt',
                                     singular1_negative = 'merkinnyt',
                                     singular2          = 'merkinnyt',
                                     singular2_negative = 'merkinnyt',
                                     singular3          = 'merkinnyt',
                                     singular3_negative = 'merkinnyt',
                                     plural1            = 'merkinneet',
                                     plural1_negative   = 'merkinneet',
                                     plural2            = 'merkinneet',
                                     plural2_negative   = 'merkinneet',
                                     plural3            = 'merkinneet',
                                     plural3_negative   = 'merkinneet',
                                     passive            = 'merkitty',
                                     passive_negative   = 'merkitty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'merkitsisin',
                                     singular1_negative = 'merkitsisi',
                                     singular2          = 'merkitsisit',
                                     singular2_negative = 'merkitsisi',
                                     singular3          = 'merkitsisi',
                                     singular3_negative = 'merkitsisi',
                                     plural1            = 'merkitsisimme',
                                     plural1_negative   = 'merkitsisi',
                                     plural2            = 'merkitsisitte',
                                     plural2_negative   = 'merkitsisi',
                                     plural3            = 'merkitsisivät',
                                     plural3_negative   = 'merkitsisi',
                                     passive            = 'merkittäisiin',
                                     passive_negative   = 'merkittäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'merkinnen',
                                     singular1_negative = 'merkinne',
                                     singular2          = 'merkinnet',
                                     singular2_negative = 'merkinne',
                                     singular3          = 'merkinnee',
                                     singular3_negative = 'merkinne',
                                     plural1            = 'merkinnemme',
                                     plural1_negative   = 'merkinne',
                                     plural2            = 'merkinnette',
                                     plural2_negative   = 'merkinne',
                                     plural3            = 'merkinnevät',
                                     plural3_negative   = 'merkinne',
                                     passive            = 'merkittäneen',
                                     passive_negative   = 'merkittäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'merkitse',
            singular2_negative = 'merkitse',
            singular3          = 'merkitköön',
            singular3_negative = 'merkitkö',
            plural1            = 'merkitkäämme',
            plural1_negative   = 'merkitkö',
            plural2            = 'merkitkää',
            plural2_negative   = 'merkitkö',
            plural3            = 'merkitkööt',
            plural3_negative   = 'merkitkö',
            passive            = 'merkittäköön',
            passive_negative   = 'merkittäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb69Valita("iloita").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("iloitseva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("iloinnut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("iloitsema")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("iloittava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("iloittu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("iloitsematon")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb69Valita("iloita").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='iloita',
            translative='iloitakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "iloitessa",
            inessive_passive = "iloittaessa",
            instructive      = "iloiten",
            elative          = "iloitesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "iloittaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("iloitseminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "iloitsemaisilla")

        ensure_inflections_equal(expected, data)
