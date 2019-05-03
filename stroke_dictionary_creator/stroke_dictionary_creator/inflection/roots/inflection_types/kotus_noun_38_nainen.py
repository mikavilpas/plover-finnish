from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_38_nainen(word, gradation_fn = identity):
    # Nominals ending with -nen, such as adjectives formed with the suffixes
    # -inen and -lainen, nouns formed using the suffix -minen, and fourth
    # infinitives of verbs.
    #
    # No consonant gradation.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/nainen

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, nen_ending) = reverse_parse(word, word_nen_ending)

    # TODO the essive can also be "naisna" as well as "naisina", but this form
    # is rare

    return InflectionInfo(nominative          = word,
                          nominative_plural   = root + s("set"),
                          genitive            = root + s("sen"),
                          genitives_plural    = [root + s("sten"),
                                                root + s("sien")],
                          partitives          = [root + s("sta")],
                          partitives_plural   = [root + s("sia")],
                          accusatives         = [word,
                                                root + s("sen")],
                          accusative_plural   = root + s("set"),
                          inessive            = root + s("sessa"),
                          inessives_plural    = [root + s("sissa")],
                          elative             = root + s("sesta"),
                          elatives_plural     = [root + s("sista")],
                          illatives           = [root + s("seen")],
                          illatives_plural    = [root + s("siin")],
                          adessive            = root + s("sella"),
                          adessives_plural    = [root + s("silla")],
                          ablative            = root + s("selta"),
                          ablatives_plural    = [root + s("silta")],
                          allative            = root + s("selle"),
                          allatives_plural    = [root + s("sille")],
                          essives             = [root + s("sena")],
                          essives_plural      = [root + s("sina")],
                          translative         = root + s("seksi"),
                          translatives_plural = [root + s("siksi")],
                          abessive            = root + s("setta"),
                          abessives_plural    = [root + s("sitta")],
                          instructives_plural = [root + s("sin")],
                          comitatives_plural  = [root + s("sine")])
