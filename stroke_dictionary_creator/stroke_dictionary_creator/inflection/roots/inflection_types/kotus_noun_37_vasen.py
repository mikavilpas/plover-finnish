from .base import *

from parsy import *
from ..tokens import *

def kotus_noun_37_vasen(word, gradation_fn = identity):
    # The word vasen only, and its compound words.
    # https://en.wiktionary.org/wiki/Appendix:Finnish_nominal_inflection/vasen

    # suffix
    def s(text): return change_to_same_vowel_group_prefer_umlauts(word, text)

    vasen       = word
    (vas, e, n) = reverse_parse(vasen, root_and_vc_ending)

    vasem       = vas + e + s("m")
    vasemm      = vas + e + s("mm")
    vasemp      = vas + e + s("mp")

    # Notice: Wiktionary says that the comitative form is either vasempineen or
    # vasempiine, but I don't think either is correct!

    return InflectionInfo(nominative          =  vasen,
                          nominative_plural   =  vasemm + s("at"),
                          genitive            =  vasemm + s("an"),
                          genitives_plural    = [vasemp + s("ien"),
                                                 vasen + s("ten"),
                                                 vasem + s("pain")],
                          partitives          = [vasen + s("ta"),
                                                 vasemp + s("aa")],
                          partitives_plural   = [vasemp + s("ia")],
                          accusatives         = [vasen,
                                                 vasemm + s("an")],
                          accusative_plural   =  vasemm + s("at"),
                          inessive            =  vasemm + s("assa"),
                          inessives_plural    = [vasemm + s("missa")],
                          elative             =  vasemm + s("asta"),
                          elatives_plural     = [vasemm + s("mista")],
                          illatives           = [vasemp + s("aan")],
                          illatives_plural    = [vasemp + s("iin")],
                          adessive            =  vasemm + s("alla"),
                          adessives_plural    = [vasemm + s("illa")],
                          ablative            =  vasemm + s("alta"),
                          ablatives_plural    = [vasemm + s("ilta")],
                          allative            =  vasemm + s("alle"),
                          allatives_plural    = [vasemm + s("ille")],
                          essives             = [vasemp + s("ana")],
                          essives_plural      = [vasemp + s("ina")],
                          translative         =  vasemm + s("aksi"),
                          translatives_plural = [vasemm + s("iksi")],
                          abessive            =  vasemm + s("atta"),
                          abessives_plural    = [vasemm + s("itta")],
                          instructives_plural = [vasemm + s("in")],
                          comitatives_plural  = [vasemp + s("ine")])
