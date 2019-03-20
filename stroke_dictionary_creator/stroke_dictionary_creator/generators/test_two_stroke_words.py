import unittest
from ensure import ensure
from .two_stroke_words import *

class TestTwoStrokeWords(unittest.TestCase):
    def test_two_strokes(self):
        ensure(two_strokes("kokonainen")).equals(["kokonainen", "KOKo/TPHAINe"])
        ensure(two_strokes("hiatuksen")).equals(["hiatuksen", "HA*ITeo/K-Se"])

    def test_with_suffix(self):
        ensure(two_strokes("kokon")).equals(["koko", "KOKo"])
        ensure(two_strokes("aamuiksi")).equals(["aamui", "A*SHeoi"])

        ensure(two_strokes("aattoja")).equals(["aattoja", "A*STRoia"])

        ensure(two_strokes("aatelit")).equals(["aatelit", "A*Te/HRIT"])
        ensure(two_strokes("aatelistoa")).equals(["aatelistoa", "A*Te/HRISToa"])
        ensure(two_strokes("aatelistoja")).equals(["aatelistoja", "A*Te/HRISToia"])

        ensure(two_strokes("etenen")).equals(["etenen", "ETe/EN"])
