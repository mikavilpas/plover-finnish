import unittest
from ensure import ensure
from .two_stroke_words import *

class TestTwoStrokeWords(unittest.TestCase):
    def test_two_strokes(self):
        ensure(two_strokes.parse("kokonainen")).equals("KOKo/TPHAINe")
        ensure(two_strokes.parse("hiatuksen")).equals("HA*ITeo/K-Se")
