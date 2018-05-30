import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_a_takki_takin_hake_hakkeen
from .kotus_noun_8_nalle import kotus_noun_8_nalle

class TestInflectionType8(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_8_nalle("nalle")

        expected = InflectionInfo(nominative="nalle",
                                  nominative_plural="nallet",
                                  genitive="nallen",
                                  genitives_plural=["nallejen", "nallein"],
                                  partitive="nallea",
                                  partitives_plural=["nalleja"],
                                  accusatives=["nalle",
                                               "nallen"],
                                  accusative_plural="nallet",
                                  inessive="nallessa",
                                  inessive_plural="nalleissa",
                                  elative="nallesta",
                                  elative_plural="nalleista",
                                  illative="nalleen",
                                  illatives_plural=["nalleihin"],
                                  adessive="nallella",
                                  adessive_plural="nalleilla",
                                  ablative="nallelta",
                                  ablative_plural="nalleilta",
                                  allative="nallelle",
                                  allative_plural="nalleille",
                                  essive="nallena",
                                  essive_plural="nalleina",
                                  translative="nalleksi",
                                  translative_plural="nalleiksi",
                                  abessive="nalletta",
                                  abessive_plural="nalleitta",
                                  instructive_plural="nallein",
                                  comitative_plural="nalleine")

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_8_nalle("nukke",
                                  gradate_kotus_a_takki_takin_hake_hakkeen)

        expected = InflectionInfo(nominative='nukke',
                                  nominative_plural='nuket',
                                  genitive='nuken',
                                  genitives_plural=['nukkejen',
                                                    'nukkein'],
                                  partitive='nukkea',
                                  partitives_plural=['nukkeja'],
                                  accusatives=['nukke',
                                               'nuken'],
                                  accusative_plural='nuket',
                                  inessive='nukessa',
                                  inessive_plural='nukeissa',
                                  elative='nukesta',
                                  elative_plural='nukeista',
                                  illative='nukkeen',
                                  illatives_plural=['nukkeihin'],
                                  adessive='nukella',
                                  adessive_plural='nukeilla',
                                  ablative='nukelta',
                                  ablative_plural='nukeilta',
                                  allative='nukelle',
                                  allative_plural='nukeille',
                                  essive='nukkena',
                                  essive_plural='nukkeina',
                                  translative='nukeksi',
                                  translative_plural='nukeiksi',
                                  abessive='nuketta',
                                  abessive_plural='nukeitta',
                                  instructive_plural='nukein',
                                  comitative_plural='nukkeine')

        ensure_inflections_equal(expected, data)


    # could find no umlaut cases
    # could find no cases with a consonant in the end
