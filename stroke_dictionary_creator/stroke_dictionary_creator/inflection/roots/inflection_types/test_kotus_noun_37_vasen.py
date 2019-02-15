import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_h_lumme_lumpeen
from .kotus_noun_37_vasen import kotus_noun_37_vasen

class TestInflection(unittest.TestCase):
    def test_basic_example(self):

        # special case: does not need gradation!

        data = kotus_noun_37_vasen("vasen")

        expected = InflectionInfo(nominative='vasen',
                                  nominative_plural='vasemmat',
                                  genitive='vasemman',
                                  genitives_plural=['vasempien',
                                                    'vasenten',
                                                    'vasempain'],
                                  partitives=['vasenta', 'vasempaa'],
                                  partitives_plural=['vasempia'],
                                  accusatives=['vasen',
                                               'vasemman'],
                                  accusative_plural='vasemmat',
                                  inessive='vasemmassa',
                                  inessives_plural=['vasemmmissa'],
                                  elative='vasemmasta',
                                  elatives_plural=['vasemmmista'],
                                  illatives=['vasempaan'],
                                  illatives_plural=['vasempiin'],
                                  adessive='vasemmalla',
                                  adessives_plural=['vasemmilla'],
                                  ablative='vasemmalta',
                                  ablatives_plural=['vasemmilta'],
                                  allative='vasemmalle',
                                  allatives_plural=['vasemmille'],
                                  essives=['vasempana'],
                                  essives_plural=['vasempina'],
                                  translative='vasemmaksi',
                                  translatives_plural=['vasemmiksi'],
                                  abessive='vasemmatta',
                                  abessives_plural=['vasemmitta'],
                                  instructives_plural=['vasemmin'],
                                  comitatives_plural=['vasempine'])


        ensure_inflections_equal(expected, data)

    # only one word in this class
