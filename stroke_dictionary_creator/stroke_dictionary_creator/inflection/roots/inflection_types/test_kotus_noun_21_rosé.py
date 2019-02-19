import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon
from .kotus_noun_21_rosé import kotus_noun_21_rosé

class TestInflectionType10(unittest.TestCase):
    def test_basic_example(self):
        # this word could also be inflected as 8 (nalle)

        data = kotus_noun_21_rosé("smoothie")

        expected = InflectionInfo(nominative='smoothie',
                                  nominative_plural='smoothiet',
                                  genitive='smoothien',
                                  genitives_plural=['smoothieiden',
                                                    'smoothieitten'],
                                  partitives=['smoothieta'],
                                  partitives_plural=['smoothieita'],
                                  accusatives=['smoothie',
                                               'smoothien'],
                                  accusative_plural='smoothiet',
                                  inessive='smoothiessa',
                                  inessives_plural=['smoothieissa'],
                                  elative='smoothiesta',
                                  elatives_plural=['smoothieista'],
                                  illatives=['smoothieen'],
                                  illatives_plural=['smoothieihin',
                                                    'smoothieihin'],
                                  adessive='smoothiella',
                                  adessives_plural=['smoothieilla'],
                                  ablative='smoothielta',
                                  ablatives_plural=['smoothieilta'],
                                  allative='smoothielle',
                                  allatives_plural=['smoothieille'],
                                  essives=['smoothiena'],
                                  essives_plural=['smoothieina'],
                                  translative='smoothieksi',
                                  translatives_plural=['smoothieiksi'],
                                  abessive='smoothietta',
                                  abessives_plural=['smoothieitta'],
                                  instructives_plural=['smoothiein'],
                                  comitatives_plural=['smoothieine'])

        ensure_inflections_equal(expected, data)

    # no gradation possible
