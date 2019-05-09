from ensure import ensure
from .joukahainen_adjective_sisin import joukahainen_adjective_sisin
from ... import gradation as g

def test_no_gradation():
    adjective = joukahainen_adjective_sisin("lähin")
    ensure(adjective.word.inessive).equals("lähimmässä")
    ensure(adjective.word.abessive).equals("lähimmättä")

def test_another_case():
    adjective = joukahainen_adjective_sisin("uloin")
    ensure(adjective.word.inessive).equals("uloimmassa")
    ensure(adjective.word.abessive).equals("uloimmatta")
