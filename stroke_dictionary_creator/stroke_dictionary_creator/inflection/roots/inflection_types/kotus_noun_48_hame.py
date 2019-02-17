from .base import *

def kotus_noun_48_hame(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    aie = word
    (ai, e) = reverse_parse(word, root_and_end_vowel)
    (aik, _e) = reverse_parse(gradation_fn(word), root_and_end_vowel)

    return InflectionInfo(nominative          =  aie,
                          nominative_plural   =  aik + s("eet"),
                          genitive            =  aik + s("een"),
                          genitives_plural    = [aik + s("eiden"),
                                                 aik + s("eitten")],
                          partitives          = [aie + s("tta")],
                          partitives_plural   = [aik + s("eita")],
                          accusatives         = [aie,
                                                 aik + s("een")],
                          accusative_plural   =  aik + s("eet"),
                          inessive            =  aik + s("eessa"),
                          inessives_plural    = [aik + s("eissa")],
                          elative             =  aik + s("eesta"),
                          elatives_plural     = [aik + s("eista")],
                          illatives           = [aik + s("eeseen")],
                          illatives_plural    = [aik + s("eisiin"),
                                                 aik + s("eihin")],
                          adessive            =  aik + s("eella"),
                          adessives_plural    = [aik + s("eilla")],
                          ablative            =  aik + s("eelta"),
                          ablatives_plural    = [aik + s("eilta")],
                          allative            =  aik + s("eelle"),
                          allatives_plural    = [aik + s("eille")],
                          essives             = [aik + s("eena")],
                          essives_plural      = [aik + s("eina")],
                          translative         =  aik + s("eeksi"),
                          translatives_plural = [aik + s("eiksi")],
                          abessive            =  aik + s("eetta"),
                          abessives_plural    = [aik + s("eitta")],
                          instructives_plural = [aik + s("ein")],
                          comitatives_plural  = [aik + s("eine")])
