import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_a_takki_takin_hake_hakkeen, gradate_kotus_b_kaappi_kaapin_opas_oppaan
from .kotus_noun_15_korkea import kotus_noun_15_korkea

class TestInflectionType15(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_15_korkea("korkea")

        expected = InflectionInfo(nominative="korkea",
                                  nominative_plural   = "korkeat",
                                  genitive            = "korkean",
                                  genitives_plural    = ["korkeiden",
                                                         "korkeitten",
                                                         "korkeain"],
                                  partitives          = ["korkeata", "korkeaa"],
                                  partitives_plural   = ["korkeita"],
                                  accusatives         = ["korkea", "korkean"],
                                  accusative_plural   = "korkeat",
                                  inessive            = "korkeassa",
                                  inessives_plural    = ["korkeissa"],
                                  elative             = "korkeasta",
                                  elatives_plural     = ["korkeista"],
                                  illatives           = ["korkeaan"],
                                  illatives_plural    = ["korkeisiin", "korkeihin"],
                                  adessive            = "korkealla",
                                  adessives_plural    = ["korkeilla"],
                                  ablative            = "korkealta",
                                  ablatives_plural    = ["korkeilta"],
                                  allative            = "korkealle",
                                  allatives_plural    = ["korkeille"],
                                  essives             = ["korkeana"],
                                  essives_plural      = ["korkeina"],
                                  translative         = "korkeaksi",
                                  translatives_plural = ["korkeiksi"],
                                  abessive            = "korkeatta",
                                  abessives_plural    = ["korkeitta"],
                                  instructives_plural = ["korkein"],
                                  comitatives_plural  = ["korkeine"])

        ensure_inflections_equal(expected, data)

    # no words with gradation in this class
    # no words end in a consonant.

    def test_umlauts(self):
        data = kotus_noun_15_korkea("eheä")
        expected = InflectionInfo(nominative='eheä',
                                  nominative_plural='eheät',
                                  genitive='eheän',
                                  genitives_plural=['eheiden',
                                                    'eheitten',
                                                    'eheäin'],
                                  partitives=['eheätä',
                                              'eheää'],
                                  partitives_plural=['eheitä'],
                                  accusatives=['eheä',
                                               'eheän'],
                                  accusative_plural='eheät',
                                  inessive='eheässä',
                                  inessives_plural=['eheissä'],
                                  elative='eheästä',
                                  elatives_plural=['eheistä'],
                                  illatives=['eheään'],
                                  illatives_plural=['eheisiin',
                                                    'eheihin'],
                                  adessive='eheällä',
                                  adessives_plural=['eheillä'],
                                  ablative='eheältä',
                                  ablatives_plural=['eheiltä'],
                                  allative='eheälle',
                                  allatives_plural=['eheille'],
                                  essives=['eheänä'],
                                  essives_plural=['eheinä'],
                                  translative='eheäksi',
                                  translatives_plural=['eheiksi'],
                                  abessive='eheättä',
                                  abessives_plural=['eheittä'],
                                  instructives_plural=['ehein'],
                                  comitatives_plural=['eheine'])

        ensure_inflections_equal(expected, data)
