from parsy import *
from .parse_utils import reverse, reverse_parse
from .tokens import *

identity = lambda a: a

def replace_first(target, replacement):
    target = reverse(target)
    replacement = reverse(replacement)

    @generate
    def replacer():
        p = string(target).should_fail("found " + target) >> character
        start = yield p.at_least(1).concat()
        yield string(target)
        end = yield character.at_least(1).concat()
        return start + replacement + end

    return replacer

def gradation(target, replacement):
    p = replace_first(target, replacement) | replace_first(replacement, target)

    def parser(word):
        return reverse_parse(word, p)
    return parser

def gradation_one_way(target, replacement):
    p = replace_first(target, replacement)

    def parser(word):
        return reverse_parse(word, p)
    return parser

gradate_kotus_a_takki_takin_hake_hakkeen  = gradation("kk", "k")
gradate_kotus_b_kaappi_kaapin_opas_oppaan = gradation("pp", "p")
gradate_kotus_c_tyttö_tytön_kate_katteen  = gradation("tt", "t")

# TODO how to know at which position in the word to apply the gradation?
# gradate_kotus_d_reikä_reiän_aie_aikeen = gradation("k", "")

gradate_kotus_e_sopu_sovun_taive_taipeen        = gradation("p", "v")
gradate_kotus_f_satu_sadun_keidas_keitaan       = gradation("t", "d")
gradate_kotus_g_aurinko_auringon_rengas_renkaan = gradation("nk", "ng")
gradate_kotus_h_kumpi_kumman_lumme_lumpeen      = gradation("mp", "mm")
gradate_kotus_i_ilta_illan_sivellin_siveltimen  = gradation("lt", "ll")
gradate_kotus_j_hento_hennon_vanne_vanteen      = gradation("nt", "nn")
gradate_kotus_k_virta_virran_porras_portaan     = gradation("rt", "rr")
gradate_kotus_l_arki_arjen_hylje_hylkeen        = gradation("k", "j")
gradate_kotus_m_suku_suvun                      = gradation_one_way("k", "v")
