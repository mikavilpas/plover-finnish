import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_6_paperi import kotus_noun_6_paperi

class TestInflectionType6(unittest.TestCase):
    # There are no words with gradation in this class.

    def test_kotus_noun_6_paperi_full_cases(self):
        data = kotus_noun_6_paperi("paperi")

        expected = InflectionInfo(nominative='paperi',
                                  nominative_plural='paperit',
                                  genitive='paperin',
                                  genitives_plural=['paperien',
                                                    'papereiden',
                                                    'papereitten'],
                                  partitives=['paperia'],
                                  partitives_plural=['papereita',
                                                     'papereja'],
                                  accusatives=['paperi',
                                               'paperin'],
                                  accusative_plural='paperit',
                                  inessive='paperissa',
                                  inessives_plural=['papereissa'],
                                  elative='paperista',
                                  elatives_plural=['papereista'],
                                  illative='paperiin',
                                  illatives_plural=['papereihin'],
                                  adessive='paperilla',
                                  adessives_plural=['papereilla'],
                                  ablative='paperilta',
                                  ablatives_plural=['papereilta'],
                                  allative='paperille',
                                  allatives_plural=['papereille'],
                                  essive='paperina',
                                  essives_plural=['papereina'],
                                  translative='paperiksi',
                                  translatives_plural=['papereiksi'],
                                  abessive='paperitta',
                                  abessives_plural=['papereitta'],
                                  instructives_plural=['paperein'],
                                  comitatives_plural=['papereine'])
        ensure_inflections_equal(expected, data)

    def test_with_end_consonant(self):
        data = kotus_noun_6_paperi("nylon")
        expected = InflectionInfo(nominative='nylon',
                                  nominative_plural='nylonit',
                                  genitive='nylonin',
                                  genitives_plural=['nylonien',
                                                    'nyloneiden',
                                                    'nyloneitten'],
                                  partitives=['nylonia'],
                                  partitives_plural=['nyloneita',
                                                     'nyloneja'],
                                  accusatives=['nylon',
                                               'nylonin'],
                                  accusative_plural='nylonit',
                                  inessive='nylonissa',
                                  inessives_plural=['nyloneissa'],
                                  elative='nylonista',
                                  elatives_plural=['nyloneista'],
                                  illative='nyloniin',
                                  illatives_plural=['nyloneihin'],
                                  adessive='nylonilla',
                                  adessives_plural=['nyloneilla'],
                                  ablative='nylonilta',
                                  ablatives_plural=['nyloneilta'],
                                  allative='nylonille',
                                  allatives_plural=['nyloneille'],
                                  essive='nylonina',
                                  essives_plural=['nyloneina'],
                                  translative='nyloniksi',
                                  translatives_plural=['nyloneiksi'],
                                  abessive='nylonitta',
                                  abessives_plural=['nyloneitta'],
                                  instructives_plural=['nylonein'],
                                  comitatives_plural=['nyloneine'])
        ensure_inflections_equal(expected, data)

    def test_with_umlaut_inflections(self):
        data = kotus_noun_6_paperi("bensiini")
        expected = InflectionInfo(nominative='bensiini',
                                  nominative_plural='bensiinit',
                                  genitive='bensiinin',
                                  genitives_plural=['bensiinien',
                                                    'bensiineiden',
                                                    'bensiineitten'],
                                  partitives=['bensiiniä'],
                                  partitives_plural=['bensiineitä',
                                                     'bensiinejä'],
                                  accusatives=['bensiini',
                                               'bensiinin'],
                                  accusative_plural='bensiinit',
                                  inessive='bensiinissä',
                                  inessives_plural=['bensiineissä'],
                                  elative='bensiinistä',
                                  elatives_plural=['bensiineistä'],
                                  illative='bensiiniin',
                                  illatives_plural=['bensiineihin'],
                                  adessive='bensiinillä',
                                  adessives_plural=['bensiineillä'],
                                  ablative='bensiiniltä',
                                  ablatives_plural=['bensiineiltä'],
                                  allative='bensiinille',
                                  allatives_plural=['bensiineille'],
                                  essive='bensiininä',
                                  essives_plural=['bensiineinä'],
                                  translative='bensiiniksi',
                                  translatives_plural=['bensiineiksi'],
                                  abessive='bensiinittä',
                                  abessives_plural=['bensiineittä'],
                                  instructives_plural=['bensiinein'],
                                  comitatives_plural=['bensiineine'])
        ensure_inflections_equal(expected, data)
