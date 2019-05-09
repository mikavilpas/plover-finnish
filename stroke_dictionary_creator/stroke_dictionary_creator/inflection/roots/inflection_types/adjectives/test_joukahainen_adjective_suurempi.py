from ensure import ensure
from .joukahainen_adjective_suurempi import joukahainen_adjective_suurempi
from ... import gradation as g

def test_with_gradation():
    words = joukahainen_adjective_suurempi("idempi",
                                           g.gradate_kotus_h_kumpi_kumman)
    # note: only a single form available
    ensure(words.word.inessive).equals("idemmässä")

def test_deduces_correct_gradation():
    # should also deduce the correct gradation
    words = joukahainen_adjective_suurempi("idempi"
                                           # Gradation not passed as argument!
    )
    # note: only a single form available
    ensure(words.word.inessive).equals("idemmässä")
