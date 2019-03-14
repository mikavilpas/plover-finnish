from parsy import *

vowel     = char_from("aeiouyäöAEIOUYÄÖ")
consonant = char_from("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
character = vowel | consonant
number    = char_from("1234567890")

@generate
def double_consonant():
    c = yield consonant
    yield string(c)
    return c
