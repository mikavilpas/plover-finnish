import unittest
from ensure import ensure
from .kotus_verb_57_saartaa import KotusVerb57Saartaa, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_k_virta_virran
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb57Saartaa("saartaa",
                                 gradate_kotus_k_virta_virran).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "saarran",
                                     singular2          = "saarrat",
                                     singular3          = "saartaa",
                                     singular1_negative = "saarra",
                                     singular2_negative = "saarra",
                                     singular3_negative = "saarra",
                                     plural1            = "saarramme",
                                     plural2            = "saarratte",
                                     plural3            = "saartavat",
                                     plural1_negative   = "saarra",
                                     plural2_negative   = "saarra",
                                     plural3_negative   = "saarra",
                                     passive            = "saarretaan",
                                     passive_negative   = "saarreta",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["saarsin", "saarroin"],
            singular2s         = ["saarsit", "saarroit"],
            singular3s         = ["saarsi", "saartoi"],
            singular1_negative = "saartanut",
            singular2_negative = "saartanut",
            singular3_negative = "saartanut",
            plural1s           = ["saarsimme", "saarroimme"],
            plural2s           = ["saarsitte", "saarroitte"],
            plural3s           = ["saarsivat", "saartoivat"],
            plural1_negative   = "saartaneet",
            plural2_negative   = "saartaneet",
            plural3_negative   = "saartaneet",
            passive            = "saarrettiin",
            passive_negative   = "saarrettu",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "saartanut",
                                     singular2          = "saartanut",
                                     singular3          = "saartanut",
                                     singular1_negative = "saartanut",
                                     singular2_negative = "saartanut",
                                     singular3_negative = "saartanut",
                                     plural1            = "saartaneet",
                                     plural2            = "saartaneet",
                                     plural3            = "saartaneet",
                                     plural1_negative   = "saartaneet",
                                     plural2_negative   = "saartaneet",
                                     plural3_negative   = "saartaneet",
                                     passive            = "saarrettu",
                                     passive_negative   = "saarrettu",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "saartaisin",
                                     singular2          = "saartaisit",
                                     singular3          = "saartaisi",
                                     singular1_negative = "saartaisi",
                                     singular2_negative = "saartaisi",
                                     singular3_negative = "saartaisi",
                                     plural1            = "saartaisimme",
                                     plural2            = "saartaisitte",
                                     plural3            = "saartaisivat",
                                     plural1_negative   = "saartaisi",
                                     plural2_negative   = "saartaisi",
                                     plural3_negative   = "saartaisi",
                                     passive            = "saarrettaisiin",
                                     passive_negative   = "saarrettaisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "saartanen",
                                     singular2          = "saartanet",
                                     singular3          = "saartanee",
                                     singular1_negative = "saartane",
                                     singular2_negative = "saartane",
                                     singular3_negative = "saartane",
                                     plural1            = "saartanemme",
                                     plural2            = "saartanette",
                                     plural3            = "saartanevat",
                                     plural1_negative   = "saartane",
                                     plural2_negative   = "saartane",
                                     plural3_negative   = "saartane",
                                     passive            = "saarrettaneen",
                                     passive_negative   = "saarrettane",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "saarra",
            singular3          = "saartakoon",
            singular2_negative = "saarra",
            singular3_negative = "saartako",
            plural1            = "saartakaamme",
            plural2            = "saartakaa",
            plural3            = "saartakoot",
            plural1_negative   = "saartako",
            plural2_negative   = "saartako",
            plural3_negative   = "saartako",
            passive            = "saarrettakoon",
            passive_negative   = "saarrettako",)

        ensure_inflections_equal(expected, conjugations)


# No umlauts to test

class TestGradation(unittest.TestCase):
    moduses = KotusVerb57Saartaa("saartaa",
                                 gradate_kotus_k_virta_virran) \
                                 .moduses()

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "saartanen",
                                     singular2          = "saartanet",
                                     singular3          = "saartanee",
                                     singular1_negative = "saartane",
                                     singular2_negative = "saartane",
                                     singular3_negative = "saartane",
                                     plural1            = "saartanemme",
                                     plural2            = "saartanette",
                                     plural3            = "saartanevat",
                                     plural1_negative   = "saartane",
                                     plural2_negative   = "saartane",
                                     plural3_negative   = "saartane",
                                     passive            = "saarrettaneen",
                                     passive_negative   = "saarrettane",)

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):
    participles = KotusVerb57Saartaa("saartaa",
                                     gradate_kotus_k_virta_virran) \
                                     .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("saartava")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("saartanut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("saartama")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("saarrettava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("saarrettu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("saartamaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb57Saartaa("saartaa",
                                     gradate_kotus_k_virta_virran)\
                                     .infinitives()
    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='saartaa',
            translative='saartaakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "saartaessa",
            inessive_passive = "saarrettaessa",
            instructive      = "saartaen",
            elative          = "saartaesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "saarrettaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("saartaminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "saartamaisilla")

        ensure_inflections_equal(expected, data)
