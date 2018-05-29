import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection.roots.root_word_service import *

class TestRootWordService(unittest.TestCase):
    def test_kotus_noun_1_valo_full_cases(self):
        data = kotus_noun_1_valo("aamu")

        ensure(data.nominative).equals("aamu")
        ensure(data.nominative_plural).equals("aamujen")

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
