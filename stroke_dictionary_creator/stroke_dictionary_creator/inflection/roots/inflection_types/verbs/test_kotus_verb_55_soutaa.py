import unittest
from ensure import ensure
from .kotus_verb_55_soutaa import KotusVerb55Soutaa
from ..test_utils import ensure_inflections_equal
from ...gradation import gradate_kotus_i_ilta_illan, gradate_kotus_f_satu_sadun
from ...noun_inflection_info import InflectionInfo
from .infinitives import VerbInfinitive_1_A, VerbInfinitive_2_E, VerbInfinitiveAPersonalForms, VerbInfinitive_5_MAINEN, VerbInfinitive_3_MA
from .moduses import VerbPersonalForms, VerbRoots, VerbModuses, VerbPersonalFormsImperativePresent, VerbPersonalFormsMultipleRoots

class TestBasic(unittest.TestCase):
    moduses = KotusVerb55Soutaa("yltää",
                                gradate_kotus_i_ilta_illan)\
                                .moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "yllän",
                                     singular2          = "yllät",
                                     singular3          = "yltää",
                                     singular1_negative = "yllä",
                                     singular2_negative = "yllä",
                                     singular3_negative = "yllä",
                                     plural1            = "yllämme",
                                     plural2            = "yllätte",
                                     plural3            = "yltävät",
                                     plural1_negative   = "yllä",
                                     plural2_negative   = "yllä",
                                     plural3_negative   = "yllä",
                                     passive            = "ylletään",
                                     passive_negative   = "ylletä",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalFormsMultipleRoots(
            singular1s         = ["yllin", "ylsin"],
            singular2s         = ["yllit", "ylsit"],
            singular3s         = ["ylti", "ylsi"],
            singular1_negative = "yltänyt",
            singular2_negative = "yltänyt",
            singular3_negative = "yltänyt",
            plural1s           = ["yllimme", "ylsimme"],
            plural2s           = ["yllitte", "ylsitte"],
            plural3s           = ["yltivät", "ylsivät"],
            plural1_negative   = "yltäneet",
            plural2_negative   = "yltäneet",
            plural3_negative   = "yltäneet",
            passive            = "yllettiin",
            passive_negative   = "ylletty",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "yltänyt",
                                     singular2          = "yltänyt",
                                     singular3          = "yltänyt",
                                     singular1_negative = "yltänyt",
                                     singular2_negative = "yltänyt",
                                     singular3_negative = "yltänyt",
                                     plural1            = "yltäneet",
                                     plural2            = "yltäneet",
                                     plural3            = "yltäneet",
                                     plural1_negative   = "yltäneet",
                                     plural2_negative   = "yltäneet",
                                     plural3_negative   = "yltäneet",
                                     passive            = "ylletty",
                                     passive_negative   = "ylletty",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "yltäisin",
                                     singular2          = "yltäisit",
                                     singular3          = "yltäisi",
                                     singular1_negative = "yltäisi",
                                     singular2_negative = "yltäisi",
                                     singular3_negative = "yltäisi",
                                     plural1            = "yltäisimme",
                                     plural2            = "yltäisitte",
                                     plural3            = "yltäisivät",
                                     plural1_negative   = "yltäisi",
                                     plural2_negative   = "yltäisi",
                                     plural3_negative   = "yltäisi",
                                     passive            = "yllettäisiin",
                                     passive_negative   = "yllettäisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "yltänen",
                                     singular2          = "yltänet",
                                     singular3          = "yltänee",
                                     singular1_negative = "yltäne",
                                     singular2_negative = "yltäne",
                                     singular3_negative = "yltäne",
                                     plural1            = "yltänemme",
                                     plural2            = "yltänette",
                                     plural3            = "yltänevät",
                                     plural1_negative   = "yltäne",
                                     plural2_negative   = "yltäne",
                                     plural3_negative   = "yltäne",
                                     passive            = "yllettäneen",
                                     passive_negative   = "yllettäne",)


        ensure_inflections_equal(expected, conjugations)

    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "yllä",
            singular3          = "yltäköön",
            singular2_negative = "yllä",
            singular3_negative = "yltäkö",
            plural1            = "yltäkäämme",
            plural2            = "yltäkää",
            plural3            = "yltäkööt",
            plural1_negative   = "yltäkö",
            plural2_negative   = "yltäkö",
            plural3_negative   = "yltäkö",
            passive            = "yllettäköön",
            passive_negative   = "yllettäkö",)

        ensure_inflections_equal(expected, conjugations)


