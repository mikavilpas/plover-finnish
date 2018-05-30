import unittest
from ensure import ensure
from .kotus_noun_2_palvelu import *
from ..gradation import *

class TestInflectionType2(unittest.TestCase):
    def test_kotus_noun_2_palvelu_full_cases(self):
        data = kotus_noun_2_palvelu("palvelu")

        ensure(data.nominative).equals("palvelu")
        ensure(data.nominative_plural).equals("palvelut")

        ensure(data.genitive).equals("palvelun")
        ensure(data.genitives_plural).equals(["palvelujen",
                                              "palveluiden",
                                              "palveluitten"])

        ensure(data.partitive).equals("palvelua")
        ensure(data.partitives_plural).equals(["palveluita",
                                               "palveluja"])

        ensure(data.accusatives).equals(["palvelu", "palvelun"])
        ensure(data.accusative_plural).equals("palvelut")

        ensure(data.inessive).equals("palvelussa")
        ensure(data.inessive_plural).equals("palveluissa")

        ensure(data.elative).equals("palvelusta")
        ensure(data.elative_plural).equals("palveluista")

        ensure(data.illative).equals("palveluun")
        ensure(data.illatives_plural).equals(["palveluihin"])

        ensure(data.adessive).equals("palvelulla")
        ensure(data.adessive_plural).equals("palveluilla")

        ensure(data.ablative).equals("palvelulta")
        ensure(data.ablative_plural).equals("palveluilta")

        ensure(data.allative).equals("palvelulle")
        ensure(data.allative_plural).equals("palveluille")

        ensure(data.essive).equals("palveluna")
        ensure(data.essive_plural).equals("palveluina")

        ensure(data.translative).equals("palveluksi")
        ensure(data.translative_plural).equals("palveluiksi")

        ensure(data.abessive).equals("palvelutta")
        ensure(data.abessive_plural).equals("palveluitta")

        ensure(data.instructive_plural).equals("palveluin")

        ensure(data.comitative_plural).equals("palveluine")

    def test_kotus_noun_2_palvelu_umlauts(self):
        data = kotus_noun_2_palvelu("epäily")
        ensure(data.comitative_plural).equals("epäilyine")

    # The kotus wordlist does not contain any words that belong to class 2 and
    # have a gradation class. Have to skip testing that.
