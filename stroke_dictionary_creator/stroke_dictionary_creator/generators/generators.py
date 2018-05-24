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

middle_vowel = vowel_A | vowel_O | vowel_E | vowel_I | vowel_U | vowel_Y | vowel_Ä | vowel_Ö

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
