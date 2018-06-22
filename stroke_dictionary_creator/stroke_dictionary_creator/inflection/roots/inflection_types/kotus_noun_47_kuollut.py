from .base import *

from parsy import *
from ..tokens import *

@generate
def word_vowel_consonant_ending():
    # words in this class end in "-ut"
    c = yield consonant
    v = yield vowel
    root = yield character.at_least(1).concat()
    return [root, v + c]

def kotus_noun_47_kuollut(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    (root, on_ending) = reverse_parse(word, word_vowel_consonant_ending)
    v = ""

    return InflectionInfo(nominative          = word,
                          nominative_plural   = root + s("eet"),
                          genitive            = root + s("een"),
                          genitives_plural    = [root + s("eiden"),
                                                root + s("eitten")],
                          partitives          = [root + s("utta")],
                          partitives_plural   = [root + s("eita")],
                          accusatives         = [word,
                                                root + s("een")],
                          accusative_plural   = root + s("eet"),
                          inessive            = root + s("eessa"),
                          inessives_plural    = [root + s("eissa")],
                          elative             = root + s("eesta"),
                          elatives_plural     = [root + s("eista")],
                          illatives           = [root + s("eeseen")],
                          illatives_plural    = [root + s("eisiin"),
                                                 root + s("eihin")],
                          adessive            = root + s("eella"),
                          adessives_plural    = [root + s("eilla")],
                          ablative            = root + s("eelta"),
                          ablatives_plural    = [root + s("eilta")],
                          allative            = root + s("eelle"),
                          allatives_plural    = [root + s("eille")],
                          essives             = [root + s("eena")],
                          essives_plural      = [root + s("eina")],
                          translative         = root + s("eeksi"),
                          translatives_plural = [root + s("eiksi")],
                          abessive            = root + s("eetta"),
                          abessives_plural    = [root + s("eitta")],
                          instructives_plural = [root + s("ein")],
                          comitatives_plural  = [root + s("eine")])
