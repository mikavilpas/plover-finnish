import unittest
from ensure import ensure
from .kotus_verb_56_laulaa import KotusVerb56Laulaa, VerbPersonalForms, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_b_kaappi_kaapin_opas_oppaan, gradate_kotus_j_hento_hennon_vanne_vanteen
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA

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

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["lauloin"],
            singular2s         = ["lauloit"],
            singular3s         = ["lauloi"],
            singular1_negative = "laulanut",
            singular2_negative = "laulanut",
            singular3_negative = "laulanut",
            plural1s           = ["lauloimme"],
            plural2s           = ["lauloitte"],
            plural3s           = ["lauloivat"],
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
                                  genitives_plural=['tappavien',
                                                    'tappavain'],
                                  partitives=['tappavaa'],
                                  partitives_plural=['tappavia'],
                                  accusatives=['tappava',
                                               'tappavan'],
                                  accusative_plural='tappavat',
                                  inessive='tappavassa',
                                  inessives_plural=['tappavissa'],
                                  elative='tappavasta',
                                  elatives_plural=['tappavista'],
                                  illatives=['tappavaan'],
                                  illatives_plural=['tappaviin'],
                                  adessive='tappavalla',
                                  adessives_plural=['tappavilla'],
                                  ablative='tappavalta',
                                  ablatives_plural=['tappavilta'],
                                  allative='tappavalle',
                                  allatives_plural=['tappaville'],
                                  essive='tappavana',
                                  essives_plural=['tappavina'],
                                  translative='tappavaksi',
                                  translatives_plural=['tappaviksi'],
                                  abessive='tappavatta',
                                  abessives_plural=['tappavitta'],
                                  instructives_plural=['tappavin'],
                                  comitatives_plural=['tappavine'])

        ensure_inflections_equal(expected, data)

    def test_group_2_nut(self):
        data = KotusVerb56Laulaa("tappaa",
                                 gradate_kotus_b_kaappi_kaapin_opas_oppaan) \
                                 .participles() \
                                 .group_2_NUT()

        expected = InflectionInfo(nominative='tappanut',
                                  nominative_plural='tappaneet',
                                  genitive='tappaneen',
                                  genitives_plural=['tappaneiden',
                                                    'tappaneitten'],
                                  partitives=['tappanutta'],
                                  partitives_plural=['tappaneita'],
                                  accusatives=['tappanut',
                                               'tappaneen'],
                                  accusative_plural='tappaneet',
                                  inessive='tappaneessa',
                                  inessives_plural=['tappaneissa'],
                                  elative='tappaneesta',
                                  elatives_plural=['tappaneista'],
                                  illatives=['tappaneeseen'],
                                  illatives_plural=['tappaneisiin',
                                                    'tappaneihin'],
                                  adessive='tappaneella',
                                  adessives_plural=['tappaneilla'],
                                  ablative='tappaneelta',
                                  ablatives_plural=['tappaneilta'],
                                  allative='tappaneelle',
                                  allatives_plural=['tappaneille'],
                                  essive='tappaneena',
                                  essives_plural=['tappaneina'],
                                  translative='tappaneeksi',
                                  translatives_plural=['tappaneiksi'],
                                  abessive='tappaneetta',
                                  abessives_plural=['tappaneitta'],
                                  instructives_plural=['tappanein'],
                                  comitatives_plural=['tappaneine'])

        ensure_inflections_equal(expected, data)

    def test_group_3_ma(self):
        data = KotusVerb56Laulaa("kantaa",
                                 gradate_kotus_j_hento_hennon_vanne_vanteen) \
                                 .participles() \
                                 .group_3_MA_agent_participle()

        expected = InflectionInfo(nominative='kantama',
                                  nominative_plural='kantamat',
                                  genitive='kantaman',
                                  genitives_plural=['kantamien',
                                                    'kantamain'],
                                  partitives=['kantamaa'],
                                  partitives_plural=['kantamia'],
                                  accusatives=['kantama',
                                               'kantaman'],
                                  accusative_plural='kantamat',
                                  inessive='kantamassa',
                                  inessives_plural=['kantamissa'],
                                  elative='kantamasta',
                                  elatives_plural=['kantamista'],
                                  illatives=['kantamaan'],
                                  illatives_plural=['kantamiin'],
                                  adessive='kantamalla',
                                  adessives_plural=['kantamilla'],
                                  ablative='kantamalta',
                                  ablatives_plural=['kantamilta'],
                                  allative='kantamalle',
                                  allatives_plural=['kantamille'],
                                  essive='kantamana',
                                  essives_plural=['kantamina'],
                                  translative='kantamaksi',
                                  translatives_plural=['kantamiksi'],
                                  abessive='kantamatta',
                                  abessives_plural=['kantamitta'],
                                  instructives_plural=['kantamin'],
                                  comitatives_plural=['kantamine'])

        ensure_inflections_equal(expected, data)

    def test_group_4_va_passive(self):
        data = KotusVerb56Laulaa("kantaa",
                                 gradate_kotus_j_hento_hennon_vanne_vanteen) \
                                 .participles() \
                                 .group_4_VA_passive()

        expected = InflectionInfo(nominative='kannettava',
                                  nominative_plural='kannettavat',
                                  genitive='kannettavan',
                                  genitives_plural=['kannettavien',
                                                    'kannettavain'],
                                  partitives=['kannettavaa'],
                                  partitives_plural=['kannettavia'],
                                  accusatives=['kannettava',
                                               'kannettavan'],
                                  accusative_plural='kannettavat',
                                  inessive='kannettavassa',
                                  inessives_plural=['kannettavissa'],
                                  elative='kannettavasta',
                                  elatives_plural=['kannettavista'],
                                  illatives=['kannettavaan'],
                                  illatives_plural=['kannettaviin'],
                                  adessive='kannettavalla',
                                  adessives_plural=['kannettavilla'],
                                  ablative='kannettavalta',
                                  ablatives_plural=['kannettavilta'],
                                  allative='kannettavalle',
                                  allatives_plural=['kannettaville'],
                                  essive='kannettavana',
                                  essives_plural=['kannettavina'],
                                  translative='kannettavaksi',
                                  translatives_plural=['kannettaviksi'],
                                  abessive='kannettavatta',
                                  abessives_plural=['kannettavitta'],
                                  instructives_plural=['kannettavin'],
                                  comitatives_plural=['kannettavine'])

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

    def test_group_6_negation(self):
        data = KotusVerb56Laulaa("tappaa",
                                 gradate_kotus_b_kaappi_kaapin_opas_oppaan) \
                                 .participles() \
                                 .group_6_negation()

        expected = InflectionInfo(nominative='tappamaton',
                                  nominative_plural='tappamattomat',
                                  genitive='tappamattoman',
                                  genitives_plural=['tappamattomien',
                                                    'tappamatonten'],
                                  partitives=['tappamatonta'],
                                  partitives_plural=['tappamattomia'],
                                  accusatives=['tappamaton',
                                               'tappamattoman'],
                                  accusative_plural='tappamattomat',
                                  inessive='tappamattomassa',
                                  inessives_plural=['tappamattomissa'],
                                  elative='tappamattomasta',
                                  elatives_plural=['tappamattomista'],
                                  illatives=['tappamattomaan'],
                                  illatives_plural=['tappamattomiin'],
                                  adessive='tappamattomalla',
                                  adessives_plural=['tappamattomilla'],
                                  ablative='tappamattomalta',
                                  ablatives_plural=['tappamattomilta'],
                                  allative='tappamattomalle',
                                  allatives_plural=['tappamattomille'],
                                  essive='tappamattomana',
                                  essives_plural=['tappamattomina'],
                                  translative='tappamattomaksi',
                                  translatives_plural=['tappamattomiksi'],
                                  abessive='tappamattomatta',
                                  abessives_plural=['tappamattomitta'],
                                  instructives_plural=['tappamattomin'],
                                  comitatives_plural=['tappamattomine'])

        ensure_inflections_equal(expected, data)


