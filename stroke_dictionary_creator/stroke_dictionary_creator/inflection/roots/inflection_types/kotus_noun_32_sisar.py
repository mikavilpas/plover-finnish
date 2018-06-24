from .base import *

def kotus_noun_32_sisar(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # the examples use the word ien (gradation d: ien-ikenet)
    ien = word
    iken = gradation_fn(ien)

    (i_strong, k, e, n) = reverse_parse(iken, root_and_cvc_ending)
    ikene = iken + s("e")

    return InflectionInfo(nominative          = ien,
                          nominative_plural   = ikene + s("t"),
                          genitive            = ikene + s("n"),
                          genitives_plural    = [iken + s("ien")],
                          partitives          = [ien + s("tä")],
                          partitives_plural   = [iken + s("iä")],
                          accusatives         = [ien,
                                                 ikene + s("n")],
                          accusative_plural   = ikene + s("t"),
                          inessive            = ikene + s("ssä"),
                          inessives_plural    = [iken + s("issä")],
                          elative             = ikene + s("stä"),
                          elatives_plural     = [iken + s("istä")],
                          illatives           = [iken + s("een")],
                          illatives_plural    = [iken + s("iin")],
                          adessive            = ikene + s("llä"),
                          adessives_plural    = [iken + s("illä")],
                          ablative            = ikene + s("ltä"),
                          ablatives_plural    = [iken + s("iltä")],
                          allative            = ikene + s("lle"),
                          allatives_plural    = [iken + s("ille")],
                          essives             = [iken + s("enä")],
                          essives_plural      = [iken + s("inä")],
                          translative         = ikene + s("ksi"),
                          translatives_plural = [iken + s("iksi")],
                          abessive            = ikene + s("ttä"),
                          abessives_plural    = [iken + s("ittä")],
                          instructives_plural = [iken + s("in")],
                          comitatives_plural  = [iken + s("ine")])
