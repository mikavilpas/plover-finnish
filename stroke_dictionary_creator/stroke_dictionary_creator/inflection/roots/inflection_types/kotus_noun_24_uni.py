from .base import *
from .kotus_noun_23_lohi import kotus_noun_23_lohi

def kotus_noun_24_uni(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in "i".
    # There is no gradation in this class.
    uni = word
    (un, i) = reverse_parse(uni, root_and_end_vowel)

    reference = kotus_noun_23_lohi(uni, gradation_fn)._replace(
        genitives_plural = [un + s("ien"),
                            un + s("ten")],
        essives = [un + s("ena"),
                   un + s("na")])

    return reference
