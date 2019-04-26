from ensure import ensure
from .joukahainen_adjective_loppu import joukahainen_adjective_loppu
from ... import gradation as g

def test_with_gradation():
    words = joukahainen_adjective_loppu("pikku", g.gradate_kotus_a_takki_takin)
    ensure(words.positive.elatives_plural).equals(["pikuista"])
    ensure(words.comparative.inessive).equals("pikummassa")
    ensure(words.superlative.abessive).equals("pikuimmatta")
