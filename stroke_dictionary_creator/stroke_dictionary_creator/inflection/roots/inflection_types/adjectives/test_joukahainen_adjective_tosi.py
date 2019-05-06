from ensure import ensure
from .joukahainen_adjective_tosi import joukahainen_adjective_tosi
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_tosi("täysi")
    ensure(words.positive.elatives_plural).equals(["täysistä"])
    ensure(words.comparative.inessive).equals("täydemmässä")
    ensure(words.superlative.abessive).equals("täysimmättä")
