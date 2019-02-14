import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .kotus_noun_29_lapsi import kotus_noun_29_lapsi

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_29_lapsi("lapsi")

        expected = InflectionInfo(nominative='lapsi',
                                  nominative_plural='lapset',
                                  genitive='lapsen',
                                  genitives_plural=['lapsien',
                                                    'lasten'],
                                  partitives=['lasta'],
                                  partitives_plural=['lapsia'],
                                  accusatives=['lapsi',
                                               'lapsen'],
                                  accusative_plural='lapset',
                                  inessive='lapsessa',
                                  inessives_plural=['lapsissa'],
                                  elative='lapsesta',
                                  elatives_plural=['lapsista'],
                                  illatives=['lapseen'],
                                  illatives_plural=['lapsiin'],
                                  adessive='lapsella',
                                  adessives_plural=['lapsilla'],
                                  ablative='lapselta',
                                  ablatives_plural=['lapsilta'],
                                  allative='lapselle',
                                  allatives_plural=['lapsille'],
                                  essives=['lapsena'],
                                  essives_plural=['lapsina'],
                                  translative='lapseksi',
                                  translatives_plural=['lapsiksi'],
                                  abessive='lapsetta',
                                  abessives_plural=['lapsitta'],
                                  instructives_plural=['lapsin'],
                                  comitatives_plural=['lapsine'])

        ensure_inflections_equal(expected, data)

    # there are only 3 words in this group, and they all share the same vowel
    # harmony group.

    # no words with gradation
    # no words ending in a consonant.
