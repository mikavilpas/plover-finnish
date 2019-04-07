import unittest
from ensure import ensure
from .joukahainen_adjective_iäkäs import joukahainen_adjective_iäkäs
from ... import gradation as g

def test_gradation():
    words = joukahainen_adjective_iäkäs("kyvykäs", g.gradate_kotus_a_hake_hakkeen)
    ensure(words.positive.elatives_plural).equals(["kyvykkäistä"])
    ensure(words.comparative.inessive).equals("kyvykkäämmässä")
    ensure(words.superlative.abessive).equals("kyvykkäimmättä")
