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
                                  partitives=['laatikkoa'],
                                  partitives_plural=['laatikkoja',
                                                     'laatikoita'],
                                  accusatives=['laatikko',
                                               'laatikon'],
                                  accusative_plural='laatikot',
                                  inessive='laatikossa',
                                  inessives_plural=['laatikoissa'],
                                  elative='laatikosta',
                                  elatives_plural=['laatikoista'],
                                  illatives=['laatikkoon'],
                                  illatives_plural=['laatikkoihin',
                                                    'laatikoihin'],
                                  adessive='laatikolla',
                                  adessives_plural=['laatikoilla'],
                                  ablative='laatikolta',
                                  ablatives_plural=['laatikoilta'],
                                  allative='laatikolle',
                                  allatives_plural=['laatikoille'],
                                  essives=['laatikkona'],
                                  essives_plural=['laatikoina'],
                                  translative='laatikoksi',
                                  translatives_plural=['laatikoiksi'],
                                  abessive='laatikotta',
                                  abessives_plural=['laatikoitta'],
                                  instructives_plural=['laatikoin'],
                                  comitatives_plural=['laatikkoine'])
        ensure_inflections_equal(expected, data)

    def test_kotus_noun_4_laatikko_umlauts(self):
        data = kotus_noun_4_laatikko("älykkö", gradate_kotus_a_takki_takin_hake_hakkeen)
        ensure(data.genitives_plural).equals(["älyköiden", "älyköitten", "älykköjen"])
