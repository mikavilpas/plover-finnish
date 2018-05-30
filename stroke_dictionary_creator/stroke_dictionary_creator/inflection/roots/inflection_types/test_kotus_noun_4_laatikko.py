import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_a_takki_takin_hake_hakkeen
from .kotus_noun_4_laatikko import kotus_noun_4_laatikko

class TestInflectionType4(unittest.TestCase):
    # all the cases seem to belong to the gradation class A

    def test_kotus_noun_4_laatikko_full_cases(self):
        data = kotus_noun_4_laatikko("laatikko", gradate_kotus_a_takki_takin_hake_hakkeen)
        expected = InflectionInfo(nominative='laatikko',
                                  nominative_plural='laatikot',
                                  genitive='laatikon',
                                  genitives_plural=['laatikoiden',
                                                    'laatikoitten',
                                                    'laatikkojen'],
                                  partitive='laatikkoa',
                                  partitives_plural=['laatikkoja',
                                                     'laatikoita'],
                                  accusatives=['laatikko',
                                               'laatikon'],
                                  accusative_plural='laatikot',
                                  inessive='laatikossa',
                                  inessive_plural='laatikoissa',
                                  elative='laatikosta',
                                  elative_plural='laatikoista',
                                  illative='laatikkoon',
                                  illatives_plural=['laatikkoihin',
                                                    'laatikoihin'],
                                  adessive='laatikolla',
                                  adessive_plural='laatikoilla',
                                  ablative='laatikolta',
                                  ablative_plural='laatikoilta',
                                  allative='laatikolle',
                                  allative_plural='laatikoille',
                                  essive='laatikkona',
                                  essive_plural='laatikoina',
                                  translative='laatikoksi',
                                  translative_plural='laatikoiksi',
                                  abessive='laatikotta',
                                  abessive_plural='laatikoitta',
                                  instructive_plural='laatikoin',
                                  comitative_plural='laatikkoine')
        ensure_inflections_equal(expected, data)

    def test_kotus_noun_4_laatikko_umlauts(self):
        data = kotus_noun_4_laatikko("älykkö", gradate_kotus_a_takki_takin_hake_hakkeen)
        ensure(data.genitives_plural).equals(["älyköiden", "älyköitten", "älykköjen"])
