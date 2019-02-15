from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_35_lämmin(word, gradation_fn = identity):
    # https://en.wiktionary.org/wiki/Appendix:Finnish_niminal_inflection/l%C3%A4mmin
    # https://fi.wiktionary.org/wiki/seitsen

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    lämmin   = word
    word_alt = gradation_fn(lämmin)

    (lämm, i, n) = reverse_parse(lämmin, root_and_vc_ending)
    (lämp, *_) = reverse_parse(word_alt, root_and_vc_ending)
    lämmi = lämm + i
    lämpi = lämp + i

    return InflectionInfo(nominative          = lämmin,
                          nominative_plural   = lämpi + s("mät"),
                          genitive            = lämpi + s("män"),
                          genitives_plural    = [lämpi + s("mien"),
                                                 lämpi + s("mäin")],
                          partitives          = [lämmin + s("tä")],
                          partitives_plural   = [lämpi + s("miä")],
                          accusatives         = [lämmin,
                                                lämpi + s("män")],
                          accusative_plural   = lämpi + s("mät"),
                          inessive            = lämpi + s("mässä"),
                          inessives_plural    = [lämpi + s("missä")],
                          elative             = lämpi + s("mästä"),
                          elatives_plural     = [lämpi + s("mistä")],
                          illatives           = [lämpi + s("mään")],
                          illatives_plural    = [lämpi + s("miin")],
                          adessive            = lämpi + s("mällä"),
                          adessives_plural    = [lämpi + s("millä")],
                          ablative            = lämpi + s("mältä"),
                          ablatives_plural    = [lämpi + s("miltä")],
                          allative            = lämpi + s("mälle"),
                          allatives_plural    = [lämpi + s("mille")],
                          essives             = [lämpi + s("mänä")],
                          essives_plural      = [lämpi + s("minä")],
                          translative         = lämpi + s("mäksi"),
                          translatives_plural = [lämpi + s("miksi")],
                          abessive            = lämpi + s("mättä"),
                          abessives_plural    = [lämpi + s("mittä")],
                          instructives_plural = [lämpi + s("min")],
                          comitatives_plural  = [lämpi + s("mine")])
