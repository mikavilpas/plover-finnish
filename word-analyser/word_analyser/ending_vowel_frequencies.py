# -*- coding: utf-8 -*-

import sys
import tools
import re
import character_analysis_tools as analysis

# The vowel harmony rule states that vowels in the left and right groups can
# never be in the same word. It has exceptions, but I don't think they apply at
# the very end of the word.
left   = u"äöy"
right  = u"aou"
middle = u"ei"

def pairs(vowels):
    return tools.all_character_pairs(vowels, length = 2)

# ija is a special case. It's expressed via the -IA stroke.
vowel_permutations = pairs(left + middle) + pairs(right + middle) + [u"ija"] + [u"ijä"]

def non_name_with_ending_vowels(word, vowels):
    return analysis.not_a_name(word, vowels) and word.endswith(vowels)

def main():
    print("Finding the frequencies of words that have these ending vowel sounds:")
    print(vowel_permutations)

    results = analysis.frequency_analysis(vowel_permutations,
                                          word_filter = non_name_with_ending_vowels)
    tools.save_results_into_file(results, "../results/ending_vowel_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
