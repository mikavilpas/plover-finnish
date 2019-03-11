"""Mapping of joukahainen inflection types to those used in kotus."""

from collections import namedtuple
from inflection_types import *
from inflection_types.verbs import *
import gradation as g

NominalInflection = namedtuple("NominalInflection",
                               ["inflection_fn", "gradation_fn"])
Conjugation = namedtuple("Conjugation",
                         ["verb_class", "gradation_fn"])

def infl(fn, gradation_fn = g.identity) -> NominalInflection:
    "Shorthand for the readability of inflection definitions"
    return NominalInflection(inflection_fn = fn,
                             gradation_fn = gradation_fn)

def conj(fn, gradation_fn = g.identity) -> Conjugation:
    return Conjugation(inflection_fn = fn,
                       gradation_fn = gradation_fn)

# TODO check that missing classes are inflected correctly!

joukahainen_refwords = {
    "valo":      infl(kotus_noun_1_valo),
    "arvelu":    infl(kotu_noun_2_palvelu),
    "autio":     infl(kotus_noun_3_valtio),
    "kiiski":    infl(kotus_noun_7_ovi),
    "siisti":    infl(kotus_noun_5_risti),
    "risti":     infl(kotus_noun_5_risti),
    "paperi":    infl(kotus_noun_6_paperi),
    "edam":      infl(kotus_noun_6_paperi),
    "kalsium":   infl(kotus_noun_5_risti),
    "lovi":      infl(kotus_noun_7_ovi),
    "toholampi": infl(kotus_noun_7_ovi, g.gradate_kotus_h_kumpi_kumman),
    "suksi":     infl(kotus_noun_7_ovi),
    "veli":      infl(kotus_noun_7_ovi),
    "nalle":     infl(kotus_noun_8_nalle),
    "kala":      infl(kotus_noun_9_kala),
    "nahka":     infl(kotus_noun_9_kala, g.gradate_kotus_d_reikä_reiän),
    "jumala":    infl(kotus_noun_10_koira),
    "koira":     infl(kotus_noun_10_koira),
    "ylkä":      infl(kotus_noun_10_koira, g.gradate_kotus_l_arki_arjen),
    "pitkä":     infl(kotus_noun_10_koira),
    "ruoka":     infl(kotus_noun_10_koira, g.gradate_kotus_d_reikä_reiän),
    "poika":     infl(joukahainen_noun_10_poika),
    "matala":    infl(kotus_noun_10_koira),
    "asema":     infl(kotus_noun_10_koira),
    "kulkija":   infl(kotus_noun_12_kulkija),
    "video":     infl(kotus_noun_3_valtio),
    "karahka":   infl(kotus_noun_13_katiska),
    "apaja":     infl(kotus_noun_11_omena),
    "peruna":    infl(kotus_noun_11_omena),
    "korkea":    infl(kotus_noun_15_korkea),
    "suurempi":  infl(kotus_noun_16_vanhempi, g.gradate_kotus_h_kumpi_kumman),
    "vapaa":     infl(kotus_noun_17_vapaa),
    "kamee":     infl(kotus_noun_20_filee),
    "pii":       infl(kotus_noun_18_maa),
    "suo":       infl(kotus_noun_19_suo),
    "askel":     infl(kotus_noun_32_sisar),
    "rosé":      infl(kotus_noun_21_rosé),
    "spray":     infl(kotus_noun_21_rosé),
    "parfait":   infl(kotus_noun_22_parfait),
    "huuli":     infl(kotus_noun_24_uni),
    "meri":      infl(kotus_noun_24_uni),
    "tuohi":     infl(kotus_noun_23_lohi),
    "niemi":     infl(kotus_noun_25_toimi),
    "pieni":     infl(kotus_noun_26_pieni),
    "lumi":      infl(kotus_noun_25_toimi),
    "susi":      infl(kotus_noun_27_käsi),
    "tosi":      infl(kotus_noun_27_käsi),
    "kansi":     infl(kotus_noun_28_kynsi),
    "sisar":     infl(kotus_noun_32_sisar),
    "hapan":     infl(kotus_noun_33_kytkin, g.gradate_kotus_b_kaappi_kaapin),
    "uistin":    infl(kotus_noun_33_kytkin),
    "laidun":    infl(kotus_noun_33_kytkin, g.gradate_kotus_f_keidas_keitaan),
    "onneton":   infl(kotus_noun_34_onneton, g.gradate_kotus_c_kate_katteen),
    "lämmin":    infl(kotus_noun_35_lämmin, g.gradate_kotus_h_lumme_lumpeen),
    "vasen":     infl(kotus_noun_37_vasen),
    "sisin":     infl(kotus_noun_36_sisin),
    "nainen":    infl(kotus_noun_38_nainen),
    "vastaus":   infl(kotus_noun_39_vastaus),
    "kalleus":   infl(kotus_noun_40_kalleus),
    "kaunis":    infl(kotus_noun_41_vieras),
    "autuas":    infl(kotus_noun_41_vieras),
    "laupias":   infl(kotus_noun_41_vieras),
    "vieras":    infl(kotus_noun_41_vieras),
    "iäkäs":     infl(kotus_noun_41_vieras, g.gradate_kotus_a_hake_hakkeen),
    "ohut":      infl(kotus_noun_43_ohut),
    "kevät":     infl(kotus_noun_44_kevät),
    "mies":      infl(kotus_noun_42_mies),
    "kuollut":   infl(kotus_noun_47_kuollut),
    "hame":      infl(kotus_noun_48_hame),

    # TODO only has the plural form!
    # "alkeet",

    "tie":       infl(kotus_noun_19_suo),
    "lapsi":     infl(kotus_noun_7_ovi),
    "hapsi":     infl(kotus_noun_7_ovi), # TODO can also be 29 when poetic,
    "loppu":     infl(kotus_noun_1_valo, g.gradate_kotus_b_kaappi_kaapin),
    "veitsi":    infl(kotus_noun_30_veitsi),

    # verbs
    "punoa":      conj(KotusVerb52Sanoa),
    "aavistaa":   conj(KotusVerb53Muistaa),
    "hidastaa":   conj(KotusVerb53Muistaa),
    "heittää":    conj(KotusVerb53Muistaa, g.gradate_kotus_c_tyttö_tytön),
    "muistaa":    conj(KotusVerb53Muistaa),
    "inttää":     conj(KotusVerb53Muistaa),
    "sulaa":      conj(KotusVerb53Muistaa),
    "hohtaa":     conj(KotusVerb53Muistaa, g.gradate_kotus_f_satu_sadun),
    "hujahtaa":   conj(KotusVerb53Muistaa, g.gradate_kotus_f_satu_sadun),
    "kirjoittaa": conj(KotusVerb53Muistaa, g.gradate_kotus_c_tyttö_tytön),
    "loistaa":    conj(KotusVerb53Muistaa),
    "vuotaa":     conj(KotusVerb55Soutaa, g.gradate_kotus_f_satu_sadun),
    "huutaa":     conj(KotusVerb54Huutaa, g.gradate_kotus_f_satu_sadun),
    "sukeltaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_i_ilta_illan),
    "paleltaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_i_ilta_illan),
    "murtaa":     conj(KotusVerb54Huutaa, g.gradate_kotus_k_virta_virran),
    "juontaa":    conj(KotusVerb54Huutaa, g.gradate_kotus_j_hento_hennon),
    "pahentaa":   conj(KotusVerb54Huutaa, g.gradate_kotus_j_hento_hennon),
    "kaivaa":     conj(KotusVerb56Laulaa),

    # TODO irregular (78), see:
    # https://fi.wiktionary.org/wiki/Liite:Verbitaivutus/suomi/kaikaa
    # "kaikaa",

    "soutaa":    conj(KotusVerb55Soutaa),
    "saartaa":   conj(KotusVerb57Saartaa),
    "laskea":    conj(KotusVerb58Laskea),
    "tuntea":    conj(KotusVerb59Tuntea, g.gradate_kotus_j_hento_hennon),
    "lähteä":    conj(KotusVerb60Lähteä, g.gradate_kotus_f_satu_sadun),
    "sallia":    conj(KotusVerb61Sallia),
    "voida":     conj(KotusVerb62Voida),
    "käydä":     conj(KotusVerb65Käydä),
    "kanavoida": conj(KotusVerb62Voida),
    "saada":     conj(KotusVerb63Saada),
    "juoda":     conj(KotusVerb64Juoda),
    "nuolaista": conj(KotusVerb66Rohkaista),
    "mennä":     conj(KotusVerb67Tulla),
    "purra":     conj(KotusVerb67Tulla),
    "katsella":  conj(KotusVerb67Tulla),
    "haravoida": conj(KotusVerb68Tupakoida),
    "valita":    conj(KotusVerb69Valita),
    "saneerata": conj(KotusVerb73Salata),
    "aleta": conj(KotusVerb72Vanheta),
    # "haluta",
    "juoruta": conj(KotusVerb74Katketa),
    "salata":  conj(KotusVerb73Salata),
    "katketa": conj(KotusVerb74Katketa),
    "kohota":  conj(KotusVerb74Katketa),
    "kihistä": conj(KotusVerb66Rohkaista),
    "kitistä": conj(KotusVerb66Rohkaista),
    # "taitaa",
    "juosta": conj(KotusVerb70Juosta),
    "nähdä":  conj(KotusVerb71Nähdä),
    "kevetä": conj(KotusVerb72Vanheta, g.gradate_kotus_e_sopu_sovun)
}