class TestNoGradation(unittest.TestCase):
    moduses = KotusVerb55Soutaa("soutaa",
                                gradate_kotus_f_satu_sadun)\
                                .moduses()

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = 'soutanut',
                                     singular1_negative = 'soutanut',
                                     singular2          = 'soutanut',
                                     singular2_negative = 'soutanut',
                                     singular3          = 'soutanut',
                                     singular3_negative = 'soutanut',
                                     plural1            = 'soutaneet',
                                     plural1_negative   = 'soutaneet',
                                     plural2            = 'soutaneet',
                                     plural2_negative   = 'soutaneet',
                                     plural3            = 'soutaneet',
                                     plural3_negative   = 'soutaneet',
                                     passive            = 'soudettu',
                                     passive_negative   = 'soudettu')

        ensure_inflections_equal(expected, conjugations)

class TestParticiples(unittest.TestCase):

    participles = KotusVerb55Soutaa("kiitää",
                                    gradate_kotus_f_satu_sadun) \
                                    .participles()

    def test_group_1_va(self):
        data = self.participles.group_1_VA()

        expected = InflectionInfo(nominative='kiitävä',
                                  nominative_plural='kiitävät',
                                  genitive='kiitävän',
                                  genitives_plural=['kiitävien',
                                                    'kiitäväin'],
                                  partitives=['kiitävää'],
                                  partitives_plural=['kiitäviä'],
                                  accusatives=['kiitävä',
                                               'kiitävän'],
                                  accusative_plural='kiitävät',
                                  inessive='kiitävässä',
                                  inessives_plural=['kiitävissä'],
                                  elative='kiitävästä',
                                  elatives_plural=['kiitävistä'],
                                  illatives=['kiitävään'],
                                  illatives_plural=['kiitäviin'],
                                  adessive='kiitävällä',
                                  adessives_plural=['kiitävillä'],
                                  ablative='kiitävältä',
                                  ablatives_plural=['kiitäviltä'],
                                  allative='kiitävälle',
                                  allatives_plural=['kiitäville'],
                                  essives=['kiitävänä'],
                                  essives_plural=['kiitävinä'],
                                  translative='kiitäväksi',
                                  translatives_plural=['kiitäviksi'],
                                  abessive='kiitävättä',
                                  abessives_plural=['kiitävittä'],
                                  instructives_plural=['kiitävin'],
                                  comitatives_plural=['kiitävine'])

        ensure_inflections_equal(expected, data)

    def test_group_2_nut(self):
        data = self.participles.group_2_NUT()

        expected = InflectionInfo(nominative='kiitänyt',
                                  nominative_plural='kiitäneet',
                                  genitive='kiitäneen',
                                  genitives_plural=['kiitäneiden',
                                                    'kiitäneitten'],
                                  partitives=['kiitänyttä'],
                                  partitives_plural=['kiitäneitä'],
                                  accusatives=['kiitänyt',
                                               'kiitäneen'],
                                  accusative_plural='kiitäneet',
                                  inessive='kiitäneessä',
                                  inessives_plural=['kiitäneissä'],
                                  elative='kiitäneestä',
                                  elatives_plural=['kiitäneistä'],
                                  illatives=['kiitäneeseen'],
                                  illatives_plural=['kiitäneisiin',
                                                    'kiitäneihin'],
                                  adessive='kiitäneellä',
                                  adessives_plural=['kiitäneillä'],
                                  ablative='kiitäneeltä',
                                  ablatives_plural=['kiitäneiltä'],
                                  allative='kiitäneelle',
                                  allatives_plural=['kiitäneille'],
                                  essives=['kiitäneenä'],
                                  essives_plural=['kiitäneinä'],
                                  translative='kiitäneeksi',
                                  translatives_plural=['kiitäneiksi'],
                                  abessive='kiitäneettä',
                                  abessives_plural=['kiitäneittä'],
                                  instructives_plural=['kiitänein'],
                                  comitatives_plural=['kiitäneine'])

        ensure_inflections_equal(expected, data)

    def test_group_3_ma(self):
        data = self.participles.group_3_MA_agent_participle()

        expected = InflectionInfo(nominative='kiitämä',
                                  nominative_plural='kiitämät',
                                  genitive='kiitämän',
                                  genitives_plural=['kiitämien',
                                                    'kiitämäin'],
                                  partitives=['kiitämää'],
                                  partitives_plural=['kiitämiä'],
                                  accusatives=['kiitämä',
                                               'kiitämän'],
                                  accusative_plural='kiitämät',
                                  inessive='kiitämässä',
                                  inessives_plural=['kiitämissä'],
                                  elative='kiitämästä',
                                  elatives_plural=['kiitämistä'],
                                  illatives=['kiitämään'],
                                  illatives_plural=['kiitämiin'],
                                  adessive='kiitämällä',
                                  adessives_plural=['kiitämillä'],
                                  ablative='kiitämältä',
                                  ablatives_plural=['kiitämiltä'],
                                  allative='kiitämälle',
                                  allatives_plural=['kiitämille'],
                                  essives=['kiitämänä'],
                                  essives_plural=['kiitäminä'],
                                  translative='kiitämäksi',
                                  translatives_plural=['kiitämiksi'],
                                  abessive='kiitämättä',
                                  abessives_plural=['kiitämittä'],
                                  instructives_plural=['kiitämin'],
                                  comitatives_plural=['kiitämine'])

        ensure_inflections_equal(expected, data)

    def test_group_4_va_passive(self):
        data = self.participles.group_4_VA_passive()

        expected = InflectionInfo(nominative='kiidettävä',
                                  nominative_plural='kiidettävät',
                                  genitive='kiidettävän',
                                  genitives_plural=['kiidettävien',
                                                    'kiidettäväin'],
                                  partitives=['kiidettävää'],
                                  partitives_plural=['kiidettäviä'],
                                  accusatives=['kiidettävä',
                                               'kiidettävän'],
                                  accusative_plural='kiidettävät',
                                  inessive='kiidettävässä',
                                  inessives_plural=['kiidettävissä'],
                                  elative='kiidettävästä',
                                  elatives_plural=['kiidettävistä'],
                                  illatives=['kiidettävään'],
                                  illatives_plural=['kiidettäviin'],
                                  adessive='kiidettävällä',
                                  adessives_plural=['kiidettävillä'],
                                  ablative='kiidettävältä',
                                  ablatives_plural=['kiidettäviltä'],
                                  allative='kiidettävälle',
                                  allatives_plural=['kiidettäville'],
                                  essives=['kiidettävänä'],
                                  essives_plural=['kiidettävinä'],
                                  translative='kiidettäväksi',
                                  translatives_plural=['kiidettäviksi'],
                                  abessive='kiidettävättä',
                                  abessives_plural=['kiidettävittä'],
                                  instructives_plural=['kiidettävin'],
                                  comitatives_plural=['kiidettävine'])

        ensure_inflections_equal(expected, data)

    def test_group_5_tu(self):
        data = self.participles.group_5_TU_passive()

        expected = InflectionInfo(nominative='kiidetty',
                                  nominative_plural='kiidetyt',
                                  genitive='kiidetyn',
                                  genitives_plural=['kiidettyjen'],
                                  partitives=['kiidettyä'],
                                  partitives_plural=['kiidettyjä'],
                                  accusatives=['kiidetty',
                                               'kiidetyn'],
                                  accusative_plural='kiidettyjä',
                                  inessive='kiidetyssä',
                                  inessives_plural=['kiidetyissä'],
                                  elative='kiidetystä',
                                  elatives_plural=['kiidetyistä'],
                                  illatives=['kiidettyyn'],
                                  illatives_plural=['kiidettyihin'],
                                  adessive='kiidetyllä',
                                  adessives_plural=['kiidetyillä'],
                                  ablative='kiidetyltä',
                                  ablatives_plural=['kiidetyiltä'],
                                  allative='kiidetylle',
                                  allatives_plural=['kiidetyille'],
                                  essives=['kiidettynä'],
                                  essives_plural=['kiidettyinä'],
                                  translative='kiidetyksi',
                                  translatives_plural=['kiidetyiksi'],
                                  abessive='kiidetyttä',
                                  abessives_plural=['kiidetyittä'],
                                  instructives_plural=['kiidetyin'],
                                  comitatives_plural=['kiidettyine'])

        ensure_inflections_equal(expected, data)

    def test_group_6_negation(self):
        data = self.participles.group_6_negation()

        expected = InflectionInfo(nominative='kiitämätön',
                                  nominative_plural='kiitämättömät',
                                  genitive='kiitämättömän',
                                  genitives_plural=['kiitämättömien',
                                                    'kiitämätönten'],
                                  partitives=['kiitämätöntä'],
                                  partitives_plural=['kiitämättömiä'],
                                  accusatives=['kiitämätön',
                                               'kiitämättömän'],
                                  accusative_plural='kiitämättömät',
                                  inessive='kiitämättömässä',
                                  inessives_plural=['kiitämättömissä'],
                                  elative='kiitämättömästä',
                                  elatives_plural=['kiitämättömistä'],
                                  illatives=['kiitämättömään'],
                                  illatives_plural=['kiitämättömiin'],
                                  adessive='kiitämättömällä',
                                  adessives_plural=['kiitämättömillä'],
                                  ablative='kiitämättömältä',
                                  ablatives_plural=['kiitämättömiltä'],
                                  allative='kiitämättömälle',
                                  allatives_plural=['kiitämättömille'],
                                  essives=['kiitämättömänä'],
                                  essives_plural=['kiitämättöminä'],
                                  translative='kiitämättömäksi',
                                  translatives_plural=['kiitämättömiksi'],
                                  abessive='kiitämättömättä',
                                  abessives_plural=['kiitämättömittä'],
                                  instructives_plural=['kiitämättömin'],
                                  comitatives_plural=['kiitämättömine'])

        ensure_inflections_equal(expected, data)


