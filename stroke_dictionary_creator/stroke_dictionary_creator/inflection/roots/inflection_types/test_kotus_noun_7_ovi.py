import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_e_sopu_sovun_taive_taipeen, gradate_kotus_f_satu_sadun_keidas_keitaan
from .kotus_noun_7_ovi import kotus_noun_7_ovi

class TestInflectionType7(unittest.TestCase):
    def test_basic_example(self):
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
                                  inessives_plural=["ovissa"],
                                  elative="ovesta",
                                  elatives_plural=["ovista"],
                                  illative="oveen",
                                  illatives_plural=["oviin"],
                                  adessive="ovella",
                                  adessives_plural=["ovilla"],
                                  ablative="ovelta",
                                  ablatives_plural=["ovilta"],
                                  allative="ovelle",
                                  allatives_plural=["oville"],
                                  essive="ovena",
                                  essives_plural=["ovina"],
                                  translative="oveksi",
                                  translatives_plural=["oviksi"],
                                  abessive="ovetta",
                                  abessives_plural=["ovitta"],
                                  instructives_plural=["ovin"],
                                  comitatives_plural=["ovine"])

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
                                  inessives_plural=["arvissa"],
                                  elative="arvesta",
                                  elatives_plural=["arvista"],
                                  illative="arpeen",
                                  illatives_plural=["arpiin"],
                                  adessive="arvella",
                                  adessives_plural=["arvilla"],
                                  ablative="arvelta",
                                  ablatives_plural=["arvilta"],
                                  allative="arvelle",
                                  allatives_plural=["arville"],
                                  essive="arpena",
                                  essives_plural=["arpina"],
                                  translative="arveksi",
                                  translatives_plural=["arviksi"],
                                  abessive="arvetta",
                                  abessives_plural=["arvitta"],
                                  instructives_plural=["arvin"],
                                  comitatives_plural=["arpine"])

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
                                  inessives_plural=['tähdissä'],
                                  elative='tähdestä',
                                  elatives_plural=['tähdistä'],
                                  illative='tähteen',
                                  illatives_plural=['tähtiin'],
                                  adessive='tähdellä',
                                  adessives_plural=['tähdillä'],
                                  ablative='tähdeltä',
                                  ablatives_plural=['tähdiltä'],
                                  allative='tähdelle',
                                  allatives_plural=['tähdille'],
                                  essive='tähtenä',
                                  essives_plural=['tähtinä'],
                                  translative='tähdeksi',
                                  translatives_plural=['tähdiksi'],
                                  abessive='tähdettä',
                                  abessives_plural=['tähdittä'],
                                  instructives_plural=['tähdin'],
                                  comitatives_plural=['tähtine'])

        ensure_inflections_equal(expected, data)

    # There are no singular words in this class that end in a consonant
