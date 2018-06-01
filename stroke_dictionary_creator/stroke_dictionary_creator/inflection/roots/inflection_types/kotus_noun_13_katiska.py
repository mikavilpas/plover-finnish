from .base import *
from .kotus_noun_12_kulkija import kotus_noun_12_kulkija

def kotus_noun_13_katiska(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "a" or "ä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_12_kulkija(word, gradation_fn)

    return reference._replace(genitives_plural    = [root + s("oiden"),
                                                     root + s("oitten"),
                                                     root + s("ojen"),
                                                     root + s("ain")],
                              partitives_plural   = [root + s("oita"), root + s("oja")])

    # there are no words in the kotus wordlist with gradition in this class