class TestInfinitives(unittest.TestCase):
    infinitives = KotusVerb55Soutaa("kiitää",
                                    gradate_kotus_f_satu_sadun) \
                                    .infinitives()

    def test_group_1(self):
        data = self.infinitives.group_1_A()

        expected = VerbInfinitive_1_A(
            basic_form='kiitää',
            translative='kiitääkse')

        ensure_inflections_equal(expected, data)

    def test_group_2(self):
        data = self.infinitives.group_2_E()

        expected = VerbInfinitive_2_E(
            inessive         = "kiitäessä",
            inessive_passive = "kiidettäessä",
            instructive      = "kiitäen",
            elative          = "kiitäestä")

        ensure_inflections_equal(expected, data)

    def test_group_3(self):
        data = self.infinitives.group_3_MA()

        expected = VerbInfinitive_3_MA(instructive_passive = "kiidettämän")

        ensure_inflections_equal(expected, data)

    def test_group_4(self):
        data = self.infinitives.group_4_MINEN()

        expected = InflectionInfo(nominative='kiitäminen',
                                  nominative_plural='kiitämiset',
                                  genitive='kiitämisen',
                                  genitives_plural=['kiitämisten',
                                                    'kiitämisien'],
                                  partitives=['kiitämistä'],
                                  partitives_plural=['kiitämisiä'],
                                  accusatives=['kiitäminen',
                                               'kiitämisen'],
                                  accusative_plural='kiitämiset',
                                  inessive='kiitämisessä',
                                  inessives_plural=['kiitämisissä'],
                                  elative='kiitämisestä',
                                  elatives_plural=['kiitämisistä'],
                                  illatives=['kiitämiseen'],
                                  illatives_plural=['kiitämisiin'],
                                  adessive='kiitämisellä',
                                  adessives_plural=['kiitämisillä'],
                                  ablative='kiitämiseltä',
                                  ablatives_plural=['kiitämisiltä'],
                                  allative='kiitämiselle',
                                  allatives_plural=['kiitämisille'],
                                  essives=['kiitämisenä'],
                                  essives_plural=['kiitämisinä'],
                                  translative='kiitämiseksi',
                                  translatives_plural=['kiitämisiksi'],
                                  abessive='kiitämisettä',
                                  abessives_plural=['kiitämisittä'],
                                  instructives_plural=['kiitämisin'],
                                  comitatives_plural=['kiitämisine'])

        ensure_inflections_equal(expected, data)

    def test_group_5(self):
        data = self.infinitives.group_5_MAINEN()

        expected = VerbInfinitive_5_MAINEN(
            adessive = "kiitämäisillä")

        ensure_inflections_equal(expected, data)
