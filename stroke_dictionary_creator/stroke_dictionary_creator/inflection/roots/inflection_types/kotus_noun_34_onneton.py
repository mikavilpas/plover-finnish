from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_34_onneton(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    (root, *_) = reverse_parse(word, root_and_vc_ending)
    (root_alt, *_) = reverse_parse(word_alt, root_and_vc_ending)

    return InflectionInfo(nominative          = word,
                          nominative_plural   = root_alt + s("omat"),
                          genitive            = root_alt + s("oman"),
                          genitives_plural    = [root_alt + s("omien"),
                                                root + s("onten")],
                          partitives          = [root + s("onta")],
                          partitives_plural   = [root_alt + s("omia")],
                          accusatives         = [word,
                                                root_alt + s("oman")],
                          accusative_plural   = root_alt + s("omat"),
                          inessive            = root_alt + s("omassa"),
                          inessives_plural    = [root_alt + s("omissa")],
                          elative             = root_alt + s("omasta"),
                          elatives_plural     = [root_alt + s("omista")],
                          illatives           = [root_alt + s("omaan")],
                          illatives_plural    = [root_alt + s("omiin")],
                          adessive            = root_alt + s("omalla"),
                          adessives_plural    = [root_alt + s("omilla")],
                          ablative            = root_alt + s("omalta"),
                          ablatives_plural    = [root_alt + s("omilta")],
                          allative            = root_alt + s("omalle"),
                          allatives_plural    = [root_alt + s("omille")],
                          essives             = [root_alt + s("omana")],
                          essives_plural      = [root_alt + s("omina")],
                          translative         = root_alt + s("omaksi"),
                          translatives_plural = [root_alt + s("omiksi")],
                          abessive            = root_alt + s("omatta"),
                          abessives_plural    = [root_alt + s("omitta")],
                          instructives_plural = [root_alt + s("omin")],
                          comitatives_plural  = [root_alt + s("omine")])
