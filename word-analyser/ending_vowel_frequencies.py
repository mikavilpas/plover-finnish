#!/usr/bin/env python
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

def has_ending_vowels(word):
    for vowel_permutation in vowel_permutations:
        regex = ".*" + vowel_permutation + "$"
        if re.match(regex, word) is not None:
            return True

def main():
    results = analysis.frequency_analysis(vowel_permutations,
                                          word_filter = has_ending_vowels)
    tools.save_results_into_file(results, "results/ending_vowel_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
