from collections import namedtuple

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
