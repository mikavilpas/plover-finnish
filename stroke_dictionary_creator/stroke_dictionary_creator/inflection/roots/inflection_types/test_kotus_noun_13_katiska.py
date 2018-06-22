import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_13_katiska import kotus_noun_13_katiska

class TestInflectionType12(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_13_katiska("katiska")

        expected = InflectionInfo(nominative="katiska",
                                  nominative_plural   = "katiskat",
                                  genitive            = "katiskan",
                                  genitives_plural    = ["katiskoiden",
                                                         "katiskoitten",
                                                         "katiskojen",
                                                         "katiskain"],
                                  partitives          = ["katiskaa"],
                                  partitives_plural   = ["katiskoita", "katiskoja"],
                                  accusatives         = ["katiska", "katiskan"],
                                  accusative_plural   = "katiskat",
                                  inessive            = "katiskassa",
                                  inessives_plural    = ["katiskoissa"],
                                  elative             = "katiskasta",
                                  elatives_plural     = ["katiskoista"],
                                  illatives           = ["katiskaan"],
                                  illatives_plural    = ["katiskoihin"],
                                  adessive            = "katiskalla",
                                  adessives_plural    = ["katiskoilla"],
                                  ablative            = "katiskalta",
                                  ablatives_plural    = ["katiskoilta"],
                                  allative            = "katiskalle",
                                  allatives_plural    = ["katiskoille"],
                                  essives             = ["katiskana"],
                                  essives_plural      = ["katiskoina"],
                                  translative         = "katiskaksi",
                                  translatives_plural = ["katiskoiksi"],
                                  abessive            = "katiskatta",
                                  abessives_plural    = ["katiskoitta"],
                                  instructives_plural = ["katiskoin"],
                                  comitatives_plural  = ["katiskoine"])

        ensure_inflections_equal(expected, data)


    def test_umlauts(self):
        data = kotus_noun_13_katiska("mölinä")

        expected = InflectionInfo(nominative='mölinä',
                                  nominative_plural='mölinät',
                                  genitive='mölinän',
                                  genitives_plural=['mölinöiden',
                                                    'mölinöitten',
                                                    'mölinöjen',
                                                    'mölinäin'],
                                  partitives=['mölinää'],
                                  partitives_plural=['mölinöitä',
                                                     'mölinöjä'],
                                  accusatives=['mölinä',
                                               'mölinän'],
                                  accusative_plural='mölinät',
                                  inessive='mölinässä',
                                  inessives_plural=['mölinöissä'],
                                  elative='mölinästä',
                                  elatives_plural=['mölinöistä'],
                                  illatives=['mölinään'],
                                  illatives_plural=['mölinöihin'],
                                  adessive='mölinällä',
                                  adessives_plural=['mölinöillä'],
                                  ablative='mölinältä',
                                  ablatives_plural=['mölinöiltä'],
                                  allative='mölinälle',
                                  allatives_plural=['mölinöille'],
                                  essives=['mölinänä'],
                                  essives_plural=['mölinöinä'],
                                  translative='mölinäksi',
                                  translatives_plural=['mölinöiksi'],
                                  abessive='mölinättä',
                                  abessives_plural=['mölinöittä'],
                                  instructives_plural=['mölinöin'],
                                  comitatives_plural=['mölinöine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no singular words end in a consonant.
