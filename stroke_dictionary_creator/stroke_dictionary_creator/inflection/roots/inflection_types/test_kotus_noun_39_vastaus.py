import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön
from .kotus_noun_39_vastaus import kotus_noun_39_vastaus

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_39_vastaus("vihannes")

        expected = InflectionInfo(nominative='vihannes',
                                  nominative_plural='vihannekset',
                                  genitive='vihanneksen',
                                  genitives_plural=['vihannesten',
                                                    'vihanneksien'],
                                  partitives=['vihannesta'],
                                  partitives_plural=['vihanneksia'],
                                  accusatives=['vihannes'],
                                  accusative_plural='vihannekset',
                                  inessive='vihanneksessa',
                                  inessives_plural=['vihanneksissa'],
                                  elative='vihanneksesta',
                                  elatives_plural=['vihanneksista'],
                                  illatives=['vihannekseen'],
                                  illatives_plural=['vihanneksiin'],
                                  adessive='vihanneksella',
                                  adessives_plural=['vihanneksilla'],
                                  ablative='vihannekselta',
                                  ablatives_plural=['vihanneksilta'],
                                  allative='vihannekselle',
                                  allatives_plural=['vihanneksille'],
                                  essives=['vihanneksena'],
                                  essives_plural=['vihanneksina'],
                                  translative='vihannekseksi',
                                  translatives_plural=['vihanneksiksi'],
                                  abessive='vihanneksetta',
                                  abessives_plural=['vihanneksitta'],
                                  instructives_plural=['vihanneksin'],
                                  comitatives_plural=['vihanneksine'])


        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_39_vastaus("elämys")

        expected = InflectionInfo(nominative='elämys',
                                  nominative_plural='elämykset',
                                  genitive='elämyksen',
                                  genitives_plural=['elämysten',
                                                    'elämyksien'],
                                  partitives=['elämystä'],
                                  partitives_plural=['elämyksiä'],
                                  accusatives=['elämys'],
                                  accusative_plural='elämykset',
                                  inessive='elämyksessä',
                                  inessives_plural=['elämyksissä'],
                                  elative='elämyksestä',
                                  elatives_plural=['elämyksistä'],
                                  illatives=['elämykseen'],
                                  illatives_plural=['elämyksiin'],
                                  adessive='elämyksellä',
                                  adessives_plural=['elämyksillä'],
                                  ablative='elämykseltä',
                                  ablatives_plural=['elämyksiltä'],
                                  allative='elämykselle',
                                  allatives_plural=['elämyksille'],
                                  essives=['elämyksenä'],
                                  essives_plural=['elämyksinä'],
                                  translative='elämykseksi',
                                  translatives_plural=['elämyksiksi'],
                                  abessive='elämyksettä',
                                  abessives_plural=['elämyksittä'],
                                  instructives_plural=['elämyksin'],
                                  comitatives_plural=['elämyksine'])


        ensure_inflections_equal(expected, data)

    # all words use no gradation
