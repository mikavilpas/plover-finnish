import unittest
from ensure import ensure
from .kotus_noun_1_valo import kotus_noun_1_valo
from ..gradation import gradate_kotus_i_ilta_illan_sivellin_siveltimen
from .test_utils import ensure_inflections_equal
from ..noun_inflection_info import InflectionInfo

class TestInflectionType1(unittest.TestCase):
    def test_kotus_noun_1_valo_full_cases(self):
        data = kotus_noun_1_valo("aamu")

        expected = InflectionInfo(nominative='aamu',
                                  nominative_plural='aamut',
                                  genitive='aamun',
                                  genitives_plural=['aamujen'],
                                  partitive='aamua',
                                  partitives_plural=['aamuja'],
                                  accusatives=['aamu',
                                               'aamun'],
                                  accusative_plural='aamuja',
                                  inessive='aamussa',
                                  inessive_plural='aamuissa',
                                  elative='aamusta',
                                  elative_plural='aamuista',
                                  illative='aamuun',
                                  illatives_plural=['aamuihin'],
                                  adessive='aamulla',
                                  adessive_plural='aamuilla',
                                  ablative='aamulta',
                                  ablative_plural='aamuilta',
                                  allative='aamulle',
                                  allative_plural='aamuille',
                                  essive='aamuna',
                                  essive_plural='aamuina',
                                  translative='aamuksi',
                                  translative_plural='aamuiksi',
                                  abessive='aamutta',
                                  abessive_plural='aamuitta',
                                  instructive_plural='aamuin',
                                  comitative_plural='aamuine')
        ensure_inflections_equal(expected, data)

    def test_kotus_noun_1_valo_umlauts(self):
        data = kotus_noun_1_valo("emännistö")
        ensure(data.abessive_plural).equals("emännistöittä")

        data = kotus_noun_1_valo("öljy")
        ensure(data.abessive_plural).equals("öljyittä")

    def test_kotus_noun_1_valo_gradation(self):
        data = kotus_noun_1_valo("aalto",
                                 gradate_kotus_i_ilta_illan_sivellin_siveltimen)
        ensure(data.nominative_plural).equals("aallot")
        ensure(data.genitive).equals("aallon")
        ensure(data.genitives_plural).equals(["aaltojen"])


        data = kotus_noun_1_valo("sisältö",
                                 gradate_kotus_i_ilta_illan_sivellin_siveltimen)
        ensure(data.nominative_plural).equals("sisällöt")
        ensure(data.genitive).equals("sisällön")
        ensure(data.genitives_plural).equals(["sisältöjen"])
