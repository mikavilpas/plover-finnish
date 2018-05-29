from parsy import *
from ..tokens import *
from ..noun_inflection_info import InflectionInfo
from ..gradation import identity
from ..parse_utils import reverse_parse

sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group

@generate
def root_and_end_vowel():
    end_vowel = yield vowel
    rest = yield character.at_least(1).concat()
    return [rest, end_vowel]

def kotus_noun_1_valo(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group(word, text)

    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    word_alt = gradation_fn(word)

    v = end_vowel
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
