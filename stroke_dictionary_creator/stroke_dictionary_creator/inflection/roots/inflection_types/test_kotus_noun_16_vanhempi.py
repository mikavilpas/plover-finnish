import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_16_vanhempi import kotus_noun_16_vanhempi

class TestInflectionType16(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_16_vanhempi("vanhempi",
                                      gradate_kotus_h_kumpi_kumman_lumme_lumpeen)

        expected = InflectionInfo(nominative="vanhempi",
                                  nominative_plural   = "vanhemmat",
                                  genitive            = "vanhemman",
                                  genitives_plural    = ["vanhempien",
                                                         "vanhempain"],
                                  partitives          = ["vanhempaa"],
                                  partitives_plural   = ["vanhempia"],
                                  accusatives         = ["vanhempi", "vanhemman"],
                                  accusative_plural   = "vanhemmat",
                                  inessive            = "vanhemmassa",
                                  inessives_plural    = ["vanhemmissa"],
                                  elative             = "vanhemmasta",
                                  elatives_plural     = ["vanhemmista"],
                                  illatives           = ["vanhempaan"],
                                  illatives_plural    = ["vanhempiin"],
                                  adessive            = "vanhemmalla",
                                  adessives_plural    = ["vanhemmilla"],
                                  ablative            = "vanhemmalta",
                                  ablatives_plural    = ["vanhemmilta"],
                                  allative            = "vanhemmalle",
                                  allatives_plural    = ["vanhemmille"],
                                  essive              = "vanhempana",
                                  essives_plural      = ["vanhempina"],
                                  translative         = "vanhemmaksi",
                                  translatives_plural = ["vanhemmiksi"],
                                  abessive            = "vanhemmatta",
                                  abessives_plural    = ["vanhemmitta"],
                                  instructives_plural = ["vanhemmin"],
                                  comitatives_plural  = ["vanhempine"])

        ensure_inflections_equal(expected, data)

    def test_with_umlauts(self):
        data = kotus_noun_16_vanhempi("vähempi",
                                      gradate_kotus_h_kumpi_kumman_lumme_lumpeen)

        expected = InflectionInfo(nominative='vähempi',
                                  nominative_plural='vähemmät',
                                  genitive='vähemmän',
                                  genitives_plural=['vähempien',
                                                    'vähempäin'],
                                  partitives=['vähempää'],
                                  partitives_plural=['vähempiä'],
                                  accusatives=['vähempi',
                                               'vähemmän'],
                                  accusative_plural='vähemmät',
                                  inessive='vähemmässä',
                                  inessives_plural=['vähemmissä'],
                                  elative='vähemmästä',
                                  elatives_plural=['vähemmistä'],
                                  illatives=['vähempään'],
                                  illatives_plural=['vähempiin'],
                                  adessive='vähemmällä',
                                  adessives_plural=['vähemmillä'],
                                  ablative='vähemmältä',
                                  ablatives_plural=['vähemmiltä'],
                                  allative='vähemmälle',
                                  allatives_plural=['vähemmille'],
                                  essive='vähempänä',
                                  essives_plural=['vähempinä'],
                                  translative='vähemmäksi',
                                  translatives_plural=['vähemmiksi'],
                                  abessive='vähemmättä',
                                  abessives_plural=['vähemmittä'],
                                  instructives_plural=['vähemmin'],
                                  comitatives_plural=['vähempine'])

        ensure_inflections_equal(expected, data)


    # all words with gradation in this class use the gradation class h
    # no words end in a consonant.
