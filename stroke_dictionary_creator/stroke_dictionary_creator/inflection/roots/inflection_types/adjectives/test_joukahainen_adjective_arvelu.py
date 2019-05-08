from ensure import ensure
from .joukahainen_adjective_arvelu import joukahainen_adjective_arvelu
from ... import gradation as g

def test_gradation():
    words = joukahainen_adjective_arvelu("mainittu", g.gradate_kotus_c_tyttö_tytön)
    ensure(words.positive.elatives_plural).equals(["mainituista"])
    ensure(words.comparative.inessive).equals("mainitummassa")
    ensure(words.superlative.abessive).equals("mainituimmatta")
