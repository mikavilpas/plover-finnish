import unittest
from ensure import ensure
from stroke_dictionary_creator.generators.generators import *

class TestGenerators(unittest.TestCase):
    def test_middle_vowel(self):
        ensure(middle_vowel.parse("a")).equals("A")
        ensure(middle_vowel.parse("e")).equals("E")
        ensure(middle_vowel.parse("i")).equals("I")
        ensure(middle_vowel.parse("o")).equals("O")
        ensure(middle_vowel.parse("u")).equals("AO")
        ensure(middle_vowel.parse("y")).equals("AO")
        ensure(middle_vowel.parse("ä")).equals("A")
        ensure(middle_vowel.parse("ö")).equals("O")

    def test_end_vowel(self):
        ensure(end_vowel.parse("e")).equals("e")
        ensure(end_vowel.parse("o")).equals("o")
        ensure(end_vowel.parse("i")).equals("i")
        ensure(end_vowel.parse("a")).equals("a")
