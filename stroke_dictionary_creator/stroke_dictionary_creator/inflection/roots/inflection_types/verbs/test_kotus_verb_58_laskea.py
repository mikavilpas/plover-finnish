import unittest
from ensure import ensure
from .kotus_verb_58_laskea import KotusVerb58Laskea, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb58Laskea("kulkea",
                                g.gradate_kotus_l_arki_arjen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1='kuljen',
                                     singular1_negative='kulje',
                                     singular2='kuljet',
                                     singular2_negative='kulje',
                                     singular3='kulkee',
                                     singular3_negative='kulje',
                                     plural1='kuljemme',
                                     plural1_negative='kulje',
                                     plural2='kuljette',
                                     plural2_negative='kulje',
                                     plural3='kulkevat',
                                     plural3_negative='kulje',
                                     passive='kuljetaan',
                                     passive_negative='kuljeta')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s=['kuljin'],
                                                  singular1_negative='kulkenut',
                                                  singular2s=['kuljit'],
                                                  singular2_negative='kulkenut',
                                                  singular3s=['kulki'],
                                                  singular3_negative='kulkenut',
                                                  plural1s=['kuljimme'],
                                                  plural1_negative='kulkeneet',
                                                  plural2s=['kuljitte'],
                                                  plural2_negative='kulkeneet',
                                                  plural3s=['kulkivat'],
                                                  plural3_negative='kulkeneet',
                                                  passive='kuljettiin',
                                                  passive_negative='kuljettu')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1='kulkenut',
                                     singular1_negative='kulkenut',
                                     singular2='kulkenut',
                                     singular2_negative='kulkenut',
                                     singular3='kulkenut',
                                     singular3_negative='kulkenut',
                                     plural1='kulkeneet',
                                     plural1_negative='kulkeneet',
                                     plural2='kulkeneet',
                                     plural2_negative='kulkeneet',
                                     plural3='kulkeneet',
                                     plural3_negative='kulkeneet',
                                     passive='kuljettu',
                                     passive_negative='kuljettu')

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1='kulkisin',
                                     singular1_negative='kulkisi',
                                     singular2='kulkisit',
                                     singular2_negative='kulkisi',
                                     singular3='kulkisi',
                                     singular3_negative='kulkisi',
                                     plural1='kulkisimme',
                                     plural1_negative='kulkisi',
                                     plural2='kulkisitte',
                                     plural2_negative='kulkisi',
                                     plural3='kulkisivat',
                                     plural3_negative='kulkisi',
                                     passive='kuljettaisiin',
                                     passive_negative='kuljettaisi')

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1='kulkenen',
                                     singular1_negative='kulkene',
                                     singular2='kulkenet',
                                     singular2_negative='kulkene',
                                     singular3='kulkenee',
                                     singular3_negative='kulkene',
                                     plural1='kulkenemme',
                                     plural1_negative='kulkene',
                                     plural2='kulkenette',
                                     plural2_negative='kulkene',
                                     plural3='kulkenevat',
                                     plural3_negative='kulkene',
                                     passive='kuljettaneen',
                                     passive_negative='kuljettane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2='kulje',
                                                      singular2_negative='kulje',
                                                      singular3='kulkekoon',
                                                      singular3_negative='kulkeko',
                                                      plural1='kulkekaamme',
                                                      plural1_negative='kulkeko',
                                                      plural2='kulkekaa',
                                                      plural2_negative='kulkeko',
                                                      plural3='kulkekoot',
                                                      plural3_negative='kulkeko',
                                                      passive='kuljettakoon',
                                                      passive_negative='kuljettako')

        ensure_inflections_equal(expected, conjugations)


class TestGradationWithUmlauts(unittest.TestCase):
    moduses = KotusVerb58Laskea("särkeä",
                                g.gradate_kotus_l_arki_arjen) \
                                .moduses()

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "särkenen",
                                     singular2          = "särkenet",
                                     singular3          = "särkenee",
                                     singular1_negative = "särkene",
                                     singular2_negative = "särkene",
                                     singular3_negative = "särkene",
                                     plural1            = "särkenemme",
                                     plural2            = "särkenette",
                                     plural3            = "särkenevät",
                                     plural1_negative   = "särkene",
                                     plural2_negative   = "särkene",
                                     plural3_negative   = "särkene",
                                     passive            = "särjettäneen",
                                     passive_negative   = "särjettäne",)

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):
    participles = KotusVerb58Laskea("särkeä",
                                    g.gradate_kotus_l_arki_arjen) \
                                    .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("särkevä")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("särkenyt")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("särkemä")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("särjettävä")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("särjetty")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("särkemätön")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb58Laskea("särkeä",
                                    g.gradate_kotus_l_arki_arjen)\
                                    .infinitives()
    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='särkeä',
            translative='särkeäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "särkiessä",
            inessive_passive = "särjettäessä",
            instructive      = "särkien",
            elative          = "särkiestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "särjettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("särkeminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "särkemäisillä")

        ensure_inflections_equal(expected, data)
