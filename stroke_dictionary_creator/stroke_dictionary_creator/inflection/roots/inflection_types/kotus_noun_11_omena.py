from .base import *

def kotus_noun_11_omena(word, gradation_fn = identity):
    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    word_alt = gradation_fn(word)

    # all words in this class end in "a" or "ä"
    (root, end_vowel) = reverse_parse(word, root_and_end_vowel)
    (root_alt, _) = reverse_parse(word_alt, root_and_end_vowel)
    v = end_vowel

    # all words in the kotus wordlist for this class use the e vowel at the
    # end, it seems
    return InflectionInfo(nominative          = word,
                          nominative_plural   = root_alt + v + s("t"),
                          genitive            = root_alt + v + s("n"),
                          genitives_plural    = [root + s("ien"),
                                                root + s("oiden"),
                                                root + s("oitten"),
                                                root + s("ojen"),
                                                root + v + s("in")],
                          partitives           = [root + v + s("a")],
                          partitives_plural   = [root + s("ia"),
                                                root + s("oita"),
                                                root + s("oja")],
                          accusatives         = [word,
                                                root_alt + v + s("n")],
                          accusative_plural   = root_alt + v + s("t"),
                          inessive            = root_alt + v + s("ssa"),
                          inessives_plural    = [root_alt + s("oissa"),
                                                root_alt + s("issa")],
                          elative             = root_alt + v + s("sta"),
                          elatives_plural     = [root_alt + s("oista"),
                                                 root_alt + s("ista")],
                          illatives           = [root + v + s("an")],
                          illatives_plural    = [root + s("oihin"),
                                                root + s("iin")],
                          adessive            = root_alt + v + s("lla"),
                          adessives_plural    = [root_alt + s("oilla"),
                                                 root_alt + s("illa")],
                          ablative            = root_alt + v + s("lta"),
                          ablatives_plural    = [root_alt + s("oilta"),
                                                 root_alt + s("ilta")],
                          allative            = root_alt + v + s("lle"),
                          allatives_plural    = [root_alt + s("oille"),
                                                 root_alt + s("ille")],
                          essives             = [root + v + s("na")],
                          essives_plural      = [root + s("oina"),
                                                 root + s("ina")],
                          translative         = root_alt + v + s("ksi"),
                          translatives_plural = [root_alt + s("oiksi"),
                                                 root_alt + s("iksi")],
                          abessive            = root_alt + v + s("tta"),
                          abessives_plural    = [root_alt + s("oitta"),
                                                 root_alt + s("itta")],
                          instructives_plural = [root_alt + s("oin"),
                                                 root_alt + s("in")],
                          comitatives_plural  = [root + s("oine"),
                                                 root + s("ine")])

    # there are no words in the kotus wordlist with gradation in this class
