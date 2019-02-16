import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_41_vieras import kotus_noun_41_vieras

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_41_vieras("kirves")

        expected = InflectionInfo(nominative='kirves',
                                  nominative_plural='kirveet',
                                  genitive='kirveen',
                                  genitives_plural=['kirveiden',
                                                    'kirveitten'],
                                  partitives=['kirvestä'],
                                  partitives_plural=['kirveitä'],
                                  accusatives=['kirves',
                                               'kirveen'],
                                  accusative_plural='kirveet',
                                  inessive='kirveessä',
                                  inessives_plural=['kirveissä'],
                                  elative='kirveestä',
                                  elatives_plural=['kirveistä'],
                                  illatives=['kirveeseen'],
                                  illatives_plural=['kirveisiin',
                                                    'kirveihin'],
                                  adessive='kirveellä',
                                  adessives_plural=['kirveillä'],
                                  ablative='kirveeltä',
                                  ablatives_plural=['kirveiltä'],
                                  allative='kirveelle',
                                  allatives_plural=['kirveille'],
                                  essives=['kirveenä'],
                                  essives_plural=['kirveinä'],
                                  translative='kirveeksi',
                                  translatives_plural=['kirveiksi'],
                                  abessive='kirveettä',
                                  abessives_plural=['kirveittä'],
                                  instructives_plural=['kirvein'],
                                  comitatives_plural=['kirveine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_41_vieras("eväs")

        expected = InflectionInfo(nominative='eväs',
                                  nominative_plural='eväät',
                                  genitive='evään',
                                  genitives_plural=['eväiden',
                                                    'eväitten'],
                                  partitives=['evästä'],
                                  partitives_plural=['eväitä'],
                                  accusatives=['eväs',
                                               'evään'],
                                  accusative_plural='eväät',
                                  inessive='eväässä',
                                  inessives_plural=['eväissä'],
                                  elative='eväästä',
                                  elatives_plural=['eväistä'],
                                  illatives=['evääseen'],
                                  illatives_plural=['eväisiin',
                                                    'eväihin'],
                                  adessive='eväällä',
                                  adessives_plural=['eväillä'],
                                  ablative='eväältä',
                                  ablatives_plural=['eväiltä'],
                                  allative='eväälle',
                                  allatives_plural=['eväille'],
                                  essives=['eväänä'],
                                  essives_plural=['eväinä'],
                                  translative='evääksi',
                                  translatives_plural=['eväiksi'],
                                  abessive='eväättä',
                                  abessives_plural=['eväittä'],
                                  instructives_plural=['eväin'],
                                  comitatives_plural=['eväine'])

        ensure_inflections_equal(expected, data)

    def test_gradation(self):

        data = kotus_noun_41_vieras("ies",
                                    g.gradate_kotus_d_joukahainen_av6_aie_aikeen)

        expected = InflectionInfo(nominative='ies',
                                  nominative_plural='ikeet',
                                  genitive='ikeen',
                                  genitives_plural=['ikeiden',
                                                    'ikeitten'],
                                  partitives=['iestä'],
                                  partitives_plural=['ikeitä'],
                                  accusatives=['ies',
                                               'ikeen'],
                                  accusative_plural='ikeet',
                                  inessive='ikeessä',
                                  inessives_plural=['ikeissä'],
                                  elative='ikeestä',
                                  elatives_plural=['ikeistä'],
                                  illatives=['ikeeseen'],
                                  illatives_plural=['ikeisiin',
                                                    'ikeihin'],
                                  adessive='ikeellä',
                                  adessives_plural=['ikeillä'],
                                  ablative='ikeeltä',
                                  ablatives_plural=['ikeiltä'],
                                  allative='ikeelle',
                                  allatives_plural=['ikeille'],
                                  essives=['ikeenä'],
                                  essives_plural=['ikeinä'],
                                  translative='ikeeksi',
                                  translatives_plural=['ikeiksi'],
                                  abessive='ikeettä',
                                  abessives_plural=['ikeittä'],
                                  instructives_plural=['ikein'],
                                  comitatives_plural=['ikeine'])

        ensure_inflections_equal(expected, data)
