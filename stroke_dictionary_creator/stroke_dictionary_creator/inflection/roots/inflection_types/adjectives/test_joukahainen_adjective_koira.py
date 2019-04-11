from ensure import ensure
from .joukahainen_adjective_koira import joukahainen_adjective_koira
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_koira("pyhä")
    ensure(words.positive.elatives_plural).equals(["pyhistä"])
    ensure(words.comparative.inessive).equals("pyhemmässä")
    ensure(words.superlative.abessive).equals("pyhimmättä")

def test_gradation_av1():
    words = joukahainen_adjective_koira("hoikka", g.gradate_kotus_a_takki_takin)
    ensure(words.positive.elatives_plural).equals(["hoikista"])
    ensure(words.comparative.inessive).equals("hoikemmassa")
    ensure(words.superlative.abessive).equals("hoikimmatta")

def test_gradation_av5():
    words = joukahainen_adjective_koira("märkä", g.gradate_kotus_d_reikä_reiän)
    ensure(words.positive.elatives_plural).equals(["märistä"])
    ensure(words.comparative.inessive).equals("märemmässä")
    ensure(words.superlative.abessive).equals("märimmättä")
