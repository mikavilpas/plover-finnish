from ensure import ensure
from .joukahainen_adjective_siisti import joukahainen_adjective_siisti
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_siisti("siisti")
    ensure(words.positive.elatives_plural).equals(["siisteistä"])
    ensure(words.comparative.inessive).equals("siistimmässä")
    ensure(words.superlative.abessive).equals("siisteimmättä")
