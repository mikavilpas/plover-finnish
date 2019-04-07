import unittest
from ensure import ensure
from .joukahainen_adjective_hame import joukahainen_adjective_hame
from ... import gradation as g

def test_gradation():
    words = joukahainen_adjective_hame("tuore")
    ensure(words.positive.elatives_plural).equals(["tuoreista"])
    ensure(words.comparative.inessive).equals("tuoreemmassa")
    ensure(words.superlative.abessive).equals("tuoreimmatta")
