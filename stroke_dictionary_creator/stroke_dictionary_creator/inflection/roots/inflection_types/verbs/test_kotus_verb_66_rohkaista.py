import unittest
from ensure import ensure
from .kotus_verb_66_rohkaista import KotusVerb66Rohkaista, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb66Rohkaista("vavista",
                                   g.gradate_kotus_e_taive_taipeen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'vapisen',
                                     singular1_negative = 'vapise',
                                     singular2          = 'vapiset',
                                     singular2_negative = 'vapise',
                                     singular3          = 'vapisee',
                                     singular3_negative = 'vapise',
                                     plural1            = 'vapisemme',
                                     plural1_negative   = 'vapise',
                                     plural2            = 'vapisette',
                                     plural2_negative   = 'vapise',
                                     plural3            = 'vapisevat',
                                     plural3_negative   = 'vapise',
                                     passive            = 'vavistaan',
                                     passive_negative   = 'vavista')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['vapisin'],
                                                  singular1_negative = 'vavissut',
                                                  singular2s         = ['vapisit'],
                                                  singular2_negative = 'vavissut',
                                                  singular3s         = ['vapisi'],
                                                  singular3_negative = 'vavissut',
                                                  plural1s           = ['vapisimme'],
                                                  plural1_negative   = 'vavisseet',
                                                  plural2s           = ['vapisitte'],
                                                  plural2_negative   = 'vavisseet',
                                                  plural3s           = ['vapisivat'],
                                                  plural3_negative   = 'vavisseet',
                                                  passive            = 'vavistiin',
                                                  passive_negative   = 'vavistu')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'vavissut',
                                     singular1_negative = 'vavissut',
                                     singular2          = 'vavissut',
                                     singular2_negative = 'vavissut',
                                     singular3          = 'vavissut',
                                     singular3_negative = 'vavissut',
                                     plural1            = 'vavisseet',
                                     plural1_negative   = 'vavisseet',
                                     plural2            = 'vavisseet',
                                     plural2_negative   = 'vavisseet',
                                     plural3            = 'vavisseet',
                                     plural3_negative   = 'vavisseet',
                                     passive            = 'vavistu',
                                     passive_negative   = 'vavistu')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'vapisisin',
                                     singular1_negative = 'vapisisi',
                                     singular2          = 'vapisisit',
                                     singular2_negative = 'vapisisi',
                                     singular3          = 'vapisisi',
                                     singular3_negative = 'vapisisi',
                                     plural1            = 'vapisisimme',
                                     plural1_negative   = 'vapisisi',
                                     plural2            = 'vapisisitte',
                                     plural2_negative   = 'vapisisi',
                                     plural3            = 'vapisisivat',
                                     plural3_negative   = 'vapisisi',
                                     passive            = 'vavistaisiin',
                                     passive_negative   = 'vavistaisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'vavissen',
                                     singular1_negative = 'vavisse',
                                     singular2          = 'vavisset',
                                     singular2_negative = 'vavisse',
                                     singular3          = 'vavissee',
                                     singular3_negative = 'vavisse',
                                     plural1            = 'vavissemme',
                                     plural1_negative   = 'vavisse',
                                     plural2            = 'vavissette',
                                     plural2_negative   = 'vavisse',
                                     plural3            = 'vavissevat',
                                     plural3_negative   = 'vavisse',
                                     passive            = 'vavistaneen',
                                     passive_negative   = 'vavistane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'vapise',
            singular2_negative = 'vapise',
            singular3          = 'vaviskoon',
            singular3_negative = 'vavisko',
            plural1            = 'vaviskaamme',
            plural1_negative   = 'vavisko',
            plural2            = 'vaviskaa',
            plural2_negative   = 'vavisko',
            plural3            = 'vaviskoot',
            plural3_negative   = 'vavisko',
            passive            = 'vavistakoon',
            passive_negative   = 'vavistako')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb66Rohkaista("pestä").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("pesevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("pessyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("pesemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("pestävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("pesty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("pesemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb66Rohkaista("vavista",
                                       g.gradate_kotus_e_taive_taipeen).infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='vavista',
            translative='vavistakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "vavistessa",
            inessive_passive = "vavistaessa",
            instructive      = "vavisten",
            elative          = "vavistesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "vavistaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("vapiseminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "vapisemaisilla")

        ensure_inflections_equal(expected, data)
