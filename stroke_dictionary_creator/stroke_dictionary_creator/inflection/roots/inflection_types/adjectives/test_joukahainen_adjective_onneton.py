from ensure import ensure
from .joukahainen_adjective_onneton import joukahainen_adjective_onneton
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_onneton("alaston")
    ensure(words.positive.elatives_plural).equals(["alastomista"])
    ensure(words.comparative.inessive).equals("alastomammassa")
    ensure(words.superlative.abessive).equals("alastomimmatta")

def test_with_gradation():
    words = joukahainen_adjective_onneton("hillitön", g.gradate_kotus_c_kate_katteen)
    ensure(words.positive.elatives_plural).equals(["hillittömistä"])
    ensure(words.comparative.inessive).equals("hillittömämmässä")
    ensure(words.superlative.abessive).equals("hillittömimmättä")
