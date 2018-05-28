# -*- coding: utf-8 -*-
import stroke_dictionary_creator.inflection.voikko_inflection as voikko_inflection
from stroke_dictionary_creator.inflection.parsing import word_and_class

def inflected_forms(word_and_infclass):
    (word, infclass) = word_and_class.parse(word_and_infclass)

    return voikko_inflection.inflected_forms(word, infclass)
