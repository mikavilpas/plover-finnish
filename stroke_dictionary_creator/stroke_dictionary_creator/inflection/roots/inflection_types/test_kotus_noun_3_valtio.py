import unittest
from ensure import ensure
from .kotus_noun_3_valtio import kotus_noun_3_valtio
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal

class TestInflectionType3(unittest.TestCase):
    def test_kotus_noun_3_valtio_full_cases(self):
        data = kotus_noun_3_valtio("valtio")
        expected = InflectionInfo(nominative='valtio',
                                  nominative_plural='valtiot',
                                  genitive='valtion',
                                  genitives_plural=['valtioiden',
                                                    'valtioitten'],
                                  partitives=['valtiota'],
                                  partitives_plural=['valtioita'],
                                  accusatives=['valtio',
                                               'valtion'],
                                  accusative_plural='valtiot',
                                  inessive='valtiossa',
                                  inessives_plural=['valtioissa'],
                                  elative='valtiosta',
                                  elatives_plural=['valtioista'],
                                  illative='valtioon',
                                  illatives_plural=['valtioihin'],
                                  adessive='valtiolla',
                                  adessives_plural=['valtioilla'],
                                  ablative='valtiolta',
                                  ablatives_plural=['valtioilta'],
                                  allative='valtiolle',
                                  allatives_plural=['valtioille'],
                                  essive='valtiona',
                                  essives_plural=['valtioina'],
                                  translative='valtioksi',
                                  translatives_plural=['valtioiksi'],
                                  abessive='valtiotta',
                                  abessives_plural=['valtioitta'],
                                  instructives_plural=['valtioin'],
                                  comitatives_plural=['valtioine'])

    def test_kotus_noun_3_valtio_umlauts(self):
        data = kotus_noun_3_valtio("häiriö")
        ensure(data.comitatives_plural).equals(["häiriöine"])

    # The kotus wordlist does not contain any words that belong to class 3 and
    # have a gradation class. Have to skip testing that.
