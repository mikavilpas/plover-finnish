import unittest
from ensure import ensure
from .kotus_verb_61_sallia import KotusVerb61Sallia, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb61Sallia("sopia",
                                g.gradate_kotus_e_sopu_sovun).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'sovin',
                                     singular1_negative = 'sovi',
                                     singular2          = 'sovit',
                                     singular2_negative = 'sovi',
                                     singular3          = 'sopii',
                                     singular3_negative = 'sovi',
                                     plural1            = 'sovimme',
                                     plural1_negative   = 'sovi',
                                     plural2            = 'sovitte',
                                     plural2_negative   = 'sovi',
                                     plural3            = 'sopivat',
                                     plural3_negative   = 'sovi',
                                     passive            = 'sovitaan',
                                     passive_negative   = 'sovita')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        # try a different gradation and umlauts too
        conjugations = KotusVerb61Sallia("märkiä",
                                         g.gradate_kotus_d_reikä_reiän)\
                                         .moduses().indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['märin'],
                                                  singular1_negative = 'märkinyt',
                                                  singular2s         = ['märit'],
                                                  singular2_negative = 'märkinyt',
                                                  singular3s         = ['märki'],
                                                  singular3_negative = 'märkinyt',
                                                  plural1s           = ['märimme'],
                                                  plural1_negative   = 'märkineet',
                                                  plural2s           = ['märitte'],
                                                  plural2_negative   = 'märkineet',
                                                  plural3s           = ['märkivät'],
                                                  plural3_negative   = 'märkineet',
                                                  passive            = 'märittiin',
                                                  passive_negative   = 'märitty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = KotusVerb61Sallia("henkiä",
                                         g.gradate_kotus_g_aurinko_auringon)\
                                         .moduses().indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'henkinyt',
                                     singular1_negative = 'henkinyt',
                                     singular2          = 'henkinyt',
                                     singular2_negative = 'henkinyt',
                                     singular3          = 'henkinyt',
                                     singular3_negative = 'henkinyt',
                                     plural1            = 'henkineet',
                                     plural1_negative   = 'henkineet',
                                     plural2            = 'henkineet',
                                     plural2_negative   = 'henkineet',
                                     plural3            = 'henkineet',
                                     plural3_negative   = 'henkineet',
                                     passive            = 'hengitty',
                                     passive_negative   = 'hengitty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'sopisin',
                                     singular1_negative = 'sopisi',
                                     singular2          = 'sopisit',
                                     singular2_negative = 'sopisi',
                                     singular3          = 'sopisi',
                                     singular3_negative = 'sopisi',
                                     plural1            = 'sopisimme',
                                     plural1_negative   = 'sopisi',
                                     plural2            = 'sopisitte',
                                     plural2_negative   = 'sopisi',
                                     plural3            = 'sopisivat',
                                     plural3_negative   = 'sopisi',
                                     passive            = 'sovittaisiin',
                                     passive_negative   = 'sovittaisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'sopinen',
                                     singular1_negative = 'sopine',
                                     singular2          = 'sopinet',
                                     singular2_negative = 'sopine',
                                     singular3          = 'sopinee',
                                     singular3_negative = 'sopine',
                                     plural1            = 'sopinemme',
                                     plural1_negative   = 'sopine',
                                     plural2            = 'sopinette',
                                     plural2_negative   = 'sopine',
                                     plural3            = 'sopinevat',
                                     plural3_negative   = 'sopine',
                                     passive            = 'sovittaneen',
                                     passive_negative   = 'sovittane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'sovi',
            singular2_negative = 'sovi',
            singular3          = 'sopikoon',
            singular3_negative = 'sopiko',
            plural1            = 'sopikaamme',
            plural1_negative   = 'sopiko',
            plural2            = 'sopikaa',
            plural2_negative   = 'sopiko',
            plural3            = 'sopikoot',
            plural3_negative   = 'sopiko',
            passive            = 'sovittakoon',
            passive_negative   = 'sovittako')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb61Sallia("sopia",
                                    g.gradate_kotus_e_sopu_sovun).participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("sopiva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("sopinut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("sopima")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("sovittava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("sovittu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("sopimaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb61Sallia("sopia",
                                    g.gradate_kotus_e_sopu_sovun).infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='sopia',
            translative='sopiakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "sopiessa",
            inessive_passive = "sovittaessa",
            instructive      = "sopien",
            elative          = "sopiesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "sovittaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("sopiminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "sopimaisilla")

        ensure_inflections_equal(expected, data)
