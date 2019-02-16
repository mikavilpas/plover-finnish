import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_42_mies import kotus_noun_42_mies

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_42_mies("mies")

        expected = InflectionInfo(nominative='mies',
                                  nominative_plural='miehet',
                                  genitive='miehen',
                                  genitives_plural=['miesten',
                                                    'miehien'],
                                  partitives=['miestä'],
                                  partitives_plural=['miehiä'],
                                  accusatives=['mies',
                                               'miehen'],
                                  accusative_plural='miehet',
                                  inessive='miehessä',
                                  inessives_plural=['miehissä'],
                                  elative='miehestä',
                                  elatives_plural=['miehistä'],
                                  illatives=['mieheen'],
                                  illatives_plural=['miehiin'],
                                  adessive='miehellä',
                                  adessives_plural=['miehillä'],
                                  ablative='mieheltä',
                                  ablatives_plural=['miehiltä'],
                                  allative='miehelle',
                                  allatives_plural=['miehille'],
                                  essives=['miehenä'],
                                  essives_plural=['miehinä'],
                                  translative='mieheksi',
                                  translatives_plural=['miehiksi'],
                                  abessive='miehettä',
                                  abessives_plural=['miehittä'],
                                  instructives_plural=['miehin'],
                                  comitatives_plural=['miehine'])



        ensure_inflections_equal(expected, data)
