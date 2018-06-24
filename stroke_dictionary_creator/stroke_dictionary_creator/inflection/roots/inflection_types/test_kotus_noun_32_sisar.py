import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_32_sisar import kotus_noun_32_sisar

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_32_sisar("kämmen")

        expected = InflectionInfo(nominative='kämmen',
                                  nominative_plural='kämmenet',
                                  genitive='kämmenen',
                                  genitives_plural=['kämmenien'],
                                  partitives=['kämmentä'],
                                  partitives_plural=['kämmeniä'],
                                  accusatives=['kämmen',
                                               'kämmenen'],
                                  accusative_plural='kämmenet',
                                  inessive='kämmenessä',
                                  inessives_plural=['kämmenissä'],
                                  elative='kämmenestä',
                                  elatives_plural=['kämmenistä'],
                                  illatives=['kämmeneen'],
                                  illatives_plural=['kämmeniin'],
                                  adessive='kämmenellä',
                                  adessives_plural=['kämmenillä'],
                                  ablative='kämmeneltä',
                                  ablatives_plural=['kämmeniltä'],
                                  allative='kämmenelle',
                                  allatives_plural=['kämmenille'],
                                  essives=['kämmenenä'],
                                  essives_plural=['kämmeninä'],
                                  translative='kämmeneksi',
                                  translatives_plural=['kämmeniksi'],
                                  abessive='kämmenettä',
                                  abessives_plural=['kämmenittä'],
                                  instructives_plural=['kämmenin'],
                                  comitatives_plural=['kämmenine'])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):
        # tricky gradation class
        data = kotus_noun_32_sisar("ien",
                                   g.gradate_kotus_d_joukahainen_av6_aie_aikeen)

        expected = InflectionInfo(nominative='ien',
                                  nominative_plural='ikenet',
                                  genitive='ikenen',
                                  genitives_plural=['ienten',
                                                    'ikenien'],
                                  partitives=['ientä'],
                                  partitives_plural=['ikeniä'],
                                  accusatives=['ien',
                                               'ikenen'],
                                  accusative_plural='ikenet',
                                  inessive='ikenessä',
                                  inessives_plural=['ikenissä'],
                                  elative='ikenestä',
                                  elatives_plural=['ikenistä'],
                                  illatives=['ikeneen'],
                                  illatives_plural=['ikeniin'],
                                  adessive='ikenellä',
                                  adessives_plural=['ikenillä'],
                                  ablative='ikeneltä',
                                  ablatives_plural=['ikeniltä'],
                                  allative='ikenelle',
                                  allatives_plural=['ikenille'],
                                  essives=['ikenenä'],
                                  essives_plural=['ikeninä'],
                                  translative='ikeneksi',
                                  translatives_plural=['ikeniksi'],
                                  abessive='ikenettä',
                                  abessives_plural=['ikenittä'],
                                  instructives_plural=['ikenin'],
                                  comitatives_plural=['ikenine'])
