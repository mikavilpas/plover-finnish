import unittest
from ensure import ensure
from .kotus_noun_1_valo import KotusNoun1Valo
from ..gradation import gradate_kotus_i_ilta_illan_sivellin_siveltimen
from .test_utils import ensure_inflections_equal
from ..noun_inflection_info import InflectionInfo

class TestInflectionType1(unittest.TestCase):
    def test_kotus_noun_1_valo_full_cases(self):
        data = KotusNoun1Valo("aamu").inflections()

        expected = InflectionInfo(nominative='aamu',
                                  nominative_plural='aamut',
                                  genitive='aamun',
                                  genitives_plural=['aamujen'],
                                  partitives=['aamua'],
                                  partitives_plural=['aamuja'],
                                  accusatives=['aamu',
                                               'aamun'],
                                  accusative_plural='aamut',
                                  inessive='aamussa',
                                  inessives_plural=['aamuissa'],
                                  elative='aamusta',
                                  elatives_plural=['aamuista'],
                                  illatives=['aamuun'],
                                  illatives_plural=['aamuihin'],
                                  adessive='aamulla',
                                  adessives_plural=['aamuilla'],
                                  ablative='aamulta',
                                  ablatives_plural=['aamuilta'],
                                  allative='aamulle',
                                  allatives_plural=['aamuille'],
                                  essive='aamuna',
                                  essives_plural=['aamuina'],
                                  translative='aamuksi',
                                  translatives_plural=['aamuiksi'],
                                  abessive='aamutta',
                                  abessives_plural=['aamuitta'],
                                  instructives_plural=['aamuin'],
                                  comitatives_plural=['aamuine'])

        ensure_inflections_equal(expected, data)

    def test_kotus_noun_1_valo_umlauts(self):
        data = KotusNoun1Valo("emännistö").inflections()
        ensure(data.abessives_plural).equals(["emännistöittä"])

        data = KotusNoun1Valo("öljy").inflections()
        ensure(data.abessives_plural).equals(["öljyittä"])

    def test_kotus_noun_1_valo_gradation(self):
        data = KotusNoun1Valo(
            "aalto",
            gradate_kotus_i_ilta_illan_sivellin_siveltimen).inflections()
        ensure(data.nominative_plural).equals("aallot")
        ensure(data.genitive).equals("aallon")
        ensure(data.genitives_plural).equals(["aaltojen"])


        data = KotusNoun1Valo(
            "sisältö",
            gradate_kotus_i_ilta_illan_sivellin_siveltimen).inflections()
        ensure(data.nominative_plural).equals("sisällöt")
        ensure(data.genitive).equals("sisällön")
        ensure(data.genitives_plural).equals(["sisältöjen"])
