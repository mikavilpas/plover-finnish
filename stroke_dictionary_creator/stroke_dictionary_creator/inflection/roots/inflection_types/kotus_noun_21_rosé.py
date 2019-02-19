from .base import *

def kotus_noun_21_rosé(word, gradation_fn = identity):
    # Foreign words ending in a vowel; no consonant gradation.
    # Endings are attached directly to the word.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/ros%C3%A9

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    return InflectionInfo(nominative          =  word,
                          nominative_plural   =  word + s("t"),
                          genitive            =  word + s("n"),
                          genitives_plural    = [word + s("iden"),
                                                 word + s("itten")],
                          partitives          = [word + s("ta")],
                          partitives_plural   = [word + s("ita")],
                          accusatives         = [word,
                                                 word + s("n")],
                          accusative_plural   =  word + s("t"),
                          inessive            =  word + s("ssa"),
                          inessives_plural    = [word + s("issa")],
                          elative             =  word + s("sta"),
                          elatives_plural     = [word + s("ista")],
                          illatives           = [word + s("en")],
                          illatives_plural    = [word + s("ihin"),
                                                 word + s("ihin")],
                          adessive            =  word + s("lla"),
                          adessives_plural    = [word + s("illa")],
                          ablative            =  word + s("lta"),
                          ablatives_plural    = [word + s("ilta")],
                          allative            =  word + s("lle"),
                          allatives_plural    = [word + s("ille")],
                          essives             = [word + s("na")],
                          essives_plural      = [word + s("ina")],
                          translative         =  word + s("ksi"),
                          translatives_plural = [word + s("iksi")],
                          abessive            =  word + s("tta"),
                          abessives_plural    = [word + s("itta")],
                          instructives_plural = [word + s("in")],
                          comitatives_plural  = [word + s("ine")])
