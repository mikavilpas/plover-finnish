from parsy import *

from .generators import *

no_middle_key = success("-")
end_EN_ending = morpheme("en", "e")

end = end_EN_ending | end_vocal_sound

# all words of length 2
word_vv = middle_vowel + end
word_vc = middle_vowel + final_consonant
word_cv = initial_consonant + no_middle_key + end

word_v_end_diphtong = middle_vowel + end

word_vcv = middle_vowel + final_consonant + end
word_cvv = initial_consonant + middle_vowel + end
word_cvc = initial_consonant + middle_vowel + final_consonant

word_cvcv   = initial_consonant + middle_vowel + final_consonant + end
word_vccv   = middle_vowel + final_two_consonants + end
word_vcvv   = middle_vowel + final_consonant + end
word_vvcv   = middle_vocal_sound + final_consonant + end
word_nainen = initial_consonant + middle_vocal_sound + final_consonant + end

word_cvvccv = initial_consonant \
              + middle_vocal_sound \
              + final_two_consonants \
              + end

# short_word_2 = word_vv
short_word = word_cvvccv | word_nainen | word_vcvv | word_vvcv | word_cvcv |\
             word_vccv | word_cvc | \
             word_cvv | word_vcv | word_v_end_diphtong | \
             word_cv | word_vc | word_vv
