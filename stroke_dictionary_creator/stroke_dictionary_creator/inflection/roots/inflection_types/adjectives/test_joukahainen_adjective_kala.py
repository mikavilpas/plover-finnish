import unittest
from ensure import ensure
from .joukahainen_adjective_kala import joukahainen_adjective_kala
from ... import gradation as g

def test_with_no_gradation():
    words = joukahainen_adjective_kala("harva")
    ensure(words.positive.elatives_plural).equals(["harvoista"])
    ensure(words.comparative.inessive).equals("harvemmassa")
    ensure(words.superlative.abessive).equals("harvimmatta")

def test_with_av1_gradation():
    words = joukahainen_adjective_kala("halpa", g.gradate_kotus_e_sopu_sovun)
    ensure(words.positive.elatives_plural).equals(["halvoista"])
    ensure(words.comparative.inessive).equals("halvemmassa")
    ensure(words.superlative.abessive).equals("halvimmatta")

def test_with_av5_gradation():
    words = joukahainen_adjective_kala("arka", g.gradate_kotus_d_reikä_reiän)
    ensure(words.positive.elatives_plural).equals(["aroista"])
    ensure(words.comparative.inessive).equals("aremmassa")
    ensure(words.superlative.abessive).equals("arimmatta")
