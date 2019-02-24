import unittest
from ensure import ensure
from .kotus_verb_64_juoda import KotusVerb64Juoda, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb64Juoda("juoda").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'juon',
                                     singular1_negative = 'juo',
                                     singular2          = 'juot',
                                     singular2_negative = 'juo',
                                     singular3          = 'juo',
                                     singular3_negative = 'juo',
                                     plural1            = 'juomme',
                                     plural1_negative   = 'juo',
                                     plural2            = 'juotte',
                                     plural2_negative   = 'juo',
                                     plural3            = 'juovat',
                                     plural3_negative   = 'juo',
                                     passive            = 'juodaan',
                                     passive_negative   = 'juoda')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        # try other vowel group
        conjugations = moduses = KotusVerb64Juoda("lyödä").moduses().indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['löin'],
                                                  singular1_negative = 'lyönyt',
                                                  singular2s         = ['löit'],
                                                  singular2_negative = 'lyönyt',
                                                  singular3s         = ['löi'],
                                                  singular3_negative = 'lyönyt',
                                                  plural1s           = ['löimme'],
                                                  plural1_negative   = 'lyöneet',
                                                  plural2s           = ['löitte'],
                                                  plural2_negative   = 'lyöneet',
                                                  plural3s           = ['löivät'],
                                                  plural3_negative   = 'lyöneet',
                                                  passive            = 'lyötiin',
                                                  passive_negative   = 'lyöty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'juonut',
                                     singular1_negative = 'juonut',
                                     singular2          = 'juonut',
                                     singular2_negative = 'juonut',
                                     singular3          = 'juonut',
                                     singular3_negative = 'juonut',
                                     plural1            = 'juoneet',
                                     plural1_negative   = 'juoneet',
                                     plural2            = 'juoneet',
                                     plural2_negative   = 'juoneet',
                                     plural3            = 'juoneet',
                                     plural3_negative   = 'juoneet',
                                     passive            = 'juotu',
                                     passive_negative   = 'juotu')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'joisin',
                                     singular1_negative = 'joisi',
                                     singular2          = 'joisit',
                                     singular2_negative = 'joisi',
                                     singular3          = 'joisi',
                                     singular3_negative = 'joisi',
                                     plural1            = 'joisimme',
                                     plural1_negative   = 'joisi',
                                     plural2            = 'joisitte',
                                     plural2_negative   = 'joisi',
                                     plural3            = 'joisivat',
                                     plural3_negative   = 'joisi',
                                     passive            = 'juotaisiin',
                                     passive_negative   = 'juotaisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'juonen',
                                     singular1_negative = 'juone',
                                     singular2          = 'juonet',
                                     singular2_negative = 'juone',
                                     singular3          = 'juonee',
                                     singular3_negative = 'juone',
                                     plural1            = 'juonemme',
                                     plural1_negative   = 'juone',
                                     plural2            = 'juonette',
                                     plural2_negative   = 'juone',
                                     plural3            = 'juonevat',
                                     plural3_negative   = 'juone',
                                     passive            = 'juotaneen',
                                     passive_negative   = 'juotane')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(singular2          = 'juo',
                                                      singular2_negative = 'juo',
                                                      singular3          = 'juokoon',
                                                      singular3_negative = 'juoko',
                                                      plural1            = 'juokaamme',
                                                      plural1_negative   = 'juoko',
                                                      plural2            = 'juokaa',
                                                      plural2_negative   = 'juoko',
                                                      plural3            = 'juokoot',
                                                      plural3_negative   = 'juoko',
                                                      passive            = 'juotakoon',
                                                      passive_negative   = 'juotako')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb64Juoda("juoda").participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.nominative).equals("juova")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.nominative).equals("juonut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.nominative).equals("juoma")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.nominative).equals("juotava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.nominative).equals("juotu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.nominative).equals("juomaton")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb64Juoda("juoda").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='juoda',
            translative='juodakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "juodessa",
            inessive_passive = "juotaessa",
            instructive      = "juoden",
            elative          = "juodesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "juotaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("juominen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "juomaisilla")

        ensure_inflections_equal(expected, data)
