import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_31_kaksi import kotus_noun_31_kaksi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_31_kaksi("kaksi")

        expected = InflectionInfo(nominative='kaksi',
                                  nominative_plural='kahdet',
                                  genitive='kahden',
                                  genitives_plural=['kaksien'],
                                  partitives=['kahta'],
                                  partitives_plural=['kaksia'],
                                  accusatives=['kaksi',
                                               'kahden'],
                                  accusative_plural='kahdet',
                                  inessive='kahdessa',
                                  inessives_plural=['kaksissa'],
                                  elative='kahdesta',
                                  elatives_plural=['kaksista'],
                                  illatives=['kahteen'],
                                  illatives_plural=['kaksiin'],
                                  adessive='kahdella',
                                  adessives_plural=['kaksilla'],
                                  ablative='kahdelta',
                                  ablatives_plural=['kaksilta'],
                                  allative='kahdelle',
                                  allatives_plural=['kaksille'],
                                  essives=['kahtena'],
                                  essives_plural=['kaksina'],
                                  translative='kahdeksi',
                                  translatives_plural=['kaksiksi'],
                                  abessive='kahdetta',
                                  abessives_plural=['kaksitta'],
                                  instructives_plural=['kaksin'],
                                  comitatives_plural=['kaksine'])

        ensure_inflections_equal(expected, data)

    # both words in this class belong to the same vowel harmony group

    # no words with gradation
    # no words ending in a consonant.
