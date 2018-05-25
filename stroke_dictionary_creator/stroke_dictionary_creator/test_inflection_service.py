import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection_service import *

class TestInflectionService(unittest.TestCase):

    def test_inflected_forms(self):
        # must be able to distinguish nouns ans verbos based on the class of the word
        forms = inflected_forms("koe", infclass = "subst-hame-av6")
        ensure(forms["genetiivi"]).equals("kokeen")

        forms = inflected_forms("koettaa", infclass = "verbi-aavistaa-av1")
        ensure(forms["imperfekti_pass"]).equals("koetettiin")

        # fails for irregular words, which have to be added manually. There are
        # only about 40 of them.
        forms = inflected_forms("yö")
        ensure(forms).equals(None)
