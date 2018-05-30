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
                                  partitive='paperia',
                                  partitives_plural=['papereita',
                                                     'papereja'],
                                  accusatives=['paperi',
                                               'paperin'],
                                  accusative_plural='paperit',
                                  inessive='paperissa',
                                  inessive_plural='papereissa',
                                  elative='paperista',
                                  elative_plural='papereista',
                                  illative='paperiin',
                                  illatives_plural=['papereihin'],
                                  adessive='paperilla',
                                  adessive_plural='papereilla',
                                  ablative='paperilta',
                                  ablative_plural='papereilta',
                                  allative='paperille',
                                  allative_plural='papereille',
                                  essive='paperina',
                                  essive_plural='papereina',
                                  translative='paperiksi',
                                  translative_plural='papereiksi',
                                  abessive='paperitta',
                                  abessive_plural='papereitta',
                                  instructive_plural='paperein',
                                  comitative_plural='papereine')
        ensure_inflections_equal(expected, data)

    def test_with_end_consonant(self):
        data = kotus_noun_6_paperi("nylon")
        expected = InflectionInfo(nominative='nylon',
                                  nominative_plural='nylonit',
                                  genitive='nylonin',
                                  genitives_plural=['nylonien',
                                                    'nyloneiden',
                                                    'nyloneitten'],
                                  partitive='nylonia',
                                  partitives_plural=['nyloneita',
                                                     'nyloneja'],
                                  accusatives=['nylon',
                                               'nylonin'],
                                  accusative_plural='nylonit',
                                  inessive='nylonissa',
                                  inessive_plural='nyloneissa',
                                  elative='nylonista',
                                  elative_plural='nyloneista',
                                  illative='nyloniin',
                                  illatives_plural=['nyloneihin'],
                                  adessive='nylonilla',
                                  adessive_plural='nyloneilla',
                                  ablative='nylonilta',
                                  ablative_plural='nyloneilta',
                                  allative='nylonille',
                                  allative_plural='nyloneille',
                                  essive='nylonina',
                                  essive_plural='nyloneina',
                                  translative='nyloniksi',
                                  translative_plural='nyloneiksi',
                                  abessive='nylonitta',
                                  abessive_plural='nyloneitta',
                                  instructive_plural='nylonein',
                                  comitative_plural='nyloneine')
        ensure_inflections_equal(expected, data)

    def test_with_umlaut_inflections(self):
        data = kotus_noun_6_paperi("bensiini")
        expected = InflectionInfo(nominative='bensiini',
                                  nominative_plural='bensiinit',
                                  genitive='bensiinin',
                                  genitives_plural=['bensiinien',
                                                    'bensiineiden',
                                                    'bensiineitten'],
                                  partitive='bensiiniä',
                                  partitives_plural=['bensiineitä',
                                                     'bensiinejä'],
                                  accusatives=['bensiini',
                                               'bensiinin'],
                                  accusative_plural='bensiinit',
                                  inessive='bensiinissä',
                                  inessive_plural='bensiineissä',
                                  elative='bensiinistä',
                                  elative_plural='bensiineistä',
                                  illative='bensiiniin',
                                  illatives_plural=['bensiineihin'],
                                  adessive='bensiinillä',
                                  adessive_plural='bensiineillä',
                                  ablative='bensiiniltä',
                                  ablative_plural='bensiineiltä',
                                  allative='bensiinille',
                                  allative_plural='bensiineille',
                                  essive='bensiininä',
                                  essive_plural='bensiineinä',
                                  translative='bensiiniksi',
                                  translative_plural='bensiineiksi',
                                  abessive='bensiinittä',
                                  abessive_plural='bensiineittä',
                                  instructive_plural='bensiinein',
                                  comitative_plural='bensiineine')
        ensure_inflections_equal(expected, data)
