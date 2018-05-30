import unittest
from ensure import ensure
from .kotus_noun_2_palvelu import kotus_noun_2_palvelu
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal

class TestInflectionType2(unittest.TestCase):
    def test_kotus_noun_2_palvelu_full_cases(self):
        data = kotus_noun_2_palvelu("palvelu")
        print(data)
        expected = InflectionInfo(nominative='palvelu',
                                  nominative_plural='palvelut',
                                  genitive='palvelun',
                                  genitives_plural=['palvelujen',
                                                    'palveluiden',
                                                    'palveluitten'],
                                  partitive='palvelua',
                                  partitives_plural=['palveluita',
                                                     'palveluja'],
                                  accusatives=['palvelu',
                                               'palvelun'],
                                  accusative_plural='palvelut',
                                  inessive='palvelussa',
                                  inessive_plural='palveluissa',
                                  elative='palvelusta',
                                  elative_plural='palveluista',
                                  illative='palveluun',
                                  illatives_plural=['palveluihin'],
                                  adessive='palvelulla',
                                  adessive_plural='palveluilla',
                                  ablative='palvelulta',
                                  ablative_plural='palveluilta',
                                  allative='palvelulle',
                                  allative_plural='palveluille',
                                  essive='palveluna',
                                  essive_plural='palveluina',
                                  translative='palveluksi',
                                  translative_plural='palveluiksi',
                                  abessive='palvelutta',
                                  abessive_plural='palveluitta',
                                  instructive_plural='palveluin',
                                  comitative_plural='palveluine')
        ensure_inflections_equal(expected, data)

    def test_kotus_noun_2_palvelu_umlauts(self):
        data = kotus_noun_2_palvelu("epäily")
        ensure(data.comitative_plural).equals("epäilyine")

    # The kotus wordlist does not contain any words that belong to class 2 and
    # have a gradation class. Have to skip testing that.
