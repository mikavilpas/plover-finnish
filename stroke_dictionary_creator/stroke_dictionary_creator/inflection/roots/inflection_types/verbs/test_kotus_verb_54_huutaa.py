import unittest
from ensure import ensure
from .kotus_verb_54_huutaa import KotusVerb54Huutaa
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_f_satu_sadun, gradate_kotus_j_hento_hennon
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots

class TestBasic(unittest.TestCase):
    moduses = KotusVerb54Huutaa("vääntää",
                                gradate_kotus_j_hento_hennon)\
                                .moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "väännän",
                                     singular2          = "väännät",
                                     singular3          = "vääntää",
                                     singular1_negative = "väännä",
                                     singular2_negative = "väännä",
                                     singular3_negative = "väännä",
                                     plural1            = "väännämme",
                                     plural2            = "väännätte",
                                     plural3            = "vääntävät",
                                     plural1_negative   = "väännä",
                                     plural2_negative   = "väännä",
                                     plural3_negative   = "väännä",
                                     passive            = "väännetään",
                                     passive_negative   = "väännetä",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["väänsin"],
            singular2s         = ["väänsit"],
            singular3s         = ["väänsi"],
            singular1_negative = "vääntänyt",
            singular2_negative = "vääntänyt",
            singular3_negative = "vääntänyt",
            plural1s           = ["väänsimme"],
            plural2s           = ["väänsitte"],
            plural3s           = ["väänsivät"],
            plural1_negative   = "vääntäneet",
            plural2_negative   = "vääntäneet",
            plural3_negative   = "vääntäneet",
            passive            = "väännettiin",
            passive_negative   = "väännetty",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "vääntänyt",
                                     singular2          = "vääntänyt",
                                     singular3          = "vääntänyt",
                                     singular1_negative = "vääntänyt",
                                     singular2_negative = "vääntänyt",
                                     singular3_negative = "vääntänyt",
                                     plural1            = "vääntäneet",
                                     plural2            = "vääntäneet",
                                     plural3            = "vääntäneet",
                                     plural1_negative   = "vääntäneet",
                                     plural2_negative   = "vääntäneet",
                                     plural3_negative   = "vääntäneet",
                                     passive            = "väännetty",
                                     passive_negative   = "väännetty",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "vääntäisin",
                                     singular2          = "vääntäisit",
                                     singular3          = "vääntäisi",
                                     singular1_negative = "vääntäisi",
                                     singular2_negative = "vääntäisi",
                                     singular3_negative = "vääntäisi",
                                     plural1            = "vääntäisimme",
                                     plural2            = "vääntäisitte",
                                     plural3            = "vääntäisivät",
                                     plural1_negative   = "vääntäisi",
                                     plural2_negative   = "vääntäisi",
                                     plural3_negative   = "vääntäisi",
                                     passive            = "väännettäisiin",
                                     passive_negative   = "väännettäisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "vääntänen",
                                     singular2          = "vääntänet",
                                     singular3          = "vääntänee",
                                     singular1_negative = "vääntäne",
                                     singular2_negative = "vääntäne",
                                     singular3_negative = "vääntäne",
                                     plural1            = "vääntänemme",
                                     plural2            = "vääntänette",
                                     plural3            = "vääntänevät",
                                     plural1_negative   = "vääntäne",
                                     plural2_negative   = "vääntäne",
                                     plural3_negative   = "vääntäne",
                                     passive            = "väännettäneen",
                                     passive_negative   = "väännettäne",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "väännä",
            singular3          = "vääntäköön",
            singular2_negative = "väännä",
            singular3_negative = "vääntäkö",
            plural1            = "vääntäkäämme",
            plural2            = "vääntäkää",
            plural3            = "vääntäkööt",
            plural1_negative   = "vääntäkö",
            plural2_negative   = "vääntäkö",
            plural3_negative   = "vääntäkö",
            passive            = "väännettäköön",
            passive_negative   = "väännettäkö",)

        ensure_inflections_equal(expected, conjugations)


