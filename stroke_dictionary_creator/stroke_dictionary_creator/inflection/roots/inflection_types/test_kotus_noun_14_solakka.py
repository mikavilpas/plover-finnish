import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_a_takki_takin, gradate_kotus_b_kaappi_kaapin
from .kotus_noun_14_solakka import kotus_noun_14_solakka

class TestInflectionType14(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_14_solakka("solakka",
                                     gradate_kotus_a_takki_takin)

        expected = InflectionInfo(nominative="solakka",
                                  nominative_plural   = "solakat",
                                  genitive            = "solakan",
                                  genitives_plural    = ["solakoiden",
                                                         "solakoitten",
                                                         "solakkojen",
                                                         "solakkain"],
                                  partitives          = ["solakkaa"],
                                  partitives_plural   = ["solakoita", "solakkoja"],
                                  accusatives         = ["solakka", "solakan"],
                                  accusative_plural   = "solakat",
                                  inessive            = "solakassa",
                                  inessives_plural    = ["solakoissa"],
                                  elative             = "solakasta",
                                  elatives_plural     = ["solakoista"],
                                  illatives           = ["solakkaan"],
                                  illatives_plural    = ["solakoihin"],
                                  adessive            = "solakalla",
                                  adessives_plural    = ["solakoilla"],
                                  ablative            = "solakalta",
                                  ablatives_plural    = ["solakoilta"],
                                  allative            = "solakalle",
                                  allatives_plural    = ["solakoille"],
                                  essives             = ["solakkana"],
                                  essives_plural      = ["solakoina"],
                                  translative         = "solakaksi",
                                  translatives_plural = ["solakoiksi"],
                                  abessive            = "solakatta",
                                  abessives_plural    = ["solakoitta"],
                                  instructives_plural = ["solakoin"],
                                  comitatives_plural  = ["solakoine"])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_14_solakka("ulappa",
                                     gradate_kotus_b_kaappi_kaapin)

        expected = InflectionInfo(nominative='ulappa',
                                  nominative_plural='ulapat',
                                  genitive='ulapan',
                                  genitives_plural=['ulapoiden',
                                                    'ulapoitten',
                                                    'ulappojen',
                                                    'ulappain'],
                                  partitives=['ulappaa'],
                                  partitives_plural=['ulapoita',
                                                     'ulappoja'],
                                  accusatives=['ulappa',
                                               'ulapan'],
                                  accusative_plural='ulapat',
                                  inessive='ulapassa',
                                  inessives_plural=['ulapoissa'],
                                  elative='ulapasta',
                                  elatives_plural=['ulapoista'],
                                  illatives=['ulappaan'],
                                  illatives_plural=['ulapoihin'],
                                  adessive='ulapalla',
                                  adessives_plural=['ulapoilla'],
                                  ablative='ulapalta',
                                  ablatives_plural=['ulapoilta'],
                                  allative='ulapalle',
                                  allatives_plural=['ulapoille'],
                                  essives=['ulappana'],
                                  essives_plural=['ulapoina'],
                                  translative='ulapaksi',
                                  translatives_plural=['ulapoiksi'],
                                  abessive='ulapatta',
                                  abessives_plural=['ulapoitta'],
                                  instructives_plural=['ulapoin'],
                                  comitatives_plural=['ulapoine'])

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_14_solakka("ärhäkkä",
                                     gradate_kotus_a_takki_takin)
        expected = InflectionInfo(nominative='ärhäkkä',
                                  nominative_plural='ärhäkät',
                                  genitive='ärhäkän',
                                  genitives_plural=['ärhäköiden',
                                                    'ärhäköitten',
                                                    'ärhäkköjen',
                                                    'ärhäkkäin'],
                                  partitives=['ärhäkkää'],
                                  partitives_plural=['ärhäköitä',
                                                     'ärhäkköjä'],
                                  accusatives=['ärhäkkä',
                                               'ärhäkän'],
                                  accusative_plural='ärhäkät',
                                  inessive='ärhäkässä',
                                  inessives_plural=['ärhäköissä'],
                                  elative='ärhäkästä',
                                  elatives_plural=['ärhäköistä'],
                                  illatives=['ärhäkkään'],
                                  illatives_plural=['ärhäköihin'],
                                  adessive='ärhäkällä',
                                  adessives_plural=['ärhäköillä'],
                                  ablative='ärhäkältä',
                                  ablatives_plural=['ärhäköiltä'],
                                  allative='ärhäkälle',
                                  allatives_plural=['ärhäköille'],
                                  essives=['ärhäkkänä'],
                                  essives_plural=['ärhäköinä'],
                                  translative='ärhäkäksi',
                                  translatives_plural=['ärhäköiksi'],
                                  abessive='ärhäkättä',
                                  abessives_plural=['ärhäköittä'],
                                  instructives_plural=['ärhäköin'],
                                  comitatives_plural=['ärhäköine'])

        ensure_inflections_equal(expected, data)

    # no words end in a consonant.
