from ensure import ensure
from .joukahainen_adjective_ohut import joukahainen_adjective_ohut
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_ohut("ehyt")
    ensure(words.positive.elatives_plural).equals(["ehyistä"])
    ensure(words.comparative.inessive).equals("ehyemmässä")
    ensure(words.superlative.abessive).equals("ehyimmättä")
