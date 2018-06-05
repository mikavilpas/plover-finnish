from .base import *
from .kotus_noun_13_katiska import kotus_noun_13_katiska

def kotus_noun_16_vanhempi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "a" or "ä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_13_katiska(word, gradation_fn)
    return reference._replace(nominative_plural   = root_alt + s("at"),
                              genitive            = root_alt + s("an"),
                              genitives_plural    = [root + s("ien"),
                                                     root + s("ain")],
                              partitives          = [root + s("aa")],
                              partitives_plural   = [root + s("ia")],
                              accusatives         = [word,
                                                     root_alt + s("an")],
                              accusative_plural   = root_alt + s("at"),
                              inessive            = root_alt + s("assa"),
                              inessives_plural    = [root_alt + s("issa")],
                              elative             = root_alt + s("asta"),
                              elatives_plural     = [root_alt + s("ista")],
                              illatives           = [root + s("aan")],
                              illatives_plural    = [root + s("iin")],
                              adessive            = root_alt + s("alla"),
                              adessives_plural    = [root_alt + s("illa")],
                              ablative            = root_alt + s("alta"),
                              ablatives_plural    = [root_alt + s("ilta")],
                              allative            = root_alt + s("alle"),
                              allatives_plural    = [root_alt + s("ille")],
                              essive              = root + s("ana"),
                              essives_plural      = [root + s("ina")],
                              translative         = root_alt + s("aksi"),
                              translatives_plural = [root_alt + s("iksi")],
                              abessive            = root_alt + s("atta"),
                              abessives_plural    = [root_alt + s("itta")],
                              instructives_plural = [root_alt + s("in")],
                              comitatives_plural  = [root + s("ine")],)
