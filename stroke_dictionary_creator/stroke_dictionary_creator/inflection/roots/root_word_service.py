from parsy import *
sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group

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
    # suffix
    def s(text): return change_to_same_vowel_group(word, text)

    (root, data) = reverse_parse(word, kotus_noun_1_valo_parser)

    v = data["end_vowel"]
    return InflectionInfo(nominative         = word,
                          nominative_plural  = word + "jen",
                          genitive           = word + "n",
                          genitive_plural    = word + "jen",
                          partitive          = word + s("a"),
                          partitive_plural   = word + s("ja"),
                          accusatives        = [word, word + "n"],
                          accusative_plural  = word + s("ja"),
                          inessive           = word + s("ssa"),
                          inessive_plural    = word + s("issa"),
                          elative            = word + s("sta"),
                          elative_plural     = word + s("ista"),
                          illative           = word + v + "n",
                          illative_plural    = word + "ihin",
                          adessive           = word + s("lla"),
                          adessive_plural    = word + s("illa"),
                          ablative           = word + s("lta"),
                          ablative_plural    = word + s("ilta"),
                          allative           = word + "lle",
                          allative_plural    = word + "ille",
                          essive             = word + s("na"),
                          essive_plural      = word + s("ina"),
                          translative        = word + "ksi",
                          translative_plural = word + "iksi",
                          abessive           = word + s("tta"),
                          abessive_plural    = word + s("itta"),
                          instructive_plural = word + "in",
                          comitative_plural  = word + "ine",
    )
