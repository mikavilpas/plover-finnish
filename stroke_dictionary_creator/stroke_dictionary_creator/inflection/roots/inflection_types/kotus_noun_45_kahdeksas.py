from .base import *

def kotus_noun_45_kahdeksas(word, gradation_fn = identity):
    # Ordinals ending with -s; consonant gradation in the inflectional stem.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/kahdeksas

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    sadas        = word
    (sad, a, s_) = reverse_parse(word, root_and_vc_ending)
    sada         = sad + a
    sadan        = sada + "n"
    sadanne      = sadan + "ne"
    sadansi      = sadan + "si"
    sadante      = sadan + "te"

    return InflectionInfo(nominative          =  sadas,
                          nominative_plural   =  sadanne + s("t"),
                          genitive            =  sadanne + s("n"),
                          genitives_plural    = [sadan + s("sien")],
                          partitives          = [sada + s("tta")],
                          partitives_plural   = [sadan + s("sia")],
                          accusatives         = [sadas,
                                                 sadanne + s("n")],
                          accusative_plural   =  sadanne + s("t"),
                          inessive            =  sadanne + s("ssa"),
                          inessives_plural    = [sadansi + s("ssa")],
                          elative             =  sadanne + s("sta"),
                          elatives_plural     = [sadansi + s("sta")],
                          illatives           = [sadan + s("teen")],
                          illatives_plural    = [sadansi  + s("in")],
                          adessive            =  sadanne + s("lla"),
                          adessives_plural    = [sadansi + s("lla")],
                          ablative            =  sadanne + s("lta"),
                          ablatives_plural    = [sadansi + s("lta")],
                          allative            =  sadanne + s("lle"),
                          allatives_plural    = [sadansi + s("lle")],
                          essives             = [sadante + s("na")],
                          essives_plural      = [sadansi + s("na")],
                          translative         =  sadanne + s("ksi"),
                          translatives_plural = [sadansi + s("ksi")],
                          abessive            =  sadanne + s("tta"),
                          abessives_plural    = [sadansi + s("tta")],
                          instructives_plural = [sadansi + s("n")],
                          comitatives_plural  = [sadansi + s("ne")])
