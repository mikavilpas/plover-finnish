from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_39_vastaus(word, gradation_fn = identity):
    # Nominals ending with -s — these include nouns formed from verbs using the
    # suffix -us. See also type kalleus.
    #
    # Inflectional stem replaces -s with -kse-, with the -e- dropped before the
    # plural suffix -i-; no consonant gradation.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/vastaus

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    vastaus       = word
    (vasta, u, s_) = reverse_parse(word, root_and_vc_ending)
    vastauks      = vasta + u + s("ks")

    return InflectionInfo(nominative          =  vastaus,
                          nominative_plural   =  vastauks + s("et"),
                          genitive            =  vastauks + s("en"),
                          genitives_plural    = [vastaus + s("ten"),
                                                 vastauks + s("ien")],
                          partitives          = [vastaus + s("ta")],
                          partitives_plural   = [vastauks + s("ia")],
                          accusatives         = [vastaus],
                          accusative_plural   =  vastauks + s("et"),
                          inessive            =  vastauks + s("essa"),
                          inessives_plural    = [vastauks + s("issa")],
                          elative             =  vastauks + s("esta"),
                          elatives_plural     = [vastauks + s("ista")],
                          illatives           = [vastauks + s("een")],
                          illatives_plural    = [vastauks + s("iin")],
                          adessive            =  vastauks + s("ella"),
                          adessives_plural    = [vastauks + s("illa")],
                          ablative            =  vastauks + s("elta"),
                          ablatives_plural    = [vastauks + s("ilta")],
                          allative            =  vastauks + s("elle"),
                          allatives_plural    = [vastauks + s("ille")],
                          essives             = [vastauks + s("ena")],
                          essives_plural      = [vastauks + s("ina")],
                          translative         =  vastauks + s("eksi"),
                          translatives_plural = [vastauks + s("iksi")],
                          abessive            =  vastauks + s("etta"),
                          abessives_plural    = [vastauks + s("itta")],
                          instructives_plural = [vastauks + s("in")],
                          comitatives_plural  = [vastauks + s("ine")])
