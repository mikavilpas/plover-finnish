from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_40_kalleus(word, gradation_fn = identity):
    # Nominals ending with -(u)us/-(y)ys — these are mainly nouns formed from
    # nouns and adjectives using the suffix -uus. See also type vastaus.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/kalleus

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    kalleus        = word
    (kalle, u, s_) = reverse_parse(word, root_and_vc_ending)
    kalleu         = kalle + u
    kalleud        = kalle + u + s("d")
    kalleuks       = kalle + u + s("ks")

    return InflectionInfo(nominative          =  kalleus,
                          nominative_plural   =  kalleud + s("et"),
                          genitive            =  kalleud + s("en"),
                          genitives_plural    = [kalleuks + s("ien")],
                          partitives          = [kalleu + s("tta")],
                          partitives_plural   = [kalleuks + s("ia")],
                          accusatives         = [kalleus,
                                                 kalleud + s("en")],
                          accusative_plural   =  kalleud + s("et"),
                          inessive            =  kalleud + s("essa"),
                          inessives_plural    = [kalleuks + s("issa")],
                          elative             =  kalleud + s("esta"),
                          elatives_plural     = [kalleuks + s("ista")],
                          illatives           = [kalleu + s("teen")],
                          illatives_plural    = [kalleuks + s("iin")],
                          adessive            =  kalleud + s("ella"),
                          adessives_plural    = [kalleuks + s("illa")],
                          ablative            =  kalleud + s("elta"),
                          ablatives_plural    = [kalleuks + s("ilta")],
                          allative            =  kalleud + s("elle"),
                          allatives_plural    = [kalleuks + s("ille")],
                          essives             = [kalleu + s("tena")],
                          essives_plural      = [kalleuks + s("ina")],
                          translative         =  kalleud + s("eksi"),
                          translatives_plural = [kalleuks + s("iksi")],
                          abessive            =  kalleud + s("etta"),
                          abessives_plural    = [kalleuks + s("itta")],
                          instructives_plural = [kalleuks + s("in")],
                          comitatives_plural  = [kalleuks + s("ine")])
