import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_27_käsi import kotus_noun_27_käsi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_27_käsi("käsi")

        expected = InflectionInfo(nominative='käsi',
                                  nominative_plural='kädet',
                                  genitive='käden',
                                  genitives_plural=['käsien',
                                                    'kätten'],
                                  partitives=['kättä'],
                                  partitives_plural=['käsiä'],
                                  accusatives=['käsi',
                                               'käden'],
                                  accusative_plural='kädet',
                                  inessive='kädessä',
                                  inessives_plural=['käsissä'],
                                  elative='kädestä',
                                  elatives_plural=['käsistä'],
                                  illatives=['käteen'],
                                  illatives_plural=['käsiin'],
                                  adessive='kädellä',
                                  adessives_plural=['käsillä'],
                                  ablative='kädeltä',
                                  ablatives_plural=['käsiltä'],
                                  allative='kädelle',
                                  allatives_plural=['käsille'],
                                  essives=['kätenä'],
                                  essives_plural=['käsinä'],
                                  translative='kädeksi',
                                  translatives_plural=['käsiksi'],
                                  abessive='kädettä',
                                  abessives_plural=['käsittä'],
                                  instructives_plural=['käsin'],
                                  comitatives_plural=['käsine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_27_käsi("tosi")

        expected = InflectionInfo(nominative='tosi',
                                  nominative_plural='todet',
                                  genitive='toden',
                                  genitives_plural=['tosien',
                                                    'totten'],
                                  partitives=['totta'],
                                  partitives_plural=['tosia'],
                                  accusatives=['tosi',
                                               'toden'],
                                  accusative_plural='todet',
                                  inessive='todessa',
                                  inessives_plural=['tosissa'],
                                  elative='todesta',
                                  elatives_plural=['tosista'],
                                  illatives=['toteen'],
                                  illatives_plural=['tosiin'],
                                  adessive='todella',
                                  adessives_plural=['tosilla'],
                                  ablative='todelta',
                                  ablatives_plural=['tosilta'],
                                  allative='todelle',
                                  allatives_plural=['tosille'],
                                  essives=['totena'],
                                  essives_plural=['tosina'],
                                  translative='todeksi',
                                  translatives_plural=['tosiksi'],
                                  abessive='todetta',
                                  abessives_plural=['tositta'],
                                  instructives_plural=['tosin'],
                                  comitatives_plural=['tosine'])


        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
