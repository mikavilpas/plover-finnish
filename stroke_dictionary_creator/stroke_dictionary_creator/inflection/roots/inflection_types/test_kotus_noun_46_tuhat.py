import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_46_tuhat import kotus_noun_46_tuhat

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_46_tuhat("tuhat")

        expected = InflectionInfo(nominative='tuhat',
                                  nominative_plural='tuhannet',
                                  genitive='tuhannen',
                                  genitives_plural=['tuhansien',
                                                    'tuhanten'],
                                  partitives=['tuhatta'],
                                  partitives_plural=['tuhansia'],
                                  accusatives=['tuhat',
                                               'tuhannen'],
                                  accusative_plural='tuhannet',
                                  inessive='tuhannessa',
                                  inessives_plural=['tuhansissa'],
                                  elative='tuhannesta',
                                  elatives_plural=['tuhansista'],
                                  illatives=['tuhanteen'],
                                  illatives_plural=['tuhansiin'],
                                  adessive='tuhannella',
                                  adessives_plural=['tuhansilla'],
                                  ablative='tuhannelta',
                                  ablatives_plural=['tuhansilta'],
                                  allative='tuhannelle',
                                  allatives_plural=['tuhansille'],
                                  essives=['tuhantena'],
                                  essives_plural=['tuhansina'],
                                  translative='tuhanneksi',
                                  translatives_plural=['tuhansiksi'],
                                  abessive='tuhannetta',
                                  abessives_plural=['tuhansitta'],
                                  instructives_plural=['tuhansin'],
                                  comitatives_plural=['tuhansine'])

        ensure_inflections_equal(expected, data)
