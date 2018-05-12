#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import itertools
from ruamel.yaml import YAML

utf8 = "utf-8"

def all_character_pairs(characters, length):
    pair_tuples = itertools.permutations(characters, length)

    return [u"".join(pair)
            for pair in sorted(pair_tuples)]

def get_wordlist(path):
    with io.open(path, "r", encoding = utf8) as f:
        lines = f.readlines()
        return [l.strip()
                for l in lines
                if not l == u""]

def get_finnish_wordlist():
    return get_wordlist("../wordlists/joukahainen.txt")

def characters_anywhere_in_word(word, chars):
    return chars in word

def permutations_present_in_words(character_pair, words, word_filter = characters_anywhere_in_word):
    matched_words = [w for w in words
                     if word_filter(w, character_pair)]
    return dict(character_pair = character_pair,
                matched_words = matched_words)

def save_results_into_file(data, filename):
    with io.open(filename, "w", encoding = utf8) as f:
        yaml=YAML()
        yaml.default_flow_style = False
        return yaml.dump(data, f)
