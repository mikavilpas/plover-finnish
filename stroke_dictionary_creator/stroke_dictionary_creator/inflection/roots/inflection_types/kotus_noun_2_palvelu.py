from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_2_palvelu(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    inflections: InflectionInfo = kotus_noun_1_valo(word, gradation_fn)
    word_alt = gradation_fn(word)

    return inflections._replace(genitives_plural  = [word + "jen",
                                                     word_alt + "iden",
                                                     word_alt + "itten"],
                                partitives_plural = [word_alt + s("ita"),
                                                     word + s("ja")],
                                accusative_plural = word_alt + "t",
                                accusatives       = [word,
                                                     word_alt + "n"])
