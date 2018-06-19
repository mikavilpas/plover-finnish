import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection.voikko_inflection import *

from .roots import gradation as gr

class TestVoikkoInflection(unittest.TestCase):

    def test_joukahainen_gradation_to_kotus(self):
        ensure(joukahainen_gradation_to_kotus("aalto", "valo", "av1")).equals("I")
        ensure(joukahainen_gradation_to_kotus("adagio", "valo", None)).equals(None)
        ensure(joukahainen_gradation_to_kotus("aironveto", "valo", "av1")).equals("F")
        ensure(joukahainen_gradation_to_kotus("höltyä", "punoa", "av1")).equals("I")

        ensure(joukahainen_gradation_to_kotus("tavoittaa", "aavistaa", "av1")).equals("C")
        ensure(joukahainen_gradation_to_kotus("muistaa", "muistaa", None)).equals(None)
