from parsy import *

def vowel(key, chord):
    return string(key).map(lambda _: chord)

vowel_A = vowel("a", "A")
vowel_O = vowel("o", "O")
vowel_E = vowel("e", "E")
vowel_I = vowel("i", "I")
vowel_U = vowel("u", "AO")
vowel_Y = vowel("y", "AO")
vowel_Ä = vowel("ä", "A")
vowel_Ö = vowel("ö", "O")

middle_vowel = vowel_A | vowel_O | vowel_E | vowel_I | vowel_U | vowel_Y | vowel_Ä | vowel_Ö

end_vowel_e = vowel("e", "e")
end_vowel_o = vowel("o", "o")
end_vowel_i = vowel("i", "i")
end_vowel_a = vowel("a", "a")

end_vowel = end_vowel_e | end_vowel_o | end_vowel_i | end_vowel_a
