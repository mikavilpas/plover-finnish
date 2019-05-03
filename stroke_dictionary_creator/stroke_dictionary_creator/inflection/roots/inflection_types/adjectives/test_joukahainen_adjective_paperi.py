from ensure import ensure
from .joukahainen_adjective_paperi import joukahainen_adjective_paperi
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_paperi("passeli")
    ensure(words.positive.elatives_plural).equals(["passeleista"])
    ensure(words.comparative.inessive).equals("passelimmassa")
    ensure(words.superlative.abessive).equals("passeleimmatta")
