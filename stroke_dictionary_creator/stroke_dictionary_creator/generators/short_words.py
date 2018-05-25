from parsy import *

from stroke_dictionary_creator.generators.generators import *

no_middle_key = success("-")

# all words of length 2
word_vv       = middle_vowel + end_vowel
word_vc = middle_vowel + final_consonant
word_cv = initial_consonant + no_middle_key + end_vowel

word_v_end_diphtong    = middle_vowel + end_diphtong
word_cvv = initial_consonant + middle_vowel + end_vowel
word_cvcv   = initial_consonant + middle_vowel + final_consonant + end_vowel
word_vcvv   = middle_vowel + final_consonant + end_diphtong
