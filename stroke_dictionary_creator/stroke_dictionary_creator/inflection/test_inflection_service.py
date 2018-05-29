import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection.inflection_service import *

class TestInflectionService(unittest.TestCase):

    def test_inflected_forms(self):
        # must be able to distinguish nouns ans verbos based on the class of the word
        forms = inflected_forms("koe;noun-hame-av6")
        ensure(forms).contains("kokeen")

        forms = inflected_forms("koettaa;verb-aavistaa-av1")
        ensure(forms).contains("koetettiin")

        # print(inflected_forms("koettaa;verb-aavistaa-av1"))
        print(inflected_forms("kuunnella;verb-katsella-av2"))

    def test_word_and_class_parser(self):
        ensure(word_and_class.parse("koe;noun-hame-av6"))\
            .equals(["koe", "subst-hame-av6"])

        # can parse umlauts
        ensure(word_and_class.parse("käheä;adjective-korkea"))\
            .equals(["käheä", "subst-korkea"])

        # can parse underscores
        ensure(word_and_class.parse("ARA;pnoun_misc-kala"))\
            .equals(["ARA", "subst-kala"])