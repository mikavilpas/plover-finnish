import unittest
from ensure import ensure
from .kotus_noun_2_palvelu import KotusNoun2Palvelu
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal

class TestInflectionType2(unittest.TestCase):
    def test_kotus_noun_2_palvelu_full_cases(self):
        data = KotusNoun2Palvelu("palvelu").inflections()
        expected = InflectionInfo(nominative='palvelu',
                                  nominative_plural='palvelut',
                                  genitive='palvelun',
                                  genitives_plural=['palvelujen',
                                                    'palveluiden',
                                                    'palveluitten'],
                                  partitives=['palvelua'],
                                  partitives_plural=['palveluita',
                                                     'palveluja'],
                                  accusatives=['palvelu',
                                               'palvelun'],
                                  accusative_plural='palvelut',
                                  inessive='palvelussa',
                                  inessives_plural=['palveluissa'],
                                  elative='palvelusta',
                                  elatives_plural=['palveluista'],
                                  illatives=['palveluun'],
                                  illatives_plural=['palveluihin'],
                                  adessive='palvelulla',
                                  adessives_plural=['palveluilla'],
                                  ablative='palvelulta',
                                  ablatives_plural=['palveluilta'],
                                  allative='palvelulle',
                                  allatives_plural=['palveluille'],
                                  essive='palveluna',
                                  essives_plural=['palveluina'],
                                  translative='palveluksi',
                                  translatives_plural=['palveluiksi'],
                                  abessive='palvelutta',
                                  abessives_plural=['palveluitta'],
                                  instructives_plural=['palveluin'],
                                  comitatives_plural=['palveluine'])
        ensure_inflections_equal(expected, data)

    def test_kotus_noun_2_palvelu_umlauts(self):
        data = KotusNoun2Palvelu("epäily").inflections()
        ensure(data.comitatives_plural).equals(["epäilyine"])

    # The kotus wordlist does not contain any words that belong to class 2 and
    # have a gradation class. Have to skip testing that.
