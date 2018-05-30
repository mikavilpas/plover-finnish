from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_5_risti(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("i"))

    return InflectionInfo(nominative         = word,
                          nominative_plural  = root_alt + s("it"),
                          genitive           = root_alt + end_vowel + s("n"),
                          genitives_plural   = [root + end_vowel + s("en")],
                          partitive          = word + s("a"),
                          partitives_plural  = [root + s("eja")],
                          accusatives        = [word, root_alt + end_vowel + s("n")],
                          accusative_plural  = root_alt + end_vowel + s("t"),
                          inessive           = root_alt + end_vowel + s("ssa"),
                          inessive_plural    = root_alt + s("eissa"),
                          elative            = root_alt + end_vowel + s("sta"),
                          elative_plural     = root_alt + s("eista"),
                          illative           = word + end_vowel + s("n"),
                          illatives_plural   = [root + s("eihin")],
                          adessive           = root_alt + end_vowel + s("lla"),
                          adessive_plural    = root_alt + s("eilla"),
                          ablative           = root_alt + end_vowel + s("lta"),
                          ablative_plural    = root_alt + s("eilta"),
                          allative           = root_alt + end_vowel + "lle",
                          allative_plural    = root_alt + s("eille"),
                          essive             = root + s("ina"),
                          essive_plural      = root + s("eina"),
                          translative        = root_alt + "iksi",
                          translative_plural = root_alt + s("eiksi"),
                          abessive           = root_alt + end_vowel + s("tta"),
                          abessive_plural    = root_alt + s("eitta"),
                          instructive_plural = root_alt + s("ein"),
                          comitative_plural  = root + s("eine"),
    )