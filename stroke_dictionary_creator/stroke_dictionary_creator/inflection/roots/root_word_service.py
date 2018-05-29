from parsy import *

vowel = char_from("aeiouyäö")
consonant = char_from("bcdfghjklmnpqrstvwxz")
character = vowel | consonant

@generate
def double_consonant():
    c = yield consonant
    yield string(c)
    return c

@generate
def kotus_noun_1_valo_parser():
    v = yield vowel
    rest = yield character.at_least(1).concat()
    return [rest, dict(end_vowel = v)]

def reverse_parse(word, p):
    # root words are simpler to parse in reverse order
    def reverse(w): return w[::-1]
    (root, data) = p.parse(reverse(word))
    return (reverse(root), data)

from collections import namedtuple

InflectionInfo = namedtuple("InflectionInfo",
                            ["nominative",         "nominative_plural",
                             "genitive",           "genitive_plural",
                             "partitive",          "partitive_plural",
                             "accusatives",        "accusative_plural",
                             "inessive",           "inessive_plural",
                             "elative",            "elative_plural",
                             "illative",           "illative_plural",
                             "adessive",           "adessive_plural",
                             "ablative",           "ablative_plural",
                             "allative",           "allative_plural",
                             "essive",             "essive_plural",
                             "translative",        "translative_plural",
                             "abessive",           "abessive_plural",
                             "instructive_plural",
                             "comitative_plural"])

def kotus_noun_1_valo(word):
    (root, data) = reverse_parse(word, kotus_noun_1_valo_parser)
    v = data["end_vowel"]
    return InflectionInfo(nominative         = word,
                          nominative_plural  = word + "jen",
                          genitive           = word + "n",
                          genitive_plural    = word + "jen",
                          partitive          = word + "a",
                          partitive_plural   = word + "j" + "a",
                          accusatives        = [word, word + "n"],
                          accusative_plural  = word + "ja",
                          inessive           = word + "ssa",
                          inessive_plural    = word + "issa",
                          elative            = word + "sta",
                          elative_plural     = word + "ista",
                          illative           = word + v + "n",
                          illative_plural    = word + "ihin",
                          adessive           = word + "lla",
                          adessive_plural    = word + "illa",
                          ablative           = word + "lta",
                          ablative_plural    = word + "ilta",
                          allative           = word + "lle",
                          allative_plural    = word + "ille",
                          essive             = word + "na",
                          essive_plural      = word + "ina",
                          translative        = word + "ksi",
                          translative_plural = word + "iksi",
                          abessive           = word + "tta",
                          abessive_plural    = word + "itta",
                          instructive_plural = word + "in",
                          comitative_plural  = word + "ine",
    )
