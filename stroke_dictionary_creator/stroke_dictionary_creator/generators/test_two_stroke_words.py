import unittest
from ensure import ensure
from .two_stroke_words import *

class TestTwoStrokeWords(unittest.TestCase):
    def test_two_strokes(self):
        ensure(two_strokes("kokonainen")).equals(["kokonainen", "KOKo/TPHAINe"])
        ensure(two_strokes("hiatuksen")).equals(["hiatuksen", "HA*ITeo/K-Se"])

    def test_with_suffix(self):
        ensure(two_strokes("kokon")).equals(["kokon", "KOKo"])
        ensure(two_strokes("aamuiksi")).equals(["aamuiksi", "A*SHeoi"])
