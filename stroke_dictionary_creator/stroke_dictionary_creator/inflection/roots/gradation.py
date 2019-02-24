#
# Definitions for the more machine readable Joukahainen mappings into the
# (could be argued) more understandable Kotus system for gradation classes.

from parsy import *
from .parse_utils import reverse, reverse_parse
from .tokens import *

from .gradation_helpers import gradator, gradate_kotus_d_joukahainen_av6_aie_aikeen, reference_options, matching_gradations

# Main function for gradating
def gradate_joukahainen(word, refword, gradation_class):
    gradations = reference_options(word, refword)
    matching = matching_gradations(word, gradation_class, gradations)

    if len(matching) == 0:
        raise ValueError("The gradation class {} is unknown/invalid for the word {}."
                         .format(gradation_class, word))
    gradtype = matching[0]

    gradator_fn = gradation_dispatch[gradation_class][gradtype]
    gradated_word = gradator_fn(word)

    return gradated_word

gradation_dispatch = dict(
    # the gradations have the same keys as defined in hfconv
    av1 = dict(
        # strong to weak
        uku = gradator("uku", "uvu"), # kotus M
        yky = gradator("yky", "yvy"), # kotus M (again)
        tt  = gradator("tt",  "t"),   # kotus C
        pp  = gradator("pp",  "p"),   # kotus B
        kk  = gradator("kk",  "k"),   # kotus A
        mp  = gradator("mp",  "mm"),  # kotus H
        nt  = gradator("nt",  "nn"),  # kotus J
        lt  = gradator("lt",  "ll"),  # kotus I
        rt  = gradator("rt",  "rr"),  # kotus K
        nk  = gradator("nk",  "ng"),  # kotus G
        p   = gradator("p",   "v"),   # kotus E
        t   = gradator("t",   "d"),   # kotus F
    ),
    av2 = dict(
        # weak to strong
        mm = gradator("mm", "mp"), # kotus H
        nn = gradator("nn", "nt"), # kotus J
        ll = gradator("ll", "lt"), # kotus I
        rr = gradator("rr", "rt"), # kotus K
        ng = gradator("ng", "nk"), # kotus G
        b = gradator("b",  "bb"),  # kind of like kotus B. (lobata -> lobbaan)
        g = gradator("g",  "gg"),  # kind of like kotus B. (digata -> diggaan)
        t = gradator("t",  "tt"),  # kotus C
        p = gradator("p",  "pp"),  # kotus B
        k = gradator("k",  "kk"),  # kotus A
        v = gradator("v",  "p"),   # kotus E
        d = gradator("d",  "t"),   # kotus F
    ),
    av3 = {"k>j": gradator("k", "j")}, # kotus L, strong to weak
    av4 = {"j>k": gradator("j", "k")}, # kotus L, weak to strong
    av5 = {"k>" : gradator("k", "")},  # kotus D, strong to weak

    # kotus D, weak (nonexisting) to strong
    av6 = {">k" : gradate_kotus_d_joukahainen_av6_aie_aikeen}
)

# some of the gradations have to be set in stone because they are needed for
# the creation of infinitives, and they are useful in tests as well.
gradate_kotus_a_takki_takin      = gradation_dispatch["av1"]["kk"]
gradate_kotus_a_hake_hakkeen     = gradation_dispatch["av2"]["k"]
gradate_kotus_b_kaappi_kaapin    = gradation_dispatch["av1"]["pp"]
gradate_kotus_c_tyttö_tytön      = gradation_dispatch["av1"]["tt"]
gradate_kotus_c_kate_katteen     = gradation_dispatch["av2"]["t"]
gradate_kotus_d_reikä_reiän      = gradation_dispatch["av5"]["k>"]
gradate_kotus_e_sopu_sovun       = gradation_dispatch["av1"]["p"]
gradate_kotus_e_taive_taipeen    = gradation_dispatch["av2"]["v"]
gradate_kotus_f_satu_sadun       = gradation_dispatch["av1"]["t"]
gradate_kotus_f_keidas_keitaan   = gradation_dispatch["av2"]["d"]
gradate_kotus_g_aurinko_auringon = gradation_dispatch["av1"]["nk"]
gradate_kotus_g_rengas_renkaan   = gradation_dispatch["av2"]["ng"]
gradate_kotus_i_ilta_illan       = gradation_dispatch["av1"]["lt"]
gradate_kotus_j_hento_hennon     = gradation_dispatch["av1"]["nt"]
gradate_kotus_h_kumpi_kumman     = gradation_dispatch["av1"]["mp"]
gradate_kotus_h_lumme_lumpeen    = gradation_dispatch["av2"]["mm"]
gradate_kotus_i_ilta_illan       = gradation_dispatch["av1"]["lt"]
gradate_kotus_k_virta_virran     = gradation_dispatch["av1"]["rt"]
gradate_kotus_l_arki_arjen       = gradation_dispatch["av3"]["k>j"]

identity = lambda a: a
