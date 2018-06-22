from .base import *

def kotus_noun_28_kynsi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in some consonant and "si", and the consonant
    # is used in the inflections.

    # no gradation in this class.
    kynsi = word
    (ky, n, s_, i) = reverse_parse(kynsi, root_and_ccv_ending)
    kyn   = ky + n
    kyns  = kyn + s_
    kynne = kyn + n + s("e")

    return InflectionInfo(nominative          = kynsi,
                          nominative_plural   = kynne + s("t"),
                          genitive            = kynne + s("n"),
                          genitives_plural    = [kyns + s("ien"),
                                                kyn + s("tten")],
                          partitives          = [kyn + s("ttä")],
                          partitives_plural   = [kyns + s("iä")],
                          accusatives         = [kynsi,
                                                kynne + s("n")],
                          accusative_plural   = kynne + s("t"),
                          inessive            = kynne + s("ssä"),
                          inessives_plural    = [kyns + s("issä")],
                          elative             = kynne + s("stä"),
                          elatives_plural     = [kyns + s("istä")],
                          illatives           = [kyn + s("teen")],
                          illatives_plural    = [kyns + s("iin")],
                          adessive            = kynne + s("llä"),
                          adessives_plural    = [kyns + s("illä")],
                          ablative            = kynne + s("ltä"),
                          ablatives_plural    = [kyns + s("iltä")],
                          allative            = kynne + s("lle"),
                          allatives_plural    = [kyns + s("ille")],
                          essives             = [kyn + s("tenä")],
                          essives_plural      = [kyns + s("inä")],
                          translative         = kynne + s("ksi"),
                          translatives_plural = [kyns + s("iksi")],
                          abessive            = kynne + s("ttä"),
                          abessives_plural    = [kyns + s("ittä")],
                          instructives_plural = [kyns + s("in")],
                          comitatives_plural  = [kyns + s("ine")])
