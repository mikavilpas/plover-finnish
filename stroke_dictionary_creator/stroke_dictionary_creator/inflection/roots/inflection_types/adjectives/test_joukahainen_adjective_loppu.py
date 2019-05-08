from ensure import ensure
from .joukahainen_adjective_loppu import joukahainen_adjective_loppu
from ... import gradation as g

def test_with_gradation():
    # gradation is not used, though
    word = joukahainen_adjective_loppu("pikku", g.gradate_kotus_a_takki_takin)
    ensure(word.word.elatives_plural).equals(["pikuista"])
