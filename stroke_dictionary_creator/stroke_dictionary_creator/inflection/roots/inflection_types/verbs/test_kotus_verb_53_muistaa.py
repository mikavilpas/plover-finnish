import unittest
from ensure import ensure
from .kotus_verb_53_muistaa import KotusVerb53Muistaa
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_c_tyttö_tytön
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots

class TestBasic(unittest.TestCase):
    moduses = KotusVerb53Muistaa("esittää",
                                 gradate_kotus_c_tyttö_tytön)\
                                 .moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "esitän",
                                     singular2          = "esität",
                                     singular3          = "esittää",
                                     singular1_negative = "esitä",
                                     singular2_negative = "esitä",
                                     singular3_negative = "esitä",
                                     plural1            = "esitämme",
                                     plural2            = "esitätte",
                                     plural3            = "esittävät",
                                     plural1_negative   = "esitä",
                                     plural2_negative   = "esitä",
                                     plural3_negative   = "esitä",
                                     passive            = "esitetään",
                                     passive_negative   = "esitetä",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["esitin"],
            singular2s         = ["esitit"],
            singular3s         = ["esitti"],
            singular1_negative = "esittänyt",
            singular2_negative = "esittänyt",
            singular3_negative = "esittänyt",
            plural1s           = ["esitimme"],
            plural2s           = ["esititte"],
            plural3s           = ["esittivät"],
            plural1_negative   = "esittäneet",
            plural2_negative   = "esittäneet",
            plural3_negative   = "esittäneet",
            passive            = "esitettiin",
            passive_negative   = "esitetty",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "esittänyt",
                                     singular2          = "esittänyt",
                                     singular3          = "esittänyt",
                                     singular1_negative = "esittänyt",
                                     singular2_negative = "esittänyt",
                                     singular3_negative = "esittänyt",
                                     plural1            = "esittäneet",
                                     plural2            = "esittäneet",
                                     plural3            = "esittäneet",
                                     plural1_negative   = "esittäneet",
                                     plural2_negative   = "esittäneet",
                                     plural3_negative   = "esittäneet",
                                     passive            = "esitetty",
                                     passive_negative   = "esitetty",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "esittäisin",
                                     singular2          = "esittäisit",
                                     singular3          = "esittäisi",
                                     singular1_negative = "esittäisi",
                                     singular2_negative = "esittäisi",
                                     singular3_negative = "esittäisi",
                                     plural1            = "esittäisimme",
                                     plural2            = "esittäisitte",
                                     plural3            = "esittäisivät",
                                     plural1_negative   = "esittäisi",
                                     plural2_negative   = "esittäisi",
                                     plural3_negative   = "esittäisi",
                                     passive            = "esitettäisiin",
                                     passive_negative   = "esitettäisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "esittänen",
                                     singular2          = "esittänet",
                                     singular3          = "esittänee",
                                     singular1_negative = "esittäne",
                                     singular2_negative = "esittäne",
                                     singular3_negative = "esittäne",
                                     plural1            = "esittänemme",
                                     plural2            = "esittänette",
                                     plural3            = "esittänevät",
                                     plural1_negative   = "esittäne",
                                     plural2_negative   = "esittäne",
                                     plural3_negative   = "esittäne",
                                     passive            = "esitettäneen",
                                     passive_negative   = "esitettäne",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "esitä",
            singular3          = "esittäköön",
            singular2_negative = "esitä",
            singular3_negative = "esittäkö",
            plural1            = "esittäkäämme",
            plural2            = "esittäkää",
            plural3            = "esittäkööt",
            plural1_negative   = "esittäkö",
            plural2_negative   = "esittäkö",
            plural3_negative   = "esittäkö",
            passive            = "esitettäköön",
            passive_negative   = "esitettäkö",)

        ensure_inflections_equal(expected, conjugations)


