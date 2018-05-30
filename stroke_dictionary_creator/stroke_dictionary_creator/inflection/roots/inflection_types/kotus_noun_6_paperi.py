from .base import *
from .kotus_noun_5_risti import kotus_noun_5_risti

def kotus_noun_6_paperi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("i"))

    inflections = kotus_noun_5_risti(word, gradation_fn)
    return inflections._replace(genitives_plural   = [root + s("ien"),
                                                      root + s("eiden"),
                                                      root + s("eitten")],
                                partitive          = root + end_vowel + s("a"),
                                partitives_plural  = [root + s("eita"),
                                                     root + s("eja")],
                                inessive_plural    = root + s("eissa"),
                                elative_plural     = root + s("eista"),
                                illative           = root + end_vowel + end_vowel + s("n"),
                                illatives_plural   = [root + s("eihin")],
                                adessive_plural    = root + s("eilla"),
                                ablative_plural    = root + s("eilta"),
                                allative_plural    = root + s("eille"),
                                essive_plural      = root + s("eina"),
                                translative_plural = root + s("eiksi"),
                                abessive_plural    = root + s("eitta"),
                                instructive_plural = root + s("ein"),
                                comitative_plural  = root + s("eine"))
    return inflections
