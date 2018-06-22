import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_12_kulkija import kotus_noun_12_kulkija

class TestInflectionType12(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_12_kulkija("kulkija")

        expected = InflectionInfo(nominative="kulkija",
                                  nominative_plural   = "kulkijat",
                                  genitive            = "kulkijan",
                                  genitives_plural    = ["kulkijoiden",
                                                         "kulkijoitten",
                                                         "kulkijain"],
                                  partitives          = ["kulkijaa"],
                                  partitives_plural   = ["kulkijoita"],
                                  accusatives         = ["kulkija", "kulkijan"],
                                  accusative_plural   = "kulkijat",
                                  inessive            = "kulkijassa",
                                  inessives_plural    = ["kulkijoissa"],
                                  elative             = "kulkijasta",
                                  elatives_plural     = ["kulkijoista"],
                                  illatives           = ["kulkijaan"],
                                  illatives_plural    = ["kulkijoihin"],
                                  adessive            = "kulkijalla",
                                  adessives_plural    = ["kulkijoilla"],
                                  ablative            = "kulkijalta",
                                  ablatives_plural    = ["kulkijoilta"],
                                  allative            = "kulkijalle",
                                  allatives_plural    = ["kulkijoille"],
                                  essives             = ["kulkijana"],
                                  essives_plural      = ["kulkijoina"],
                                  translative         = "kulkijaksi",
                                  translatives_plural = ["kulkijoiksi"],
                                  abessive            = "kulkijatta",
                                  abessives_plural    = ["kulkijoitta"],
                                  instructives_plural = ["kulkijoin"],
                                  comitatives_plural  = ["kulkijoine"])

        ensure_inflections_equal(expected, data)


    def test_umlauts(self):
        data = kotus_noun_12_kulkija("irvistelijä")

        expected = InflectionInfo(nominative='irvistelijä',
                                  nominative_plural='irvistelijät',
                                  genitive='irvistelijän',
                                  genitives_plural=['irvistelijöiden',
                                                    'irvistelijöitten',
                                                    'irvistelijäin'],
                                  partitives=['irvistelijää'],
                                  partitives_plural=['irvistelijöitä'],
                                  accusatives=['irvistelijä',
                                               'irvistelijän'],
                                  accusative_plural='irvistelijät',
                                  inessive='irvistelijässä',
                                  inessives_plural=['irvistelijöissä'],
                                  elative='irvistelijästä',
                                  elatives_plural=['irvistelijöistä'],
                                  illatives=['irvistelijään'],
                                  illatives_plural=['irvistelijöihin'],
                                  adessive='irvistelijällä',
                                  adessives_plural=['irvistelijöillä'],
                                  ablative='irvistelijältä',
                                  ablatives_plural=['irvistelijöiltä'],
                                  allative='irvistelijälle',
                                  allatives_plural=['irvistelijöille'],
                                  essives=['irvistelijänä'],
                                  essives_plural=['irvistelijöinä'],
                                  translative='irvistelijäksi',
                                  translatives_plural=['irvistelijöiksi'],
                                  abessive='irvistelijättä',
                                  abessives_plural=['irvistelijöittä'],
                                  instructives_plural=['irvistelijöin'],
                                  comitatives_plural=['irvistelijöine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no singular words end in a consonant.