class TestInfinitives(unittest.TestCase):
    def test_group_1(self):
        data = KotusVerb56Laulaa("tappaa").infinitives().group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='tappaa',
            translative='tappaakse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = KotusVerb56Laulaa("laulaa").infinitives().group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "laulaessa",
            inessive_passive = "laulettaessa",
            instructive      = "laulaen",
            elative          = "laulaesta")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = KotusVerb56Laulaa("laulaa").infinitives().group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "laulettaman")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = KotusVerb56Laulaa("laulaa").infinitives().group_4_MINEN()

        expected = InflectionInfo(nominative='laulaminen',
                                  nominative_plural='laulamiset',
                                  genitive='laulamisen',
                                  genitives_plural=['laulamisten',
                                                    'laulamisien'],
                                  partitives=['laulamista'],
                                  partitives_plural=['laulamisia'],
                                  accusatives=['laulaminen',
                                               'laulamisen'],
                                  accusative_plural='laulamiset',
                                  inessive='laulamisessa',
                                  inessives_plural=['laulamisissa'],
                                  elative='laulamisesta',
                                  elatives_plural=['laulamisista'],
                                  illatives=['laulamiseen'],
                                  illatives_plural=['laulamisiin'],
                                  adessive='laulamisella',
                                  adessives_plural=['laulamisilla'],
                                  ablative='laulamiselta',
                                  ablatives_plural=['laulamisilta'],
                                  allative='laulamiselle',
                                  allatives_plural=['laulamisille'],
                                  essive='laulamisena',
                                  essives_plural=['laulamisina'],
                                  translative='laulamiseksi',
                                  translatives_plural=['laulamisiksi'],
                                  abessive='laulamisetta',
                                  abessives_plural=['laulamisitta'],
                                  instructives_plural=['laulamisin'],
                                  comitatives_plural=['laulamisine'])

        ensure_inflections_equal(expected, data)

    def test_group_5(self):
        data = KotusVerb56Laulaa("laulaa").infinitives().group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "laulamaisilla")

        ensure_inflections_equal(expected, data)
