from .base import *

def joukahainen_noun_10_poika(word, gradation_fn = identity):
    # This is marked as the class 10 in kotus, but it is not easy to make the
    # class 10 support the word "poika". So I made this special function to
    # account for this word.

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    poika         = word
    (po, i, k, a) = reverse_parse(word, root_and_vcv_ending)
    poj           = po + "j"
    poja          = poj + s("a")
    poji          = poj + i
    poik          = po + i + k

    return InflectionInfo(nominative          =  poika,
                          nominative_plural   =  poja + s("t"),
                          genitive            =  poja + s("n"),
                          genitives_plural    = [poik + s("ien"),
                                                 poik + a + s("in")],
                          partitives          = [poika + s("a")],
                          partitives_plural   = [poik + s("ia")],
                          accusatives         = [poika,
                                                 poja + s("n")],
                          accusative_plural   =  poja + s("t"),
                          inessive            =  poja + s("ssa"),
                          inessives_plural    = [poji + s("ssa")],
                          elative             =  poja + s("sta"),
                          elatives_plural     = [poji + s("sta")],
                          illatives           = [poika + s("an")],
                          illatives_plural    = [poik + s("iin")],
                          adessive            =  poja + s("lla"),
                          adessives_plural    = [poji + s("lla")],
                          ablative            =  poja + s("lta"),
                          ablatives_plural    = [poji + s("lta")],
                          allative            =  poja + s("lle"),
                          allatives_plural    = [poji + s("lle")],
                          essives             = [poika + s("na")],
                          essives_plural      = [poik + s("ina")],
                          translative         =  poja + s("ksi"),
                          translatives_plural = [poji + s("ksi")],
                          abessive            =  poja + s("tta"),
                          abessives_plural    = [poji + s("tta")],
                          instructives_plural = [poji + s("n")],
                          comitatives_plural  = [poik + s("ine")])
