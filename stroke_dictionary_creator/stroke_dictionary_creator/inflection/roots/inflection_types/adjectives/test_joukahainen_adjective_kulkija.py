import unittest
from ensure import ensure
from .joukahainen_adjective_kulkija import joukahainen_adjective_kulkija
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_kulkija("viheriä")
    ensure(words.positive.elatives_plural).equals(["viheriöistä"])
    ensure(words.comparative.inessive).equals("viheriämmässä")
    ensure(words.superlative.abessive).equals("viheriäimmättä")
