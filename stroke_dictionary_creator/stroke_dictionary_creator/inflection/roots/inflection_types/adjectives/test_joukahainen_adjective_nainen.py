from ensure import ensure
from .joukahainen_adjective_nainen import joukahainen_adjective_nainen
from ... import gradation as g

def test_with_gradation():
    words = joukahainen_adjective_nainen("ylhäinen")
    ensure(words.positive.elatives_plural).equals(["ylhäisestä"])
    ensure(words.comparative.inessive).equals("ylhäisemmässä")
    ensure(words.superlative.abessive).equals("ylhäisimmättä")
