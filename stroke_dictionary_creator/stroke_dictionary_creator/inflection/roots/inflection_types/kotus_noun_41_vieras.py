from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_41_vieras(word, gradation_fn = identity):
    # Nominals ending with -s; inverse consonant gradation possible.
    #
    # The final -s of the nominative and partitive singular is replaced by the
    # preceding vowel in the inflectional stem. Partitive ending -ta/-tä and
    # genitive plural ending -iden/itten.
    #
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/vieras

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    keidas               = word
    (kei, d, a, s_)      = reverse_parse(word, root_and_optional_X_vc_ending)
    (kei_alt, t, _a, _s) = reverse_parse(gradation_fn(word),
                                         root_and_optional_X_vc_ending)
    # a will change to e and ä in different words!
    aa                   = a + a
    keit                 = kei_alt + t
    keid                 = kei + d

    return InflectionInfo(nominative          =  keidas,
                          nominative_plural   =  keit + aa + s("t"),
                          genitive            =  keit + aa + s("n"),
                          genitives_plural    = [keit + a  + s("iden"),
                                                 keit + a  + s("itten")],
                          partitives          = [keid + a  + s("sta")],
                          partitives_plural   = [keit + a  + s("ita")],
                          accusatives         = [keidas,
                                                 keit + aa + s("n")],
                          accusative_plural   =  keit + aa + s("t"),
                          inessive            =  keit + aa + s("ssa"),
                          inessives_plural    = [keit + a  + s("issa")],
                          elative             =  keit + aa + s("sta"),
                          elatives_plural     = [keit + a  + s("ista")],
                          illatives           = [keit + aa + s("seen")],
                          illatives_plural    = [keit + a  + s("isiin"),
                                                 keit + a  + s("ihin")],
                          adessive            =  keit + aa + s("lla"),
                          adessives_plural    = [keit + a  + s("illa")],
                          ablative            =  keit + aa + s("lta"),
                          ablatives_plural    = [keit + a  + s("ilta")],
                          allative            =  keit + aa + s("lle"),
                          allatives_plural    = [keit + a  + s("ille")],
                          essives             = [keit + aa + s("na")],
                          essives_plural      = [keit + a  + s("ina")],
                          translative         =  keit + aa + s("ksi"),
                          translatives_plural = [keit + a  + s("iksi")],
                          abessive            =  keit + aa + s("tta"),
                          abessives_plural    = [keit + a  + s("itta")],
                          instructives_plural = [keit + a  + s("in")],
                          comitatives_plural  = [keit + a  + s("ine")])
