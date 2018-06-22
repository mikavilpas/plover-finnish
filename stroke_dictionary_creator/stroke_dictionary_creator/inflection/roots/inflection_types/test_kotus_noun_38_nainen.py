import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön_kate_katteen
from .kotus_noun_38_nainen import kotus_noun_38_nainen

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_38_nainen("nainen")

        expected = InflectionInfo(nominative          = "nainen",
                                  nominative_plural   = "naiset",
                                  genitive            = "naisen",
                                  genitives_plural    = ["naisten",
                                                         "naisien"],
                                  partitives          = ["naista"],
                                  partitives_plural   = ["naisia"],
                                  accusatives         = ["nainen", "naisen"],
                                  accusative_plural   = "naiset",
                                  inessive            = "naisessa",
                                  inessives_plural    = ["naisissa"],
                                  elative             = "naisesta",
                                  elatives_plural     = ["naisista"],
                                  illatives           = ["naiseen"],
                                  illatives_plural    = ["naisiin"],
                                  adessive            = "naisella",
                                  adessives_plural    = ["naisilla"],
                                  ablative            = "naiselta",
                                  ablatives_plural    = ["naisilta"],
                                  allative            = "naiselle",
                                  allatives_plural    = ["naisille"],
                                  essives             = ["naisena"],
                                  essives_plural      = ["naisina"],
                                  translative         = "naiseksi",
                                  translatives_plural = ["naisiksi"],
                                  abessive            = "naisetta",
                                  abessives_plural    = ["naisitta"],
                                  instructives_plural = ["naisin"],
                                  comitatives_plural  = ["naisine"])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_38_nainen("hännällinen")

        expected = InflectionInfo(nominative='hännällinen',
                                  nominative_plural='hännälliset',
                                  genitive='hännällisen',
                                  genitives_plural=['hännällisten',
                                                    'hännällisien'],
                                  partitives=['hännällistä'],
                                  partitives_plural=['hännällisiä'],
                                  accusatives=['hännällinen',
                                               'hännällisen'],
                                  accusative_plural='hännälliset',
                                  inessive='hännällisessä',
                                  inessives_plural=['hännällisissä'],
                                  elative='hännällisestä',
                                  elatives_plural=['hännällisistä'],
                                  illatives=['hännälliseen'],
                                  illatives_plural=['hännällisiin'],
                                  adessive='hännällisellä',
                                  adessives_plural=['hännällisillä'],
                                  ablative='hännälliseltä',
                                  ablatives_plural=['hännällisiltä'],
                                  allative='hännälliselle',
                                  allatives_plural=['hännällisille'],
                                  essives=['hännällisenä'],
                                  essives_plural=['hännällisinä'],
                                  translative='hännälliseksi',
                                  translatives_plural=['hännällisiksi'],
                                  abessive='hännällisettä',
                                  abessives_plural=['hännällisittä'],
                                  instructives_plural=['hännällisin'],
                                  comitatives_plural=['hännällisine'])

        ensure_inflections_equal(expected, data)

    # all words use no gradation
