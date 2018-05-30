from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_2_palvelu(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group(word, text)

    inflections = kotus_noun_1_valo(word, gradation_fn)
    return inflections._replace(genitives_plural = [word + "jen",
                                                    word + "iden",
                                                    word + "itten"],
                                partitives_plural = [word + s("ita"),
                                                     word + s("ja")],
                                accusative_plural = word + "t")
