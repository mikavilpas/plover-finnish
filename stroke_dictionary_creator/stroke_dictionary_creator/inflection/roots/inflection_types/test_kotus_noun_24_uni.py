import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .kotus_noun_24_uni import kotus_noun_24_uni

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_24_uni("uni")

        expected = InflectionInfo(nominative='uni',
                                  nominative_plural='unet',
                                  genitive='unen',
                                  genitives_plural=['unien', 'unten'],
                                  partitives=['unta'],
                                  partitives_plural=['unia'],
                                  accusatives=['uni',
                                               'unen'],
                                  accusative_plural='unet',
                                  inessive='unessa',
                                  inessives_plural=['unissa'],
                                  elative='unesta',
                                  elatives_plural=['unista'],
                                  illatives=['uneen'],
                                  illatives_plural=['uniin'],
                                  adessive='unella',
                                  adessives_plural=['unilla'],
                                  ablative='unelta',
                                  ablatives_plural=['unilta'],
                                  allative='unelle',
                                  allatives_plural=['unille'],
                                  essives=['unena','unna'],
                                  essives_plural=['unina'],
                                  translative='uneksi',
                                  translatives_plural=['uniksi'],
                                  abessive='unetta',
                                  abessives_plural=['unitta'],
                                  instructives_plural=['unin'],
                                  comitatives_plural=['unine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_24_uni("riihi")

        expected = InflectionInfo(nominative='riihi',
                                  nominative_plural='riihet',
                                  genitive='riihen',
                                  genitives_plural=['riihien', 'riihten'],
                                  partitives=['riihtä'],
                                  partitives_plural=['riihiä'],
                                  accusatives=['riihi',
                                               'riihen'],
                                  accusative_plural='riihet',
                                  inessive='riihessä',
                                  inessives_plural=['riihissä'],
                                  elative='riihestä',
                                  elatives_plural=['riihistä'],
                                  illatives=['riiheen'],
                                  illatives_plural=['riihiin'],
                                  adessive='riihellä',
                                  adessives_plural=['riihillä'],
                                  ablative='riiheltä',
                                  ablatives_plural=['riihiltä'],
                                  allative='riihelle',
                                  allatives_plural=['riihille'],
                                  essives=['riihenä','riihnä'],
                                  essives_plural=['riihinä'],
                                  translative='riiheksi',
                                  translatives_plural=['riihiksi'],
                                  abessive='riihettä',
                                  abessives_plural=['riihittä'],
                                  instructives_plural=['riihin'],
                                  comitatives_plural=['riihine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