class TestNoGradation(unittest.TestCase):
    moduses = KotusVerb53Muistaa("ahdistaa").moduses()

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'ahdistanut',
                                     singular1_negative = 'ahdistanut',
                                     singular2          = 'ahdistanut',
                                     singular2_negative = 'ahdistanut',
                                     singular3          = 'ahdistanut',
                                     singular3_negative = 'ahdistanut',
                                     plural1            = 'ahdistaneet',
                                     plural1_negative   = 'ahdistaneet',
                                     plural2            = 'ahdistaneet',
                                     plural2_negative   = 'ahdistaneet',
                                     plural3            = 'ahdistaneet',
                                     plural3_negative   = 'ahdistaneet',
                                     passive            = 'ahdistettu',
                                     passive_negative   = 'ahdistettu')

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):

    participles = KotusVerb53Muistaa("esittää",
                                     gradate_kotus_c_tyttö_tytön) \
                                     .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()

        expected = InflectionInfo(nominative='esittävä',
                                  nominative_plural='esittävät',
                                  genitive='esittävän',
                                  genitives_plural=['esittävien',
                                                    'esittäväin'],
                                  partitives=['esittävää'],
                                  partitives_plural=['esittäviä'],
                                  accusatives=['esittävä',
                                               'esittävän'],
                                  accusative_plural='esittävät',
                                  inessive='esittävässä',
                                  inessives_plural=['esittävissä'],
                                  elative='esittävästä',
                                  elatives_plural=['esittävistä'],
                                  illatives=['esittävään'],
                                  illatives_plural=['esittäviin'],
                                  adessive='esittävällä',
                                  adessives_plural=['esittävillä'],
                                  ablative='esittävältä',
                                  ablatives_plural=['esittäviltä'],
                                  allative='esittävälle',
                                  allatives_plural=['esittäville'],
                                  essives=['esittävänä'],
                                  essives_plural=['esittävinä'],
                                  translative='esittäväksi',
                                  translatives_plural=['esittäviksi'],
                                  abessive='esittävättä',
                                  abessives_plural=['esittävittä'],
                                  instructives_plural=['esittävin'],
                                  comitatives_plural=['esittävine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()

        expected = InflectionInfo(nominative='esittänyt',
                                  nominative_plural='esittäneet',
                                  genitive='esittäneen',
                                  genitives_plural=['esittäneiden',
                                                    'esittäneitten'],
                                  partitives=['esittänyttä'],
                                  partitives_plural=['esittäneitä'],
                                  accusatives=['esittänyt',
                                               'esittäneen'],
                                  accusative_plural='esittäneet',
                                  inessive='esittäneessä',
                                  inessives_plural=['esittäneissä'],
                                  elative='esittäneestä',
                                  elatives_plural=['esittäneistä'],
                                  illatives=['esittäneeseen'],
                                  illatives_plural=['esittäneisiin',
                                                    'esittäneihin'],
                                  adessive='esittäneellä',
                                  adessives_plural=['esittäneillä'],
                                  ablative='esittäneeltä',
                                  ablatives_plural=['esittäneiltä'],
                                  allative='esittäneelle',
                                  allatives_plural=['esittäneille'],
                                  essives=['esittäneenä'],
                                  essives_plural=['esittäneinä'],
                                  translative='esittäneeksi',
                                  translatives_plural=['esittäneiksi'],
                                  abessive='esittäneettä',
                                  abessives_plural=['esittäneittä'],
                                  instructives_plural=['esittänein'],
                                  comitatives_plural=['esittäneine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()

        expected = InflectionInfo(nominative='esittämä',
                                  nominative_plural='esittämät',
                                  genitive='esittämän',
                                  genitives_plural=['esittämien',
                                                    'esittämäin'],
                                  partitives=['esittämää'],
                                  partitives_plural=['esittämiä'],
                                  accusatives=['esittämä',
                                               'esittämän'],
                                  accusative_plural='esittämät',
                                  inessive='esittämässä',
                                  inessives_plural=['esittämissä'],
                                  elative='esittämästä',
                                  elatives_plural=['esittämistä'],
                                  illatives=['esittämään'],
                                  illatives_plural=['esittämiin'],
                                  adessive='esittämällä',
                                  adessives_plural=['esittämillä'],
                                  ablative='esittämältä',
                                  ablatives_plural=['esittämiltä'],
                                  allative='esittämälle',
                                  allatives_plural=['esittämille'],
                                  essives=['esittämänä'],
                                  essives_plural=['esittäminä'],
                                  translative='esittämäksi',
                                  translatives_plural=['esittämiksi'],
                                  abessive='esittämättä',
                                  abessives_plural=['esittämittä'],
                                  instructives_plural=['esittämin'],
                                  comitatives_plural=['esittämine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()

        expected = InflectionInfo(nominative='esitettävä',
                                  nominative_plural='esitettävät',
                                  genitive='esitettävän',
                                  genitives_plural=['esitettävien',
                                                    'esitettäväin'],
                                  partitives=['esitettävää'],
                                  partitives_plural=['esitettäviä'],
                                  accusatives=['esitettävä',
                                               'esitettävän'],
                                  accusative_plural='esitettävät',
                                  inessive='esitettävässä',
                                  inessives_plural=['esitettävissä'],
                                  elative='esitettävästä',
                                  elatives_plural=['esitettävistä'],
                                  illatives=['esitettävään'],
                                  illatives_plural=['esitettäviin'],
                                  adessive='esitettävällä',
                                  adessives_plural=['esitettävillä'],
                                  ablative='esitettävältä',
                                  ablatives_plural=['esitettäviltä'],
                                  allative='esitettävälle',
                                  allatives_plural=['esitettäville'],
                                  essives=['esitettävänä'],
                                  essives_plural=['esitettävinä'],
                                  translative='esitettäväksi',
                                  translatives_plural=['esitettäviksi'],
                                  abessive='esitettävättä',
                                  abessives_plural=['esitettävittä'],
                                  instructives_plural=['esitettävin'],
                                  comitatives_plural=['esitettävine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()

        expected = InflectionInfo(nominative='esitetty',
                                  nominative_plural='esitetyt',
                                  genitive='esitetyn',
                                  genitives_plural=['esitettyjen'],
                                  partitives=['esitettyä'],
                                  partitives_plural=['esitettyjä'],
                                  accusatives=['esitetty',
                                               'esitetyn'],
                                  accusative_plural='esitettyjä',
                                  inessive='esitetyssä',
                                  inessives_plural=['esitetyissä'],
                                  elative='esitetystä',
                                  elatives_plural=['esitetyistä'],
                                  illatives=['esitettyyn'],
                                  illatives_plural=['esitettyihin'],
                                  adessive='esitetyllä',
                                  adessives_plural=['esitetyillä'],
                                  ablative='esitetyltä',
                                  ablatives_plural=['esitetyiltä'],
                                  allative='esitetylle',
                                  allatives_plural=['esitetyille'],
                                  essives=['esitettynä'],
                                  essives_plural=['esitettyinä'],
                                  translative='esitetyksi',
                                  translatives_plural=['esitetyiksi'],
                                  abessive='esitetyttä',
                                  abessives_plural=['esitetyittä'],
                                  instructives_plural=['esitetyin'],
                                  comitatives_plural=['esitettyine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()

        expected = InflectionInfo(nominative='esittämätön',
                                  nominative_plural='esittämättömät',
                                  genitive='esittämättömän',
                                  genitives_plural=['esittämättömien',
                                                    'esittämätönten'],
                                  partitives=['esittämätöntä'],
                                  partitives_plural=['esittämättömiä'],
                                  accusatives=['esittämätön',
                                               'esittämättömän'],
                                  accusative_plural='esittämättömät',
                                  inessive='esittämättömässä',
                                  inessives_plural=['esittämättömissä'],
                                  elative='esittämättömästä',
                                  elatives_plural=['esittämättömistä'],
                                  illatives=['esittämättömään'],
                                  illatives_plural=['esittämättömiin'],
                                  adessive='esittämättömällä',
                                  adessives_plural=['esittämättömillä'],
                                  ablative='esittämättömältä',
                                  ablatives_plural=['esittämättömiltä'],
                                  allative='esittämättömälle',
                                  allatives_plural=['esittämättömille'],
                                  essives=['esittämättömänä'],
                                  essives_plural=['esittämättöminä'],
                                  translative='esittämättömäksi',
                                  translatives_plural=['esittämättömiksi'],
                                  abessive='esittämättömättä',
                                  abessives_plural=['esittämättömittä'],
                                  instructives_plural=['esittämättömin'],
                                  comitatives_plural=['esittämättömine'])

        ensure_inflections_equal(expected, data.positive)


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb53Muistaa("esittää",
                                     gradate_kotus_c_tyttö_tytön) \
                                     .infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='esittää',
            translative='esittääkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "esittäessä",
            inessive_passive = "esitettäessä",
            instructive      = "esittäen",
            elative          = "esittäestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "esitettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()

        expected = InflectionInfo(nominative='esittäminen',
                                  nominative_plural='esittämiset',
                                  genitive='esittämisen',
                                  genitives_plural=['esittämisten',
                                                    'esittämisien'],
                                  partitives=['esittämistä'],
                                  partitives_plural=['esittämisiä'],
                                  accusatives=['esittäminen',
                                               'esittämisen'],
                                  accusative_plural='esittämiset',
                                  inessive='esittämisessä',
                                  inessives_plural=['esittämisissä'],
                                  elative='esittämisestä',
                                  elatives_plural=['esittämisistä'],
                                  illatives=['esittämiseen'],
                                  illatives_plural=['esittämisiin'],
                                  adessive='esittämisellä',
                                  adessives_plural=['esittämisillä'],
                                  ablative='esittämiseltä',
                                  ablatives_plural=['esittämisiltä'],
                                  allative='esittämiselle',
                                  allatives_plural=['esittämisille'],
                                  essives=['esittämisenä'],
                                  essives_plural=['esittämisinä'],
                                  translative='esittämiseksi',
                                  translatives_plural=['esittämisiksi'],
                                  abessive='esittämisettä',
                                  abessives_plural=['esittämisittä'],
                                  instructives_plural=['esittämisin'],
                                  comitatives_plural=['esittämisine'])

        ensure_inflections_equal(expected, data)

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "esittämäisillä")

        ensure_inflections_equal(expected, data)
