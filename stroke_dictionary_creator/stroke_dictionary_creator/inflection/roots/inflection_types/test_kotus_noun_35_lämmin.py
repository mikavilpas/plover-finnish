import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_lumme_lumpeen
from .kotus_noun_35_lämmin import kotus_noun_35_lämmin

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_35_lämmin("lämmin",
                                    gradate_kotus_h_lumme_lumpeen)

        expected = InflectionInfo(nominative='lämmin',
                                  nominative_plural='lämpimät',
                                  genitive='lämpimän',
                                  genitives_plural=['lämpimien',
                                                    'lämpimäin'],
                                  partitives=['lämmintä'],
                                  partitives_plural=['lämpimiä'],
                                  accusatives=['lämmin',
                                               'lämpimän'],
                                  accusative_plural='lämpimät',
                                  inessive='lämpimässä',
                                  inessives_plural=['lämpimissä'],
                                  elative='lämpimästä',
                                  elatives_plural=['lämpimistä'],
                                  illatives=['lämpimään'],
                                  illatives_plural=['lämpimiin'],
                                  adessive='lämpimällä',
                                  adessives_plural=['lämpimillä'],
                                  ablative='lämpimältä',
                                  ablatives_plural=['lämpimiltä'],
                                  allative='lämpimälle',
                                  allatives_plural=['lämpimille'],
                                  essives=['lämpimänä'],
                                  essives_plural=['lämpiminä'],
                                  translative='lämpimäksi',
                                  translatives_plural=['lämpimiksi'],
                                  abessive='lämpimättä',
                                  abessives_plural=['lämpimittä'],
                                  instructives_plural=['lämpimin'],
                                  comitatives_plural=['lämpimine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_35_lämmin("seitsen")

        expected = InflectionInfo(nominative='seitsen',
                                  nominative_plural='seitsemät',
                                  genitive='seitsemän',
                                  genitives_plural=['seitsemien',
                                                    'seitsemäin'],
                                  partitives=['seitsentä'],
                                  partitives_plural=['seitsemiä'],
                                  accusatives=['seitsen',
                                               'seitsemän'],
                                  accusative_plural='seitsemät',
                                  inessive='seitsemässä',
                                  inessives_plural=['seitsemissä'],
                                  elative='seitsemästä',
                                  elatives_plural=['seitsemistä'],
                                  illatives=['seitsemään'],
                                  illatives_plural=['seitsemiin'],
                                  adessive='seitsemällä',
                                  adessives_plural=['seitsemillä'],
                                  ablative='seitsemältä',
                                  ablatives_plural=['seitsemiltä'],
                                  allative='seitsemälle',
                                  allatives_plural=['seitsemille'],
                                  essives=['seitsemänä'],
                                  essives_plural=['seitseminä'],
                                  translative='seitsemäksi',
                                  translatives_plural=['seitsemiksi'],
                                  abessive='seitsemättä',
                                  abessives_plural=['seitsemittä'],
                                  instructives_plural=['seitsemin'],
                                  comitatives_plural=['seitsemine'])

        ensure_inflections_equal(expected, data)

    # all words use gradation C
