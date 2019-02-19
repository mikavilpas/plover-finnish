import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon
from .kotus_noun_22_parfait import kotus_noun_22_parfait

class TestInflectionType10(unittest.TestCase):
    def test_basic_example(self):

        data = kotus_noun_22_parfait("nougat")

        expected = InflectionInfo(nominative='nougat',
                                  nominative_plural="nougat't",
                                  genitive="nougat'n",
                                  genitives_plural=["nougat'iden",
                                                    "nougat'itten"],
                                  partitives=["nougat'ta"],
                                  partitives_plural=["nougat'ita"],
                                  accusatives=['nougat',
                                               "nougat'n"],
                                  accusative_plural="nougat't",
                                  inessive="nougat'ssa",
                                  inessives_plural=["nougat'issa"],
                                  elative="nougat'sta",
                                  elatives_plural=["nougat'ista"],
                                  illatives=["nougat'han"],
                                  illatives_plural=["nougat'ihin"],
                                  adessive="nougat'lla",
                                  adessives_plural=["nougat'illa"],
                                  ablative="nougat'lta",
                                  ablatives_plural=["nougat'ilta"],
                                  allative="nougat'lle",
                                  allatives_plural=["nougat'ille"],
                                  essives=["nougat'na"],
                                  essives_plural=["nougat'ina"],
                                  translative="nougat'ksi",
                                  translatives_plural=["nougat'iksi"],
                                  abessive="nougat'tta",
                                  abessives_plural=["nougat'itta"],
                                  instructives_plural=["nougat'in"],
                                  comitatives_plural=["nougat'ine"])


        ensure_inflections_equal(expected, data)

    # no gradation possible
