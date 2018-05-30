from .base import *
from .kotus_noun_1_valo import kotus_noun_1_valo

def kotus_noun_5_risti(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)

    inflections = kotus_noun_1_valo(word, gradation_fn)
    return inflections._replace(genitives_plural   = [word + "en"],
                                partitive          = word + s("a"),
                                partitives_plural  = [root + s("eja")],
                                inessive_plural    = root_alt + s("eissa"),
                                elative_plural     = root_alt + s("eista"),
                                illative           = word + end_vowel + "n",
                                illatives_plural   = [root + "eihin"],
                                adessive_plural    = root_alt + s("eilla"),
                                ablative_plural    = root_alt + s("eilta"),
                                allative_plural    = root_alt + s("eille"),
                                essive_plural      = root + s("eina"),
                                translative_plural = root_alt + s("eiksi"),
                                abessive_plural    = root_alt + s("eitta"),
                                instructive_plural = root_alt + s("ein"),
                                comitative_plural  = root + s("eine"),
                                accusative_plural  = word_alt + "t")
