from .base import *

def kotus_noun_43_ohut(word, gradation_fn = identity):
    # Nominals ending with -ut/-yt; inverse consonant gradation possible.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/ohut

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # immyt is not supported by joukahainen but is listed on the link above.
    # Better make sure we can support gradation and use immyt.
    immyt               = word
    (im, m, y, t)       = reverse_parse(word, root_and_cvc_ending)
    (im_alt, p, _y, _t) = reverse_parse(gradation_fn(word), root_and_cvc_ending)
    impy = im_alt + p + y

    return InflectionInfo(nominative          =  immyt,
                          nominative_plural   =  impy + s("et"),
                          genitive            =  impy + s("en"),
                          genitives_plural    = [impy + s("iden"),
                                                 impy + s("itten")],
                          partitives          = [immyt + s("tä")],
                          partitives_plural   = [impy + s("itä")],
                          accusatives         = [immyt,
                                                 impy + s("en")],
                          accusative_plural   =  impy + s("et"),
                          inessive            =  impy + s("essä"),
                          inessives_plural    = [impy + s("issä")],
                          elative             =  impy + s("estä"),
                          elatives_plural     = [impy + s("istä")],
                          illatives           = [impy + s("een")],
                          illatives_plural    = [impy + s("isiin"),
                                                 impy + s("ihin")],
                          adessive            =  impy + s("ellä"),
                          adessives_plural    = [impy + s("illä")],
                          ablative            =  impy + s("eltä"),
                          ablatives_plural    = [impy + s("iltä")],
                          allative            =  impy + s("elle"),
                          allatives_plural    = [impy + s("ille")],
                          essives             = [impy + s("enä")],
                          essives_plural      = [impy + s("inä")],
                          translative         =  impy + s("eksi"),
                          translatives_plural = [impy + s("iksi")],
                          abessive            =  impy + s("että"),
                          abessives_plural    = [impy + s("ittä")],
                          instructives_plural = [impy + s("in")],
                          comitatives_plural  = [impy + s("ine")])
