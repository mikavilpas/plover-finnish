import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .joukahainen_noun_10_poika import joukahainen_noun_10_poika

class TestInflectionType10(unittest.TestCase):
    def test_basic_example(self):
        data = joukahainen_noun_10_poika("poika")

        expected = InflectionInfo(nominative='poika',
                                  nominative_plural='pojat',
                                  genitive='pojan',
                                  genitives_plural=['poikien',
                                                    'poikain'],
                                  partitives=['poikaa'],
                                  partitives_plural=['poikia'],
                                  accusatives=['poika',
                                               'pojan'],
                                  accusative_plural='pojat',
                                  inessive='pojassa',
                                  inessives_plural=['pojissa'],
                                  elative='pojasta',
                                  elatives_plural=['pojista'],
                                  illatives=['poikaan'],
                                  illatives_plural=['poikiin'],
                                  adessive='pojalla',
                                  adessives_plural=['pojilla'],
                                  ablative='pojalta',
                                  ablatives_plural=['pojilta'],
                                  allative='pojalle',
                                  allatives_plural=['pojille'],
                                  essives=['poikana'],
                                  essives_plural=['poikina'],
                                  translative='pojaksi',
                                  translatives_plural=['pojiksi'],
                                  abessive='pojatta',
                                  abessives_plural=['pojitta'],
                                  instructives_plural=['pojin'],
                                  comitatives_plural=['poikine'])

        ensure_inflections_equal(expected, data)
