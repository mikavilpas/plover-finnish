import unittest
from ensure import ensure
from .kotus_noun_4_laatikko import *
from ..gradation import *

class TestInflectionType4(unittest.TestCase):
    # all the cases seem to belong to the gradation class A

    def test_kotus_noun_4_laatikko_full_cases(self):
        data = kotus_noun_4_laatikko("laatikko", gradate_kotus_a_takki_takin_hake_hakkeen)

        ensure(data.nominative).equals("laatikko")
        ensure(data.nominative_plural).equals("laatikot")

        ensure(data.genitive).equals("laatikon")
        ensure(data.genitives_plural).equals(["laatikoiden",
                                              "laatikoitten",
                                              "laatikkojen"])

        ensure(data.partitive).equals("laatikkoa")
        ensure(data.partitives_plural).equals(["laatikkoja", "laatikoita"])

        ensure(data.accusatives).equals(["laatikko", "laatikon"])
        ensure(data.accusative_plural).equals("laatikot")

        ensure(data.inessive).equals("laatikossa")
        ensure(data.inessive_plural).equals("laatikoissa")

        ensure(data.elative).equals("laatikosta")
        ensure(data.elative_plural).equals("laatikoista")

        ensure(data.illative).equals("laatikkoon")
        ensure(data.illatives_plural).equals(["laatikkoihin", "laatikoihin"])

        ensure(data.adessive).equals("laatikolla")
        ensure(data.adessive_plural).equals("laatikoilla")

        ensure(data.ablative).equals("laatikolta")
        ensure(data.ablative_plural).equals("laatikoilta")

        ensure(data.allative).equals("laatikolle")
        ensure(data.allative_plural).equals("laatikoille")

        ensure(data.essive).equals("laatikkona")
        ensure(data.essive_plural).equals("laatikoina")

        ensure(data.translative).equals("laatikoksi")
        ensure(data.translative_plural).equals("laatikoiksi")

        ensure(data.abessive).equals("laatikotta")
        ensure(data.abessive_plural).equals("laatikoitta")

        ensure(data.instructive_plural).equals("laatikoin")

        ensure(data.comitative_plural).equals("laatikkoine")

    def test_kotus_noun_4_laatikko_umlauts(self):
        data = kotus_noun_4_laatikko("älykkö", gradate_kotus_a_takki_takin_hake_hakkeen)
        ensure(data.genitives_plural).equals(["älyköiden", "älyköitten", "älykköjen"])
