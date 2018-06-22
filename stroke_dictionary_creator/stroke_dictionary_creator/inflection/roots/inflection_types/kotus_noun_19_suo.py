from .base import *

def kotus_noun_19_suo(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in a double vowel
    # and most start with a consonant, but not all ("yö" does not)
    (c, _, v) = optional_consonant_double_vowel.parse(word)
    alt = (c or "") + v

    return InflectionInfo(nominative          = word,
                          nominative_plural   = word + s("t"),
                          genitive            = word + s("n"),
                          genitives_plural    = [alt + s("iden"),
                                                alt + s("itten")],
                          partitives          = [word + s("ta")],
                          partitives_plural   = [alt + s("ita")],
                          accusatives         = [word,
                                                word + s("n")],
                          accusative_plural   = word + s("t"),
                          inessive            = word + s("ssa"),
                          inessives_plural    = [alt + s("issa")],
                          elative             = word + s("sta"),
                          elatives_plural     = [alt + s("ista")],
                          illatives           = [word + s("hon")],
                          illatives_plural    = [alt + s("ihin")],
                          adessive            = word + s("lla"),
                          adessives_plural    = [alt + s("illa")],
                          ablative            = word + s("lta"),
                          ablatives_plural    = [alt + s("ilta")],
                          allative            = word + s("lle"),
                          allatives_plural    = [alt + s("ille")],
                          essives             = [word + s("na")],
                          essives_plural      = [alt + s("ina")],
                          translative         = word + s("ksi"),
                          translatives_plural = [alt + s("iksi")],
                          abessive            = word + s("tta"),
                          abessives_plural    = [alt + s("itta")],
                          instructives_plural = [alt + s("in")],
                          comitatives_plural  = [alt + s("ine")])
