import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_17_vapaa import kotus_noun_17_vapaa

class TestInflectionType17(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_17_vapaa("vapaa")

        expected = InflectionInfo(nominative="vapaa",
                                  nominative_plural   = "vapaat",
                                  genitive            = "vapaan",
                                  genitives_plural    = ["vapaiden",
                                                         "vapaitten"],
                                  partitives          = ["vapaata"],
                                  partitives_plural   = ["vapaita"],
                                  accusatives         = ["vapaa", "vapaan"],
                                  accusative_plural   = "vapaat",
                                  inessive            = "vapaassa",
                                  inessives_plural    = ["vapaissa"],
                                  elative             = "vapaasta",
                                  elatives_plural     = ["vapaista"],
                                  illative            = "vapaaseen",
                                  illatives_plural    = ["vapaisiin"],
                                  adessive            = "vapaalla",
                                  adessives_plural    = ["vapailla"],
                                  ablative            = "vapaalta",
                                  ablatives_plural    = ["vapailta"],
                                  allative            = "vapaalle",
                                  allatives_plural    = ["vapaille"],
                                  essive              = "vapaana",
                                  essives_plural      = ["vapaina"],
                                  translative         = "vapaaksi",
                                  translatives_plural = ["vapaiksi"],
                                  abessive            = "vapaatta",
                                  abessives_plural    = ["vapaitta"],
                                  instructives_plural = ["vapain"],
                                  comitatives_plural  = ["vapaine"])

        ensure_inflections_equal(expected, data)

    def test_ending_in_different_vowel(self):
        data = kotus_noun_17_vapaa("kaipuu")
        expected = InflectionInfo(nominative='kaipuu',
                                  nominative_plural='kaipuut',
                                  genitive='kaipuun',
                                  genitives_plural=['kaipuiden',
                                                    'kaipuitten'],
                                  partitives=['kaipuuta'],
                                  partitives_plural=['kaipuita'],
                                  accusatives=['kaipuu',
                                               'kaipuun'],
                                  accusative_plural='kaipuut',
                                  inessive='kaipuussa',
                                  inessives_plural=['kaipuissa'],
                                  elative='kaipuusta',
                                  elatives_plural=['kaipuista'],
                                  illative='kaipuuseen',
                                  illatives_plural=['kaipuisiin'],
                                  adessive='kaipuulla',
                                  adessives_plural=['kaipuilla'],
                                  ablative='kaipuulta',
                                  ablatives_plural=['kaipuilta'],
                                  allative='kaipuulle',
                                  allatives_plural=['kaipuille'],
                                  essive='kaipuuna',
                                  essives_plural=['kaipuina'],
                                  translative='kaipuuksi',
                                  translatives_plural=['kaipuiksi'],
                                  abessive='kaipuutta',
                                  abessives_plural=['kaipuitta'],
                                  instructives_plural=['kaipuin'],
                                  comitatives_plural=['kaipuine'])

        ensure_inflections_equal(expected, data)

    # No words with umlauts in this class
    # no words with gradation
    # no words ending in a consonant.
