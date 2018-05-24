from parsy import *

def chord(keys): return lambda _: keys.upper()
def vowel(key, steno_key):
    return string(key).map(chord(steno_key))

vowel_A = vowel("a", "A")
vowel_O = vowel("o", "O")
vowel_E = vowel("e", "E")
vowel_I = vowel("i", "I")
vowel_U = vowel("u", "AO")
vowel_Y = vowel("y", "AO")
vowel_Ä = vowel("ä", "A")
vowel_Ö = vowel("ö", "O")

middle_vowel = vowel_A | vowel_O | vowel_E | vowel_I | vowel_U | vowel_Y | vowel_Ä | vowel_Ö
