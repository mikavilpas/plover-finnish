import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_kate_katteen
from .kotus_noun_34_onneton import kotus_noun_34_onneton

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_34_onneton("onneton",
                                     gradate_kotus_c_kate_katteen)

        expected = InflectionInfo(nominative="onneton",
                                  nominative_plural   = "onnettomat",
                                  genitive            = "onnettoman",
                                  genitives_plural    = ["onnettomien",
                                                         "onnetonten"],
                                  partitives          = ["onnetonta"],
                                  partitives_plural   = ["onnettomia"],
                                  accusatives         = ["onneton", "onnettoman"],
                                  accusative_plural   = "onnettomat",
                                  inessive            = "onnettomassa",
                                  inessives_plural    = ["onnettomissa"],
                                  elative             = "onnettomasta",
                                  elatives_plural     = ["onnettomista"],
                                  illatives           = ["onnettomaan"],
                                  illatives_plural    = ["onnettomiin"],
                                  adessive            = "onnettomalla",
                                  adessives_plural    = ["onnettomilla"],
                                  ablative            = "onnettomalta",
                                  ablatives_plural    = ["onnettomilta"],
                                  allative            = "onnettomalle",
                                  allatives_plural    = ["onnettomille"],
                                  essives             = ["onnettomana"],
                                  essives_plural      = ["onnettomina"],
                                  translative         = "onnettomaksi",
                                  translatives_plural = ["onnettomiksi"],
                                  abessive            = "onnettomatta",
                                  abessives_plural    = ["onnettomitta"],
                                  instructives_plural = ["onnettomin"],
                                  comitatives_plural  = ["onnettomine"])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_34_onneton("hyödytön",
                                     gradate_kotus_c_kate_katteen)

        expected = InflectionInfo(nominative='hyödytön',
                                  nominative_plural='hyödyttömät',
                                  genitive='hyödyttömän',
                                  genitives_plural=['hyödyttömien',
                                                    'hyödytönten'],
                                  partitives=['hyödytöntä'],
                                  partitives_plural=['hyödyttömiä'],
                                  accusatives=['hyödytön',
                                               'hyödyttömän'],
                                  accusative_plural='hyödyttömät',
                                  inessive='hyödyttömässä',
                                  inessives_plural=['hyödyttömissä'],
                                  elative='hyödyttömästä',
                                  elatives_plural=['hyödyttömistä'],
                                  illatives=['hyödyttömään'],
                                  illatives_plural=['hyödyttömiin'],
                                  adessive='hyödyttömällä',
                                  adessives_plural=['hyödyttömillä'],
                                  ablative='hyödyttömältä',
                                  ablatives_plural=['hyödyttömiltä'],
                                  allative='hyödyttömälle',
                                  allatives_plural=['hyödyttömille'],
                                  essives=['hyödyttömänä'],
                                  essives_plural=['hyödyttöminä'],
                                  translative='hyödyttömäksi',
                                  translatives_plural=['hyödyttömiksi'],
                                  abessive='hyödyttömättä',
                                  abessives_plural=['hyödyttömittä'],
                                  instructives_plural=['hyödyttömin'],
                                  comitatives_plural=['hyödyttömine'])

        ensure_inflections_equal(expected, data)

    # all words use gradation C
