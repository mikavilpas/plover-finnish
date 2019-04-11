import unittest
from ensure import ensure
from .joukahainen_adjective_kaunis import joukahainen_adjective_kaunis
from ... import gradation as g

def test_gradation_av1():
    words = joukahainen_adjective_kaunis("kallis")
    ensure(words.positive.elatives_plural).equals(["kalliista"])
    ensure(words.comparative.inessive).equals("kalliimmassa")
    ensure(words.superlative.abessive).equals("kalleimmatta")
