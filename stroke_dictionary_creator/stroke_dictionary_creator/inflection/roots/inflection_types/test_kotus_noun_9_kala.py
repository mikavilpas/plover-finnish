import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön_kate_katteen
from .kotus_noun_9_kala import kotus_noun_9_kala

class TestInflectionType9(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_9_kala("kala")

        expected = InflectionInfo(nominative="kala",
                                  nominative_plural="kalat",
                                  genitive="kalan",
                                  genitives_plural=["kalojen", "kalain"],
                                  partitives=["kalaa"],
                                  partitives_plural=["kaloja"],
                                  accusatives=["kala",
                                               "kalan"],
                                  accusative_plural="kalat",
                                  inessive="kalassa",
                                  inessives_plural=["kaloissa"],
                                  elative="kalasta",
                                  elatives_plural=["kaloista"],
                                  illatives=["kalaan"],
                                  illatives_plural=["kaloihin"],
                                  adessive="kalalla",
                                  adessives_plural=["kaloilla"],
                                  ablative="kalalta",
                                  ablatives_plural=["kaloilta"],
                                  allative="kalalle",
                                  allatives_plural=["kaloille"],
                                  essive="kalana",
                                  essives_plural=["kaloina"],
                                  translative="kalaksi",
                                  translatives_plural=["kaloiksi"],
                                  abessive="kalatta",
                                  abessives_plural=["kaloitta"],
                                  instructives_plural=["kaloin"],
                                  comitatives_plural=["kaloine"])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):

        data = kotus_noun_9_kala("aortta",
                                 gradate_kotus_c_tyttö_tytön_kate_katteen)

        expected = InflectionInfo(nominative='aortta',
                                  nominative_plural='aortat',
                                  genitive='aortan',
                                  genitives_plural=['aorttojen',
                                                    'aorttain'],
                                  partitives=['aorttaa'],
                                  partitives_plural=['aorttoja'],
                                  accusatives=['aortta',
                                               'aortan'],
                                  accusative_plural='aortat',
                                  inessive='aortassa',
                                  inessives_plural=['aortoissa'],
                                  elative='aortasta',
                                  elatives_plural=['aortoista'],
                                  illatives=['aorttaan'],
                                  illatives_plural=['aorttoihin'],
                                  adessive='aortalla',
                                  adessives_plural=['aortoilla'],
                                  ablative='aortalta',
                                  ablatives_plural=['aortoilta'],
                                  allative='aortalle',
                                  allatives_plural=['aortoille'],
                                  essive='aorttana',
                                  essives_plural=['aorttoina'],
                                  translative='aortaksi',
                                  translatives_plural=['aortoiksi'],
                                  abessive='aortatta',
                                  abessives_plural=['aortoitta'],
                                  instructives_plural=['aortoin'],
                                  comitatives_plural=['aorttoine'])

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_9_kala("iskä")

        expected = InflectionInfo(nominative='iskä',
                                  nominative_plural='iskät',
                                  genitive='iskän',
                                  genitives_plural=['isköjen',
                                                    'iskäin'],
                                  partitives=['iskää'],
                                  partitives_plural=['isköjä'],
                                  accusatives=['iskä',
                                               'iskän'],
                                  accusative_plural='iskät',
                                  inessive='iskässä',
                                  inessives_plural=['isköissä'],
                                  elative='iskästä',
                                  elatives_plural=['isköistä'],
                                  illatives=['iskään'],
                                  illatives_plural=['isköihin'],
                                  adessive='iskällä',
                                  adessives_plural=['isköillä'],
                                  ablative='iskältä',
                                  ablatives_plural=['isköiltä'],
                                  allative='iskälle',
                                  allatives_plural=['isköille'],
                                  essive='iskänä',
                                  essives_plural=['isköinä'],
                                  translative='iskäksi',
                                  translatives_plural=['isköiksi'],
                                  abessive='iskättä',
                                  abessives_plural=['isköittä'],
                                  instructives_plural=['isköin'],
                                  comitatives_plural=['isköine'])

        ensure_inflections_equal(expected, data)

    # no singular words end in a consonant.
