from ensure import ensure
from .joukahainen_adjective_pii import joukahainen_adjective_pii
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_pii("peeaa")
    ensure(words.positive.elatives_plural).equals(["peeaista"])
    ensure(words.comparative.inessive).equals("peeaammassa")
    ensure(words.superlative.abessive).equals("peeaimmatta")
