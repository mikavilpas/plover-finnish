#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tools
import double_consonant_frequencies as double
import character_analysis_tools as analysis

def main():
    triple_consonant_permutations = tools.all_character_pairs(double.consonants, length = 3)
    results = analysis.frequency_analysis(triple_consonant_permutations,
                                          word_filter = analysis.not_a_name)

    tools.save_results_into_file(results, "results/triple_consonant_frequencies.yaml")

if __name__ == '__main__':
    sys.exit(main())
