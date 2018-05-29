import unittest
from ensure import ensure
from .gradation import *

class TestGradation(unittest.TestCase):
    def test_gradate_kotus_a_takki_takin_hake_hakkeen(self):
        gradate = gradate_kotus_a_takki_takin_hake_hakkeen
        ensure(gradate("takki")).equals("taki")
        ensure(gradate("hake")).equals("hakke")

    def test_gradate_kotus_b_kaappi_kaapin_opas_oppaan(self):
        gradate = gradate_kotus_b_kaappi_kaapin_opas_oppaan
        ensure(gradate("kaappi")).equals("kaapi")
        ensure(gradate("opas")).equals("oppas")

    def test_gradate_kotus_c_tyttö_tytön_kate_katteen(self):
        gradate = gradate_kotus_c_tyttö_tytön_kate_katteen
        ensure(gradate("tyttö")).equals("tytö")
        ensure(gradate("kate")).equals("katte")

    def test_gradate_kotus_e_sopu_sovun_taive_taipeen(self):
        gradate = gradate_kotus_e_sopu_sovun_taive_taipeen
        ensure(gradate("sopu")).equals("sovu")
        ensure(gradate("taive")).equals("taipe")

    def test_gradate_kotus_f_satu_sadun_keidas_keitaan(self):
        gradate = gradate_kotus_f_satu_sadun_keidas_keitaan
        ensure(gradate("satu")).equals("sadu")
        ensure(gradate("keidas")).equals("keitas")

    def test_gradate_kotus_g_aurinko_auringon_rengas_renkaan(self):
        gradate = gradate_kotus_g_aurinko_auringon_rengas_renkaan
        ensure(gradate("aurinko")).equals("auringo")
        ensure(gradate("rengas")).equals("renkas")

    def test_gradate_kotus_h_kumpi_kumman_lumme_lumpeen(self):
        gradate = gradate_kotus_h_kumpi_kumman_lumme_lumpeen
        ensure(gradate("kumpi")).equals("kummi")
        ensure(gradate("lumme")).equals("lumpe")

    def test_gradate_kotus_i_ilta_illan_sivellin_siveltimen(self):
        gradate = gradate_kotus_i_ilta_illan_sivellin_siveltimen
        ensure(gradate("ilta")).equals("illa")
        ensure(gradate("sivellin")).equals("siveltin")

    def test_gradate_kotus_j_hento_hennon_vanne_vanteen(self):
        gradate = gradate_kotus_j_hento_hennon_vanne_vanteen
        ensure(gradate("hento")).equals("henno")
        ensure(gradate("vanne")).equals("vante")

    def test_gradate_kotus_k_virta_virran_porras_portaan(self):
        gradate = gradate_kotus_k_virta_virran_porras_portaan
        ensure(gradate("virta")).equals("virra")
        ensure(gradate("porras")).equals("portas")

    def test_gradate_kotus_l_arki_arjen_hylje_hylkeen(self):
        gradate = gradate_kotus_l_arki_arjen_hylje_hylkeen
        ensure(gradate("arki")).equals("arji")
        ensure(gradate("hylje")).equals("hylke")

    def test_gradate_kotus_gradate_kotus_m_suku_suvun(self):
        gradate = gradate_kotus_m_suku_suvun
        ensure(gradate("suku")).equals("suvu")
        ensure(gradate).called_with("suvu").raises(Exception) # one way gradation
