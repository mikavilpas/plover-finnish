from parsy import *

vowel = char_from("aeiouyäö")
consonant = char_from("bcdfghjklmnpqrstvwxz")
character = vowel | consonant

@generate
def double_consonant():
    c = yield consonant
    yield string(c)
    return c
