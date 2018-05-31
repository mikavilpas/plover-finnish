import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_11_omena import kotus_noun_11_omena

class TestInflectionType11(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_11_omena("omena")

        expected = InflectionInfo(nominative="omena",
                                  nominative_plural   = "omenat",
                                  genitive            = "omenan",
                                  genitives_plural    = ["omenien",
                                                         "omenoiden",
                                                         "omenoitten",
                                                         "omenojen",
                                                         "omenain"],
                                  partitive           = "omenaa",
                                  partitives_plural   = ["omenia",
                                                         "omenoita",
                                                         "omenoja"],
                                  accusatives         = ["omena", "omenan"],
                                  accusative_plural   = "omenat",
                                  inessive            = "omenassa",
                                  inessives_plural    = ["omenoissa", "omenissa"],
                                  elative             = "omenasta",
                                  elatives_plural     = ["omenoista", "omenista"],
                                  illative            = "omenaan",
                                  illatives_plural    = ["omenoihin", "omeniin"],
                                  adessive            = "omenalla",
                                  adessives_plural    = ["omenoilla", "omenilla"],
                                  ablative            = "omenalta",
                                  ablatives_plural    = ["omenoilta", "omenilta"],
                                  allative            = "omenalle",
                                  allatives_plural    = ["omenoille", "omenille"],
                                  essive              = "omenana",
                                  essives_plural      = ["omenoina", "omenina"],
                                  translative         = "omenaksi",
                                  translatives_plural = ["omenoiksi", "omeniksi"],
                                  abessive            = "omenatta",
                                  abessives_plural    = ["omenoitta", "omenitta"],
                                  instructives_plural = ["omenoin", "omenin"],
                                  comitatives_plural  = ["omenoine", "omenine"])

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_11_omena("käpälä")

        expected = InflectionInfo(nominative='käpälä',
                                  nominative_plural='käpälät',
                                  genitive='käpälän',
                                  genitives_plural=['käpälien',
                                                    'käpälöiden',
                                                    'käpälöitten',
                                                    'käpälöjen',
                                                    'käpäläin'],
                                  partitive='käpälää',
                                  partitives_plural=['käpäliä',
                                                     'käpälöitä',
                                                     'käpälöjä'],
                                  accusatives=['käpälä', 'käpälän'],
                                  accusative_plural='käpälät',
                                  inessive='käpälässä',
                                  inessives_plural=['käpälöissä', 'käpälissä'],
                                  elative='käpälästä',
                                  elatives_plural=['käpälöistä', 'käpälistä'],
                                  illative='käpälään',
                                  illatives_plural=['käpälöihin', 'käpäliin'],
                                  adessive='käpälällä',
                                  adessives_plural=['käpälöillä', 'käpälillä'],
                                  ablative='käpälältä',
                                  ablatives_plural=['käpälöiltä', 'käpäliltä'],
                                  allative='käpälälle',
                                  allatives_plural=['käpälöille', 'käpälille'],
                                  essive='käpälänä',
                                  essives_plural=['käpälöinä', 'käpälinä'],
                                  translative='käpäläksi',
                                  translatives_plural=['käpälöiksi', 'käpäliksi'],
                                  abessive='käpälättä',
                                  abessives_plural=['käpälöittä', 'käpälittä'],
                                  instructives_plural=['käpälöin', 'käpälin'],
                                  comitatives_plural=['käpälöine', 'käpäline'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no singular words end in a consonant.
