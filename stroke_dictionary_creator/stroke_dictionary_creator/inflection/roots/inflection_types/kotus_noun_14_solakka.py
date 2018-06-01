from .base import *
from .kotus_noun_13_katiska import kotus_noun_13_katiska

def kotus_noun_14_solakka(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "kka" or "kkä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_13_katiska(word, gradation_fn)

    return reference._replace(nominative_plural   = root_alt + v + "t",
                              genitives_plural    = [root_alt + s("oiden"),
                                                     root_alt + s("oitten"),
                                                     root + s("ojen"),
                                                     root + s("ain")],
                              partitives_plural   = [root_alt + s("oita"),
                                                     root + s("oja")],
                              inessives_plural    = [root_alt + s("oissa")],
                              elatives_plural     = [root_alt + s("oista")],
                              illatives_plural    = [root_alt + s("oihin")],
                              adessives_plural    = [root_alt + s("oilla")],
                              ablatives_plural    = [root_alt + s("oilta")],
                              allatives_plural    = [root_alt + s("oille")],
                              essives_plural      = [root_alt + s("oina")],
                              translatives_plural = [root_alt + s("oiksi")],
                              abessives_plural    = [root_alt + s("oitta")],
                              instructives_plural = [root_alt + s("oin")],
                              comitatives_plural  = [root_alt + s("oine")],)
