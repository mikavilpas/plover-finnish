import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_18_maa import kotus_noun_18_maa

class TestInflectionType18(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_18_maa("maa")

        expected = InflectionInfo(nominative="maa",
                                  nominative_plural   = "maat",
                                  genitive            = "maan",
                                  genitives_plural    = ["maiden",
                                                         "maitten"],
                                  partitives          = ["maata"],
                                  partitives_plural   = ["maita"],
                                  accusatives         = ["maa", "maan"],
                                  accusative_plural   = "maat",
                                  inessive            = "maassa",
                                  inessives_plural    = ["maissa"],
                                  elative             = "maasta",
                                  elatives_plural     = ["maista"],
                                  illatives           = ["maahan"],
                                  illatives_plural    = ["maihin"],
                                  adessive            = "maalla",
                                  adessives_plural    = ["mailla"],
                                  ablative            = "maalta",
                                  ablatives_plural    = ["mailta"],
                                  allative            = "maalle",
                                  allatives_plural    = ["maille"],
                                  essive              = "maana",
                                  essives_plural      = ["maina"],
                                  translative         = "maaksi",
                                  translatives_plural = ["maiksi"],
                                  abessive            = "maatta",
                                  abessives_plural    = ["maitta"],
                                  instructives_plural = ["main"],
                                  comitatives_plural  = ["maine"])

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_18_maa("jää")
        expected = InflectionInfo(nominative='jää',
                                  nominative_plural='jäät',
                                  genitive='jään',
                                  genitives_plural=['jäiden',
                                                    'jäitten'],
                                  partitives=['jäätä'],
                                  partitives_plural=['jäitä'],
                                  accusatives=['jää',
                                               'jään'],
                                  accusative_plural='jäät',
                                  inessive='jäässä',
                                  inessives_plural=['jäissä'],
                                  elative='jäästä',
                                  elatives_plural=['jäistä'],
                                  illatives=['jäähän'],
                                  illatives_plural=['jäihin'],
                                  adessive='jäällä',
                                  adessives_plural=['jäillä'],
                                  ablative='jäältä',
                                  ablatives_plural=['jäiltä'],
                                  allative='jäälle',
                                  allatives_plural=['jäille'],
                                  essive='jäänä',
                                  essives_plural=['jäinä'],
                                  translative='jääksi',
                                  translatives_plural=['jäiksi'],
                                  abessive='jäättä',
                                  abessives_plural=['jäittä'],
                                  instructives_plural=['jäin'],
                                  comitatives_plural=['jäine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
