# -*- coding: utf-8 -*-

import sys
import tools
import character_analysis_tools as analysis

# Not all consonants are present, since many have multiple meanings.
# These are described in the design documentation.
consonants = "hklmnprst"

def consonant(character) -> bool:
    all_consonants = "bcdfghjklmnpqrstvwxz"
    return character in all_consonants

def find_neighboring_characters_in_word(word, chars):
    if len(word) == len(chars):
        return None

    index = word.find(chars)

    if index == -1:
        return None # doesn't contain chars

    preceding_character = word[index - 1] if not word.startswith(chars) else Nothing
    trailing_character = word[index - 1 + len(chars) + 1] if not word.endswith(chars) else Nothing

    return dict(preceding_character = preceding_character,
                trailing_character = trailing_character)

def after_vowel(word, chars) -> bool:
    neighbors = find_neighboring_characters_in_word(word, chars)
    return neighbors and not consonant(neighbors["preceding_character"])

def before_vowel(word, chars) -> bool:
    neighbors = find_neighboring_characters_in_word(word, chars)
    return neighbors and not consonant(neighbors["trailing_character"])

def is_a_two_consonant_cluster(word, chars) -> bool:
    # Triple consonants are either loan words (abstraktio for example from
    # English) or have a syllabic border (punt-ti).
    # They are calculated with a separate script.

    return  len(chars) == 2 \
        and chars in word \
        and after_vowel(word, chars) \
        and before_vowel(word, chars)

def not_a_name_or_triple_consonant_cluster(word, chars):
    analysis.not_a_name(word) and is_a_two_consonant_cluster(word, chars)

def main():
    consonant_permutations = tools.all_character_pairs(consonants, length = 2)
    results = analysis.frequency_analysis(consonant_permutations,
                                          word_filter = analysis.not_a_name)
    tools.save_results_into_file(results, "../results/double_consonant_frequencies.yaml")

    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
