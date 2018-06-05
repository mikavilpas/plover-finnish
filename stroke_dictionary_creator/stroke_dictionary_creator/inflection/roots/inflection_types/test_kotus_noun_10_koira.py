import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_10_koira import kotus_noun_10_koira

class TestInflectionType10(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_10_koira("koira")

        expected = InflectionInfo(nominative="koira",
                                  nominative_plural="koirat",
                                  genitive="koiran",
                                  genitives_plural=["koirien", "koirain"],
                                  partitives=["koiraa"],
                                  partitives_plural=["koiria"],
                                  accusatives=["koira",
                                               "koiran"],
                                  accusative_plural="koirat",
                                  inessive="koirassa",
                                  inessives_plural=["koirissa"],
                                  elative="koirasta",
                                  elatives_plural=["koirista"],
                                  illatives=["koiraan"],
                                  illatives_plural=["koiriin"],
                                  adessive="koiralla",
                                  adessives_plural=["koirilla"],
                                  ablative="koiralta",
                                  ablatives_plural=["koirilta"],
                                  allative="koiralle",
                                  allatives_plural=["koirille"],
                                  essive="koirana",
                                  essives_plural=["koirina"],
                                  translative="koiraksi",
                                  translatives_plural=["koiriksi"],
                                  abessive="koiratta",
                                  abessives_plural=["koiritta"],
                                  instructives_plural=["koirin"],
                                  comitatives_plural=["koirine"])

        ensure_inflections_equal(expected, data)

    def test_gradation_and_umlauts(self):
        data = kotus_noun_10_koira("emäntä",
                                   gradate_kotus_j_hento_hennon_vanne_vanteen)

        expected = InflectionInfo(nominative='emäntä',
                                  nominative_plural='emännät',
                                  genitive='emännän',
                                  genitives_plural=['emäntien',
                                                    'emäntäin'],
                                  partitives=['emäntää'],
                                  partitives_plural=['emäntiä'],
                                  accusatives=['emäntä',
                                               'emännän'],
                                  accusative_plural='emännät',
                                  inessive='emännässä',
                                  inessives_plural=['emännissä'],
                                  elative='emännästä',
                                  elatives_plural=['emännistä'],
                                  illatives=['emäntään'],
                                  illatives_plural=['emäntiin'],
                                  adessive='emännällä',
                                  adessives_plural=['emännillä'],
                                  ablative='emännältä',
                                  ablatives_plural=['emänniltä'],
                                  allative='emännälle',
                                  allatives_plural=['emännille'],
                                  essive='emäntänä',
                                  essives_plural=['emäntinä'],
                                  translative='emännäksi',
                                  translatives_plural=['emänniksi'],
                                  abessive='emännättä',
                                  abessives_plural=['emännittä'],
                                  instructives_plural=['emännin'],
                                  comitatives_plural=['emäntine'])

        ensure_inflections_equal(expected, data)

    # no singular words end in a consonant.
