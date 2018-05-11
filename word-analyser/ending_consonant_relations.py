#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import io

# Not all consonants are present, since many have multiple meanings.
# These are described in the design documentation.
consonants = "hklmnprst"

def get_wordlist(path):
    with io.open(path, "r", encoding = "utf-8") as file:
        lines = file.readlines()
        return [l.strip() for l in lines
                if not l == ""]

def combinations_present_in_words(character_pair, words):
    matched_words = [w for w in words
                     if character_pair in w]
    return dict(character_pair = character_pair,
                matched_words = matched_words)

def all_character_pairs(characters, length):
    pair_tuples = itertools.combinations(characters, length)

    return ["".join(pair)
            for pair in sorted(pair_tuples)]

def main():
    words = get_wordlist("../wordlists/joukahainen.txt")
    consonant_combinations = all_character_pairs(consonants, length = 2)

    results = map(lambda c: combinations_present_in_words(c, words),
                  consonant_combinations)

    save_results_into_file(results, "results.yaml")

    print combinations_present_in_words("tn", words)
    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
