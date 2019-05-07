from ensure import ensure
from .joukahainen_adjective_vastaus import joukahainen_adjective_vastaus

def test_no_gradation():
    words = joukahainen_adjective_vastaus("veres")
    ensure(words.positive.elatives_plural).equals(["vereksistä"])
    ensure(words.comparative.inessive).equals("vereksemmässä")
    ensure(words.superlative.abessive).equals("vereksimmättä")
