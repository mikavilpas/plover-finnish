import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_7_ovi import kotus_noun_7_ovi

class TestInflectionType7(unittest.TestCase):
    def test_kotus_noun_6_ove_full_cases(self):
        data = kotus_noun_7_ovi("ovi")

        expected = InflectionInfo(nominative="ovi",
                                  nominative_plural="ovet",
                                  genitive="oven",
                                  genitives_plural=["ovien"],
                                  partitive="ovea",
                                  partitives_plural=["ovia"],
                                  accusatives=["ovi",
                                               "oven"],
                                  accusative_plural="ovet",
                                  inessive="ovessa",
                                  inessive_plural="ovissa",
                                  elative="ovesta",
                                  elative_plural="ovista",
                                  illative="oveen",
                                  illatives_plural=["oviin"],
                                  adessive="ovella",
                                  adessive_plural="ovilla",
                                  ablative="ovelta",
                                  ablative_plural="ovilta",
                                  allative="ovelle",
                                  allative_plural="oville",
                                  essive="ovena",
                                  essive_plural="ovina",
                                  translative="oveksi",
                                  translative_plural="oviksi",
                                  abessive="ovetta",
                                  abessive_plural="ovitta",
                                  instructive_plural="ovin",
                                  comitative_plural="ovine")

        ensure_inflections_equal(expected, data)

    # TODO: test gradation
    # TODO: test with end consonants
