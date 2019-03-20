import unittest
from ensure import ensure
from stroke_dictionary_creator.generators.short_words import *

class TestShortWords(unittest.TestCase):
    def test_short_word(self):
        ensure(short_word.parse("ai")).equals("AI")
        ensure(short_word.parse("on")).equals("ON")
        ensure(short_word.parse("no")).equals("TPHO")
        ensure(short_word.parse("aha")).equals("AH")
        ensure(short_word.parse("joo")).equals("SKVRO*")
        ensure(short_word.parse("hah")).equals("HAH")
        ensure(short_word.parse("höh")).equals("HOH")
        ensure(short_word.parse("tina")).equals("TIN")
        ensure(short_word.parse("onko")).equals("ONKo")
        ensure(short_word.parse("ukko")).equals("AONKHo")
        ensure(short_word.parse("äreä")).equals("ARea")
        ensure(short_word.parse("paikka")).equals("PAINKH")
        ensure(short_word.parse("paikkoja")).equals("PAINKHoia")
        ensure(short_word.parse("seittiä")).equals("SEISTRia")
        ensure(short_word.parse("hämää")).equals("HASHa")
        ensure(short_word.parse("nainen")).equals("TPHAINe")
        ensure(short_word.parse("paimen")).equals("PAISHe")
        ensure(short_word.parse("oja")).equals("Oia")
        ensure(short_word.parse("kuja")).equals("KAOia")
        ensure(short_word.parse("aattoja")).equals("A*STRoia")

        ensure(short_word.parse("")).equals("")

    def test_end(self):
        ensure(v.parse("en")).equals("e")
