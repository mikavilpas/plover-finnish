from ensure import ensure
from .joukahainen_adjective_vieras import joukahainen_adjective_vieras
from ... import gradation as g

def test_with_gradation():
    words = joukahainen_adjective_vieras("kirkas", g.gradate_kotus_a_hake_hakkeen)
    ensure(words.positive.elatives_plural).equals(["kirkkaista"])
    ensure(words.comparative.inessive).equals("kirkkaammassa")
    ensure(words.superlative.abessive).equals("kirkkaimmatta")

def test_with_no_gradation():
    words = joukahainen_adjective_vieras("kernas")
    ensure(words.positive.elatives_plural).equals(["kernaista"])
    ensure(words.comparative.inessive).equals("kernaammassa")
    ensure(words.superlative.abessive).equals("kernaimmatta")