class TestNoGradation(unittest.TestCase):
    moduses = KotusVerb54Huutaa("huutaa",
                                gradate_kotus_f_satu_sadun)\
                                .moduses()

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'huutanut',
                                     singular1_negative = 'huutanut',
                                     singular2          = 'huutanut',
                                     singular2_negative = 'huutanut',
                                     singular3          = 'huutanut',
                                     singular3_negative = 'huutanut',
                                     plural1            = 'huutaneet',
                                     plural1_negative   = 'huutaneet',
                                     plural2            = 'huutaneet',
                                     plural2_negative   = 'huutaneet',
                                     plural3            = 'huutaneet',
                                     plural3_negative   = 'huutaneet',
                                     passive            = 'huudettu',
                                     passive_negative   = 'huudettu')

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):

    participles = KotusVerb54Huutaa("vääntää",
                                    gradate_kotus_j_hento_hennon) \
                                    .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()

        expected = InflectionInfo(nominative='vääntävä',
                                  nominative_plural='vääntävät',
                                  genitive='vääntävän',
                                  genitives_plural=['vääntävien',
                                                    'vääntäväin'],
                                  partitives=['vääntävää'],
                                  partitives_plural=['vääntäviä'],
                                  accusatives=['vääntävä',
                                               'vääntävän'],
                                  accusative_plural='vääntävät',
                                  inessive='vääntävässä',
                                  inessives_plural=['vääntävissä'],
                                  elative='vääntävästä',
                                  elatives_plural=['vääntävistä'],
                                  illatives=['vääntävään'],
                                  illatives_plural=['vääntäviin'],
                                  adessive='vääntävällä',
                                  adessives_plural=['vääntävillä'],
                                  ablative='vääntävältä',
                                  ablatives_plural=['vääntäviltä'],
                                  allative='vääntävälle',
                                  allatives_plural=['vääntäville'],
                                  essives=['vääntävänä'],
                                  essives_plural=['vääntävinä'],
                                  translative='vääntäväksi',
                                  translatives_plural=['vääntäviksi'],
                                  abessive='vääntävättä',
                                  abessives_plural=['vääntävittä'],
                                  instructives_plural=['vääntävin'],
                                  comitatives_plural=['vääntävine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()

        expected = InflectionInfo(nominative='vääntänyt',
                                  nominative_plural='vääntäneet',
                                  genitive='vääntäneen',
                                  genitives_plural=['vääntäneiden',
                                                    'vääntäneitten'],
                                  partitives=['vääntänyttä'],
                                  partitives_plural=['vääntäneitä'],
                                  accusatives=['vääntänyt',
                                               'vääntäneen'],
                                  accusative_plural='vääntäneet',
                                  inessive='vääntäneessä',
                                  inessives_plural=['vääntäneissä'],
                                  elative='vääntäneestä',
                                  elatives_plural=['vääntäneistä'],
                                  illatives=['vääntäneeseen'],
                                  illatives_plural=['vääntäneisiin',
                                                    'vääntäneihin'],
                                  adessive='vääntäneellä',
                                  adessives_plural=['vääntäneillä'],
                                  ablative='vääntäneeltä',
                                  ablatives_plural=['vääntäneiltä'],
                                  allative='vääntäneelle',
                                  allatives_plural=['vääntäneille'],
                                  essives=['vääntäneenä'],
                                  essives_plural=['vääntäneinä'],
                                  translative='vääntäneeksi',
                                  translatives_plural=['vääntäneiksi'],
                                  abessive='vääntäneettä',
                                  abessives_plural=['vääntäneittä'],
                                  instructives_plural=['vääntänein'],
                                  comitatives_plural=['vääntäneine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()

        expected = InflectionInfo(nominative='vääntämä',
                                  nominative_plural='vääntämät',
                                  genitive='vääntämän',
                                  genitives_plural=['vääntämien',
                                                    'vääntämäin'],
                                  partitives=['vääntämää'],
                                  partitives_plural=['vääntämiä'],
                                  accusatives=['vääntämä',
                                               'vääntämän'],
                                  accusative_plural='vääntämät',
                                  inessive='vääntämässä',
                                  inessives_plural=['vääntämissä'],
                                  elative='vääntämästä',
                                  elatives_plural=['vääntämistä'],
                                  illatives=['vääntämään'],
                                  illatives_plural=['vääntämiin'],
                                  adessive='vääntämällä',
                                  adessives_plural=['vääntämillä'],
                                  ablative='vääntämältä',
                                  ablatives_plural=['vääntämiltä'],
                                  allative='vääntämälle',
                                  allatives_plural=['vääntämille'],
                                  essives=['vääntämänä'],
                                  essives_plural=['vääntäminä'],
                                  translative='vääntämäksi',
                                  translatives_plural=['vääntämiksi'],
                                  abessive='vääntämättä',
                                  abessives_plural=['vääntämittä'],
                                  instructives_plural=['vääntämin'],
                                  comitatives_plural=['vääntämine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()

        expected = InflectionInfo(nominative='väännettävä',
                                  nominative_plural='väännettävät',
                                  genitive='väännettävän',
                                  genitives_plural=['väännettävien',
                                                    'väännettäväin'],
                                  partitives=['väännettävää'],
                                  partitives_plural=['väännettäviä'],
                                  accusatives=['väännettävä',
                                               'väännettävän'],
                                  accusative_plural='väännettävät',
                                  inessive='väännettävässä',
                                  inessives_plural=['väännettävissä'],
                                  elative='väännettävästä',
                                  elatives_plural=['väännettävistä'],
                                  illatives=['väännettävään'],
                                  illatives_plural=['väännettäviin'],
                                  adessive='väännettävällä',
                                  adessives_plural=['väännettävillä'],
                                  ablative='väännettävältä',
                                  ablatives_plural=['väännettäviltä'],
                                  allative='väännettävälle',
                                  allatives_plural=['väännettäville'],
                                  essives=['väännettävänä'],
                                  essives_plural=['väännettävinä'],
                                  translative='väännettäväksi',
                                  translatives_plural=['väännettäviksi'],
                                  abessive='väännettävättä',
                                  abessives_plural=['väännettävittä'],
                                  instructives_plural=['väännettävin'],
                                  comitatives_plural=['väännettävine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()

        expected = InflectionInfo(nominative='väännetty',
                                  nominative_plural='väännetyt',
                                  genitive='väännetyn',
                                  genitives_plural=['väännettyjen'],
                                  partitives=['väännettyä'],
                                  partitives_plural=['väännettyjä'],
                                  accusatives=['väännetty',
                                               'väännetyn'],
                                  accusative_plural='väännettyjä',
                                  inessive='väännetyssä',
                                  inessives_plural=['väännetyissä'],
                                  elative='väännetystä',
                                  elatives_plural=['väännetyistä'],
                                  illatives=['väännettyyn'],
                                  illatives_plural=['väännettyihin'],
                                  adessive='väännetyllä',
                                  adessives_plural=['väännetyillä'],
                                  ablative='väännetyltä',
                                  ablatives_plural=['väännetyiltä'],
                                  allative='väännetylle',
                                  allatives_plural=['väännetyille'],
                                  essives=['väännettynä'],
                                  essives_plural=['väännettyinä'],
                                  translative='väännetyksi',
                                  translatives_plural=['väännetyiksi'],
                                  abessive='väännetyttä',
                                  abessives_plural=['väännetyittä'],
                                  instructives_plural=['väännetyin'],
                                  comitatives_plural=['väännettyine'])

        ensure_inflections_equal(expected, data.positive)

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()

        expected = InflectionInfo(nominative='vääntämätön',
                                  nominative_plural='vääntämättömät',
                                  genitive='vääntämättömän',
                                  genitives_plural=['vääntämättömien',
                                                    'vääntämätönten'],
                                  partitives=['vääntämätöntä'],
                                  partitives_plural=['vääntämättömiä'],
                                  accusatives=['vääntämätön',
                                               'vääntämättömän'],
                                  accusative_plural='vääntämättömät',
                                  inessive='vääntämättömässä',
                                  inessives_plural=['vääntämättömissä'],
                                  elative='vääntämättömästä',
                                  elatives_plural=['vääntämättömistä'],
                                  illatives=['vääntämättömään'],
                                  illatives_plural=['vääntämättömiin'],
                                  adessive='vääntämättömällä',
                                  adessives_plural=['vääntämättömillä'],
                                  ablative='vääntämättömältä',
                                  ablatives_plural=['vääntämättömiltä'],
                                  allative='vääntämättömälle',
                                  allatives_plural=['vääntämättömille'],
                                  essives=['vääntämättömänä'],
                                  essives_plural=['vääntämättöminä'],
                                  translative='vääntämättömäksi',
                                  translatives_plural=['vääntämättömiksi'],
                                  abessive='vääntämättömättä',
                                  abessives_plural=['vääntämättömittä'],
                                  instructives_plural=['vääntämättömin'],
                                  comitatives_plural=['vääntämättömine'])

        ensure_inflections_equal(expected, data.positive)


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb54Huutaa("vääntää",
                                     gradate_kotus_j_hento_hennon) \
                                         .infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='vääntää',
            translative='vääntääkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "vääntäessä",
            inessive_passive = "väännettäessä",
            instructive      = "vääntäen",
            elative          = "vääntäestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "väännettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()

        expected = InflectionInfo(nominative='vääntäminen',
                                  nominative_plural='vääntämiset',
                                  genitive='vääntämisen',
                                  genitives_plural=['vääntämisten',
                                                    'vääntämisien'],
                                  partitives=['vääntämistä'],
                                  partitives_plural=['vääntämisiä'],
                                  accusatives=['vääntäminen',
                                               'vääntämisen'],
                                  accusative_plural='vääntämiset',
                                  inessive='vääntämisessä',
                                  inessives_plural=['vääntämisissä'],
                                  elative='vääntämisestä',
                                  elatives_plural=['vääntämisistä'],
                                  illatives=['vääntämiseen'],
                                  illatives_plural=['vääntämisiin'],
                                  adessive='vääntämisellä',
                                  adessives_plural=['vääntämisillä'],
                                  ablative='vääntämiseltä',
                                  ablatives_plural=['vääntämisiltä'],
                                  allative='vääntämiselle',
                                  allatives_plural=['vääntämisille'],
                                  essives=['vääntämisenä'],
                                  essives_plural=['vääntämisinä'],
                                  translative='vääntämiseksi',
                                  translatives_plural=['vääntämisiksi'],
                                  abessive='vääntämisettä',
                                  abessives_plural=['vääntämisittä'],
                                  instructives_plural=['vääntämisin'],
                                  comitatives_plural=['vääntämisine'])

        ensure_inflections_equal(expected, data)

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "vääntämäisillä")

        ensure_inflections_equal(expected, data)
