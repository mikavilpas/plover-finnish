from ensure import ensure
from .joukahainen_adjective_risti import joukahainen_adjective_risti
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_risti("iisi")
    ensure(words.positive.elatives_plural).equals(["iiseistä"])
    ensure(words.comparative.inessive).equals("iisimmässä")
    ensure(words.superlative.abessive).equals("iiseimmättä")

def test_with_gradation():
    words = joukahainen_adjective_risti("kimurantti", g.gradate_kotus_c_tyttö_tytön)
    ensure(words.positive.elatives_plural).equals(["kimuranteista"])
    ensure(words.comparative.inessive).equals("kimurantimmassa")
    ensure(words.superlative.abessive).equals("kimuranteimmatta")
