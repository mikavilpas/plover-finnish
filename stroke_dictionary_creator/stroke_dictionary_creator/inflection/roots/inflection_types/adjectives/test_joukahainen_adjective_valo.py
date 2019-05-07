from ensure import ensure

from stroke_dictionary_creator.stroke_dictionary_creator.inflection.roots import \
    gradation as g

from .joukahainen_adjective_valo import joukahainen_adjective_valo


def test_no_gradation():
    words = joukahainen_adjective_valo("fiksu")
    ensure(words.positive.elatives_plural).equals(["fiksuista"])
    ensure(words.comparative.inessive).equals("fiksummassa")
    ensure(words.superlative.abessive).equals("fiksuimmatta")


def test_with_gradation():
    words = joukahainen_adjective_valo("aito", g.gradate_kotus_f_satu_sadun)
    ensure(words.positive.elatives_plural).equals(["aidoista"])
    ensure(words.comparative.inessive).equals("aidommassa")
    ensure(words.superlative.abessive).equals("aidoimmatta")
