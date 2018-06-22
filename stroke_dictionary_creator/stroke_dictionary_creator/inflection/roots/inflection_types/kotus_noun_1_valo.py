from .base import *

def kotus_noun_1_valo(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    word_alt = gradation_fn(word)

    v = end_vowel
    return InflectionInfo(nominative          = word,
                          nominative_plural   = word_alt + "t",
                          genitive            = word_alt + "n",
                          genitives_plural    = [word + "jen"],
                          partitives          = [word + s("a")],
                          partitives_plural   = [word + s("ja")],
                          accusatives         = [word, word_alt + "n"],
                          accusative_plural   = word + s("ja"),
                          inessive            = word_alt + s("ssa"),
                          inessives_plural    = [word_alt + s("issa")],
                          elative             = word_alt + s("sta"),
                          elatives_plural     = [word_alt + s("ista")],
                          illatives           = [word + v + "n"],
                          illatives_plural    = [word + "ihin"],
                          adessive            = word_alt + s("lla"),
                          adessives_plural    = [word_alt + s("illa")],
                          ablative            = word_alt + s("lta"),
                          ablatives_plural    = [word_alt + s("ilta")],
                          allative            = word_alt + "lle",
                          allatives_plural    = [word_alt + "ille"],
                          essives             = [word + s("na")],
                          essives_plural      = [word + s("ina")],
                          translative         = word_alt + "ksi",
                          translatives_plural = [word_alt + "iksi"],
                          abessive            = word_alt + s("tta"),
                          abessives_plural    = [word_alt + s("itta")],
                          instructives_plural = [word_alt + "in"],
                          comitatives_plural  = [word + "ine"],
    )
