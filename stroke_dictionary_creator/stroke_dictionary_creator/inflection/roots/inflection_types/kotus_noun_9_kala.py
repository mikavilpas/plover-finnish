from .base import *

def kotus_noun_9_kala(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)
    (root, end_vowel) = reverse_parse(word, root_and_optional_end_vowel("e"))
    (root_alt, _) = reverse_parse(word_alt, root_and_optional_end_vowel("e"))
    v = end_vowel

    # all words in the kotus wordlist for this class use the e vowel at the
    # end, it seems
    return InflectionInfo(nominative          = word,
                          nominative_plural   = root_alt + v + s("t"),
                          genitive            = root_alt + v + s("n"),
                          genitives_plural    = [root + s("ojen"),
                                                root + v + s("in")],
                          partitives          = [root + v + s("a")],
                          partitives_plural   = [root + s("oja")],
                          accusatives         = [word,
                                                root_alt + v + s("n")],
                          accusative_plural   = root_alt + v + s("t"),
                          inessive            = root_alt + v + s("ssa"),
                          inessives_plural    = [root_alt + s("oissa")],
                          elative             = root_alt + v + s("sta"),
                          elatives_plural     = [root_alt + s("oista")],
                          illatives           = [root + v + s("an")],
                          illatives_plural    = [root + s("oihin")],
                          adessive            = root_alt + v + s("lla"),
                          adessives_plural    = [root_alt + s("oilla")],
                          ablative            = root_alt + v + s("lta"),
                          ablatives_plural    = [root_alt + s("oilta")],
                          allative            = root_alt + v + s("lle"),
                          allatives_plural    = [root_alt + s("oille")],
                          essives             = [root + v + s("na")],
                          essives_plural      = [root + s("oina")],
                          translative         = root_alt + v + s("ksi"),
                          translatives_plural = [root_alt + s("oiksi")],
                          abessive            = root_alt + v + s("tta"),
                          abessives_plural    = [root_alt + s("oitta")],
                          instructives_plural = [root_alt + s("oin")],
                          comitatives_plural  = [root + s("oine")])
