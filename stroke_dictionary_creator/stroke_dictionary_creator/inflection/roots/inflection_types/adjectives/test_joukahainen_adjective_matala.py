from ensure import ensure
from .joukahainen_adjective_matala import joukahainen_adjective_matala
from ... import gradation as g

def test_with_gradation():
    words = joukahainen_adjective_matala("säkkärä")
    ensure(words.positive.elatives_plural).equals(["säkkäristä"])
    ensure(words.comparative.inessive).equals("säkkärämmässä")
    ensure(words.superlative.abessive).equals("säkkärimmättä")
