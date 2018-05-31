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
                                  partitive="kalaa",
                                  partitives_plural=["kaloja"],
                                  accusatives=["kala",
                                               "kalan"],
                                  accusative_plural="kalat",
                                  inessive="kalassa",
                                  inessive_plural="kaloissa",
                                  elative="kalasta",
                                  elative_plural="kaloista",
                                  illative="kalaan",
                                  illatives_plural=["kaloihin"],
                                  adessive="kalalla",
                                  adessive_plural="kaloilla",
                                  ablative="kalalta",
                                  ablative_plural="kaloilta",
                                  allative="kalalle",
                                  allative_plural="kaloille",
                                  essive="kalana",
                                  essive_plural="kaloina",
                                  translative="kalaksi",
                                  translative_plural="kaloiksi",
                                  abessive="kalatta",
                                  abessive_plural="kaloitta",
                                  instructive_plural="kaloin",
                                  comitative_plural="kaloine")

        ensure_inflections_equal(expected, data)

    def test_gradation(self):

        data = kotus_noun_9_kala("aortta",
                                 gradate_kotus_c_tyttö_tytön_kate_katteen)

        expected = InflectionInfo(nominative='aortta',
                                  nominative_plural='aortat',
                                  genitive='aortan',
                                  genitives_plural=['aorttojen',
                                                    'aorttain'],
                                  partitive='aorttaa',
                                  partitives_plural=['aorttoja'],
                                  accusatives=['aortta',
                                               'aortan'],
                                  accusative_plural='aortat',
                                  inessive='aortassa',
                                  inessive_plural='aortoissa',
                                  elative='aortasta',
                                  elative_plural='aortoista',
                                  illative='aorttaan',
                                  illatives_plural=['aorttoihin'],
                                  adessive='aortalla',
                                  adessive_plural='aortoilla',
                                  ablative='aortalta',
                                  ablative_plural='aortoilta',
                                  allative='aortalle',
                                  allative_plural='aortoille',
                                  essive='aorttana',
                                  essive_plural='aorttoina',
                                  translative='aortaksi',
                                  translative_plural='aortoiksi',
                                  abessive='aortatta',
                                  abessive_plural='aortoitta',
                                  instructive_plural='aortoin',
                                  comitative_plural='aorttoine')

        ensure_inflections_equal(expected, data)

    def test_umlauts(self):
        data = kotus_noun_9_kala("iskä")

        expected = InflectionInfo(nominative='iskä',
                                  nominative_plural='iskät',
                                  genitive='iskän',
                                  genitives_plural=['isköjen',
                                                    'iskäin'],
                                  partitive='iskää',
                                  partitives_plural=['isköjä'],
                                  accusatives=['iskä',
                                               'iskän'],
                                  accusative_plural='iskät',
                                  inessive='iskässä',
                                  inessive_plural='isköissä',
                                  elative='iskästä',
                                  elative_plural='isköistä',
                                  illative='iskään',
                                  illatives_plural=['isköihin'],
                                  adessive='iskällä',
                                  adessive_plural='isköillä',
                                  ablative='iskältä',
                                  ablative_plural='isköiltä',
                                  allative='iskälle',
                                  allative_plural='isköille',
                                  essive='iskänä',
                                  essive_plural='isköinä',
                                  translative='iskäksi',
                                  translative_plural='isköiksi',
                                  abessive='iskättä',
                                  abessive_plural='isköittä',
                                  instructive_plural='isköin',
                                  comitative_plural='isköine')

        ensure_inflections_equal(expected, data)

    # no singular words end in a consonant.
