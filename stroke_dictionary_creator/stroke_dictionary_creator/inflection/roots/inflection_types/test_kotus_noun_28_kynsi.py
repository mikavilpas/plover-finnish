import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .kotus_noun_28_kynsi import kotus_noun_28_kynsi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_28_kynsi("kynsi")

        expected = InflectionInfo(nominative='kynsi',
                                  nominative_plural='kynnet',
                                  genitive='kynnen',
                                  genitives_plural=['kynsien',
                                                    'kyntten'],
                                  partitives=['kynttä'],
                                  partitives_plural=['kynsiä'],
                                  accusatives=['kynsi',
                                               'kynnen'],
                                  accusative_plural='kynnet',
                                  inessive='kynnessä',
                                  inessives_plural=['kynsissä'],
                                  elative='kynnestä',
                                  elatives_plural=['kynsistä'],
                                  illatives=['kynteen'],
                                  illatives_plural=['kynsiin'],
                                  adessive='kynnellä',
                                  adessives_plural=['kynsillä'],
                                  ablative='kynneltä',
                                  ablatives_plural=['kynsiltä'],
                                  allative='kynnelle',
                                  allatives_plural=['kynsille'],
                                  essives=['kyntenä'],
                                  essives_plural=['kynsinä'],
                                  translative='kynneksi',
                                  translatives_plural=['kynsiksi'],
                                  abessive='kynnettä',
                                  abessives_plural=['kynsittä'],
                                  instructives_plural=['kynsin'],
                                  comitatives_plural=['kynsine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_28_kynsi("varsi")

        expected = InflectionInfo(nominative='varsi',
                                  nominative_plural='varret',
                                  genitive='varren',
                                  genitives_plural=['varsien',
                                                    'vartten'],
                                  partitives=['vartta'],
                                  partitives_plural=['varsia'],
                                  accusatives=['varsi',
                                               'varren'],
                                  accusative_plural='varret',
                                  inessive='varressa',
                                  inessives_plural=['varsissa'],
                                  elative='varresta',
                                  elatives_plural=['varsista'],
                                  illatives=['varteen'],
                                  illatives_plural=['varsiin'],
                                  adessive='varrella',
                                  adessives_plural=['varsilla'],
                                  ablative='varrelta',
                                  ablatives_plural=['varsilta'],
                                  allative='varrelle',
                                  allatives_plural=['varsille'],
                                  essives=['vartena'],
                                  essives_plural=['varsina'],
                                  translative='varreksi',
                                  translatives_plural=['varsiksi'],
                                  abessive='varretta',
                                  abessives_plural=['varsitta'],
                                  instructives_plural=['varsin'],
                                  comitatives_plural=['varsine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
