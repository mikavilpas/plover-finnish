from ensure import ensure
from .joukahainen_adjective_laupias import joukahainen_adjective_laupias
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_laupias("laupias")
    ensure(words.positive.elatives_plural).equals(["laupiaista"])
    ensure(words.comparative.inessive).equals("laupiaammassa")
    ensure(words.superlative.abessive).equals("laupiaimmatta")
