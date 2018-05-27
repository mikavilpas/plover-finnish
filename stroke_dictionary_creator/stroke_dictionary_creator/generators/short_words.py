from parsy import *

from .generators import *

no_middle_key = success("-")

# all words of length 2
word_vv = middle_vowel + end_vocal_sound
word_vc = middle_vowel + final_consonant
word_cv = initial_consonant + no_middle_key + end_vocal_sound

word_v_end_diphtong = middle_vowel + end_vocal_sound

word_vcv = middle_vowel + final_consonant + end_vocal_sound
word_cvv = initial_consonant + middle_vowel + end_vocal_sound
word_cvc = initial_consonant + middle_vowel + final_consonant

word_cvcv = initial_consonant + middle_vowel + final_consonant + end_vocal_sound
word_vccv = middle_vowel + final_two_consonants + end_vocal_sound
word_vcvv = middle_vowel + final_consonant + end_vocal_sound
word_vvcv = (long_vowel | middle_diphtong) + final_consonant + end_vocal_sound

# short_word_2 = word_vv
short_word = word_vcvv | word_vvcv | word_cvcv | word_vccv | word_cvc | \
             word_cvv | word_vcv | word_v_end_diphtong | \
             word_cv | word_vc | word_vv

def safe_parse_short_word(word):
    try:
        return short_word.parse(word)
    except ParseError:
        pass
