#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tools

# Not all consonants are present, since many have multiple meanings.
# These are described in the design documentation.
consonants = "hklmnprst"

def compactify(permutation):
    # a readable view of the entire data set for this permutation
    name = permutation["character_pair"]

    words = permutation["matched_words"]
    properties = dict(matched_words_preview = words[:4],
                      count = len(words))
    return {name: properties}

def not_a_name(word):
    first_character = word[0]
    return not first_character.isupper()

def count_of_words(a):
    (char_pair, properties) = list(a.iteritems())[0]
    return properties["count"]

def main():
    words = tools.get_finnish_wordlist()
    consonant_permutations = tools.all_character_pairs(consonants, length = 2)

    results = map(
        lambda c: compactify(
            tools.permutations_present_in_words(c, words, not_a_name)),
        consonant_permutations)
    results = sorted(results, key = count_of_words, reverse = True)

    tools.save_results_into_file(results, "results.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
