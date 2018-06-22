from .base import *

def kotus_noun_27_käsi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in "si".
    # There is no gradation in this class.
    käsi = word
    (kä, s_letter, i) = reverse_parse(käsi, root_and_cv_ending)
    käs = kä + s_letter
    käde = kä + s("de")

    return InflectionInfo(nominative          = word,
                          nominative_plural   = käde + s("t"),
                          genitive            = käde + s("n"),
                          genitives_plural    = [käs + s("ien"),
                                                kä + s("tten")],
                          partitives          = [kä + s("ttä")],
                          partitives_plural   = [käs + s("iä")],
                          accusatives         = [word,
                                                käde + s("n")],
                          accusative_plural   = käde + s("t"),
                          inessive            = käde + s("ssä"),
                          inessives_plural    = [käs + s("issä")],
                          elative             = käde + s("stä"),
                          elatives_plural     = [käs + s("istä")],
                          illatives           = [kä + s("teen")],
                          illatives_plural    = [käs + s("iin")],
                          adessive            = käde + s("llä"),
                          adessives_plural    = [käs + s("illä")],
                          ablative            = käde + s("ltä"),
                          ablatives_plural    = [käs + s("iltä")],
                          allative            = käde + s("lle"),
                          allatives_plural    = [käs + s("ille")],
                          essives             = [kä + s("tenä")],
                          essives_plural      = [käs + s("inä")],
                          translative         = käde + s("ksi"),
                          translatives_plural = [käs + s("iksi")],
                          abessive            = käde + s("ttä"),
                          abessives_plural    = [käs + s("ittä")],
                          instructives_plural = [käs + s("in")],
                          comitatives_plural  = [käs + s("ine")])
