from ensure import ensure
from .joukahainen_adjective_sisin import joukahainen_adjective_sisin
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_sisin("lähin")
    # note: no positive form available
    ensure(words.comparative.inessive).equals("lähemmässä")
    ensure(words.superlative.abessive).equals("lähimmättä")
