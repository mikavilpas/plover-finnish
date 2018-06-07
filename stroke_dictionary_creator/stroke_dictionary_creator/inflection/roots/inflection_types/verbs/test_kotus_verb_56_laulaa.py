import unittest
from ensure import ensure
from .kotus_verb_56_laulaa import KotusVerb56Laulaa, VerbPersonalForms, VerbPersonalFormsImperativePresent
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_b_kaappi_kaapin_opas_oppaan
from ...noun_inflection_info import InflectionInfo

class TestBasic(unittest.TestCase):
    moduses = KotusVerb56Laulaa("laulaa").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "laulan",
                                     singular2          = "laulat",
                                     singular3          = "laulaa",
                                     singular1_negative = "laula",
                                     singular2_negative = "laula",
                                     singular3_negative = "laula",
                                     plural1            = "laulamme",
                                     plural2            = "laulatte",
                                     plural3            = "laulavat",
                                     plural1_negative   = "laula",
                                     plural2_negative   = "laula",
                                     plural3_negative   = "laula",
                                     passive            = "lauletaan",
                                     passive_negative   = "lauleta",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalForms(singular1          = "lauloin",
                                     singular2          = "lauloit",
                                     singular3          = "lauloi",
                                     singular1_negative = "laulanut",
                                     singular2_negative = "laulanut",
                                     singular3_negative = "laulanut",
                                     plural1            = "lauloimme",
                                     plural2            = "lauloitte",
                                     plural3            = "lauloivat",
                                     plural1_negative   = "laulaneet",
                                     plural2_negative   = "laulaneet",
                                     plural3_negative   = "laulaneet",
                                     passive            = "laulettiin",
                                     passive_negative   = "laulettu",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "laulanut",
                                     singular2          = "laulanut",
                                     singular3          = "laulanut",
                                     singular1_negative = "laulanut",
                                     singular2_negative = "laulanut",
                                     singular3_negative = "laulanut",
                                     plural1            = "laulaneet",
                                     plural2            = "laulaneet",
                                     plural3            = "laulaneet",
                                     plural1_negative   = "laulaneet",
                                     plural2_negative   = "laulaneet",
                                     plural3_negative   = "laulaneet",
                                     passive            = "laulettu",
                                     passive_negative   = "laulettu",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "laulaisin",
                                     singular2          = "laulaisit",
                                     singular3          = "laulaisi",
                                     singular1_negative = "laulaisi",
                                     singular2_negative = "laulaisi",
                                     singular3_negative = "laulaisi",
                                     plural1            = "laulaisimme",
                                     plural2            = "laulaisitte",
                                     plural3            = "laulaisivat",
                                     plural1_negative   = "laulaisi",
                                     plural2_negative   = "laulaisi",
                                     plural3_negative   = "laulaisi",
                                     passive            = "laulettaisiin",
                                     passive_negative   = "laulettaisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "laulanen",
                                     singular2          = "laulanet",
                                     singular3          = "laulanee",
                                     singular1_negative = "laulane",
                                     singular2_negative = "laulane",
                                     singular3_negative = "laulane",
                                     plural1            = "laulanemme",
                                     plural2            = "laulanette",
                                     plural3            = "laulanevat",
                                     plural1_negative   = "laulane",
                                     plural2_negative   = "laulane",
                                     plural3_negative   = "laulane",
                                     passive            = "laulettaneen",
                                     passive_negative   = "laulettane",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "laula",
            singular3          = "laulakoon",
            singular2_negative = "laula",
            singular3_negative = "laulako",
            plural1            = "laulakaamme",
            plural2            = "laulakaa",
            plural3            = "laulakoot",
            plural1_negative   = "laulako",
            plural2_negative   = "laulako",
            plural3_negative   = "laulako",
            passive            = "laulettakoon",
            passive_negative   = "laulettako",)

        ensure_inflections_equal(expected, conjugations)


# No umlauts to test

class TestGradation(unittest.TestCase):
    moduses = KotusVerb56Laulaa("tappaa",
                                gradate_kotus_b_kaappi_kaapin_opas_oppaan) \
                                .moduses()

    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "tappanen",
                                     singular2          = "tappanet",
                                     singular3          = "tappanee",
                                     singular1_negative = "tappane",
                                     singular2_negative = "tappane",
                                     singular3_negative = "tappane",
                                     plural1            = "tappanemme",
                                     plural2            = "tappanette",
                                     plural3            = "tappanevat",
                                     plural1_negative   = "tappane",
                                     plural2_negative   = "tappane",
                                     plural3_negative   = "tappane",
                                     passive            = "tapettaneen",
                                     passive_negative   = "tapettane",)

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):
    def test_group_1_va(self):
        data = KotusVerb56Laulaa("tappaa",
                                 gradate_kotus_b_kaappi_kaapin_opas_oppaan) \
                                 .participles() \
                                 .group_1_VA()

        expected = InflectionInfo(nominative='tappava',
                                nominative_plural='tappavat',
                                genitive='tappavan',
                                genitives_plural=['tappavoiden',
                                                    'tappavoitten',
                                                    'tappavain'],
                                partitives=['tappavaa'],
                                partitives_plural=['tappavoita'],
                                accusatives=['tappava',
                                            'tappavan'],
                                accusative_plural='tappavat',
                                inessive='tappavassa',
                                inessives_plural=['tappavoissa'],
                                elative='tappavasta',
                                elatives_plural=['tappavoista'],
                                illatives=['tappavaan'],
                                illatives_plural=['tappavoihin'],
                                adessive='tappavalla',
                                adessives_plural=['tappavoilla'],
                                ablative='tappavalta',
                                ablatives_plural=['tappavoilta'],
                                allative='tappavalle',
                                allatives_plural=['tappavoille'],
                                essive='tappavana',
                                essives_plural=['tappavoina'],
                                translative='tappavaksi',
                                translatives_plural=['tappavoiksi'],
                                abessive='tappavatta',
                                abessives_plural=['tappavoitta'],
                                instructives_plural=['tappavoin'],
                                comitatives_plural=['tappavoine'])

        ensure_inflections_equal(expected, data)

    def test_group_5_tu(self):
        data = KotusVerb56Laulaa("tappaa",
                                 gradate_kotus_b_kaappi_kaapin_opas_oppaan) \
                                 .participles() \
                                 .group_5_TU_passive()

        expected = InflectionInfo(nominative='tapettu',
                                  nominative_plural='tapetut',
                                  genitive='tapetun',
                                  genitives_plural=['tapettujen'],
                                  partitives=['tapettua'],
                                  partitives_plural=['tapettuja'],
                                  accusatives=['tapettu',
                                               'tapetun'],
                                  accusative_plural='tapettuja',
                                  inessive='tapetussa',
                                  inessives_plural=['tapetuissa'],
                                  elative='tapetusta',
                                  elatives_plural=['tapetuista'],
                                  illatives=['tapettuun'],
                                  illatives_plural=['tapettuihin'],
                                  adessive='tapetulla',
                                  adessives_plural=['tapetuilla'],
                                  ablative='tapetulta',
                                  ablatives_plural=['tapetuilta'],
                                  allative='tapetulle',
                                  allatives_plural=['tapetuille'],
                                  essive='tapettuna',
                                  essives_plural=['tapettuina'],
                                  translative='tapetuksi',
                                  translatives_plural=['tapetuiksi'],
                                  abessive='tapetutta',
                                  abessives_plural=['tapetuitta'],
                                  instructives_plural=['tapetuin'],
                                  comitatives_plural=['tapettuine'])

        ensure_inflections_equal(expected, data)
