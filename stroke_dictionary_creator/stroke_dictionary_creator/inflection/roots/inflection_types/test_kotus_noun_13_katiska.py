import unittest

from ensure import ensure

from .. import gradation as g
from ..noun_inflection_info import InflectionInfo
from .kotus_noun_13_katiska import kotus_noun_13_katiska
from .test_utils import ensure_inflections_equal


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

    # no singular words end in a consonant.

    def test_gradation(self):
        data = kotus_noun_13_katiska("ärhäkkä", g.gradate_kotus_a_takki_takin)

        expected = InflectionInfo(nominative          = 'ärhäkkä',
                                  nominative_plural   = 'ärhäkät',
                                  genitive            = 'ärhäkän',
                                  genitives_plural    = ['ärhäköiden',
                                                         'ärhäköitten',
                                                         'ärhäkköjen',
                                                         'ärhäkkäin'],
                                  partitives          = ['ärhäkkää'],
                                  partitives_plural   = ['ärhäköitä',
                                                         'ärhäkköjä'],
                                  accusatives         = ['ärhäkkä',
                                                         'ärhäkän'],
                                  accusative_plural   = 'ärhäkät',
                                  inessive            = 'ärhäkässä',
                                  inessives_plural    = ['ärhäköissä'],
                                  elative             = 'ärhäkästä',
                                  elatives_plural     = ['ärhäköistä'],
                                  illatives           = ['ärhäkkään'],
                                  illatives_plural    = ['ärhäköihin'],
                                  adessive            = 'ärhäkällä',
                                  adessives_plural    = ['ärhäköillä'],
                                  ablative            = 'ärhäkältä',
                                  ablatives_plural    = ['ärhäköiltä'],
                                  allative            = 'ärhäkälle',
                                  allatives_plural    = ['ärhäköille'],
                                  essives             = ['ärhäkkänä'],
                                  essives_plural      = ['ärhäköinä'],
                                  translative         = 'ärhäkäksi',
                                  translatives_plural = ['ärhäköiksi'],
                                  abessive            = 'ärhäkättä',
                                  abessives_plural    = ['ärhäköittä'],
                                  instructives_plural = ['ärhäköin'],
                                  comitatives_plural  = ['ärhäkköine'])

        ensure_inflections_equal(expected, data)
