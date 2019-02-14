import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .kotus_noun_30_veitsi import kotus_noun_30_veitsi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_30_veitsi("veitsi")

        expected = InflectionInfo(nominative='veitsi',
                                  nominative_plural='veitset',
                                  genitive='veitsen',
                                  genitives_plural=['veitsien',
                                                    'veisten'],
                                  partitives=['veistä'],
                                  partitives_plural=['veitsiä'],
                                  accusatives=['veitsi',
                                               'veitsen'],
                                  accusative_plural='veitset',
                                  inessive='veitsessä',
                                  inessives_plural=['veitsissä'],
                                  elative='veitsestä',
                                  elatives_plural=['veitsistä'],
                                  illatives=['veitseen'],
                                  illatives_plural=['veitsiin'],
                                  adessive='veitsellä',
                                  adessives_plural=['veitsillä'],
                                  ablative='veitseltä',
                                  ablatives_plural=['veitsiltä'],
                                  allative='veitselle',
                                  allatives_plural=['veitsille'],
                                  essives=['veitsenä'],
                                  essives_plural=['veitsinä'],
                                  translative='veitseksi',
                                  translatives_plural=['veitsiksi'],
                                  abessive='veitsettä',
                                  abessives_plural=['veitsittä'],
                                  instructives_plural=['veitsin'],
                                  comitatives_plural=['veitsine'])

        ensure_inflections_equal(expected, data)

    # both words in this class belong to the same vowel harmony group

    # no words with gradation
    # no words ending in a consonant.
