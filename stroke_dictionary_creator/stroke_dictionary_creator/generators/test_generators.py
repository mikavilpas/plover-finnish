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
        ensure(end_vowel.parse("u")).equals("eo")

    def test_initial_consonant(self):
        ensure(initial_consonant.parse("s")).equals("S")
        ensure(initial_consonant.parse("t")).equals("T")
        ensure(initial_consonant.parse("k")).equals("K")
        ensure(initial_consonant.parse("p")).equals("P")
        ensure(initial_consonant.parse("v")).equals("V")
        ensure(initial_consonant.parse("h")).equals("H")
        ensure(initial_consonant.parse("r")).equals("R")

    def test_middle_diphtong(self):
        ensure(middle_diphtong.parse("ae")).equals("AE")
        ensure(middle_diphtong.parse("ai")).equals("AI")
        ensure(middle_diphtong.parse("ue")).equals("AOE")
        ensure(middle_diphtong.parse("ui")).equals("AOI")
        ensure(middle_diphtong.parse("ei")).equals("EI")
