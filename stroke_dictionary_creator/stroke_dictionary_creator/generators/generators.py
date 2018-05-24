from parsy import *

def morpheme(key, chord):
    return string(key).map(lambda _: chord)

vowel_A = morpheme("a", "A")
vowel_O = morpheme("o", "O")
vowel_E = morpheme("e", "E")
vowel_I = morpheme("i", "I")
vowel_U = morpheme("u", "AO")
vowel_Y = morpheme("y", "AO")
vowel_Ä = morpheme("ä", "A")
vowel_Ö = morpheme("ö", "O")

middle_vowel = vowel_A | vowel_O | vowel_E | vowel_I \
               | vowel_U | vowel_Y | vowel_Ä | vowel_Ö



end_vowel_e = morpheme("e", "e")
end_vowel_o = morpheme("o", "o")
end_vowel_i = morpheme("i", "i")
end_vowel_a = morpheme("a", "a")
end_vowel_u = morpheme("u", "eo")

end_vowel = end_vowel_e | end_vowel_o | end_vowel_u | end_vowel_i | end_vowel_a



initial_g = morpheme("g", "TKPV")
initial_n = morpheme("n", "TPH")
initial_d = morpheme("d", "TK")
initial_b = morpheme("b", "PV")
initial_q = morpheme("q", "KV")
initial_m = morpheme("m", "PH")
initial_y = morpheme("y", "KVR")
initial_l = morpheme("l", "HR")

initial_s = morpheme("s", "S")
initial_t = morpheme("t", "T")
initial_k = morpheme("k", "K")
initial_p = morpheme("p", "P")
initial_v = morpheme("v", "V")
initial_h = morpheme("h", "H")
initial_r = morpheme("r", "R")

initial_consonant = initial_g | initial_n | initial_b | initial_d | initial_q \
                    | initial_m | initial_y | initial_l \
                    | initial_s | initial_t | initial_k | initial_p | initial_v \
                    | initial_h | initial_r



middle_diphtong_ae = morpheme("ae", "AE")
middle_diphtong_ai = morpheme("ai", "AI")
middle_diphtong_ue = morpheme("ue", "AOE")
middle_diphtong_ui = morpheme("ui", "AOI")
middle_diphtong_ei = morpheme("ei", "EI")

middle_diphtong = middle_diphtong_ae | middle_diphtong_ai | middle_diphtong_ue \
                  | middle_diphtong_ui | middle_diphtong_ei



end_diphtong_ei = morpheme("ei", "ei")
end_diphtong_eo = morpheme("eo", "eo")
end_diphtong_ea = morpheme("ea", "ea")
end_diphtong_ui = morpheme("ui", "ui")
end_diphtong_ua = morpheme("ua", "ua")
end_diphtong_oi = morpheme("oi", "oi")
end_diphtong_oa = morpheme("oa", "oa")
end_diphtong_ja = morpheme("ja", "ia")

end_diphtong = end_diphtong_ei | end_diphtong_eo | end_diphtong_ea | end_diphtong_ui \
               | end_diphtong_ua | end_diphtong_oi | end_diphtong_oa \
               | end_diphtong_ja



end_triphtong_uja = morpheme("uja", "eoia")
end_triphtong_ija = morpheme("ija", "eia")
end_triphtong_oja = morpheme("oja", "oia")

end_triphtong = end_triphtong_uja | end_triphtong_ija | end_triphtong_oja



final_consonant_l = morpheme("l", "NST")
final_consonant_m = morpheme("m", "SH")
final_consonant_p = morpheme("p", "HR")
final_consonant_v = morpheme("v", "SR")
final_consonant_n = morpheme("n", "N")
final_consonant_k = morpheme("k", "K")
final_consonant_s = morpheme("s", "S")
final_consonant_h = morpheme("h", "H")
final_consonant_t = morpheme("t", "T")
final_consonant_r = morpheme("r", "R")

final_consonant = final_consonant_l | final_consonant_m | final_consonant_p \
                  | final_consonant_v \
                  | final_consonant_n | final_consonant_k | final_consonant_s \
                  | final_consonant_h | final_consonant_t | final_consonant_r



long_vowel_a = morpheme("aa", "A*")
long_vowel_u = morpheme("uu", "AO*")
long_vowel_o = morpheme("oo", "O*")
long_vowel_e = morpheme("ee", "*E")
long_vowel_i = morpheme("ii", "*I")

long_vowel = long_vowel_a | long_vowel_u | long_vowel_o | long_vowel_e | long_vowel_i
