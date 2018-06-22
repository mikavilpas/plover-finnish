import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_25_toimi import kotus_noun_25_toimi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_25_toimi("toimi")

        expected = InflectionInfo(nominative='toimi',
                                  nominative_plural='toimet',
                                  genitive='toimen',
                                  genitives_plural=['tointen',
                                                    'toimien'],
                                  partitives=['tointa',
                                              'toimea'],
                                  partitives_plural=['toimia'],
                                  accusatives=['toimi',
                                               'toimen'],
                                  accusative_plural='toimet',
                                  inessive='toimessa',
                                  inessives_plural=['toimissa'],
                                  elative='toimesta',
                                  elatives_plural=['toimista'],
                                  illatives=['toimeen'],
                                  illatives_plural=['toimiin'],
                                  adessive='toimella',
                                  adessives_plural=['toimilla'],
                                  ablative='toimelta',
                                  ablatives_plural=['toimilta'],
                                  allative='toimelle',
                                  allatives_plural=['toimille'],
                                  essives=['toimena'],
                                  essives_plural=['toimina'],
                                  translative='toimeksi',
                                  translatives_plural=['toimiksi'],
                                  abessive='toimetta',
                                  abessives_plural=['toimitta'],
                                  instructives_plural=['toimin'],
                                  comitatives_plural=['toimine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_25_toimi("niemi")
        print(data)

        expected = InflectionInfo(nominative='niemi',
                                  nominative_plural='niemet',
                                  genitive='niemen',
                                  genitives_plural=['nienten',
                                                    'niemien'],
                                  partitives=['nientä',
                                              'niemeä'],
                                  partitives_plural=['niemiä'],
                                  accusatives=['niemi',
                                               'niemen'],
                                  accusative_plural='niemet',
                                  inessive='niemessä',
                                  inessives_plural=['niemissä'],
                                  elative='niemestä',
                                  elatives_plural=['niemistä'],
                                  illatives=['niemeen'],
                                  illatives_plural=['niemiin'],
                                  adessive='niemellä',
                                  adessives_plural=['niemillä'],
                                  ablative='niemeltä',
                                  ablatives_plural=['niemiltä'],
                                  allative='niemelle',
                                  allatives_plural=['niemille'],
                                  essives=['niemenä'],
                                  essives_plural=['nieminä'],
                                  translative='niemeksi',
                                  translatives_plural=['niemiksi'],
                                  abessive='niemettä',
                                  abessives_plural=['niemittä'],
                                  instructives_plural=['niemin'],
                                  comitatives_plural=['niemine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
