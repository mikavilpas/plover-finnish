import unittest
from ensure import ensure
from .double_consonant_frequencies import *

class TestDoubleConsonantFrequencies(unittest.TestCase):
    def test_after_vowel(self):
        ensure(after_vowel("abstraktio", "st")).is_(False)

    def test_is_a_double_consonant_cluster(self):
       ensure(is_a_two_consonant_cluster(word = "a", chars = "b")).is_(False)
       ensure(is_a_two_consonant_cluster("a", "bb")).is_(False)

       # # not included in word
       ensure(is_a_two_consonant_cluster("abstraktio", "bb")).is_(False)

       # # in the middle of a cluster
       ensure(is_a_two_consonant_cluster("abstraktio", "st")).is_(False)

       # # at the start
       ensure(is_a_two_consonant_cluster("abstraktio", "bs")).is_(False)

       # # at the end
       ensure(is_a_two_consonant_cluster("abstraktio", "tr")).is_(False)
       ensure(is_a_two_consonant_cluster("arktinen", "kt")).is_(False)

       # happy path
       ensure(is_a_two_consonant_cluster("abstraktio", "kt")).is_(True)
       ensure(is_a_two_consonant_cluster("akti", "kt")).is_(True)

    def test_find_neighboring_characters_in_word(self):
        expected = {'preceding_character': 'a', 'trailing_character': 'i'}
        ensure(find_neighboring_characters_in_word("abstraktio", "kt")).equals(expected)
