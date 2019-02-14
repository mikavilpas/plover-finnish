import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_lumme_lumpeen
from .kotus_noun_36_sisin import kotus_noun_36_sisin

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_36_sisin("sisin",
                                   gradate_kotus_h_lumme_lumpeen)

        expected = InflectionInfo(nominative='sisin',
                                  nominative_plural='sisimmät',
                                  genitive='sisimmän',
                                  genitives_plural=['sisimpien',
                                                    'sisinten',
                                                    'sisimpäin'],
                                  partitives=['sisintä'],
                                  partitives_plural=['sisimpiä'],
                                  accusatives=['sisin',
                                               'sisimmän'],
                                  accusative_plural='sisimmät',
                                  inessive='sisimmässä',
                                  inessives_plural=['sisimmmissä'],
                                  elative='sisimmästä',
                                  elatives_plural=['sisimmmistä'],
                                  illatives=['sisimpään'],
                                  illatives_plural=['sisimpiin'],
                                  adessive='sisimmällä',
                                  adessives_plural=['sisimmillä'],
                                  ablative='sisimmältä',
                                  ablatives_plural=['sisimmiltä'],
                                  allative='sisimmälle',
                                  allatives_plural=['sisimmille'],
                                  essives=['sisimpänä'],
                                  essives_plural=['sisimpinä'],
                                  translative='sisimmäksi',
                                  translatives_plural=['sisimmiksi'],
                                  abessive='sisimmättä',
                                  abessives_plural=['sisimmittä'],
                                  instructives_plural=['sisimmin'],
                                  comitatives_plural=['sisimpine'])


        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_36_sisin("pahin")

        expected = InflectionInfo(nominative='pahin',
                                  nominative_plural='pahimmat',
                                  genitive='pahimman',
                                  genitives_plural=['pahimpien',
                                                    'pahinten',
                                                    'pahimpain'],
                                  partitives=['pahinta'],
                                  partitives_plural=['pahimpia'],
                                  accusatives=['pahin',
                                               'pahimman'],
                                  accusative_plural='pahimmat',
                                  inessive='pahimmassa',
                                  inessives_plural=['pahimmmissa'],
                                  elative='pahimmasta',
                                  elatives_plural=['pahimmmista'],
                                  illatives=['pahimpaan'],
                                  illatives_plural=['pahimpiin'],
                                  adessive='pahimmalla',
                                  adessives_plural=['pahimmilla'],
                                  ablative='pahimmalta',
                                  ablatives_plural=['pahimmilta'],
                                  allative='pahimmalle',
                                  allatives_plural=['pahimmille'],
                                  essives=['pahimpana'],
                                  essives_plural=['pahimpina'],
                                  translative='pahimmaksi',
                                  translatives_plural=['pahimmiksi'],
                                  abessive='pahimmatta',
                                  abessives_plural=['pahimmitta'],
                                  instructives_plural=['pahimmin'],
                                  comitatives_plural=['pahimpine'])


        ensure_inflections_equal(expected, data)

    # no gradation in this class
