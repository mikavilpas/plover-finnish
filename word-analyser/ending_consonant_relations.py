#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import io

from ruamel.yaml import YAML

# Not all consonants are present, since many have multiple meanings.
# These are described in the design documentation.
consonants = "hklmnprst"

utf8 = "utf-8"

def get_wordlist(path):
    with io.open(path, "r", encoding = utf8) as f:
        lines = f.readlines()
        return [l.strip()
                for l in lines
                if not l == u""]

def combinations_present_in_words(character_pair, words):
    matched_words = [w for w in words
                     if character_pair in w]
    return dict(character_pair = character_pair,
                matched_words = matched_words)

def all_character_pairs(characters, length):
    pair_tuples = itertools.combinations(characters, length)

    return [u"".join(pair)
            for pair in sorted(pair_tuples)]

def save_results_into_file(data, filename):
    with io.open(filename, "w", encoding = utf8) as f:
        yaml=YAML()
        yaml.default_flow_style = False
        return yaml.dump(data, f)

def compactify(combination):
    # a readable view of the entire data set for this combination
    name = combination["character_pair"]

    words = combination["matched_words"]
    properties = dict(matched_words_preview = words[:4],
                      count = len(words))
    return {name: properties}

def main():
    words = get_wordlist("../wordlists/joukahainen.txt")
    consonant_combinations = all_character_pairs(consonants, length = 2)

    results = map(lambda c: compactify(combinations_present_in_words(c, words)),
                  consonant_combinations)

    save_results_into_file(results, "results.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
