from .base import *

from parsy import *
from ..tokens import *
from .kotus_noun_34_onneton import word_vc_ending

def kotus_noun_36_sisin(word, gradation_fn = identity):
    # Superlative adjectives ending with "-in"
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/sisin

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    sisin       = word
    (sis, i, n) = reverse_parse(sisin, word_vc_ending)
    sisim       = sis + i + s("m")
    sisimm      = sis + i + s("mm")
    sisimp      = sis + i + s("mp")

    return InflectionInfo(nominative          =  sisin,
                          nominative_plural   =  sisimm + s("ät"),
                          genitive            =  sisimm + s("än"),
                          genitives_plural    = [sisimp + s("ien"),
                                                 sisin + s("ten"),
                                                 sisim + s("päin")],
                          partitives          = [sisin + s("tä")],
                          partitives_plural   = [sisimp + s("iä")],
                          accusatives         = [sisin,
                                                 sisimm + s("än")],
                          accusative_plural   =  sisimm + s("ät"),
                          inessive            =  sisimm + s("ässä"),
                          inessives_plural    = [sisimm + s("missä")],
                          elative             =  sisimm + s("ästä"),
                          elatives_plural     = [sisimm + s("mistä")],
                          illatives           = [sisimp + s("ään")],
                          illatives_plural    = [sisimp + s("iin")],
                          adessive            =  sisimm + s("ällä"),
                          adessives_plural    = [sisimm + s("illä")],
                          ablative            =  sisimm + s("ältä"),
                          ablatives_plural    = [sisimm + s("iltä")],
                          allative            =  sisimm + s("älle"),
                          allatives_plural    = [sisimm + s("ille")],
                          essives             = [sisimp + s("änä")],
                          essives_plural      = [sisimp + s("inä")],
                          translative         =  sisimm + s("äksi"),
                          translatives_plural = [sisimm + s("iksi")],
                          abessive            =  sisimm + s("ättä"),
                          abessives_plural    = [sisimm + s("ittä")],
                          instructives_plural = [sisimm + s("in")],
                          comitatives_plural  = [sisimp + s("ine")])
