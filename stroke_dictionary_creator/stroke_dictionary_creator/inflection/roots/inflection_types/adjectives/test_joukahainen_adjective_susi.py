from ensure import ensure
from .joukahainen_adjective_susi import joukahainen_adjective_susi
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_susi("uusi")
    ensure(words.positive.elatives_plural).equals(["uusista"])
    ensure(words.comparative.inessive).equals("uudemmassa")
    ensure(words.superlative.abessive).equals("uusimmatta")
