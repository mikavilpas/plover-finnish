import unittest


from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön
from .kotus_noun_40_kalleus import kotus_noun_40_kalleus

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_40_kalleus("etuus")

        expected = InflectionInfo(nominative='etuus',
                                  nominative_plural='etuudet',
                                  genitive='etuuden',
                                  genitives_plural=['etuuksien'],
                                  partitives=['etuutta'],
                                  partitives_plural=['etuuksia'],
                                  accusatives=['etuus', 'etuuden'],
                                  accusative_plural='etuudet',
                                  inessive='etuudessa',
                                  inessives_plural=['etuuksissa'],
                                  elative='etuudesta',
                                  elatives_plural=['etuuksista'],
                                  illatives=['etuuteen'],
                                  illatives_plural=['etuuksiin'],
                                  adessive='etuudella',
                                  adessives_plural=['etuuksilla'],
                                  ablative='etuudelta',
                                  ablatives_plural=['etuuksilta'],
                                  allative='etuudelle',
                                  allatives_plural=['etuuksille'],
                                  essives=['etuutena'],
                                  essives_plural=['etuuksina'],
                                  translative='etuudeksi',
                                  translatives_plural=['etuuksiksi'],
                                  abessive='etuudetta',
                                  abessives_plural=['etuuksitta'],
                                  instructives_plural=['etuuksin'],
                                  comitatives_plural=['etuuksine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_40_kalleus("henkilöys")

        expected = InflectionInfo(nominative          = 'henkilöys',
                                  nominative_plural   = 'henkilöydet',
                                  genitive            = 'henkilöyden',
                                  genitives_plural    = ['henkilöyksien'],
                                  partitives          = ['henkilöyttä'],
                                  partitives_plural   = ['henkilöyksiä'],
                                  accusatives         = ['henkilöys',
                                                         'henkilöyden'],
                                  accusative_plural   = 'henkilöydet',
                                  inessive            = 'henkilöydessä',
                                  inessives_plural    = ['henkilöyksissä'],
                                  elative             = 'henkilöydestä',
                                  elatives_plural     = ['henkilöyksistä'],
                                  illatives           = ['henkilöyteen'],
                                  illatives_plural    = ['henkilöyksiin'],
                                  adessive            = 'henkilöydellä',
                                  adessives_plural    = ['henkilöyksillä'],
                                  ablative            = 'henkilöydeltä',
                                  ablatives_plural    = ['henkilöyksiltä'],
                                  allative            = 'henkilöydelle',
                                  allatives_plural    = ['henkilöyksille'],
                                  essives             = ['henkilöytenä'],
                                  essives_plural      = ['henkilöyksinä'],
                                  translative         = 'henkilöydeksi',
                                  translatives_plural = ['henkilöyksiksi'],
                                  abessive            = 'henkilöydettä',
                                  abessives_plural    = ['henkilöyksittä'],
                                  instructives_plural = ['henkilöyksin'],
                                  comitatives_plural  = ['henkilöyksine'])

        ensure_inflections_equal(expected, data)

    # all words use no gradation
