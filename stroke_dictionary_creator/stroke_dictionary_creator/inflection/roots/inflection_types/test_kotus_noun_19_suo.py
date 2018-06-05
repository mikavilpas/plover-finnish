import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_19_suo import kotus_noun_19_suo

class TestInflectionType19(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_19_suo("suo")

        expected = InflectionInfo(nominative="suo",
                                  nominative_plural   = "suot",
                                  genitive            = "suon",
                                  genitives_plural    = ["soiden",
                                                         "soitten"],
                                  partitives          = ["suota"],
                                  partitives_plural   = ["soita"],
                                  accusatives         = ["suo", "suon"],
                                  accusative_plural   = "suot",
                                  inessive            = "suossa",
                                  inessives_plural    = ["soissa"],
                                  elative             = "suosta",
                                  elatives_plural     = ["soista"],
                                  illative            = "suohon",
                                  illatives_plural    = ["soihin"],
                                  adessive            = "suolla",
                                  adessives_plural    = ["soilla"],
                                  ablative            = "suolta",
                                  ablatives_plural    = ["soilta"],
                                  allative            = "suolle",
                                  allatives_plural    = ["soille"],
                                  essive              = "suona",
                                  essives_plural      = ["soina"],
                                  translative         = "suoksi",
                                  translatives_plural = ["soiksi"],
                                  abessive            = "suotta",
                                  abessives_plural    = ["soitta"],
                                  instructives_plural = ["soin"],
                                  comitatives_plural  = ["soine"])

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_19_suo("yö")
        expected = InflectionInfo(nominative='yö',
                                  nominative_plural='yöt',
                                  genitive='yön',
                                  genitives_plural=['öiden',
                                                    'öitten'],
                                  partitives=['yötä'],
                                  partitives_plural=['öitä'],
                                  accusatives=['yö',
                                               'yön'],
                                  accusative_plural='yöt',
                                  inessive='yössä',
                                  inessives_plural=['öissä'],
                                  elative='yöstä',
                                  elatives_plural=['öistä'],
                                  illative='yöhön',
                                  illatives_plural=['öihin'],
                                  adessive='yöllä',
                                  adessives_plural=['öillä'],
                                  ablative='yöltä',
                                  ablatives_plural=['öiltä'],
                                  allative='yölle',
                                  allatives_plural=['öille'],
                                  essive='yönä',
                                  essives_plural=['öinä'],
                                  translative='yöksi',
                                  translatives_plural=['öiksi'],
                                  abessive='yöttä',
                                  abessives_plural=['öittä'],
                                  instructives_plural=['öin'],
                                  comitatives_plural=['öine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
