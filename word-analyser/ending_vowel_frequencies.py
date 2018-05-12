#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tools
import re

vowels = u"aeiouyäö"

# ija is a special case. It's expressed via the -IA stroke.
vowel_permutations = tools.all_character_pairs(vowels, length = 2) + ["ija"]

def has_ending_vowels(word):
    re.search()

def main():
    words = tools.get_finnish_wordlist()

    results = map(
        lambda c: compactify(
            tools.permutations_present_in_words(c, words, has_ending_vowels)),
        vowel_permutations)

    results = filter(has_matches, results)
    results = sorted(results, key = count_of_words, reverse = True)

    tools.save_results_into_file(results, "results/ending_vowel_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
