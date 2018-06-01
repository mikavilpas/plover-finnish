from .base import *
from .kotus_noun_13_katiska import kotus_noun_13_katiska

def kotus_noun_15_korkea(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "a" or "ä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_13_katiska(word, gradation_fn)
    return reference._replace(nominative_plural   = root_alt + v + "t",
                              genitives_plural    = [root_alt + s("iden"),
                                                     root_alt + s("itten"),
                                                     root + s("ain")],
                              partitives          = [root + s("ata"), root + s("aa")],
                              partitives_plural   = [root_alt + s("ita")],
                              inessives_plural    = [root_alt + s("issa")],
                              elatives_plural     = [root_alt + s("ista")],
                              illatives_plural    = [root_alt + s("isiin"),
                                                     root_alt + s("ihin")],
                              adessives_plural    = [root_alt + s("illa")],
                              ablatives_plural    = [root_alt + s("ilta")],
                              allatives_plural    = [root_alt + s("ille")],
                              essives_plural      = [root_alt + s("ina")],
                              translatives_plural = [root_alt + s("iksi")],
                              abessives_plural    = [root_alt + s("itta")],
                              instructives_plural = [root_alt + s("in")],
                              comitatives_plural  = [root_alt + s("ine")],)
