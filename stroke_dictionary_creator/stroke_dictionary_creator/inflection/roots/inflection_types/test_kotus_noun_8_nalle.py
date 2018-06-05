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
                                  partitives=["nallea"],
                                  partitives_plural=["nalleja"],
                                  accusatives=["nalle",
                                               "nallen"],
                                  accusative_plural="nallet",
                                  inessive="nallessa",
                                  inessives_plural=["nalleissa"],
                                  elative="nallesta",
                                  elatives_plural=["nalleista"],
                                  illatives=["nalleen"],
                                  illatives_plural=["nalleihin"],
                                  adessive="nallella",
                                  adessives_plural=["nalleilla"],
                                  ablative="nallelta",
                                  ablatives_plural=["nalleilta"],
                                  allative="nallelle",
                                  allatives_plural=["nalleille"],
                                  essive="nallena",
                                  essives_plural=["nalleina"],
                                  translative="nalleksi",
                                  translatives_plural=["nalleiksi"],
                                  abessive="nalletta",
                                  abessives_plural=["nalleitta"],
                                  instructives_plural=["nallein"],
                                  comitatives_plural=["nalleine"])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_8_nalle("nukke",
                                  gradate_kotus_a_takki_takin_hake_hakkeen)

        expected = InflectionInfo(nominative='nukke',
                                  nominative_plural='nuket',
                                  genitive='nuken',
                                  genitives_plural=['nukkejen',
                                                    'nukkein'],
                                  partitives=['nukkea'],
                                  partitives_plural=['nukkeja'],
                                  accusatives=['nukke',
                                               'nuken'],
                                  accusative_plural='nuket',
                                  inessive='nukessa',
                                  inessives_plural=['nukeissa'],
                                  elative='nukesta',
                                  elatives_plural=['nukeista'],
                                  illatives=['nukkeen'],
                                  illatives_plural=['nukkeihin'],
                                  adessive='nukella',
                                  adessives_plural=['nukeilla'],
                                  ablative='nukelta',
                                  ablatives_plural=['nukeilta'],
                                  allative='nukelle',
                                  allatives_plural=['nukeille'],
                                  essive='nukkena',
                                  essives_plural=['nukkeina'],
                                  translative='nukeksi',
                                  translatives_plural=['nukeiksi'],
                                  abessive='nuketta',
                                  abessives_plural=['nukeitta'],
                                  instructives_plural=['nukein'],
                                  comitatives_plural=['nukkeine'])

        ensure_inflections_equal(expected, data)


    # could find no umlaut cases
    # could find no cases with a consonant in the end
