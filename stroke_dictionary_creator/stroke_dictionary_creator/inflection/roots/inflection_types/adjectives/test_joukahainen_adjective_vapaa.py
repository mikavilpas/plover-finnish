from ensure import ensure
from .joukahainen_adjective_vapaa import joukahainen_adjective_vapaa

def test_no_gradation():
    words = joukahainen_adjective_vapaa("vakaa")
    ensure(words.positive.elatives_plural).equals(["vakaista"])
    ensure(words.comparative.inessive).equals("vakaammassa")
    ensure(words.superlative.abessive).equals("vakaimmatta")
