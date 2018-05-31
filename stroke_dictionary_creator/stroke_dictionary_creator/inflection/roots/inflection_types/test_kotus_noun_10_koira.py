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
                                  partitive="koiraa",
                                  partitives_plural=["koiria"],
                                  accusatives=["koira",
                                               "koiran"],
                                  accusative_plural="koirat",
                                  inessive="koirassa",
                                  inessive_plural="koirissa",
                                  elative="koirasta",
                                  elative_plural="koirista",
                                  illative="koiraan",
                                  illatives_plural=["koiriin"],
                                  adessive="koiralla",
                                  adessive_plural="koirilla",
                                  ablative="koiralta",
                                  ablative_plural="koirilta",
                                  allative="koiralle",
                                  allative_plural="koirille",
                                  essive="koirana",
                                  essive_plural="koirina",
                                  translative="koiraksi",
                                  translative_plural="koiriksi",
                                  abessive="koiratta",
                                  abessive_plural="koiritta",
                                  instructive_plural="koirin",
                                  comitative_plural="koirine")

        ensure_inflections_equal(expected, data)

    def test_gradation_and_umlauts(self):
        data = kotus_noun_10_koira("emäntä",
                                   gradate_kotus_j_hento_hennon_vanne_vanteen)

        expected = InflectionInfo(nominative='emäntä',
                                  nominative_plural='emännät',
                                  genitive='emännän',
                                  genitives_plural=['emäntien',
                                                    'emäntäin'],
                                  partitive='emäntää',
                                  partitives_plural=['emäntiä'],
                                  accusatives=['emäntä',
                                               'emännän'],
                                  accusative_plural='emännät',
                                  inessive='emännässä',
                                  inessive_plural='emännissä',
                                  elative='emännästä',
                                  elative_plural='emännistä',
                                  illative='emäntään',
                                  illatives_plural=['emäntiin'],
                                  adessive='emännällä',
                                  adessive_plural='emännillä',
                                  ablative='emännältä',
                                  ablative_plural='emänniltä',
                                  allative='emännälle',
                                  allative_plural='emännille',
                                  essive='emäntänä',
                                  essive_plural='emäntinä',
                                  translative='emännäksi',
                                  translative_plural='emänniksi',
                                  abessive='emännättä',
                                  abessive_plural='emännittä',
                                  instructive_plural='emännin',
                                  comitative_plural='emäntine')

        ensure_inflections_equal(expected, data)

    # no singular words end in a consonant.
