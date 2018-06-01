from .base import *
from .kotus_noun_6_paperi import kotus_noun_6_paperi

def kotus_noun_7_ovi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("i"))

    return InflectionInfo(nominative          = word,
                          nominative_plural   = root_alt + s("et"),
                          genitive            = root_alt + s("en"),
                          genitives_plural    = [root + s("ien")],
                          partitives          = [root + s("ea")],
                          partitives_plural   = [root + end_vowel + s("a")],
                          accusatives         = [word, root_alt + s("en")],
                          accusative_plural   = root_alt + s("et"),
                          inessive            = root_alt + s("essa"),
                          inessives_plural    = [root_alt + end_vowel + s("ssa")],
                          elative             = root_alt + s("esta"),
                          elatives_plural     = [root_alt + end_vowel + s("sta")],
                          illative            = root + s("een"),
                          illatives_plural    = [root + end_vowel + s("in")],
                          adessive            = root_alt + s("ella"),
                          adessives_plural    = [root_alt + s("illa")],
                          ablative            = root_alt + s("elta"),
                          ablatives_plural    = [root_alt + s("ilta")],
                          allative            = root_alt + s("elle"),
                          allatives_plural    = [root_alt + s("ille")],
                          essive              = root + s("ena"),
                          essives_plural      = [root + s("ina")],
                          translative         = root_alt + s("eksi"),
                          translatives_plural = [root_alt + s("iksi")],
                          abessive            = root_alt + s("etta"),
                          abessives_plural    = [root_alt + s("itta")],
                          instructives_plural = [root_alt + s("in")],
                          comitatives_plural  = [root + s("ine")])
