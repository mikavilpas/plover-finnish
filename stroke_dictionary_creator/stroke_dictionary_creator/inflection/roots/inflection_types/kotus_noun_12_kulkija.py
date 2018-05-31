from .base import *
from .kotus_noun_11_omena import kotus_noun_11_omena

def kotus_noun_12_kulkija(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "a" or "ä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    reference = kotus_noun_11_omena(word, gradation_fn)

    return reference._replace(genitives_plural    = [root + s("oiden"),
                                                     root + s("oitten"),
                                                     root + s("ain")],
                              partitives_plural   = [root + s("oita")],
                              inessives_plural    = [root + s("oissa")],
                              elatives_plural     = [root + s("oista")],
                              illatives_plural    = [root + s("oihin")],
                              adessives_plural    = [root + s("oilla")],
                              ablatives_plural    = [root + s("oilta")],
                              allatives_plural    = [root + s("oille")],
                              essives_plural      = [root + s("oina")],
                              translatives_plural = [root + s("oiksi")],
                              abessives_plural    = [root + s("oitta")],
                              instructives_plural = [root + s("oin")],
                              comitatives_plural  = [root + s("oine")])

    # there are no words in the kotus wordlist with gradition in this class
