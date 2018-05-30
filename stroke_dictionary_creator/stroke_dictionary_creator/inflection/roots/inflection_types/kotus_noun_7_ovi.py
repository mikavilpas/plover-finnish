from .base import *
from .kotus_noun_6_paperi import kotus_noun_6_paperi

def kotus_noun_7_ovi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("i"))

    return InflectionInfo(nominative         = word,
                          nominative_plural  = root_alt + s("et"),
                          genitive           = root_alt + s("en"),
                          genitives_plural   = [root + s("ien")],
                          partitive          = root + s("ea"),
                          partitives_plural  = [root + end_vowel + s("a")],
                          accusatives        = [word, root_alt + s("en")],
                          accusative_plural  = root_alt + s("et"),
                          inessive           = root_alt + s("essa"),
                          inessive_plural    = root_alt + end_vowel + s("ssa"),
                          elative            = root_alt + s("esta"),
                          elative_plural     = root_alt + end_vowel + s("sta"),
                          illative           = root + s("een"),
                          illatives_plural   = [root + end_vowel + s("in")],
                          adessive           = root_alt + s("ella"),
                          adessive_plural    = root_alt + s("illa"),
                          ablative           = root_alt + s("elta"),
                          ablative_plural    = root_alt + s("ilta"),
                          allative           = root_alt + s("elle"),
                          allative_plural    = root_alt + s("ille"),
                          essive             = root + s("ena"),
                          essive_plural      = root + s("ina"),
                          translative        = root_alt + s("eksi"),
                          translative_plural = root_alt + s("iksi"),
                          abessive           = root_alt + s("etta"),
                          abessive_plural    = root_alt + s("itta"),
                          instructive_plural = root_alt + s("in"),
                          comitative_plural  = root + s("ine"))
