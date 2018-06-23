from .base import *

def kotus_noun_31_kaksi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in some consonant and "si".
    # Only 3 words in this class in the kotus wordlist!

    # no gradation in this class.
    kaksi = word

    (ka, k, s_, i) = reverse_parse(kaksi, root_and_ccv_ending)
    kah   = ka + s("h")
    kahde = kah + s("de")
    kaks  = ka + k + s_

    return InflectionInfo(nominative          = kaksi,
                          nominative_plural   = kahde + s("t"),
                          genitive            = kahde + s("n"),
                          genitives_plural    = [kaks + s("ien")],
                          partitives          = [kah + s("ta")],
                          partitives_plural   = [kaks + s("ia")],
                          accusatives         = [kaksi,
                                                kahde + s("n")],
                          accusative_plural   = kahde + s("t"),
                          inessive            = kahde + s("ssa"),
                          inessives_plural    = [kaks + s("issa")],
                          elative             = kahde + s("sta"),
                          elatives_plural     = [kaks + s("ista")],
                          illatives           = [kah + s("teen")],
                          illatives_plural    = [kaks + s("iin")],
                          adessive            = kahde + s("lla"),
                          adessives_plural    = [kaks + s("illa")],
                          ablative            = kahde + s("lta"),
                          ablatives_plural    = [kaks + s("ilta")],
                          allative            = kahde + s("lle"),
                          allatives_plural    = [kaks + s("ille")],
                          essives             = [kah + s("tena")],
                          essives_plural      = [kaks + s("ina")],
                          translative         = kahde + s("ksi"),
                          translatives_plural = [kaks + s("iksi")],
                          abessive            = kahde + s("tta"),
                          abessives_plural    = [kaks + s("itta")],
                          instructives_plural = [kaks + s("in")],
                          comitatives_plural  = [kaks + s("ine")])
