import unittest
from ensure import ensure
from .kotus_verb_52_sanoa import KotusVerb52Sanoa, VerbPersonalForms, VerbPersonalFormsImperativePresent
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_f_satu_sadun
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots

class TestBasic(unittest.TestCase):
    moduses = KotusVerb52Sanoa("sanoa").moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "sanon",
                                     singular2          = "sanot",
                                     singular3          = "sanoo",
                                     singular1_negative = "sano",
                                     singular2_negative = "sano",
                                     singular3_negative = "sano",
                                     plural1            = "sanomme",
                                     plural2            = "sanotte",
                                     plural3            = "sanovat",
                                     plural1_negative   = "sano",
                                     plural2_negative   = "sano",
                                     plural3_negative   = "sano",
                                     passive            = "sanotaan",
                                     passive_negative   = "sanota",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["sanoin"],
            singular2s         = ["sanoit"],
            singular3s         = ["sanoi"],
            singular1_negative = "sanonut",
            singular2_negative = "sanonut",
            singular3_negative = "sanonut",
            plural1s           = ["sanoimme"],
            plural2s           = ["sanoitte"],
            plural3s           = ["sanoivat"],
            plural1_negative   = "sanoneet",
            plural2_negative   = "sanoneet",
            plural3_negative   = "sanoneet",
            passive            = "sanottiin",
            passive_negative   = "sanottu",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "sanonut",
                                     singular2          = "sanonut",
                                     singular3          = "sanonut",
                                     singular1_negative = "sanonut",
                                     singular2_negative = "sanonut",
                                     singular3_negative = "sanonut",
                                     plural1            = "sanoneet",
                                     plural2            = "sanoneet",
                                     plural3            = "sanoneet",
                                     plural1_negative   = "sanoneet",
                                     plural2_negative   = "sanoneet",
                                     plural3_negative   = "sanoneet",
                                     passive            = "sanottu",
                                     passive_negative   = "sanottu",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "sanoisin",
                                     singular2          = "sanoisit",
                                     singular3          = "sanoisi",
                                     singular1_negative = "sanoisi",
                                     singular2_negative = "sanoisi",
                                     singular3_negative = "sanoisi",
                                     plural1            = "sanoisimme",
                                     plural2            = "sanoisitte",
                                     plural3            = "sanoisivat",
                                     plural1_negative   = "sanoisi",
                                     plural2_negative   = "sanoisi",
                                     plural3_negative   = "sanoisi",
                                     passive            = "sanottaisiin",
                                     passive_negative   = "sanottaisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "sanonen",
                                     singular2          = "sanonet",
                                     singular3          = "sanonee",
                                     singular1_negative = "sanone",
                                     singular2_negative = "sanone",
                                     singular3_negative = "sanone",
                                     plural1            = "sanonemme",
                                     plural2            = "sanonette",
                                     plural3            = "sanonevat",
                                     plural1_negative   = "sanone",
                                     plural2_negative   = "sanone",
                                     plural3_negative   = "sanone",
                                     passive            = "sanottaneen",
                                     passive_negative   = "sanottane",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "sano",
            singular3          = "sanokoon",
            singular2_negative = "sano",
            singular3_negative = "sanoko",
            plural1            = "sanokaamme",
            plural2            = "sanokaa",
            plural3            = "sanokoot",
            plural1_negative   = "sanoko",
            plural2_negative   = "sanoko",
            plural3_negative   = "sanoko",
            passive            = "sanottakoon",
            passive_negative   = "sanottako",)

        ensure_inflections_equal(expected, conjugations)


