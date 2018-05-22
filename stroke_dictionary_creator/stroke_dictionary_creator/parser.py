from parsy import *

def join(char_list):
    return "".join([c for c in char_list if c is not None])

def steno_keys(charmap):
    # Returns a parser that parses steno keys in the order that is given in charmap.
    # Disallows characters that are:
    # - not present in the given charmap
    # - given in the reverse (steno) order defined in charmap
    # If nothing matches, raises a ParseError like most parsers by default.
    char_sequence_parsers = [(string(c) | success("")) for c in charmap]
    return seq(*char_sequence_parsers).map(join)

initial_consonants = steno_keys("STKPVHR")
middle_keys        = steno_keys("AO*EI") | success("-")
end_keys           = steno_keys("NKSHTReoia")

@generate
def stroke():
    left = yield initial_consonants
    middle = yield middle

stroke = seq(initial_consonants,
             middle_keys,
             end_keys).map(join)
