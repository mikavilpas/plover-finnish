import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön
from .kotus_noun_48_hame import kotus_noun_48_hame
from .. import gradation as g

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_48_hame("hame")

        expected = InflectionInfo(nominative='hame',
                                  nominative_plural='hameet',
                                  genitive='hameen',
                                  genitives_plural=['hameiden',
                                                    'hameitten'],
                                  partitives=['hametta'],
                                  partitives_plural=['hameita'],
                                  accusatives=['hame',
                                               'hameen'],
                                  accusative_plural='hameet',
                                  inessive='hameessa',
                                  inessives_plural=['hameissa'],
                                  elative='hameesta',
                                  elatives_plural=['hameista'],
                                  illatives=['hameeseen'],
                                  illatives_plural=['hameisiin',
                                                    'hameihin'],
                                  adessive='hameella',
                                  adessives_plural=['hameilla'],
                                  ablative='hameelta',
                                  ablatives_plural=['hameilta'],
                                  allative='hameelle',
                                  allatives_plural=['hameille'],
                                  essives=['hameena'],
                                  essives_plural=['hameina'],
                                  translative='hameeksi',
                                  translatives_plural=['hameiksi'],
                                  abessive='hameetta',
                                  abessives_plural=['hameitta'],
                                  instructives_plural=['hamein'],
                                  comitatives_plural=['hameine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_48_hame("eväste")

        expected = InflectionInfo(nominative='eväste',
                                  nominative_plural='evästeet',
                                  genitive='evästeen',
                                  genitives_plural=['evästeiden',
                                                    'evästeitten'],
                                  partitives=['evästettä'],
                                  partitives_plural=['evästeitä'],
                                  accusatives=['eväste',
                                               'evästeen'],
                                  accusative_plural='evästeet',
                                  inessive='evästeessä',
                                  inessives_plural=['evästeissä'],
                                  elative='evästeestä',
                                  elatives_plural=['evästeistä'],
                                  illatives=['evästeeseen'],
                                  illatives_plural=['evästeisiin',
                                                    'evästeihin'],
                                  adessive='evästeellä',
                                  adessives_plural=['evästeillä'],
                                  ablative='evästeeltä',
                                  ablatives_plural=['evästeiltä'],
                                  allative='evästeelle',
                                  allatives_plural=['evästeille'],
                                  essives=['evästeenä'],
                                  essives_plural=['evästeinä'],
                                  translative='evästeeksi',
                                  translatives_plural=['evästeiksi'],
                                  abessive='evästeettä',
                                  abessives_plural=['evästeittä'],
                                  instructives_plural=['evästein'],
                                  comitatives_plural=['evästeine'])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        data = kotus_noun_48_hame("pyyhe",
                                  g.gradate_kotus_d_joukahainen_av6_aie_aikeen)

        expected = InflectionInfo(nominative='pyyhe',
                                  nominative_plural='pyyhkeet',
                                  genitive='pyyhkeen',
                                  genitives_plural=['pyyhkeiden',
                                                    'pyyhkeitten'],
                                  partitives=['pyyhettä'],
                                  partitives_plural=['pyyhkeitä'],
                                  accusatives=['pyyhe',
                                               'pyyhkeen'],
                                  accusative_plural='pyyhkeet',
                                  inessive='pyyhkeessä',
                                  inessives_plural=['pyyhkeissä'],
                                  elative='pyyhkeestä',
                                  elatives_plural=['pyyhkeistä'],
                                  illatives=['pyyhkeeseen'],
                                  illatives_plural=['pyyhkeisiin',
                                                    'pyyhkeihin'],
                                  adessive='pyyhkeellä',
                                  adessives_plural=['pyyhkeillä'],
                                  ablative='pyyhkeeltä',
                                  ablatives_plural=['pyyhkeiltä'],
                                  allative='pyyhkeelle',
                                  allatives_plural=['pyyhkeille'],
                                  essives=['pyyhkeenä'],
                                  essives_plural=['pyyhkeinä'],
                                  translative='pyyhkeeksi',
                                  translatives_plural=['pyyhkeiksi'],
                                  abessive='pyyhkeettä',
                                  abessives_plural=['pyyhkeittä'],
                                  instructives_plural=['pyyhkein'],
                                  comitatives_plural=['pyyhkeine'])

        ensure_inflections_equal(expected, data)
