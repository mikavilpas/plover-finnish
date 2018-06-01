from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_3_valtio(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    inflections = kotus_noun_1_valo(word, gradation_fn)
    return inflections._replace(genitives_plural = [word + "iden",
                                                    word + "itten"],
                                partitives = [word + s("ta")],
                                partitives_plural = [word + s("ita")],
                                accusative_plural = word + "t")
