from .base import *

def kotus_noun_33_kytkin(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # the examples use the word paahdin (gradation f: paahdin-paahtimen)
    paahdin = word
    paahtin = gradation_fn(paahdin)

    (paah, d, i, n) = reverse_parse(paahdin, root_and_Xvc_ending)
    (paah, t, _, _) = reverse_parse(paahtin, root_and_Xvc_ending)
    paahdi   = paah + d + i
    paahti   = paah + t + i
    paahtim  = paahti + s("m")
    paahtime = paahti + s("me")
    paahtimi = paahti + s("mi")

    return InflectionInfo(nominative          = paahdin,
                          nominative_plural   = paahtime + s("t"),
                          genitive            = paahtime + s("n"),
                          genitives_plural    = [paahtimi + s("en"),
                                                 paahdi + s("nten")],
                          partitives          = [paahdin + s("ta")],
                          partitives_plural   = [paahtim + s("ia")],
                          accusatives         = [paahdin,
                                                 paahtime + s("n")],
                          accusative_plural   = paahtime + s("t"),
                          inessive            = paahtime + s("ssa"),
                          inessives_plural    = [paahtim + s("issa")],
                          elative             = paahtime + s("sta"),
                          elatives_plural     = [paahtim + s("ista")],
                          illatives           = [paahtim + s("een")],
                          illatives_plural    = [paahtim + s("iin")],
                          adessive            = paahtime + s("lla"),
                          adessives_plural    = [paahtim + s("illa")],
                          ablative            = paahtime + s("lta"),
                          ablatives_plural    = [paahtim + s("ilta")],
                          allative            = paahtime + s("lle"),
                          allatives_plural    = [paahtim + s("ille")],
                          essives             = [paahtim + s("ena"),
                                                 paahdi + n + s("na")],
                          essives_plural      = [paahtim + s("ina")],
                          translative         = paahtime + s("ksi"),
                          translatives_plural = [paahtim + s("iksi")],
                          abessive            = paahtime + s("tta"),
                          abessives_plural    = [paahtim + s("itta")],
                          instructives_plural = [paahtim + s("in")],
                          comitatives_plural  = [paahtim + s("ine")])
