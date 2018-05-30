import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_e_sopu_sovun_taive_taipeen, gradate_kotus_f_satu_sadun_keidas_keitaan
from .kotus_noun_7_ovi import kotus_noun_7_ovi

class TestInflectionType7(unittest.TestCase):
    def test_kotus_noun_6_ove_full_cases(self):
        data = kotus_noun_7_ovi("ovi")

        expected = InflectionInfo(nominative="ovi",
                                  nominative_plural="ovet",
                                  genitive="oven",
                                  genitives_plural=["ovien"],
                                  partitive="ovea",
                                  partitives_plural=["ovia"],
                                  accusatives=["ovi",
                                               "oven"],
                                  accusative_plural="ovet",
                                  inessive="ovessa",
                                  inessive_plural="ovissa",
                                  elative="ovesta",
                                  elative_plural="ovista",
                                  illative="oveen",
                                  illatives_plural=["oviin"],
                                  adessive="ovella",
                                  adessive_plural="ovilla",
                                  ablative="ovelta",
                                  ablative_plural="ovilta",
                                  allative="ovelle",
                                  allative_plural="oville",
                                  essive="ovena",
                                  essive_plural="ovina",
                                  translative="oveksi",
                                  translative_plural="oviksi",
                                  abessive="ovetta",
                                  abessive_plural="ovitta",
                                  instructive_plural="ovin",
                                  comitative_plural="ovine")

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_7_ovi("arpi",
                                gradate_kotus_e_sopu_sovun_taive_taipeen)

        expected = InflectionInfo(nominative="arpi",
                                  nominative_plural="arvet",
                                  genitive="arven",
                                  genitives_plural=["arpien"],
                                  partitive="arpea",
                                  partitives_plural=["arpia"],
                                  accusatives=["arpi",
                                               "arven"],
                                  accusative_plural="arvet",
                                  inessive="arvessa",
                                  inessive_plural="arvissa",
                                  elative="arvesta",
                                  elative_plural="arvista",
                                  illative="arpeen",
                                  illatives_plural=["arpiin"],
                                  adessive="arvella",
                                  adessive_plural="arvilla",
                                  ablative="arvelta",
                                  ablative_plural="arvilta",
                                  allative="arvelle",
                                  allative_plural="arville",
                                  essive="arpena",
                                  essive_plural="arpina",
                                  translative="arveksi",
                                  translative_plural="arviksi",
                                  abessive="arvetta",
                                  abessive_plural="arvitta",
                                  instructive_plural="arvin",
                                  comitative_plural="arpine")

        ensure_inflections_equal(expected, data)


    def test_with_umlaut_gradation(self):
        data = kotus_noun_7_ovi("tähti",
                                gradate_kotus_f_satu_sadun_keidas_keitaan)

        expected = InflectionInfo(nominative='tähti',
                                  nominative_plural='tähdet',
                                  genitive='tähden',
                                  genitives_plural=['tähtien'],
                                  partitive='tähteä',
                                  partitives_plural=['tähtiä'],
                                  accusatives=['tähti',
                                               'tähden'],
                                  accusative_plural='tähdet',
                                  inessive='tähdessä',
                                  inessive_plural='tähdissä',
                                  elative='tähdestä',
                                  elative_plural='tähdistä',
                                  illative='tähteen',
                                  illatives_plural=['tähtiin'],
                                  adessive='tähdellä',
                                  adessive_plural='tähdillä',
                                  ablative='tähdeltä',
                                  ablative_plural='tähdiltä',
                                  allative='tähdelle',
                                  allative_plural='tähdille',
                                  essive='tähtenä',
                                  essive_plural='tähtinä',
                                  translative='tähdeksi',
                                  translative_plural='tähdiksi',
                                  abessive='tähdettä',
                                  abessive_plural='tähdittä',
                                  instructive_plural='tähdin',
                                  comitative_plural='tähtine')

        ensure_inflections_equal(expected, data)

    # There are no singular words in this class that end in a consonant
