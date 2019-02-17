from .base import *
from .kotus_noun_45_kahdeksas import kotus_noun_45_kahdeksas

def kotus_noun_46_tuhat(word, gradation_fn = identity):
    # The word tuhat only, and its compound words; consonant gradation in the
    # inflectional stem.
    #
    # Declension is the same as kahdeksas, except for the ending of the
    # nominative, and a rare genitive plural.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/tuhat

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    tuhat       = word
    (tuh, a, t) = reverse_parse(word, root_and_vc_ending)
    tuhan       = tuh + a + "n"

    reference = kotus_noun_45_kahdeksas(word, gradation_fn)

    return reference._replace(genitives_plural = [tuhan + s("sien"),
                                                  tuhan + s("ten")])
