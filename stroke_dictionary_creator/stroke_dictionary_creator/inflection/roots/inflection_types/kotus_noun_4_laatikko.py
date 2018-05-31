from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_4_laatikko(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    inflections = kotus_noun_1_valo(word, gradation_fn)
    return inflections._replace(genitives_plural  = [word_alt + "iden",
                                                     word_alt + "itten",
                                                     word + "jen"],
                                partitive         = word + s("a"),
                                partitives_plural = [word + s("ja"),
                                                     word_alt + s("ita")],
                                illative          = word + end_vowel + "n",
                                illatives_plural  = [word + "ihin",
                                                     word_alt + "ihin"],
                                essives_plural    = [word_alt + s("ina")],
                                accusative_plural = word_alt + "t")
