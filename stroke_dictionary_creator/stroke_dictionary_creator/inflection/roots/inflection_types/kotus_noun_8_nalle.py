from .base import *

def kotus_noun_8_nalle(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("e"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("e"))

    # all words in the kotus wordlist for this class use the e vowel at the
    # end, it seems
    return InflectionInfo(nominative         = word,
                          nominative_plural  = root_alt + s("et"),
                          genitive           = root_alt + s("en"),
                          genitives_plural   = [root + s("ejen"),
                                                root + s("ein")],
                          partitive          = root + s("ea"),
                          partitives_plural  = [root + s("eja")],
                          accusatives        = [word,
                                                root_alt + s("en")],
                          accusative_plural  = root_alt + s("et"),
                          inessive           = root_alt + s("essa"),
                          inessive_plural    = root_alt + s("eissa"),
                          elative            = root_alt + s("esta"),
                          elative_plural     = root_alt + s("eista"),
                          illative           = root + s("een"),
                          illatives_plural   = [root + s("eihin")],
                          adessive           = root_alt + s("ella"),
                          adessive_plural    = root_alt + s("eilla"),
                          ablative           = root_alt + s("elta"),
                          ablative_plural    = root_alt + s("eilta"),
                          allative           = root_alt + s("elle"),
                          allative_plural    = root_alt + s("eille"),
                          essive             = root + s("ena"),
                          essive_plural      = root + s("eina"),
                          translative        = root_alt + s("eksi"),
                          translative_plural = root_alt + s("eiksi"),
                          abessive           = root_alt + s("etta"),
                          abessive_plural    = root_alt + s("eitta"),
                          instructive_plural = root_alt + s("ein"),
                          comitative_plural  = root + s("eine"))
