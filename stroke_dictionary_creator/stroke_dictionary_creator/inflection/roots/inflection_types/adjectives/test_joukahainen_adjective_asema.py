import unittest
from ensure import ensure
from .joukahainen_adjective_asema import joukahainen_adjective_asema
from ... import gradation as g

def test_gradation():
    words = joukahainen_adjective_asema("kiperä")
    ensure(words.positive.elatives_plural).equals(["kiperistä"])
    ensure(words.comparative.inessive).equals("kiperämmässä")
    ensure(words.superlative.abessive).equals("kiperimmättä")
