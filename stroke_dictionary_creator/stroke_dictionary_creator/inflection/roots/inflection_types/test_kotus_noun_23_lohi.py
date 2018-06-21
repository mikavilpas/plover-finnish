import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_23_lohi import kotus_noun_23_lohi

class TestInflectionType20(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_23_lohi("lohi")

        expected = InflectionInfo(nominative='lohi',
                                  nominative_plural='lohet',
                                  genitive='lohen',
                                  genitives_plural=['lohien'],
                                  partitives=['lohta'],
                                  partitives_plural=['lohia'],
                                  accusatives=['lohi',
                                               'lohen'],
                                  accusative_plural='lohet',
                                  inessive='lohessa',
                                  inessives_plural=['lohissa'],
                                  elative='lohesta',
                                  elatives_plural=['lohista'],
                                  illatives=['loheen'],
                                  illatives_plural=['lohiin'],
                                  adessive='lohella',
                                  adessives_plural=['lohilla'],
                                  ablative='lohelta',
                                  ablatives_plural=['lohilta'],
                                  allative='lohelle',
                                  allatives_plural=['lohille'],
                                  essive='lohena',
                                  essives_plural=['lohina'],
                                  translative='loheksi',
                                  translatives_plural=['lohiksi'],
                                  abessive='lohetta',
                                  abessives_plural=['lohitta'],
                                  instructives_plural=['lohin'],
                                  comitatives_plural=['lohine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_23_lohi("riihi")
        print(data)

        expected = InflectionInfo(nominative='riihi',
                                  nominative_plural='riihet',
                                  genitive='riihen',
                                  genitives_plural=['riihien'],
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
                                  essive='riihenä',
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
