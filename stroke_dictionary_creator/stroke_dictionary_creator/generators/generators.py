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

end_vowel = end_vowel_e | end_vowel_o | end_vowel_i | end_vowel_a | end_vowel_u



initial_s = morpheme("s", "S")
initial_t = morpheme("t", "T")
initial_k = morpheme("k", "K")
initial_p = morpheme("p", "P")
initial_v = morpheme("v", "V")
initial_h = morpheme("h", "H")
initial_r = morpheme("r", "R")

initial_consonant =   initial_s | initial_t | initial_k | initial_p | initial_v \
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
