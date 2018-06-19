# -*- coding: utf-8 -*-
from . import voikko_inflection
from .parsing import word_and_class

def inflected_forms(word_and_infclass):
    (word, infclass) = word_and_class.parse(word_and_infclass)

    return voikko_inflection.inflected_forms(word, infclass)
