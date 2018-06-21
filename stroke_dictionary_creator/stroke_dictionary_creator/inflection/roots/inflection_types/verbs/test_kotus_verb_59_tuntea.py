import unittest
from ensure import ensure
from .kotus_verb_59_tuntea import KotusVerb59Tuntea, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb59Tuntea("tuntea",
                                g.gradate_kotus_j_hento_hennon_vanne_vanteen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1='tunnen',
                                     singular1_negative='tunne',
                                     singular2='tunnet',
                                     singular2_negative='tunne',
                                     singular3='tuntee',
                                     singular3_negative='tunne',
                                     plural1='tunnemme',
                                     plural1_negative='tunne',
                                     plural2='tunnette',
                                     plural2_negative='tunne',
                                     plural3='tuntevat',
                                     plural3_negative='tunne',
                                     passive='tunnetaan',
                                     passive_negative='tunneta')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s=['tunsin'],
                                                  singular1_negative='tuntenut',
                                                  singular2s=['tunsit'],
                                                  singular2_negative='tuntenut',
                                                  singular3s=['tunsi'],
                                                  singular3_negative='tuntenut',
                                                  plural1s=['tunsimme'],
                                                  plural1_negative='tunteneet',
                                                  plural2s=['tunsitte'],
                                                  plural2_negative='tunteneet',
                                                  plural3s=['tunsivat'],
                                                  plural3_negative='tunteneet',
                                                  passive='tunnettiin',
                                                  passive_negative='tunnettu')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1='tuntenut',
                                     singular1_negative='tuntenut',
                                     singular2='tuntenut',
                                     singular2_negative='tuntenut',
                                     singular3='tuntenut',
                                     singular3_negative='tuntenut',
                                     plural1='tunteneet',
                                     plural1_negative='tunteneet',
                                     plural2='tunteneet',
                                     plural2_negative='tunteneet',
                                     plural3='tunteneet',
                                     plural3_negative='tunteneet',
                                     passive='tunnettu',
                                     passive_negative='tunnettu')


        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1='tuntisin',
                                     singular1_negative='tuntisi',
                                     singular2='tuntisit',
                                     singular2_negative='tuntisi',
                                     singular3='tuntisi',
                                     singular3_negative='tuntisi',
                                     plural1='tuntisimme',
                                     plural1_negative='tuntisi',
                                     plural2='tuntisitte',
                                     plural2_negative='tuntisi',
                                     plural3='tuntisivat',
                                     plural3_negative='tuntisi',
                                     passive='tunnettaisiin',
                                     passive_negative='tunnettaisi')


        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1='tuntenen',
                                     singular1_negative='tuntene',
                                     singular2='tuntenet',
                                     singular2_negative='tuntene',
                                     singular3='tuntenee',
                                     singular3_negative='tuntene',
                                     plural1='tuntenemme',
                                     plural1_negative='tuntene',
                                     plural2='tuntenette',
                                     plural2_negative='tuntene',
                                     plural3='tuntenevat',
                                     plural3_negative='tuntene',
                                     passive='tunnettaneen',
                                     passive_negative='tunnettane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2='tunne',
                                                      singular2_negative='tunne',
                                                      singular3='tuntekoon',
                                                      singular3_negative='tunteko',
                                                      plural1='tuntekaamme',
                                                      plural1_negative='tunteko',
                                                      plural2='tuntekaa',
                                                      plural2_negative='tunteko',
                                                      plural3='tuntekoot',
                                                      plural3_negative='tunteko',
                                                      passive='tunnettakoon',
                                                      passive_negative='tunnettako')

        ensure_inflections_equal(expected, conjugations)


class TestGradationWithUmlauts(unittest.TestCase):
    moduses = KotusVerb59Tuntea("tuntea",
                                g.gradate_kotus_j_hento_hennon_vanne_vanteen) \
                                .moduses()

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "tuntenen",
                                     singular2          = "tuntenet",
                                     singular3          = "tuntenee",
                                     singular1_negative = "tuntene",
                                     singular2_negative = "tuntene",
                                     singular3_negative = "tuntene",
                                     plural1            = "tuntenemme",
                                     plural2            = "tuntenette",
                                     plural3            = "tuntenevat",
                                     plural1_negative   = "tuntene",
                                     plural2_negative   = "tuntene",
                                     plural3_negative   = "tuntene",
                                     passive            = "tunnettaneen",
                                     passive_negative   = "tunnettane",)

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):
    participles = KotusVerb59Tuntea("tuntea",
                                    g.gradate_kotus_j_hento_hennon_vanne_vanteen) \
                                    .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("tunteva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("tuntenut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("tuntema")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("tunnettava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("tunnettu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("tuntematon")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb59Tuntea("tuntea",
                                    g.gradate_kotus_j_hento_hennon_vanne_vanteen)\
                                    .infinitives()
    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='tuntea',
            translative='tunteakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "tuntiessa",
            inessive_passive = "tunnettaessa",
            instructive      = "tuntien",
            elative          = "tuntiesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "tunnettaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("tunteminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "tuntemaisilla")

        ensure_inflections_equal(expected, data)
