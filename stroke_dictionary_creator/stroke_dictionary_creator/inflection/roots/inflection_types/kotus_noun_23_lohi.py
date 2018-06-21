from .base import *
from .kotus_noun_7_ovi import kotus_noun_7_ovi

def kotus_noun_23_lohi(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    # All words in this class end in "i".
    # There is no gradation in this class.
    lohi = word
    (loh, i) = reverse_parse(lohi, root_and_end_vowel)

    reference = kotus_noun_7_ovi(lohi, gradation_fn)._replace(
        partitives = [loh + s("ta")])

    return reference
