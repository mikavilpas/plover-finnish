from .base import *
from .kotus_noun_6_paperi import kotus_noun_6_paperi

def kotus_noun_7_ovi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))

    return InflectionInfo(nominative         = word,
                          nominative_plural  = root + s("et"),
                          genitive           = root + s("en"),
                          genitives_plural   = [root + s("ien")],
                          partitive          = root + s("ea"),
                          partitives_plural  = [root + end_vowel + s("a")],
                          accusatives        = [word, root + s("en")],
                          accusative_plural  = root + s("et"),
                          inessive           = root + s("essa"),
                          inessive_plural    = root + end_vowel + s("ssa"),
                          elative            = root + s("esta"),
                          elative_plural     = root + end_vowel + s("sta"),
                          illative           = root + s("een"),
                          illatives_plural   = [root + end_vowel + s("in")],
                          adessive           = root + s("ella"),
                          adessive_plural    = root + s("illa"),
                          ablative           = root + s("elta"),
                          ablative_plural    = root + s("ilta"),
                          allative           = root + s("elle"),
                          allative_plural    = root + s("ille"),
                          essive             = root + s("ena"),
                          essive_plural      = root + s("ina"),
                          translative        = root + s("eksi"),
                          translative_plural = root + s("iksi"),
                          abessive           = root + s("etta"),
                          abessive_plural    = root + s("itta"),
                          instructive_plural = root + s("in"),
                          comitative_plural  = root + s("ine"))
