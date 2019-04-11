import unittest
from ensure import ensure
from .joukahainen_adjective_korkea import joukahainen_adjective_korkea
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_korkea("himmeä")
    ensure(words.positive.elatives_plural).equals(["himmeistä"])
    ensure(words.comparative.inessive).equals("himmeämmässä")
    ensure(words.superlative.abessive).equals("himmeimmättä")
