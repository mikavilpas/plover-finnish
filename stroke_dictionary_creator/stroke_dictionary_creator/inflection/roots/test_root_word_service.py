import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection.roots.root_word_service import *

class TestRootWordService(unittest.TestCase):
    def test_kotus_noun_1_valo_full_cases(self):
        data = kotus_noun_1_valo("aamu")

        ensure(data.nominative).equals("aamu")
        ensure(data.nominative_plural).equals("aamut")

        ensure(data.genitive).equals("aamun")
        ensure(data.genitive_plural).equals("aamujen")

        ensure(data.partitive).equals("aamua")
        ensure(data.partitive_plural).equals("aamuja")

        ensure(data.accusatives).equals(["aamu", "aamun"])
        ensure(data.accusative_plural).equals("aamuja")

        ensure(data.inessive).equals("aamussa")
        ensure(data.inessive_plural).equals("aamuissa")

        ensure(data.elative).equals("aamusta")
        ensure(data.elative_plural).equals("aamuista")

        ensure(data.illative).equals("aamuun")
        ensure(data.illative_plural).equals("aamuihin")

        ensure(data.adessive).equals("aamulla")
        ensure(data.adessive_plural).equals("aamuilla")

        ensure(data.ablative).equals("aamulta")
        ensure(data.ablative_plural).equals("aamuilta")

        ensure(data.allative).equals("aamulle")
        ensure(data.allative_plural).equals("aamuille")

        ensure(data.essive).equals("aamuna")
        ensure(data.essive_plural).equals("aamuina")

        ensure(data.translative).equals("aamuksi")
        ensure(data.translative_plural).equals("aamuiksi")

        ensure(data.abessive).equals("aamutta")
        ensure(data.abessive_plural).equals("aamuitta")

        ensure(data.instructive_plural).equals("aamuin")

        ensure(data.comitative_plural).equals("aamuine")

    def test_kotus_noun_1_valo_umlauts(self):
        data = kotus_noun_1_valo("emännistö")
        ensure(data.abessive_plural).equals("emännistöittä")

        data = kotus_noun_1_valo("öljy")
        ensure(data.abessive_plural).equals("öljyittä")

    def test_gradate_kotus_i_ilta_illan_sivellin_siveltimen(self):
        gradate = gradate_kotus_i_ilta_illan_sivellin_siveltimen

        ensure(gradate("ilta")).equals("illa")
        ensure(gradate("sivellin")).equals("siveltin")

    def test_kotus_noun_1_valo_gradation(self):
        data = kotus_noun_1_valo("aalto",
                                 gradate_kotus_i_ilta_illan_sivellin_siveltimen)
        ensure(data.nominative_plural).equals("aallot")
        ensure(data.genitive).equals("aallon")
        ensure(data.genitive_plural).equals("aaltojen")


        data = kotus_noun_1_valo("sisältö",
                                 gradate_kotus_i_ilta_illan_sivellin_siveltimen)
        ensure(data.nominative_plural).equals("sisällöt")
        ensure(data.genitive).equals("sisällön")
        ensure(data.genitive_plural).equals("sisältöjen")
