import unittest
from ensure import ensure
from .joukahainen_adjective_kalsium import joukahainen_adjective_kalsium
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_kalsium("kosher")
    ensure(words.positive.elatives_plural).equals(["koshereista"])
    ensure(words.comparative.inessive).equals("kosherimmassa")
    ensure(words.superlative.abessive).equals("koshereimmatta")
