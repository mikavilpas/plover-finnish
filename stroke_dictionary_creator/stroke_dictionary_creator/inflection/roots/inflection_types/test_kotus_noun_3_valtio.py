import unittest
from ensure import ensure
from .kotus_noun_3_valtio import *
from ..gradation import *

class TestInflectionType3(unittest.TestCase):
    def test_kotus_noun_3_valtio_full_cases(self):
        data = kotus_noun_3_valtio("valtio")

        ensure(data.nominative).equals("valtio")
        ensure(data.nominative_plural).equals("valtiot")

        ensure(data.genitive).equals("valtion")
        ensure(data.genitives_plural).equals(["valtioiden",
                                              "valtioitten"])

        ensure(data.partitive).equals("valtiota")
        ensure(data.partitives_plural).equals(["valtioita"])

        ensure(data.accusatives).equals(["valtio", "valtion"])
        ensure(data.accusative_plural).equals("valtiot")

        ensure(data.inessive).equals("valtiossa")
        ensure(data.inessive_plural).equals("valtioissa")

        ensure(data.elative).equals("valtiosta")
        ensure(data.elative_plural).equals("valtioista")

        ensure(data.illative).equals("valtioon")
        ensure(data.illatives_plural).equals(["valtioihin"])

        ensure(data.adessive).equals("valtiolla")
        ensure(data.adessive_plural).equals("valtioilla")

        ensure(data.ablative).equals("valtiolta")
        ensure(data.ablative_plural).equals("valtioilta")

        ensure(data.allative).equals("valtiolle")
        ensure(data.allative_plural).equals("valtioille")

        ensure(data.essive).equals("valtiona")
        ensure(data.essive_plural).equals("valtioina")

        ensure(data.translative).equals("valtioksi")
        ensure(data.translative_plural).equals("valtioiksi")

        ensure(data.abessive).equals("valtiotta")
        ensure(data.abessive_plural).equals("valtioitta")

        ensure(data.instructive_plural).equals("valtioin")

        ensure(data.comitative_plural).equals("valtioine")

    def test_kotus_noun_3_valtio_umlauts(self):
        data = kotus_noun_3_valtio("häiriö")
        ensure(data.comitative_plural).equals("häiriöine")

    # The kotus wordlist does not contain any words that belong to class 3 and
    # have a gradation class. Have to skip testing that.
