import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_45_kahdeksas import kotus_noun_45_kahdeksas

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_45_kahdeksas("kolmas")

        expected = InflectionInfo(nominative='kolmas',
                                  nominative_plural='kolmannet',
                                  genitive='kolmannen',
                                  genitives_plural=['kolmansien'],
                                  partitives=['kolmatta'],
                                  partitives_plural=['kolmansia'],
                                  accusatives=['kolmas',
                                               'kolmannen'],
                                  accusative_plural='kolmannet',
                                  inessive='kolmannessa',
                                  inessives_plural=['kolmansissa'],
                                  elative='kolmannesta',
                                  elatives_plural=['kolmansista'],
                                  illatives=['kolmanteen'],
                                  illatives_plural=['kolmansiin'],
                                  adessive='kolmannella',
                                  adessives_plural=['kolmansilla'],
                                  ablative='kolmannelta',
                                  ablatives_plural=['kolmansilta'],
                                  allative='kolmannelle',
                                  allatives_plural=['kolmansille'],
                                  essives=['kolmantena'],
                                  essives_plural=['kolmansina'],
                                  translative='kolmanneksi',
                                  translatives_plural=['kolmansiksi'],
                                  abessive='kolmannetta',
                                  abessives_plural=['kolmansitta'],
                                  instructives_plural=['kolmansin'],
                                  comitatives_plural=['kolmansine'])


        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_45_kahdeksas("yhdeksäs")

        expected = InflectionInfo(nominative='yhdeksäs',
                                  nominative_plural='yhdeksännet',
                                  genitive='yhdeksännen',
                                  genitives_plural=['yhdeksänsien'],
                                  partitives=['yhdeksättä'],
                                  partitives_plural=['yhdeksänsiä'],
                                  accusatives=['yhdeksäs',
                                               'yhdeksännen'],
                                  accusative_plural='yhdeksännet',
                                  inessive='yhdeksännessä',
                                  inessives_plural=['yhdeksänsissä'],
                                  elative='yhdeksännestä',
                                  elatives_plural=['yhdeksänsistä'],
                                  illatives=['yhdeksänteen'],
                                  illatives_plural=['yhdeksänsiin'],
                                  adessive='yhdeksännellä',
                                  adessives_plural=['yhdeksänsillä'],
                                  ablative='yhdeksänneltä',
                                  ablatives_plural=['yhdeksänsiltä'],
                                  allative='yhdeksännelle',
                                  allatives_plural=['yhdeksänsille'],
                                  essives=['yhdeksäntenä'],
                                  essives_plural=['yhdeksänsinä'],
                                  translative='yhdeksänneksi',
                                  translatives_plural=['yhdeksänsiksi'],
                                  abessive='yhdeksännettä',
                                  abessives_plural=['yhdeksänsittä'],
                                  instructives_plural=['yhdeksänsin'],
                                  comitatives_plural=['yhdeksänsine'])


        ensure_inflections_equal(expected, data)
