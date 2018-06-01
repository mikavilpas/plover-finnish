import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_j_hento_hennon_vanne_vanteen
from .kotus_noun_5_risti import kotus_noun_5_risti

class TestInflectionType5(unittest.TestCase):
    def test_kotus_noun_5_risti_full_cases(self):
        data = kotus_noun_5_risti("risti")
        expected = InflectionInfo(nominative='risti',
                                  nominative_plural='ristit',
                                  genitive='ristin',
                                  genitives_plural=['ristien'],
                                  partitives=['ristiä'],
                                  partitives_plural=['ristejä'],
                                  accusatives=['risti',
                                               'ristin'],
                                  accusative_plural='ristit',
                                  inessive='ristissä',
                                  inessives_plural=['risteissä'],
                                  elative='rististä',
                                  elatives_plural=['risteistä'],
                                  illative='ristiin',
                                  illatives_plural=['risteihin'],
                                  adessive='ristillä',
                                  adessives_plural=['risteillä'],
                                  ablative='ristiltä',
                                  ablatives_plural=['risteiltä'],
                                  allative='ristille',
                                  allatives_plural=['risteille'],
                                  essive='ristinä',
                                  essives_plural=['risteinä'],
                                  translative='ristiksi',
                                  translatives_plural=['risteiksi'],
                                  abessive='ristittä',
                                  abessives_plural=['risteittä'],
                                  instructives_plural=['ristein'],
                                  comitatives_plural=['risteine'])

        ensure_inflections_equal(expected, data)

    def test_kotus_noun_5_risti_umlauts_and_gradation(self):
        data = kotus_noun_5_risti("käpälöinti",
                                  gradate_kotus_j_hento_hennon_vanne_vanteen)
        expected = InflectionInfo(nominative="käpälöinti",
                                  nominative_plural="käpälöinnit",
                                  genitive="käpälöinnin",
                                  genitives_plural=["käpälöintien"],
                                  partitives=["käpälöintiä"],
                                  partitives_plural=["käpälöintejä"],
                                  accusatives=["käpälöinti",
                                               "käpälöinnin"],
                                  accusative_plural="käpälöinnit",
                                  inessive="käpälöinnissä",
                                  inessives_plural=["käpälöinneissä"],
                                  elative="käpälöinnistä",
                                  elatives_plural=["käpälöinneistä"],
                                  illative="käpälöintiin",
                                  illatives_plural=["käpälöinteihin"],
                                  adessive="käpälöinnillä",
                                  adessives_plural=["käpälöinneillä"],
                                  ablative="käpälöinniltä",
                                  ablatives_plural=["käpälöinneiltä"],
                                  allative="käpälöinnille",
                                  allatives_plural=["käpälöinneille"],
                                  essive="käpälöintinä",
                                  essives_plural=["käpälöinteinä"],
                                  translative="käpälöinniksi",
                                  translatives_plural=["käpälöinneiksi"],
                                  abessive="käpälöinnittä",
                                  abessives_plural=["käpälöinneittä"],
                                  instructives_plural=["käpälöinnein"],
                                  comitatives_plural=["käpälöinteine"])

        ensure_inflections_equal(expected, data)

    def test_with_word_ending_in_consonant(self):
        data = kotus_noun_5_risti("beat")
        expected = InflectionInfo(nominative='beat',
                                  nominative_plural='beatit',
                                  genitive='beatin',
                                  genitives_plural=['beatien'],
                                  partitives=['beata'],
                                  partitives_plural=['beateja'],
                                  accusatives=['beat',
                                               'beatin'],
                                  accusative_plural='beatit',
                                  inessive='beatissa',
                                  inessives_plural=['beateissa'],
                                  elative='beatista',
                                  elatives_plural=['beateista'],
                                  illative='beatin',
                                  illatives_plural=['beateihin'],
                                  adessive='beatilla',
                                  adessives_plural=['beateilla'],
                                  ablative='beatilta',
                                  ablatives_plural=['beateilta'],
                                  allative='beatille',
                                  allatives_plural=['beateille'],
                                  essive='beatina',
                                  essives_plural=['beateina'],
                                  translative='beatiksi',
                                  translatives_plural=['beateiksi'],
                                  abessive='beatitta',
                                  abessives_plural=['beateitta'],
                                  instructives_plural=['beatein'],
                                  comitatives_plural=['beateine'])

        ensure_inflections_equal(expected, data)
