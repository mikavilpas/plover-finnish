from ensure import ensure
from .joukahainen_adjective_nalle import joukahainen_adjective_nalle
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_nalle("skrode")
    ensure(words.positive.elatives_plural).equals(["skrodeista"]) # I think this could be skrodista, too
    ensure(words.comparative.inessive).equals("skrodemmassa")
    ensure(words.superlative.abessive).equals("skrodeimmatta")
