import unittest
from ensure import ensure
from .kotus_verb_60_lähteä import KotusVerb60Lähteä, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb60Lähteä("lähteä").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1='lähden',
                                     singular1_negative='lähde',
                                     singular2='lähdet',
                                     singular2_negative='lähde',
                                     singular3='lähtee',
                                     singular3_negative='lähde',
                                     plural1='lähdemme',
                                     plural1_negative='lähde',
                                     plural2='lähdette',
                                     plural2_negative='lähde',
                                     plural3='lähtevät',
                                     plural3_negative='lähde',
                                     passive='lähdetään',
                                     passive_negative='lähdetä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s=['lähdin',
                                                              'läksin'],
                                                  singular1_negative='lähtenyt',
                                                  singular2s=['lähdit',
                                                              'läksit'],
                                                  singular2_negative='lähtenyt',
                                                  singular3s=['lähti',
                                                              'läksi'],
                                                  singular3_negative='lähtenyt',
                                                  plural1s=['lähdimme',
                                                            'läksimme'],
                                                  plural1_negative='lähteneet',
                                                  plural2s=['lähditte',
                                                            'läksitte'],
                                                  plural2_negative='lähteneet',
                                                  plural3s=['lähtivät',
                                                            'läksivät'],
                                                  plural3_negative='lähteneet',
                                                  passive='lähdettiin',
                                                  passive_negative='lähdetty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1='lähtenyt',
                                     singular1_negative='lähtenyt',
                                     singular2='lähtenyt',
                                     singular2_negative='lähtenyt',
                                     singular3='lähtenyt',
                                     singular3_negative='lähtenyt',
                                     plural1='lähteneet',
                                     plural1_negative='lähteneet',
                                     plural2='lähteneet',
                                     plural2_negative='lähteneet',
                                     plural3='lähteneet',
                                     plural3_negative='lähteneet',
                                     passive='lähdetty',
                                     passive_negative='lähdetty')

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1='lähtisin',
                                     singular1_negative='lähtisi',
                                     singular2='lähtisit',
                                     singular2_negative='lähtisi',
                                     singular3='lähtisi',
                                     singular3_negative='lähtisi',
                                     plural1='lähtisimme',
                                     plural1_negative='lähtisi',
                                     plural2='lähtisitte',
                                     plural2_negative='lähtisi',
                                     plural3='lähtisivät',
                                     plural3_negative='lähtisi',
                                     passive='lähdettäisiin',
                                     passive_negative='lähdettäisi')

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1='lähtenen',
                                     singular1_negative='lähtene',
                                     singular2='lähtenet',
                                     singular2_negative='lähtene',
                                     singular3='lähtenee',
                                     singular3_negative='lähtene',
                                     plural1='lähtenemme',
                                     plural1_negative='lähtene',
                                     plural2='lähtenette',
                                     plural2_negative='lähtene',
                                     plural3='lähtenevät',
                                     plural3_negative='lähtene',
                                     passive='lähdettäneen',
                                     passive_negative='lähdettäne')


        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2='lähde',
                                                      singular2_negative='lähde',
                                                      singular3='lähteköön',
                                                      singular3_negative='lähtekö',
                                                      plural1='lähtekäämme',
                                                      plural1_negative='lähtekö',
                                                      plural2='lähtekää',
                                                      plural2_negative='lähtekö',
                                                      plural3='lähtekööt',
                                                      plural3_negative='lähtekö',
                                                      passive='lähdettäköön',
                                                      passive_negative='lähdettäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb60Lähteä("lähteä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("lähtevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("lähtenyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("lähtemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("lähdettävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("lähdetty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("lähtemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb60Lähteä("lähteä").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='lähteä',
            translative='lähteäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "lähtiessä",
            inessive_passive = "lähdettäessä",
            instructive      = "lähtien",
            elative          = "lähtiestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "lähdettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("lähteminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "lähtemäisillä")

        ensure_inflections_equal(expected, data)
