#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tools
import double_consonant_frequencies as double

def main():
    words = tools.get_finnish_wordlist()
    triple_consonant_permutations = tools.all_character_pairs(double.consonants, length = 3)

    results = map(
        lambda c: double.compactify(
            tools.permutations_present_in_words(c, words, double.not_a_name)),
        triple_consonant_permutations)
    results = filter(double.has_matches, results)
    results = sorted(results, key = double.count_of_words, reverse = True)

    tools.save_results_into_file(results, "results/triple_consonant_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
