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

# root words are simpler to parse in reverse order
def reverse(s): return s[::-1]

def reverse_parse(word, p):
    return_value = p.parse(reverse(word))
    if len(return_value) == 2:
        (root, data) = return_value
        return (reverse(root), data)
    return reverse(return_value)

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

def replace_first(target, replacement):
    target = reverse(target)
    replacement = reverse(replacement)

    @generate
    def replacer():
        p = string(target).should_fail("found " + target) >> character
        start = yield p.at_least(1).concat()
        yield string(target)
        end = yield character.at_least(1).concat()
        return start + replacement + end

    return replacer

def gradate_kotus_i_ilta_illan_sivellin_siveltimen(word):
    p = replace_first("lt", "ll") | replace_first("ll", "lt")
    return reverse_parse(word, p)

identity = lambda a: a

def kotus_noun_1_valo(word, gradation = identity):
    # suffix
    def s(text): return change_to_same_vowel_group(word, text)

    (root, data) = reverse_parse(word, kotus_noun_1_valo_parser)
    word_alt = gradation(word)

    v = data["end_vowel"]
    return InflectionInfo(nominative         = word,
                          nominative_plural  = word_alt + "t",
                          genitive           = word_alt + "n",
                          genitive_plural    = word + "jen",
                          partitive          = word + s("a"),
                          partitive_plural   = word + s("ja"),
                          accusatives        = [word, word_alt + "n"],
                          accusative_plural  = word + s("ja"),
                          inessive           = word_alt + s("ssa"),
                          inessive_plural    = word_alt + s("issa"),
                          elative            = word_alt + s("sta"),
                          elative_plural     = word_alt + s("ista"),
                          illative           = word + v + "n",
                          illative_plural    = word + "ihin",
                          adessive           = word_alt + s("lla"),
                          adessive_plural    = word_alt + s("illa"),
                          ablative           = word_alt + s("lta"),
                          ablative_plural    = word_alt + s("ilta"),
                          allative           = word_alt + "lle",
                          allative_plural    = word_alt + "ille",
                          essive             = word + s("na"),
                          essive_plural      = word + s("ina"),
                          translative        = word_alt + "ksi",
                          translative_plural = word_alt + "iksi",
                          abessive           = word_alt + s("tta"),
                          abessive_plural    = word_alt + s("itta"),
                          instructive_plural = word_alt + "in",
                          comitative_plural  = word + "ine",
    )
