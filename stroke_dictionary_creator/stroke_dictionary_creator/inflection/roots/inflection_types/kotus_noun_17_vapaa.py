from .base import *
from .kotus_noun_13_katiska import kotus_noun_13_katiska

def kotus_noun_17_vapaa(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in a double vowel
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    print(root)
    v = end_vowel

    reference = kotus_noun_13_katiska(word, gradation_fn)
    return reference._replace(nominative_plural   = root_alt + v + s("t"),
                              genitive            = root_alt + v + s("n"),
                              genitives_plural    = [root + s("iden"),
                                                     root + s("itten")],
                              partitives          = [root + v + s("ta")],
                              partitives_plural   = [root + s("ita")],
                              accusative_plural   = root_alt + v + s("t"),
                              inessives_plural    = [root_alt + s("issa")],
                              elatives_plural     = [root_alt + s("ista")],
                              illative            = root + v + s("seen"),
                              illatives_plural    = [root + s("isiin")],
                              adessives_plural    = [root_alt + s("illa")],
                              ablatives_plural    = [root_alt + s("ilta")],
                              allatives_plural    = [root_alt + s("ille")],
                              essives_plural      = [root + s("ina")],
                              translatives_plural = [root_alt + s("iksi")],
                              abessives_plural    = [root_alt + s("itta")],
                              instructives_plural = [root_alt + s("in")],
                              comitatives_plural  = [root + s("ine")],)
