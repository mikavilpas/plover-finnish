from parsy import *

from stroke_dictionary_creator.generators.generators import *

no_middle_key = success("-")

# all words of length 2
two_vowel_word       = middle_vowel + end_vowel
vowel_consonant_word = middle_vowel + final_consonant
consonant_vowel_word = initial_consonant + no_middle_key + end_vowel

vowel_end_diphtong_word    = middle_vowel + end_diphtong
consonant_vowel_vowel_word = initial_consonant + middle_vowel + end_vowel
consonant_vowel_c_w_word   = initial_consonant + middle_vowel + final_consonant + end_vowel
vowel_consonant_v_v_word   = middle_vowel + final_consonant + end_diphtong
