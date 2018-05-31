from .base import *

def kotus_noun_10_koira(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("a"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("a"))
    v = end_vowel

    # all words in the kotus wordlist for this class use the e vowel at the
    # end, it seems
    return InflectionInfo(nominative         = word,
                          nominative_plural  = root_alt + v + s("t"),
                          genitive           = root_alt + v + s("n"),
                          genitives_plural   = [root + s("ien"),
                                                root + v + s("in")],
                          partitive          = root + v + s("a"),
                          partitives_plural  = [root + s("ia")],
                          accusatives        = [word,
                                                root_alt + v + s("n")],
                          accusative_plural  = root_alt + v + s("t"),
                          inessive           = root_alt + v + s("ssa"),
                          inessive_plural    = root_alt + s("issa"),
                          elative            = root_alt + v + s("sta"),
                          elative_plural     = root_alt + s("ista"),
                          illative           = root + v + s("an"),
                          illatives_plural   = [root + s("iin")],
                          adessive           = root_alt + v + s("lla"),
                          adessive_plural    = root_alt + s("illa"),
                          ablative           = root_alt + v + s("lta"),
                          ablative_plural    = root_alt + s("ilta"),
                          allative           = root_alt + v + s("lle"),
                          allative_plural    = root_alt + s("ille"),
                          essive             = root + v + s("na"),
                          essive_plural      = root + s("ina"),
                          translative        = root_alt + v + s("ksi"),
                          translative_plural = root_alt + s("iksi"),
                          abessive           = root_alt + v + s("tta"),
                          abessive_plural    = root_alt + s("itta"),
                          instructive_plural = root_alt + s("in"),
                          comitative_plural  = root + s("ine"))
