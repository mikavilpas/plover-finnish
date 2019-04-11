import unittest
from ensure import ensure
from .joukahainen_adjective_karahka import joukahainen_adjective_karahka
from ... import gradation as g

def test_gradation_av1():
    words = joukahainen_adjective_karahka("ärhäkkä", g.gradate_kotus_a_takki_takin)
    ensure(words.positive.elatives_plural).equals(["ärhäköistä"])
    ensure(words.comparative.inessive).equals("ärhäkämmässä")
    ensure(words.superlative.abessive).equals("ärhäköimmättä")
