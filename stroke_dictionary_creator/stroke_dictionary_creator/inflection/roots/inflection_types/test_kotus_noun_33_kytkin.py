import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .. import gradation as g
from .kotus_noun_33_kytkin import kotus_noun_33_kytkin

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_33_kytkin("paahdin",
                                    g.gradate_kotus_f_keidas_keitaan)

        expected = InflectionInfo(nominative='paahdin',
                                  nominative_plural='paahtimet',
                                  genitive='paahtimen',
                                  genitives_plural=['paahtimien',
                                                    'paahdinten'],
                                  partitives=['paahdinta'],
                                  partitives_plural=['paahtimia'],
                                  accusatives=['paahdin',
                                               'paahtimen'],
                                  accusative_plural='paahtimet',
                                  inessive='paahtimessa',
                                  inessives_plural=['paahtimissa'],
                                  elative='paahtimesta',
                                  elatives_plural=['paahtimista'],
                                  illatives=['paahtimeen'],
                                  illatives_plural=['paahtimiin'],
                                  adessive='paahtimella',
                                  adessives_plural=['paahtimilla'],
                                  ablative='paahtimelta',
                                  ablatives_plural=['paahtimilta'],
                                  allative='paahtimelle',
                                  allatives_plural=['paahtimille'],
                                  essives=['paahtimena'],
                                  essives_plural=['paahtimina'],
                                  translative='paahtimeksi',
                                  translatives_plural=['paahtimiksi'],
                                  abessive='paahtimetta',
                                  abessives_plural=['paahtimitta'],
                                  instructives_plural=['paahtimin'],
                                  comitatives_plural=['paahtimine'])

        ensure_inflections_equal(expected, data)

    def test_basic_example_no_gradation(self):
        data = kotus_noun_33_kytkin("eläin")

        expected = InflectionInfo(nominative='eläin',
                                  nominative_plural='eläimet',
                                  genitive='eläimen',
                                  genitives_plural=['eläimien',
                                                    'eläinten'],
                                  partitives=['eläintä'],
                                  partitives_plural=['eläimiä'],
                                  accusatives=['eläin',
                                               'eläimen'],
                                  accusative_plural='eläimet',
                                  inessive='eläimessä',
                                  inessives_plural=['eläimissä'],
                                  elative='eläimestä',
                                  elatives_plural=['eläimistä'],
                                  illatives=['eläimeen'],
                                  illatives_plural=['eläimiin'],
                                  adessive='eläimellä',
                                  adessives_plural=['eläimillä'],
                                  ablative='eläimeltä',
                                  ablatives_plural=['eläimiltä'],
                                  allative='eläimelle',
                                  allatives_plural=['eläimille'],
                                  essives=['eläimenä'],
                                  essives_plural=['eläiminä'],
                                  translative='eläimeksi',
                                  translatives_plural=['eläimiksi'],
                                  abessive='eläimettä',
                                  abessives_plural=['eläimittä'],
                                  instructives_plural=['eläimin'],
                                  comitatives_plural=['eläimine'])

        ensure_inflections_equal(expected, data)

    def test_basic_example_other_gradation(self):
        data = kotus_noun_33_kytkin("hiekoitin",
                                    g.gradate_kotus_c_kate_katteen)

        expected = InflectionInfo(nominative='hiekoitin',
                                  nominative_plural='hiekoittimet',
                                  genitive='hiekoittimen',
                                  genitives_plural=['hiekoittimien',
                                                    'hiekoitinten'],
                                  partitives=['hiekoitinta'],
                                  partitives_plural=['hiekoittimia'],
                                  accusatives=['hiekoitin',
                                               'hiekoittimen'],
                                  accusative_plural='hiekoittimet',
                                  inessive='hiekoittimessa',
                                  inessives_plural=['hiekoittimissa'],
                                  elative='hiekoittimesta',
                                  elatives_plural=['hiekoittimista'],
                                  illatives=['hiekoittimeen'],
                                  illatives_plural=['hiekoittimiin'],
                                  adessive='hiekoittimella',
                                  adessives_plural=['hiekoittimilla'],
                                  ablative='hiekoittimelta',
                                  ablatives_plural=['hiekoittimilta'],
                                  allative='hiekoittimelle',
                                  allatives_plural=['hiekoittimille'],
                                  essives=['hiekoittimena'],
                                  essives_plural=['hiekoittimina'],
                                  translative='hiekoittimeksi',
                                  translatives_plural=['hiekoittimiksi'],
                                  abessive='hiekoittimetta',
                                  abessives_plural=['hiekoittimitta'],
                                  instructives_plural=['hiekoittimin'],
                                  comitatives_plural=['hiekoittimine'])


        ensure_inflections_equal(expected, data)
