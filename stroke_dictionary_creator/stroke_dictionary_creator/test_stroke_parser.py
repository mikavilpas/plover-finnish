import unittest
from ensure import ensure
from stroke_dictionary_creator.stroke_parser import *

class TestParser(unittest.TestCase):
    def test_initial_consonants(self):
        ensure(initial_consonants.parse("S")).equals("S")
        ensure(initial_consonants.parse("ST")).equals("ST")
        ensure(initial_consonants.parse("STKPVHR")).equals("STKPVHR")

        # in order but not all keys pressed consecutively
        ensure(initial_consonants.parse("SR")).equals("SR")

        # the initial consonant may be left out
        ensure(initial_consonants.parse("")).equals("")

        # using a consonant twice should crash
        ensure(initial_consonants.parse).called_with("SS").raises(Exception)
        ensure(initial_consonants.parse).called_with("SRR").raises(Exception)

    def test_middle_keys(self):
        ensure(middle_keys.parse("A")).equals("A")
        ensure(middle_keys.parse("-")).equals("-")
        ensure(middle_keys.parse("AOEI")).equals("AOEI")

        # some strokes that include the asterisk
        ensure(middle_keys.parse("AO*EI")).equals("AO*EI")
        ensure(middle_keys.parse("A*")).equals("A*")
        ensure(middle_keys.parse("A*E")).equals("A*E")
        ensure(middle_keys.parse("*I")).equals("*I")

        # A missing middle key is a "-"
        ensure(middle_keys.parse("-")).equals("-")
        ensure(middle_keys.parse).called_with("").raises(Exception)

    def test_end_keys(self):
        ensure(end_keys.parse("NKST")).equals("NKST")
        ensure(end_keys.parse("NKSHTReoia")).equals("NKSHTReoia")

        # the end key may be left out
        ensure(end_keys.parse("")).equals("")

    def test_stroke(self):
        # combinations of left, middle and right keys should work
        ensure(stroke.parse("P-")).equals("P-")
        ensure(stroke.parse("I")).equals("I")
        ensure(stroke.parse("-i")).equals("-i")

        # mikä
        ensure(stroke.parse("PHIKa")).equals("PHIKa")
        # Miika
        ensure(stroke.parse("PH*IKa")).equals("PH*IKa")


        ensure(stroke.parse).called_with("SSa").raises(Exception)
