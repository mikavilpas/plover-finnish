import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_kumpi_kumman_lumme_lumpeen
from .kotus_noun_20_filee import kotus_noun_20_filee

class TestInflectionType20(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_20_filee("filee")

        expected = InflectionInfo(nominative="filee",
                                  nominative_plural   = "fileet",
                                  genitive            = "fileen",
                                  genitives_plural    = ["fileiden",
                                                         "fileitten"],
                                  partitives          = ["fileetä"],
                                  partitives_plural   = ["fileitä"],
                                  accusatives         = ["filee", "fileen"],
                                  accusative_plural   = "fileet",
                                  inessive            = "fileessä",
                                  inessives_plural    = ["fileissä"],
                                  elative             = "fileestä",
                                  elatives_plural     = ["fileistä"],
                                  illatives           = ["fileeseen", "fileehen"],
                                  illatives_plural    = ["fileisiin", "fileihin"],
                                  adessive            = "fileellä",
                                  adessives_plural    = ["fileillä"],
                                  ablative            = "fileeltä",
                                  ablatives_plural    = ["fileiltä"],
                                  allative            = "fileellä",
                                  allatives_plural    = ["fileille"],
                                  essives             = ["fileenä"],
                                  essives_plural      = ["fileinä"],
                                  translative         = "fileeksi",
                                  translatives_plural = ["fileiksi"],
                                  abessive            = "fileettä",
                                  abessives_plural    = ["fileittä"],
                                  instructives_plural = ["filein"],
                                  comitatives_plural  = ["fileine"])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_20_filee("ateljee")

        expected = InflectionInfo(nominative="ateljee",
                                  nominative_plural   = "ateljeet",
                                  genitive            = "ateljeen",
                                  genitives_plural    = ["ateljeiden",
                                                         "ateljeitten"],
                                  partitives          = ["ateljeeta"],
                                  partitives_plural   = ["ateljeita"],
                                  accusatives         = ["ateljee", "ateljeen"],
                                  accusative_plural   = "ateljeet",
                                  inessive            = "ateljeessa",
                                  inessives_plural    = ["ateljeissa"],
                                  elative             = "ateljeesta",
                                  elatives_plural     = ["ateljeista"],
                                  illatives           = ["ateljeeseen", "ateljeehen"],
                                  illatives_plural    = ["ateljeisiin", "ateljeihin"],
                                  adessive            = "ateljeella",
                                  adessives_plural    = ["ateljeilla"],
                                  ablative            = "ateljeelta",
                                  ablatives_plural    = ["ateljeilta"],
                                  allative            = "ateljeella",
                                  allatives_plural    = ["ateljeille"],
                                  essives             = ["ateljeena"],
                                  essives_plural      = ["ateljeina"],
                                  translative         = "ateljeeksi",
                                  translatives_plural = ["ateljeiksi"],
                                  abessive            = "ateljeetta",
                                  abessives_plural    = ["ateljeitta"],
                                  instructives_plural = ["ateljein"],
                                  comitatives_plural  = ["ateljeine"])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
