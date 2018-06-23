from .base import *

def kotus_noun_29_lapsi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in some consonant and "si".
    # Only 3 words in this class in the kotus wordlist!

    # no gradation in this class.
    lapsi = word

    (la, p, s_, i) = reverse_parse(lapsi, root_and_ccv_ending)

    las   = la + s_
    laps  = la + p + s_
    lapse = laps + s("e")

    return InflectionInfo(nominative          = lapsi,
                          nominative_plural   = lapse + s("t"),
                          genitive            = lapse + s("n"),
                          genitives_plural    = [laps + s("ien"),
                                                las + s("ten")],
                          partitives          = [las + s("ta")],
                          partitives_plural   = [laps + s("ia")],
                          accusatives         = [lapsi,
                                                lapse + s("n")],
                          accusative_plural   = lapse + s("t"),
                          inessive            = lapse + s("ssa"),
                          inessives_plural    = [laps + s("issa")],
                          elative             = lapse + s("sta"),
                          elatives_plural     = [laps + s("ista")],
                          illatives           = [laps + s("een")],
                          illatives_plural    = [laps + s("iin")],
                          adessive            = lapse + s("lla"),
                          adessives_plural    = [laps + s("illa")],
                          ablative            = lapse + s("lta"),
                          ablatives_plural    = [laps + s("ilta")],
                          allative            = lapse + s("lle"),
                          allatives_plural    = [laps + s("ille")],
                          essives             = [laps + s("ena")],
                          essives_plural      = [laps + s("ina")],
                          translative         = lapse + s("ksi"),
                          translatives_plural = [laps + s("iksi")],
                          abessive            = lapse + s("tta"),
                          abessives_plural    = [laps + s("itta")],
                          instructives_plural = [laps + s("in")],
                          comitatives_plural  = [laps + s("ine")])
