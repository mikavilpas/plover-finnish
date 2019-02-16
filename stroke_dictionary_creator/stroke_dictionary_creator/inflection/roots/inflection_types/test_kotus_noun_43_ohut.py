import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_43_ohut import kotus_noun_43_ohut

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_43_ohut("ohut")

        expected = InflectionInfo(nominative='ohut',
                                  nominative_plural='ohuet',
                                  genitive='ohuen',
                                  genitives_plural=['ohuiden',
                                                    'ohuitten'],
                                  partitives=['ohutta'],
                                  partitives_plural=['ohuita'],
                                  accusatives=['ohut',
                                               'ohuen'],
                                  accusative_plural='ohuet',
                                  inessive='ohuessa',
                                  inessives_plural=['ohuissa'],
                                  elative='ohuesta',
                                  elatives_plural=['ohuista'],
                                  illatives=['ohueen'],
                                  illatives_plural=['ohuisiin',
                                                    'ohuihin'],
                                  adessive='ohuella',
                                  adessives_plural=['ohuilla'],
                                  ablative='ohuelta',
                                  ablatives_plural=['ohuilta'],
                                  allative='ohuelle',
                                  allatives_plural=['ohuille'],
                                  essives=['ohuena'],
                                  essives_plural=['ohuina'],
                                  translative='ohueksi',
                                  translatives_plural=['ohuiksi'],
                                  abessive='ohuetta',
                                  abessives_plural=['ohuitta'],
                                  instructives_plural=['ohuin'],
                                  comitatives_plural=['ohuine'])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_43_ohut("immyt",
                                  g.gradate_kotus_h_lumme_lumpeen)

        expected = InflectionInfo(nominative='immyt',
                                  nominative_plural='impyet',
                                  genitive='impyen',
                                  genitives_plural=['impyiden',
                                                    'impyitten'],
                                  partitives=['immyttä'],
                                  partitives_plural=['impyitä'],
                                  accusatives=['immyt',
                                               'impyen'],
                                  accusative_plural='impyet',
                                  inessive='impyessä',
                                  inessives_plural=['impyissä'],
                                  elative='impyestä',
                                  elatives_plural=['impyistä'],
                                  illatives=['impyeen'],
                                  illatives_plural=['impyisiin',
                                                    'impyihin'],
                                  adessive='impyellä',
                                  adessives_plural=['impyillä'],
                                  ablative='impyeltä',
                                  ablatives_plural=['impyiltä'],
                                  allative='impyelle',
                                  allatives_plural=['impyille'],
                                  essives=['impyenä'],
                                  essives_plural=['impyinä'],
                                  translative='impyeksi',
                                  translatives_plural=['impyiksi'],
                                  abessive='impyettä',
                                  abessives_plural=['impyittä'],
                                  instructives_plural=['impyin'],
                                  comitatives_plural=['impyine'])

        ensure_inflections_equal(expected, data)
