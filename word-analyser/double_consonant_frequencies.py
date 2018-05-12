#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tools
import character_analysis_tools as analysis

# Not all consonants are present, since many have multiple meanings.
# These are described in the design documentation.
consonants = "hklmnprst"

def not_a_name(word):
    first_character = word[0]
    return not first_character.isupper()

def main():
    consonant_permutations = tools.all_character_pairs(consonants, length = 2)
    results = analysis.frequency_analysis(consonant_permutations,
                                          word_filter = not_a_name)
    tools.save_results_into_file(results, "results/double_consonant_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
