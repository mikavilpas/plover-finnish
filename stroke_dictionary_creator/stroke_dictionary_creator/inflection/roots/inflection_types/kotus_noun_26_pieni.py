from .base import *
from .kotus_noun_25_toimi import kotus_noun_25_toimi

def kotus_noun_26_pieni(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in "i".
    # There is no gradation in this class.
    vieri = word
    (vie, r, i) = reverse_parse(vieri, root_and_cv_ending)

    reference = kotus_noun_25_toimi(vieri, gradation_fn)._replace(
        genitives_plural = [vie + r + s("ten"),
                            vie + r + s("ien")],
        partitives = [vie + r + s("ta")])

    return reference
