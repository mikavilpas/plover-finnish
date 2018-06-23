from .base import *

def kotus_noun_30_veitsi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in some consonant and "si".
    # Only 2 words in this class in the kotus wordlist!

    # no gradation in this class.
    veitsi = word

    (vei, t, s_, i) = reverse_parse(veitsi, root_and_ccv_ending)
    veis   = vei + s_
    veit   = vei + t
    veits  = veit + s_
    veitse = veits + s("e")

    return InflectionInfo(nominative          = veitsi,
                          nominative_plural   = veitse + s("t"),
                          genitive            = veitse + s("n"),
                          genitives_plural    = [veits + s("ien"),
                                                veis + s("ten")],
                          partitives          = [veis + s("ta")],
                          partitives_plural   = [veits + s("ia")],
                          accusatives         = [veitsi,
                                                veitse + s("n")],
                          accusative_plural   = veitse + s("t"),
                          inessive            = veitse + s("ssa"),
                          inessives_plural    = [veits + s("issa")],
                          elative             = veitse + s("sta"),
                          elatives_plural     = [veits + s("ista")],
                          illatives           = [veits + s("een")],
                          illatives_plural    = [veits + s("iin")],
                          adessive            = veitse + s("lla"),
                          adessives_plural    = [veits + s("illa")],
                          ablative            = veitse + s("lta"),
                          ablatives_plural    = [veits + s("ilta")],
                          allative            = veitse + s("lle"),
                          allatives_plural    = [veits + s("ille")],
                          essives             = [veits + s("ena")],
                          essives_plural      = [veits + s("ina")],
                          translative         = veitse + s("ksi"),
                          translatives_plural = [veits + s("iksi")],
                          abessive            = veitse + s("tta"),
                          abessives_plural    = [veits + s("itta")],
                          instructives_plural = [veits + s("in")],
                          comitatives_plural  = [veits + s("ine")])
