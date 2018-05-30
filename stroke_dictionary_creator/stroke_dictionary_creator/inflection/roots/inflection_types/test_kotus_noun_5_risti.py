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
                                  partitive='ristiä',
                                  partitives_plural=['ristejä'],
                                  accusatives=['risti',
                                               'ristin'],
                                  accusative_plural='ristit',
                                  inessive='ristissä',
                                  inessive_plural='risteissä',
                                  elative='rististä',
                                  elative_plural='risteistä',
                                  illative='ristiin',
                                  illatives_plural=['risteihin'],
                                  adessive='ristillä',
                                  adessive_plural='risteillä',
                                  ablative='ristiltä',
                                  ablative_plural='risteiltä',
                                  allative='ristille',
                                  allative_plural='risteille',
                                  essive='ristinä',
                                  essive_plural='risteinä',
                                  translative='ristiksi',
                                  translative_plural='risteiksi',
                                  abessive='ristittä',
                                  abessive_plural='risteittä',
                                  instructive_plural='ristein',
                                  comitative_plural='risteine')

        ensure_inflections_equal(expected, data)

    def test_kotus_noun_5_risti_umlauts_and_gradation(self):
        data = kotus_noun_5_risti("käpälöinti",
                                  gradate_kotus_j_hento_hennon_vanne_vanteen)
        expected = InflectionInfo(nominative="käpälöinti",
                                  nominative_plural="käpälöinnit",
                                  genitive="käpälöinnin",
                                  genitives_plural=["käpälöintien"],
                                  partitive="käpälöintiä",
                                  partitives_plural=["käpälöintejä"],
                                  accusatives=["käpälöinti",
                                               "käpälöinnin"],
                                  accusative_plural="käpälöinnit",
                                  inessive="käpälöinnissä",
                                  inessive_plural="käpälöinneissä",
                                  elative="käpälöinnistä",
                                  elative_plural="käpälöinneistä",
                                  illative="käpälöintiin",
                                  illatives_plural=["käpälöinteihin"],
                                  adessive="käpälöinnillä",
                                  adessive_plural="käpälöinneillä",
                                  ablative="käpälöinniltä",
                                  ablative_plural="käpälöinneiltä",
                                  allative="käpälöinnille",
                                  allative_plural="käpälöinneille",
                                  essive="käpälöintinä",
                                  essive_plural="käpälöinteinä",
                                  translative="käpälöinniksi",
                                  translative_plural="käpälöinneiksi",
                                  abessive="käpälöinnittä",
                                  abessive_plural="käpälöinneittä",
                                  instructive_plural="käpälöinnein",
                                  comitative_plural="käpälöinteine")

        ensure_inflections_equal(expected, data)

    def test_with_word_ending_in_consonant(self):
        data = kotus_noun_5_risti("beat")
        expected = InflectionInfo(nominative='beat',
                                  nominative_plural='beatit',
                                  genitive='beatin',
                                  genitives_plural=['beatien'],
                                  partitive='beata',
                                  partitives_plural=['beateja'],
                                  accusatives=['beat',
                                               'beatin'],
                                  accusative_plural='beatit',
                                  inessive='beatissa',
                                  inessive_plural='beateissa',
                                  elative='beatista',
                                  elative_plural='beateista',
                                  illative='beatin',
                                  illatives_plural=['beateihin'],
                                  adessive='beatilla',
                                  adessive_plural='beateilla',
                                  ablative='beatilta',
                                  ablative_plural='beateilta',
                                  allative='beatille',
                                  allative_plural='beateille',
                                  essive='beatina',
                                  essive_plural='beateina',
                                  translative='beatiksi',
                                  translative_plural='beateiksi',
                                  abessive='beatitta',
                                  abessive_plural='beateitta',
                                  instructive_plural='beatein',
                                  comitative_plural='beateine')

        ensure_inflections_equal(expected, data)
