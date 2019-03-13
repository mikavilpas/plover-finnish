import unittest
from ensure import ensure
from .kotus_verb_74_katketa import KotusVerb74Katketa, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb74Katketa("ängetä",
                                 g.gradate_kotus_g_rengas_renkaan).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'änkeän',
                                     singular1_negative = 'änkeä',
                                     singular2          = 'änkeät',
                                     singular2_negative = 'änkeä',
                                     singular3          = 'änkeää',
                                     singular3_negative = 'änkeä',
                                     plural1            = 'änkeämme',
                                     plural1_negative   = 'änkeä',
                                     plural2            = 'änkeätte',
                                     plural2_negative   = 'änkeä',
                                     plural3            = 'änkeävät',
                                     plural3_negative   = 'änkeä',
                                     passive            = 'ängetään',
                                     passive_negative   = 'ängetä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['änkesin'],
                                                  singular1_negative = 'ängennyt',
                                                  singular2s         = ['änkesit'],
                                                  singular2_negative = 'ängennyt',
                                                  singular3s         = ['änkesi'],
                                                  singular3_negative = 'ängennyt',
                                                  plural1s           = ['änkesimme'],
                                                  plural1_negative   = 'ängenneet',
                                                  plural2s           = ['änkesitte'],
                                                  plural2_negative   = 'ängenneet',
                                                  plural3s           = ['änkesivät'],
                                                  plural3_negative   = 'ängenneet',
                                                  passive            = 'ängettiin',
                                                  passive_negative   = 'ängetty')


        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'ängennyt',
                                     singular1_negative = 'ängennyt',
                                     singular2          = 'ängennyt',
                                     singular2_negative = 'ängennyt',
                                     singular3          = 'ängennyt',
                                     singular3_negative = 'ängennyt',
                                     plural1            = 'ängenneet',
                                     plural1_negative   = 'ängenneet',
                                     plural2            = 'ängenneet',
                                     plural2_negative   = 'ängenneet',
                                     plural3            = 'ängenneet',
                                     plural3_negative   = 'ängenneet',
                                     passive            = 'ängetty',
                                     passive_negative   = 'ängetty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'änkeisin',
                                     singular1_negative = 'änkeisi',
                                     singular2          = 'änkeisit',
                                     singular2_negative = 'änkeisi',
                                     singular3          = 'änkeisi',
                                     singular3_negative = 'änkeisi',
                                     plural1            = 'änkeisimme',
                                     plural1_negative   = 'änkeisi',
                                     plural2            = 'änkeisitte',
                                     plural2_negative   = 'änkeisi',
                                     plural3            = 'änkeisivät',
                                     plural3_negative   = 'änkeisi',
                                     passive            = 'ängettäisiin',
                                     passive_negative   = 'ängettäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'ängennen',
                                     singular1_negative = 'ängenne',
                                     singular2          = 'ängennet',
                                     singular2_negative = 'ängenne',
                                     singular3          = 'ängennee',
                                     singular3_negative = 'ängenne',
                                     plural1            = 'ängennemme',
                                     plural1_negative   = 'ängenne',
                                     plural2            = 'ängennette',
                                     plural2_negative   = 'ängenne',
                                     plural3            = 'ängennevät',
                                     plural3_negative   = 'ängenne',
                                     passive            = 'ängettäneen',
                                     passive_negative   = 'ängettäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'änkeä',
            singular2_negative = 'änkeä',
            singular3          = 'ängetköön',
            singular3_negative = 'ängetkö',
            plural1            = 'ängetkäämme',
            plural1_negative   = 'ängetkö',
            plural2            = 'ängetkää',
            plural2_negative   = 'ängetkö',
            plural3            = 'ängetkööt',
            plural3_negative   = 'ängetkö',
            passive            = 'ängettäköön',
            passive_negative   = 'ängettäkö')

        ensure_inflections_equal(expected, conjugations)


    def test_juoruta(self):
        # regression case
        moduses = KotusVerb74Katketa("luututa",
                                     g.gradate_kotus_c_kate_katteen).moduses()
        conjugations = moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'luutunnen',
                                     singular1_negative = 'luutunne',
                                     singular2          = 'luutunnet',
                                     singular2_negative = 'luutunne',
                                     singular3          = 'luutunnee',
                                     singular3_negative = 'luutunne',
                                     plural1            = 'luutunnemme',
                                     plural1_negative   = 'luutunne',
                                     plural2            = 'luutunnette',
                                     plural2_negative   = 'luutunne',
                                     plural3            = 'luutunnevat',
                                     plural3_negative   = 'luutunne',
                                     passive            = 'luututtaneen',
                                     passive_negative   = 'luututtane')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb74Katketa("todeta",
                                     g.gradate_kotus_f_keidas_keitaan).participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("toteava")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("todennut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("toteama")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("todettava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("todettu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("toteamaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb74Katketa("todeta",
                                     g.gradate_kotus_f_keidas_keitaan).infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form  = 'todeta',
            translative = 'todetakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "todetessa",
            inessive_passive = "todettaessa",
            instructive      = "todeten",
            elative          = "todetesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "todettaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("toteaminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "toteamaisilla")

        ensure_inflections_equal(expected, data)
