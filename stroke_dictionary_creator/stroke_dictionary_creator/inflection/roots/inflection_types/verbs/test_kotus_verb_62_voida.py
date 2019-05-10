import unittest
from ensure import ensure
from .kotus_verb_62_voida import KotusVerb62Voida, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb62Voida("voida").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'voin',
                                     singular1_negative = 'voi',
                                     singular2          = 'voit',
                                     singular2_negative = 'voi',
                                     singular3          = 'voi',
                                     singular3_negative = 'voi',
                                     plural1            = 'voimme',
                                     plural1_negative   = 'voi',
                                     plural2            = 'voitte',
                                     plural2_negative   = 'voi',
                                     plural3            = 'voivat',
                                     plural3_negative   = 'voi',
                                     passive            = 'voidaan',
                                     passive_negative   = 'voida')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        # try a different gradation and umlauts too
        conjugations = KotusVerb62Voida("epäröidä").moduses().indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['epäröin'],
                                                  singular1_negative = 'epäröinyt',
                                                  singular2s         = ['epäröit'],
                                                  singular2_negative = 'epäröinyt',
                                                  singular3s         = ['epäröi'],
                                                  singular3_negative = 'epäröinyt',
                                                  plural1s           = ['epäröimme'],
                                                  plural1_negative   = 'epäröineet',
                                                  plural2s           = ['epäröitte'],
                                                  plural2_negative   = 'epäröineet',
                                                  plural3s           = ['epäröivät'],
                                                  plural3_negative   = 'epäröineet',
                                                  passive            = 'epäröitiin',
                                                  passive_negative   = 'epäröity')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'voinut',
                                     singular1_negative = 'voinut',
                                     singular2          = 'voinut',
                                     singular2_negative = 'voinut',
                                     singular3          = 'voinut',
                                     singular3_negative = 'voinut',
                                     plural1            = 'voineet',
                                     plural1_negative   = 'voineet',
                                     plural2            = 'voineet',
                                     plural2_negative   = 'voineet',
                                     plural3            = 'voineet',
                                     plural3_negative   = 'voineet',
                                     passive            = 'voitu',
                                     passive_negative   = 'voitu')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'voisin',
                                     singular1_negative = 'voisi',
                                     singular2          = 'voisit',
                                     singular2_negative = 'voisi',
                                     singular3          = 'voisi',
                                     singular3_negative = 'voisi',
                                     plural1            = 'voisimme',
                                     plural1_negative   = 'voisi',
                                     plural2            = 'voisitte',
                                     plural2_negative   = 'voisi',
                                     plural3            = 'voisivat',
                                     plural3_negative   = 'voisi',
                                     passive            = 'voitaisiin',
                                     passive_negative   = 'voitaisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'voinen',
                                     singular1_negative = 'voine',
                                     singular2          = 'voinet',
                                     singular2_negative = 'voine',
                                     singular3          = 'voinee',
                                     singular3_negative = 'voine',
                                     plural1            = 'voinemme',
                                     plural1_negative   = 'voine',
                                     plural2            = 'voinette',
                                     plural2_negative   = 'voine',
                                     plural3            = 'voinevat',
                                     plural3_negative   = 'voine',
                                     passive            = 'voitaneen',
                                     passive_negative   = 'voitane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2          = 'voi',
                                                      singular2_negative = 'voi',
                                                      singular3          = 'voikoon',
                                                      singular3_negative = 'voiko',
                                                      plural1            = 'voikaamme',
                                                      plural1_negative   = 'voiko',
                                                      plural2            = 'voikaa',
                                                      plural2_negative   = 'voiko',
                                                      plural3            = 'voikoot',
                                                      plural3_negative   = 'voiko',
                                                      passive            = 'voitakoon',
                                                      passive_negative   = 'voitako')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb62Voida("hulinoida").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("hulinoiva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("hulinoinut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("hulinoima")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("hulinoitava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("hulinoitu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("hulinoimaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb62Voida("uida").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='uida',
            translative='uidakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "uidessa",
            inessive_passive = "uitaessa",
            instructive      = "uiden",
            elative          = "uidesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "uitaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("uiminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "uimaisilla")

        ensure_inflections_equal(expected, data)
