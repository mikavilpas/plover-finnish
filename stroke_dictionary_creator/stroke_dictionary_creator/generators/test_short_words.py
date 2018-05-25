import unittest
from ensure import ensure
from stroke_dictionary_creator.generators.short_words import *

class TestShortWords(unittest.TestCase):
    def test_two_vowel_word(self):
        ensure(two_vowel_word.parse("ai")).equals("Ai")

    def test_vowel_consonant_word(self):
        ensure(vowel_consonant_word.parse("on")).equals("ON")

    def test_consonant_vowel_word(self):
        ensure(consonant_vowel_word.parse("no")).equals("TPH-o")

    def test_consonant_vowel_vowel_word(self):
        ensure(consonant_vowel_vowel_word.parse("joo")).equals("SKVROo")

    def test_vowel_end_diphtong_word(self):
        ensure(vowel_end_diphtong_word.parse("oja")).equals("Oia")

    def test_consonant_vowel_c_w_word(self):
        ensure(consonant_vowel_c_w_word.parse("tina")).equals("TINa")

    def test_vowel_consonant_v_v_word(self):
        ensure(vowel_consonant_v_v_word.parse("äreä")).equals("ARea")
