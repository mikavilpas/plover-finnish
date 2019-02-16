from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_42_mies(word, gradation_fn = identity):
    # The word mies only, and its compound words; no consonant gradation.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/mies

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    mies          = word
    (m, i, e, s_) = reverse_parse(word, root_and_vvc_ending)
    print((m, i, e, s_))
    mie           = m + i + e
    miehi         = mie + "h" + i
    miehe         = mie + "h" + e

    return InflectionInfo(nominative          =  mies,
                          nominative_plural   =  miehe + s("t"),
                          genitive            =  miehe + s("n"),
                          genitives_plural    = [mies + s("ten"),
                                                 miehi + s("en")],
                          partitives          = [mies + s("tä")],
                          partitives_plural   = [miehi + s("ä")],
                          accusatives         = [mies,
                                                 miehe + s("n")],
                          accusative_plural   =  miehe + s("t"),
                          inessive            =  miehe + s("ssä"),
                          inessives_plural    = [miehi + s("ssä")],
                          elative             =  miehe + s("stä"),
                          elatives_plural     = [miehi + s("stä")],
                          illatives           = [miehe + s("en")],
                          illatives_plural    = [miehi + s("in")],
                          adessive            =  miehe + s("llä"),
                          adessives_plural    = [miehi + s("llä")],
                          ablative            =  miehe + s("ltä"),
                          ablatives_plural    = [miehi + s("ltä")],
                          allative            =  miehe + s("lle"),
                          allatives_plural    = [miehi + s("lle")],
                          essives             = [miehe + s("nä")],
                          essives_plural      = [miehi + s("nä")],
                          translative         =  miehe + s("ksi"),
                          translatives_plural = [miehi + s("ksi")],
                          abessive            =  miehe + s("ttä"),
                          abessives_plural    = [miehi + s("ttä")],
                          instructives_plural = [miehi + s("n")],
                          comitatives_plural  = [miehi + s("ne")])
