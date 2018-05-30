from collections import namedtuple

InflectionInfo = namedtuple("InflectionInfo",
                            ["nominative",         "nominative_plural",
                             "genitive",           "genitives_plural",
                             "partitive",          "partitives_plural",
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
