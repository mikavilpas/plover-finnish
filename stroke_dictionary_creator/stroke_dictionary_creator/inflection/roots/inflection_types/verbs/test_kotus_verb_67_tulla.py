import unittest
from ensure import ensure
from .kotus_verb_67_tulla import KotusVerb67Tulla, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ... import gradation as g
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

class TestBasic(unittest.TestCase):
    moduses = KotusVerb67Tulla("mitellä",
                               g.gradate_kotus_c_kate_katteen).moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = 'mittelen',
                                     singular1_negative = 'mittele',
                                     singular2          = 'mittelet',
                                     singular2_negative = 'mittele',
                                     singular3          = 'mittelee',
                                     singular3_negative = 'mittele',
                                     plural1            = 'mittelemme',
                                     plural1_negative   = 'mittele',
                                     plural2            = 'mittelette',
                                     plural2_negative   = 'mittele',
                                     plural3            = 'mittelevät',
                                     plural3_negative   = 'mittele',
                                     passive            = 'mitellään',
                                     passive_negative   = 'mitellä')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(singular1s         = ['mittelin'],
                                                  singular1_negative = 'mitellyt',
                                                  singular2s         = ['mittelit'],
                                                  singular2_negative = 'mitellyt',
                                                  singular3s         = ['mitteli'],
                                                  singular3_negative = 'mitellyt',
                                                  plural1s           = ['mittelimme'],
                                                  plural1_negative   = 'mitelleet',
                                                  plural2s           = ['mittelitte'],
                                                  plural2_negative   = 'mitelleet',
                                                  plural3s           = ['mittelivät'],
                                                  plural3_negative   = 'mitelleet',
                                                  passive            = 'miteltiin',
                                                  passive_negative   = 'mitelty')

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'mitellyt',
                                     singular1_negative = 'mitellyt',
                                     singular2          = 'mitellyt',
                                     singular2_negative = 'mitellyt',
                                     singular3          = 'mitellyt',
                                     singular3_negative = 'mitellyt',
                                     plural1            = 'mitelleet',
                                     plural1_negative   = 'mitelleet',
                                     plural2            = 'mitelleet',
                                     plural2_negative   = 'mitelleet',
                                     plural3            = 'mitelleet',
                                     plural3_negative   = 'mitelleet',
                                     passive            = 'mitelty',
                                     passive_negative   = 'mitelty')

        ensure_inflections_equal(expected, conjugations)

    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = 'mittelisin',
                                     singular1_negative = 'mittelisi',
                                     singular2          = 'mittelisit',
                                     singular2_negative = 'mittelisi',
                                     singular3          = 'mittelisi',
                                     singular3_negative = 'mittelisi',
                                     plural1            = 'mittelisimme',
                                     plural1_negative   = 'mittelisi',
                                     plural2            = 'mittelisitte',
                                     plural2_negative   = 'mittelisi',
                                     plural3            = 'mittelisivät',
                                     plural3_negative   = 'mittelisi',
                                     passive            = 'miteltäisiin',
                                     passive_negative   = 'miteltäisi')

        ensure_inflections_equal(expected, conjugations)

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = 'mitellen',
                                     singular1_negative = 'mitelle',
                                     singular2          = 'mitellet',
                                     singular2_negative = 'mitelle',
                                     singular3          = 'mitellee',
                                     singular3_negative = 'mitelle',
                                     plural1            = 'mitellemme',
                                     plural1_negative   = 'mitelle',
                                     plural2            = 'mitellette',
                                     plural2_negative   = 'mitelle',
                                     plural3            = 'mitellevät',
                                     plural3_negative   = 'mitelle',
                                     passive            = 'miteltäneen',
                                     passive_negative   = 'miteltäne')

        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = 'mittele',
            singular2_negative = 'mittele',
            singular3          = 'mitelköön',
            singular3_negative = 'mitelkö',
            plural1            = 'mitelkäämme',
            plural1_negative   = 'mitelkö',
            plural2            = 'mitelkää',
            plural2_negative   = 'mitelkö',
            plural3            = 'mitelkööt',
            plural3_negative   = 'mitelkö',
            passive            = 'miteltäköön',
            passive_negative   = 'miteltäkö')

        ensure_inflections_equal(expected, conjugations)


class TestParticiples(unittest.TestCase):
    participles = KotusVerb67Tulla("imarrella",
                                   g.gradate_kotus_k_porras_portaan).participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()
        ensure(data.positive.nominative).equals("imarteleva")

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()
        ensure(data.positive.nominative).equals("imarrellut")

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()
        ensure(data.positive.nominative).equals("imartelema")

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()
        ensure(data.positive.nominative).equals("imarreltava")

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()
        ensure(data.positive.nominative).equals("imarreltu")

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()
        ensure(data.positive.nominative).equals("imartelematon")


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb67Tulla("tulla").infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='tulla',
            translative='tullakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "tullessa",
            inessive_passive = "tultaessa",
            instructive      = "tullen",
            elative          = "tullesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "tultaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()
        ensure(data.nominative).equals("tuleminen")

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "tulemaisilla")

        ensure_inflections_equal(expected, data)
