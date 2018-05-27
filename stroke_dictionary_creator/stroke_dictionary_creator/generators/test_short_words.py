import unittest
from ensure import ensure
from stroke_dictionary_creator.generators.short_words import *

class TestShortWords(unittest.TestCase):
    def test_word_vv(self):
        ensure(word_vv.parse("ai")).equals("Ai")

    def test_word_vc(self):
        ensure(word_vc.parse("on")).equals("ON")

    def test_word_cv(self):
        ensure(word_cv.parse("no")).equals("TPH-o")

    def test_word_vcv(self):
        ensure(word_vcv.parse("aha")).equals("AHa")

    def test_word_cvv(self):
        ensure(word_cvv.parse("joo")).equals("SKVROo")

    def test_word_cvc(self):
        ensure(word_cvc.parse("hah")).equals("HAH")
        ensure(word_cvc.parse("höh")).equals("HOH")

    def test_word_v_end_diphtong(self):
        ensure(word_v_end_diphtong.parse("oja")).equals("Oia")

    def test_word_cvcv(self):
        ensure(word_cvcv.parse("tina")).equals("TINa")

    def test_word_vccv(self):
        ensure(word_vccv.parse("onko")).equals("ONKo")
        ensure(word_vccv.parse("ukko")).equals("AONKHo")
        ensure(word_vccv.parse).called_with("ahma").raises(Exception)

    def test_word_vcvv(self):
        ensure(word_vcvv.parse("äreä")).equals("ARea")

    def test_word_cvvccv(self):
        ensure(word_cvvccv.parse("paikka")).equals("PAINKHa")
        ensure(word_cvvccv.parse("paikkoja")).equals("PAINKHoia")
