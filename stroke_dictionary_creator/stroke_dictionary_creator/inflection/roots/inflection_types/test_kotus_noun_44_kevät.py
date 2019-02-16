import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_44_kevät import kotus_noun_44_kevät

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_44_kevät("kevät")

        expected = InflectionInfo(nominative='kevät',
                                  nominative_plural='keväät',
                                  genitive='kevään',
                                  genitives_plural=['keväiden',
                                                    'keväitten'],
                                  partitives=['kevättä'],
                                  partitives_plural=['keväitä'],
                                  accusatives=['kevät',
                                               'kevään'],
                                  accusative_plural='keväät',
                                  inessive='keväässä',
                                  inessives_plural=['keväissä'],
                                  elative='keväästä',
                                  elatives_plural=['keväistä'],
                                  illatives=['kevääseen'],
                                  illatives_plural=['keväisiin',
                                                    'keväihin'],
                                  adessive='keväällä',
                                  adessives_plural=['keväillä'],
                                  ablative='keväältä',
                                  ablatives_plural=['keväiltä'],
                                  allative='keväälle',
                                  allatives_plural=['keväille'],
                                  essives=['keväänä'],
                                  essives_plural=['keväinä'],
                                  translative='kevääksi',
                                  translatives_plural=['keväiksi'],
                                  abessive='keväättä',
                                  abessives_plural=['keväittä'],
                                  instructives_plural=['keväin'],
                                  comitatives_plural=['keväine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_44_kevät("ainut")

        expected = InflectionInfo(nominative='ainut',
                                  nominative_plural='ainuut',
                                  genitive='ainuun',
                                  genitives_plural=['ainuiden',
                                                    'ainuitten'],
                                  partitives=['ainutta'],
                                  partitives_plural=['ainuita'],
                                  accusatives=['ainut',
                                               'ainuun'],
                                  accusative_plural='ainuut',
                                  inessive='ainuussa',
                                  inessives_plural=['ainuissa'],
                                  elative='ainuusta',
                                  elatives_plural=['ainuista'],
                                  illatives=['ainuuseen'],
                                  illatives_plural=['ainuisiin',
                                                    'ainuihin'],
                                  adessive='ainuulla',
                                  adessives_plural=['ainuilla'],
                                  ablative='ainuulta',
                                  ablatives_plural=['ainuilta'],
                                  allative='ainuulle',
                                  allatives_plural=['ainuille'],
                                  essives=['ainuuna'],
                                  essives_plural=['ainuina'],
                                  translative='ainuuksi',
                                  translatives_plural=['ainuiksi'],
                                  abessive='ainuutta',
                                  abessives_plural=['ainuitta'],
                                  instructives_plural=['ainuin'],
                                  comitatives_plural=['ainuine'])

        ensure_inflections_equal(expected, data)

    # no gradation
    # also no modern words besides these two in this group
