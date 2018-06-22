from .base import *
from .kotus_noun_23_lohi import kotus_noun_23_lohi

def kotus_noun_25_toimi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in "i".
    # There is no gradation in this class.
    toimi = word
    (toi, m, i) = reverse_parse(toimi, root_and_cv_ending)

    reference = kotus_noun_23_lohi(toimi, gradation_fn)._replace(
        genitives_plural = [toi + s("nten"),
                            toi + m + s("ien")],
        partitives = [toi + s("nta"),
                      toi + m + s("ea")])

    return reference