class TestGradationAndUmlauts(unittest.TestCase):
    moduses = KotusVerb52Sanoa("eheytyä",
                               gradate_kotus_f_satu_sadun) \
                               .moduses()

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'eheytynyt',
                                     singular1_negative = 'eheytynyt',
                                     singular2          = 'eheytynyt',
                                     singular2_negative = 'eheytynyt',
                                     singular3          = 'eheytynyt',
                                     singular3_negative = 'eheytynyt',
                                     plural1            = 'eheytyneet',
                                     plural1_negative   = 'eheytyneet',
                                     plural2            = 'eheytyneet',
                                     plural2_negative   = 'eheytyneet',
                                     plural3            = 'eheytyneet',
                                     plural3_negative   = 'eheytyneet',
                                     passive            = 'eheydytty',
                                     passive_negative   = 'eheydytty')

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):

    participles = KotusVerb52Sanoa("eheytyä",
                                   gradate_kotus_f_satu_sadun) \
                                   .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()

        expected = InflectionInfo(nominative='eheytyvä',
                                  nominative_plural='eheytyvät',
                                  genitive='eheytyvän',
                                  genitives_plural=['eheytyvien',
                                                    'eheytyväin'],
                                  partitives=['eheytyvää'],
                                  partitives_plural=['eheytyviä'],
                                  accusatives=['eheytyvä',
                                               'eheytyvän'],
                                  accusative_plural='eheytyvät',
                                  inessive='eheytyvässä',
                                  inessives_plural=['eheytyvissä'],
                                  elative='eheytyvästä',
                                  elatives_plural=['eheytyvistä'],
                                  illatives=['eheytyvään'],
                                  illatives_plural=['eheytyviin'],
                                  adessive='eheytyvällä',
                                  adessives_plural=['eheytyvillä'],
                                  ablative='eheytyvältä',
                                  ablatives_plural=['eheytyviltä'],
                                  allative='eheytyvälle',
                                  allatives_plural=['eheytyville'],
                                  essives=['eheytyvänä'],
                                  essives_plural=['eheytyvinä'],
                                  translative='eheytyväksi',
                                  translatives_plural=['eheytyviksi'],
                                  abessive='eheytyvättä',
                                  abessives_plural=['eheytyvittä'],
                                  instructives_plural=['eheytyvin'],
                                  comitatives_plural=['eheytyvine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()

        expected = InflectionInfo(nominative='eheytynyt',
                                  nominative_plural='eheytyneet',
                                  genitive='eheytyneen',
                                  genitives_plural=['eheytyneiden',
                                                    'eheytyneitten'],
                                  partitives=['eheytynyttä'],
                                  partitives_plural=['eheytyneitä'],
                                  accusatives=['eheytynyt',
                                               'eheytyneen'],
                                  accusative_plural='eheytyneet',
                                  inessive='eheytyneessä',
                                  inessives_plural=['eheytyneissä'],
                                  elative='eheytyneestä',
                                  elatives_plural=['eheytyneistä'],
                                  illatives=['eheytyneeseen'],
                                  illatives_plural=['eheytyneisiin',
                                                    'eheytyneihin'],
                                  adessive='eheytyneellä',
                                  adessives_plural=['eheytyneillä'],
                                  ablative='eheytyneeltä',
                                  ablatives_plural=['eheytyneiltä'],
                                  allative='eheytyneelle',
                                  allatives_plural=['eheytyneille'],
                                  essives=['eheytyneenä'],
                                  essives_plural=['eheytyneinä'],
                                  translative='eheytyneeksi',
                                  translatives_plural=['eheytyneiksi'],
                                  abessive='eheytyneettä',
                                  abessives_plural=['eheytyneittä'],
                                  instructives_plural=['eheytynein'],
                                  comitatives_plural=['eheytyneine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()

        expected = InflectionInfo(nominative='eheytymä',
                                  nominative_plural='eheytymät',
                                  genitive='eheytymän',
                                  genitives_plural=['eheytymien',
                                                    'eheytymäin'],
                                  partitives=['eheytymää'],
                                  partitives_plural=['eheytymiä'],
                                  accusatives=['eheytymä',
                                               'eheytymän'],
                                  accusative_plural='eheytymät',
                                  inessive='eheytymässä',
                                  inessives_plural=['eheytymissä'],
                                  elative='eheytymästä',
                                  elatives_plural=['eheytymistä'],
                                  illatives=['eheytymään'],
                                  illatives_plural=['eheytymiin'],
                                  adessive='eheytymällä',
                                  adessives_plural=['eheytymillä'],
                                  ablative='eheytymältä',
                                  ablatives_plural=['eheytymiltä'],
                                  allative='eheytymälle',
                                  allatives_plural=['eheytymille'],
                                  essives=['eheytymänä'],
                                  essives_plural=['eheytyminä'],
                                  translative='eheytymäksi',
                                  translatives_plural=['eheytymiksi'],
                                  abessive='eheytymättä',
                                  abessives_plural=['eheytymittä'],
                                  instructives_plural=['eheytymin'],
                                  comitatives_plural=['eheytymine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()

        expected = InflectionInfo(nominative='eheydyttävä',
                                  nominative_plural='eheydyttävät',
                                  genitive='eheydyttävän',
                                  genitives_plural=['eheydyttävien',
                                                    'eheydyttäväin'],
                                  partitives=['eheydyttävää'],
                                  partitives_plural=['eheydyttäviä'],
                                  accusatives=['eheydyttävä',
                                               'eheydyttävän'],
                                  accusative_plural='eheydyttävät',
                                  inessive='eheydyttävässä',
                                  inessives_plural=['eheydyttävissä'],
                                  elative='eheydyttävästä',
                                  elatives_plural=['eheydyttävistä'],
                                  illatives=['eheydyttävään'],
                                  illatives_plural=['eheydyttäviin'],
                                  adessive='eheydyttävällä',
                                  adessives_plural=['eheydyttävillä'],
                                  ablative='eheydyttävältä',
                                  ablatives_plural=['eheydyttäviltä'],
                                  allative='eheydyttävälle',
                                  allatives_plural=['eheydyttäville'],
                                  essives=['eheydyttävänä'],
                                  essives_plural=['eheydyttävinä'],
                                  translative='eheydyttäväksi',
                                  translatives_plural=['eheydyttäviksi'],
                                  abessive='eheydyttävättä',
                                  abessives_plural=['eheydyttävittä'],
                                  instructives_plural=['eheydyttävin'],
                                  comitatives_plural=['eheydyttävine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()

        expected = InflectionInfo(nominative='eheydytty',
                                  nominative_plural='eheydytyt',
                                  genitive='eheydytyn',
                                  genitives_plural=['eheydyttyjen'],
                                  partitives=['eheydyttyä'],
                                  partitives_plural=['eheydyttyjä'],
                                  accusatives=['eheydytty',
                                               'eheydytyn'],
                                  accusative_plural='eheydyttyjä',
                                  inessive='eheydytyssä',
                                  inessives_plural=['eheydytyissä'],
                                  elative='eheydytystä',
                                  elatives_plural=['eheydytyistä'],
                                  illatives=['eheydyttyyn'],
                                  illatives_plural=['eheydyttyihin'],
                                  adessive='eheydytyllä',
                                  adessives_plural=['eheydytyillä'],
                                  ablative='eheydytyltä',
                                  ablatives_plural=['eheydytyiltä'],
                                  allative='eheydytylle',
                                  allatives_plural=['eheydytyille'],
                                  essives=['eheydyttynä'],
                                  essives_plural=['eheydyttyinä'],
                                  translative='eheydytyksi',
                                  translatives_plural=['eheydytyiksi'],
                                  abessive='eheydytyttä',
                                  abessives_plural=['eheydytyittä'],
                                  instructives_plural=['eheydytyin'],
                                  comitatives_plural=['eheydyttyine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()

        expected = InflectionInfo(nominative='eheytymätön',
                                  nominative_plural='eheytymättömät',
                                  genitive='eheytymättömän',
                                  genitives_plural=['eheytymättömien',
                                                    'eheytymätönten'],
                                  partitives=['eheytymätöntä'],
                                  partitives_plural=['eheytymättömiä'],
                                  accusatives=['eheytymätön',
                                               'eheytymättömän'],
                                  accusative_plural='eheytymättömät',
                                  inessive='eheytymättömässä',
                                  inessives_plural=['eheytymättömissä'],
                                  elative='eheytymättömästä',
                                  elatives_plural=['eheytymättömistä'],
                                  illatives=['eheytymättömään'],
                                  illatives_plural=['eheytymättömiin'],
                                  adessive='eheytymättömällä',
                                  adessives_plural=['eheytymättömillä'],
                                  ablative='eheytymättömältä',
                                  ablatives_plural=['eheytymättömiltä'],
                                  allative='eheytymättömälle',
                                  allatives_plural=['eheytymättömille'],
                                  essives=['eheytymättömänä'],
                                  essives_plural=['eheytymättöminä'],
                                  translative='eheytymättömäksi',
                                  translatives_plural=['eheytymättömiksi'],
                                  abessive='eheytymättömättä',
                                  abessives_plural=['eheytymättömittä'],
                                  instructives_plural=['eheytymättömin'],
                                  comitatives_plural=['eheytymättömine'])

        ensure_inflections_equal(expected, data.positive)


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb52Sanoa("eheytyä",
                                   gradate_kotus_f_satu_sadun) \
                                   .infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='eheytyä',
            translative='eheytyäkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "eheytyessä",
            inessive_passive = "eheydyttäessä",
            instructive      = "eheytyen",
            elative          = "eheytyestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "eheydyttämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()

        expected = InflectionInfo(nominative='eheytyminen',
                                  nominative_plural='eheytymiset',
                                  genitive='eheytymisen',
                                  genitives_plural=['eheytymisten',
                                                    'eheytymisien'],
                                  partitives=['eheytymistä'],
                                  partitives_plural=['eheytymisiä'],
                                  accusatives=['eheytyminen',
                                               'eheytymisen'],
                                  accusative_plural='eheytymiset',
                                  inessive='eheytymisessä',
                                  inessives_plural=['eheytymisissä'],
                                  elative='eheytymisestä',
                                  elatives_plural=['eheytymisistä'],
                                  illatives=['eheytymiseen'],
                                  illatives_plural=['eheytymisiin'],
                                  adessive='eheytymisellä',
                                  adessives_plural=['eheytymisillä'],
                                  ablative='eheytymiseltä',
                                  ablatives_plural=['eheytymisiltä'],
                                  allative='eheytymiselle',
                                  allatives_plural=['eheytymisille'],
                                  essives=['eheytymisenä'],
                                  essives_plural=['eheytymisinä'],
                                  translative='eheytymiseksi',
                                  translatives_plural=['eheytymisiksi'],
                                  abessive='eheytymisettä',
                                  abessives_plural=['eheytymisittä'],
                                  instructives_plural=['eheytymisin'],
                                  comitatives_plural=['eheytymisine'])

        ensure_inflections_equal(expected, data)

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "eheytymäisillä")

        ensure_inflections_equal(expected, data)
