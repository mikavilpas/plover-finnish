import unittest
from ensure import ensure
from .joukahainen_adjective_autio import joukahainen_adjective_autio
from ... import gradation as g

def test_gradation():
    words = joukahainen_adjective_autio("riiviö")

    ensure(words.positive.elatives_plural).equals(["riiviöistä"])
    ensure(words.comparative.inessive).equals("riiviömmässä")
    ensure(words.superlative.abessive).equals("riiviöimmättä")
