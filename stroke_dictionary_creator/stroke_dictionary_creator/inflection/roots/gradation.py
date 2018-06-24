from parsy import *
from .parse_utils import reverse, reverse_parse
from .tokens import *
from toolz import itertoolz

def find(word, substring):
    if substring is None:
        return None
    index = word.find(substring)
    return index if index >= 0 else None

def is_substring_before(word, a, b):
    pos_a = find(word, a)
    pos_b = find(word, b)

    if pos_a is None:
        if pos_b is None:
            # the applied gradation class is likely invalid by programmer mistake
            raise Exception("cannot gradate {} from {} to {}. Neither found in word."\
                            .format(word, a, b))
        return False
    elif pos_b is None:
        return True
    else: # both substrings found in word
        return pos_a <= pos_b

identity = lambda a: a

def gradate(word, a, b):
    word = reverse(word)
    target = reverse(a)
    replacement = reverse(b) if b else None

    if is_substring_before(word, target, replacement):
        word = word.replace(target, replacement or '', 1)
        return reverse(word)
    return None # unsuccessful, caller should try the other way

def gradator(strong, weak):
    def do_gradate(word):
        return gradate(word, strong, weak) \
            or gradate(word, weak, strong)
    return do_gradate

def one_way_gradator(strong, weak):
    def do_gradate(word):
        # This gradation class only works one way!
        result = gradate(word, strong, weak)
        if result is None:
            raise Exception("cannot gradate {} from {} to {}."
                            .format(word, strong, weak))
        return result

    return do_gradate

gradate_kotus_a_takki_takin_hake_hakkeen  = gradator("kk", "k")
gradate_kotus_b_kaappi_kaapin_opas_oppaan = gradator("pp", "p")
gradate_kotus_c_tyttö_tytön_kate_katteen  = gradator("tt", "t")

# gradation d is defined below

gradate_kotus_e_sopu_sovun_taive_taipeen        = gradator("p", "v")
gradate_kotus_f_satu_sadun_keidas_keitaan       = gradator("t", "d")
gradate_kotus_g_aurinko_auringon_rengas_renkaan = gradator("nk", "ng")
gradate_kotus_h_kumpi_kumman_lumme_lumpeen      = gradator("mp", "mm")
gradate_kotus_i_ilta_illan_sivellin_siveltimen  = gradator("lt", "ll")
gradate_kotus_j_hento_hennon_vanne_vanteen      = gradator("nt", "nn")
gradate_kotus_k_virta_virran_porras_portaan     = gradator("rt", "rr")
gradate_kotus_l_arki_arjen_hylje_hylkeen        = gradator("k", "j")
gradate_kotus_m_suku_suvun                      = one_way_gradator("k", "v")


#### Gradation d is more complex, defined below.
# Joukahainen splits the gradation group d into two groups. Here are their
# meanings:
#
# | Joukahainen | Kotus            | Example    |
# | av5         | group d, k -> '' | laki-lait  |
# | av6         | group d, '' -> k | aie-aikeet |
#

gradate_kotus_d_joukahainen_av5_reikä_reiän = one_way_gradator("k", None)

def gradate_kotus_d_joukahainen_av6_aie_aikeen(word) -> str:
    @generate
    def split_double_vowel_with_k():
        end = yield ((vowel + consonant) | consonant).many().concat()
        vowel2 = yield vowel
        vowel1 = yield vowel
        start = yield character.many().concat()

        return end + vowel2 + "k" + vowel1 + start

    return reverse(split_double_vowel_with_k.parse(reverse(word)))
