import unittest
from ensure import ensure
from .joukahainen_adjective_kuollut import joukahainen_adjective_kuollut
from ... import gradation as g

def test_no_gradation():
    words = joukahainen_adjective_kuollut("mukanaollut")
    ensure(words.positive.elatives_plural).equals(["mukanaolleista"])
    ensure(words.comparative.inessive).equals("mukanaolleemmassa")
    ensure(words.superlative.abessive).equals("mukanaolleimmatta")
