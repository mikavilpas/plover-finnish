from parsy import *
sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group

vowel = char_from("aeiouyäö")
consonant = char_from("bcdfghjklmnpqrstvwxz")
character = vowel | consonant

@generate
def double_consonant():
    c = yield consonant
    yield string(c)
    return c

@generate
def kotus_noun_1_valo_parser():
    v = yield vowel
    rest = yield character.at_least(1).concat()
    return [rest, dict(end_vowel = v)]

# root words are simpler to parse in reverse order
def reverse(s): return s[::-1]

def reverse_parse(word, p):
    return_value = p.parse(reverse(word))
    if len(return_value) == 2:
        (root, data) = return_value
        return (reverse(root), data)
    return reverse(return_value)

from collections import namedtuple

InflectionInfo = namedtuple("InflectionInfo",
                            ["nominative",         "nominative_plural",
                             "genitive",           "genitive_plural",
                             "partitive",          "partitive_plural",
                             "accusatives",        "accusative_plural",
                             "inessive",           "inessive_plural",
                             "elative",            "elative_plural",
                             "illative",           "illative_plural",
                             "adessive",           "adessive_plural",
                             "ablative",           "ablative_plural",
                             "allative",           "allative_plural",
                             "essive",             "essive_plural",
                             "translative",        "translative_plural",
                             "abessive",           "abessive_plural",
                             "instructive_plural",
                             "comitative_plural"])

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

def gradation(word, target, replacement):
    p = replace_first(target, replacement) | replace_first(replacement, target)

    def parser(word):
        return reverse_parse(word, p)
    return parser

def gradation_one_way(word, target, replacement):
    p = replace_first(target, replacement)

    def parser(word):
        return reverse_parse(word, p)
    return parser

gradate_kotus_a_takki_takin_hake_hakkeen  = gradation("kk", "k")
gradate_kotus_b_kaappi_kaapin_opas_oppaan = gradation("pp", "p")
gradate_kotus_c_tyttö_tytön_kate_katteen  = gradation("tt", "t")

# TODO how to know at which position in the word to apply the gradation?
# gradate_kotus_d_reikä_reiän_kate_katteen = gradation("k", "")

gradate_kotus_e_sopu_sovun_taive_taipeen        = gradation("p", "v")
gradate_kotus_f_satu_sadun_keidas_keitaan       = gradation("t", "d")
gradate_kotus_g_aurinko_auringon_rengas_renkaan = gradation("nk", "ng")
gradate_kotus_h_kumpi_kumman_lumme_lumpeen      = gradation("mp", "mm")
gradate_kotus_i_ilta_illan_sivellin_siveltimen  = gradation("lt", "ll")
gradate_kotus_j_hento_hennon_vanne_vanteen      = gradation("nt", "nn")
gradate_kotus_k_virta_virran_porras_portaan     = gradation("rt", "rr")
gradate_kotus_l_arki_arjen_hylje_hylkeen        = gradation("k", "j")
gradate_kotus_m_suku_suvun                      = gradation_one_way("k", "v")

identity = lambda a: a

def kotus_noun_1_valo(word, gradation = identity):
    # suffix
    def s(text): return change_to_same_vowel_group(word, text)

    (root, data) = reverse_parse(word, kotus_noun_1_valo_parser)
    word_alt = gradation(word)

    v = data["end_vowel"]
    return InflectionInfo(nominative         = word,
                          nominative_plural  = word_alt + "t",
                          genitive           = word_alt + "n",
                          genitive_plural    = word + "jen",
                          partitive          = word + s("a"),
                          partitive_plural   = word + s("ja"),
                          accusatives        = [word, word_alt + "n"],
                          accusative_plural  = word + s("ja"),
                          inessive           = word_alt + s("ssa"),
                          inessive_plural    = word_alt + s("issa"),
                          elative            = word_alt + s("sta"),
                          elative_plural     = word_alt + s("ista"),
                          illative           = word + v + "n",
                          illative_plural    = word + "ihin",
                          adessive           = word_alt + s("lla"),
                          adessive_plural    = word_alt + s("illa"),
                          ablative           = word_alt + s("lta"),
                          ablative_plural    = word_alt + s("ilta"),
                          allative           = word_alt + "lle",
                          allative_plural    = word_alt + "ille",
                          essive             = word + s("na"),
                          essive_plural      = word + s("ina"),
                          translative        = word_alt + "ksi",
                          translative_plural = word_alt + "iksi",
                          abessive           = word_alt + s("tta"),
                          abessive_plural    = word_alt + s("itta"),
                          instructive_plural = word_alt + "in",
                          comitative_plural  = word + "ine",
    )
