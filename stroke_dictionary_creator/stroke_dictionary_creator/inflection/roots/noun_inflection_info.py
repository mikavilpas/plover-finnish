from collections import namedtuple
import sys
sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group_prefer_umlauts

InflectionInfo = namedtuple("InflectionInfo",
                            ["nominative",         "nominative_plural",
                             "genitive",           "genitives_plural",
                             "partitives",         "partitives_plural",
                             "accusatives",        "accusative_plural",
                             "inessive",           "inessives_plural",
                             "elative",            "elatives_plural",
                             "illatives",          "illatives_plural",
                             "adessive",           "adessives_plural",
                             "ablative",           "ablatives_plural",
                             "allative",           "allatives_plural",
                             "essive",             "essives_plural",
                             "translative",        "translatives_plural",
                             "abessive",           "abessives_plural",
                             "instructives_plural",
                             "comitatives_plural"])

NounStems = namedtuple("NounStems",
                       ["nominative", "genitive", "partitives", "partitives_plural",
                        # for "omena": [omenoi,omeni]+(ssa|sta|lla|lta) etc.
                        "locationals_plural", "essive", "plural", "illatives"])

class Noun():
    def __init__(self,
                 stems: NounStems,
                 genitives_plural: [str],
                 illatives_plural: [str]):
        self.stems = stems

        # Forming the plural genitive forms is very complicated, so to keep
        # things simple, each word class must just provide them verbatim.
        # http://users.jyu.fi/~pamakine/kieli/suomi/sijat/genetiivien.html
        self.genitives_plural = genitives_plural
        # this is also very complicated, so the same thing applies here.
        self.illatives_plural = illatives_plural

    def inflections(self) -> InflectionInfo:
        stems = self.stems
        word = stems.nominative
        s = self.s
        many = self.many

        return InflectionInfo(
            nominative          = stems.nominative,
            nominative_plural   = stems.genitive + "t",
            genitive            = stems.genitive + "n",
            genitives_plural    = self.genitives_plural,
            partitives          = many(stems.partitives, s("a")),
            partitives_plural   = many(stems.partitives_plural, s("a")),
            accusatives         = [stems.nominative, stems.genitive + "n"],
            accusative_plural   = stems.nominative + s("t"),
            inessive            = stems.genitive + s("ssa"),
            inessives_plural    = many(stems.locationals_plural, s("ssa")),
            elative             = stems.genitive + s("sta"),
            elatives_plural     = many(stems.locationals_plural, s("sta")),
            illatives           = many(stems.illatives, s("n")),
            illatives_plural    = self.illatives_plural,
            adessive            = stems.genitive + s("lla"),
            adessives_plural    = many(stems.locationals_plural, s("lla")),
            ablative            = stems.genitive + s("lta"),
            ablatives_plural    = many(stems.locationals_plural, s("lta")),
            allative            = stems.genitive + "lle",
            allatives_plural    = many(stems.locationals_plural, s("lle")),
            essive              = stems.genitive + s("na"),
            essives_plural      = many(stems.locationals_plural, s("na")),
            translative         = stems.genitive + "ksi",
            translatives_plural = many(stems.locationals_plural, s("ksi")),
            abessive            = stems.genitive + s("tta"),
            abessives_plural    = [stems.genitive + s("itta")],
            instructives_plural = [stems.genitive + "in"],
            comitatives_plural  = [stems.genitive + "ine"],
        )

    def many(self, roots: [str], suffix: str) -> [str]:
        return [r + suffix for r in roots]

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.word, text)
