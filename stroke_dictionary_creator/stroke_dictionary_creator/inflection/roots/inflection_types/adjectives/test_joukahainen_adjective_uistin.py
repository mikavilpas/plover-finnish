from ensure import ensure
from .joukahainen_adjective_uistin import joukahainen_adjective_uistin

def test_no_gradation():
    words = joukahainen_adjective_uistin("avoin")
    ensure(words.positive.elatives_plural).equals(["avoimista"])
    ensure(words.comparative.inessive).equals("avoimemmassa")
    ensure(words.superlative.abessive).equals("avoimimmatta")
