from parsy import *

vowel = char_from("aeiouyäöAEIOUYÄÖ")
consonant = char_from("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
character = vowel | consonant

@generate
def double_consonant():
    c = yield consonant
    yield string(c)
    return c
