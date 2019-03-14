import unittest
from ensure import ensure
from .all_words import all_words

class TestAllWords(unittest.TestCase):
    def test_all_words(self):
        ensure(all_words.parse("nainen")).equals("TPHAINe")
        ensure(all_words.parse("kokonainen")).equals("KOKo/TPHAINe")
