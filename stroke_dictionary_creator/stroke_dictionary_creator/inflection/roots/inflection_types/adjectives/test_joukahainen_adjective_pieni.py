from ensure import ensure
from .joukahainen_adjective_pieni import joukahainen_adjective_pieni
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_pieni("pieni")
    ensure(words.positive.elatives_plural).equals(["pienistä"])
    ensure(words.comparative.inessive).equals("pienemmässä")
    ensure(words.superlative.abessive).equals("pienimmättä")
