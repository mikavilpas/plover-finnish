import unittest
from ensure import ensure
from .kotus_noun_5_risti import *
from ..gradation import *

class TestInflectionType5(unittest.TestCase):
    def test_kotus_noun_5_risti_full_cases(self):
        data = kotus_noun_5_risti("risti")

        ensure(data.nominative).equals("risti")
        ensure(data.nominative_plural).equals("ristit")

        ensure(data.genitive).equals("ristin")
        ensure(data.genitives_plural).equals(["ristien"])

        ensure(data.partitive).equals("ristiä")
        ensure(data.partitives_plural).equals(["ristejä"])

        ensure(data.accusatives).equals(["risti", "ristin"])
        ensure(data.accusative_plural).equals("ristit")

        ensure(data.inessive).equals("ristissä")
        ensure(data.inessive_plural).equals("risteissä")

        ensure(data.elative).equals("rististä")
        ensure(data.elative_plural).equals("risteistä")

        ensure(data.illative).equals("ristiin")
        ensure(data.illatives_plural).equals(["risteihin"])

        ensure(data.adessive).equals("ristillä")
        ensure(data.adessive_plural).equals("risteillä")

        ensure(data.ablative).equals("ristiltä")
        ensure(data.ablative_plural).equals("risteiltä")

        ensure(data.allative).equals("ristille")
        ensure(data.allative_plural).equals("risteille")

        ensure(data.essive).equals("ristinä")
        ensure(data.essive_plural).equals("risteinä")

        ensure(data.translative).equals("ristiksi")
        ensure(data.translative_plural).equals("risteiksi")

        ensure(data.abessive).equals("ristittä")
        ensure(data.abessive_plural).equals("risteittä")

        ensure(data.instructive_plural).equals("ristein")

        ensure(data.comitative_plural).equals("risteine")

    def test_kotus_noun_5_risti_umlauts_and_gradation(self):
        data = kotus_noun_5_risti("käpälöinti",
                                  gradate_kotus_j_hento_hennon_vanne_vanteen)
        expected = InflectionInfo(nominative="käpälöinti",
                                  nominative_plural="käpälöinnit",
                                  genitive="käpälöinnin",
                                  genitives_plural=["käpälöintien"],
                                  partitive="käpälöintiä",
                                  partitives_plural=["käpälöintejä"],
                                  accusatives=["käpälöinti",
                                               "käpälöinnin"],
                                  accusative_plural="käpälöinnit",
                                  inessive="käpälöinnissä",
                                  inessive_plural="käpälöinneissä",
                                  elative="käpälöinnistä",
                                  elative_plural="käpälöinneistä",
                                  illative="käpälöintiin",
                                  illatives_plural=["käpälöinteihin"],
                                  adessive="käpälöinnillä",
                                  adessive_plural="käpälöinneillä",
                                  ablative="käpälöinniltä",
                                  ablative_plural="käpälöinneiltä",
                                  allative="käpälöinnille",
                                  allative_plural="käpälöinneille",
                                  essive="käpälöintinä",
                                  essive_plural="käpälöinteinä",
                                  translative="käpälöinniksi",
                                  translative_plural="käpälöinneiksi",
                                  abessive="käpälöinnittä",
                                  abessive_plural="käpälöinneittä",
                                  instructive_plural="käpälöinnein",
                                  comitative_plural="käpälöinteine")
        ensure(data).equals(expected)
