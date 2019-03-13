import unittest
from ensure import ensure
from . import gradation as g
from .gradation import gradation_function
from .lookup import lookup_verb

def ensure_gives(args, result):
    # It's super hard to read the tests when they get too long. I made this to
    # make it a bit more bearable.
    ensure(lookup_verb(*args)
           .moduses().potential_present().passive).equals(result)

class TestLookup(unittest.TestCase):
    def test_verbs(self):
        # go through each case and make sure gradation works
        ensure_gives(("sanoa",      "punoa"             ), "sanottaneen"     )
        ensure_gives(("aallottaa",  "aavistaa",   "av1" ), "aallotettaneen"  )
        ensure_gives(("uuttaa",     "heittää",    "av1" ), "uutettaneen"     )
        ensure_gives(("väistää",    "muistaa"           ), "väistettäneen"   )
        ensure_gives(("riittää",    "inttää",     "av1" ), "riitettäneen"    )
        ensure_gives(("hiostuttaa", "sulaa",      "av1" ), "hiostutettaneen" )
        ensure_gives(("hoitaa",     "hohtaa",     "av1" ), "hoidettaneen"    )
        ensure_gives(("heilahtaa",  "hujahtaa",   "av1" ), "heilahdettaneen" )
        ensure_gives(("ansoittaa",  "kirjoittaa", "av1" ), "ansoitettaneen"  )
        ensure_gives(("ostaa",      "loistaa"           ), "ostettaneen"     )
        ensure_gives(("huoltaa",    "vuotaa",     "av1" ), "huollettaneen"   )
        ensure_gives(("löytää",     "huutaa",     "av1" ), "löydettäneen"    )
        ensure_gives(("vaeltaa",    "sukeltaa",   "av1" ), "vaellettaneen"   )
        ensure_gives(("uskaltaa",   "paleltaa",   "av1" ), "uskallettaneen"  )
        ensure_gives(("piirtää",    "murtaa",     "av1" ), "piirrettäneen"   )
        ensure_gives(("lentää",     "juontaa",    "av1" ), "lennettäneen"    )
        ensure_gives(("väärentää",  "pahentaa",   "av1" ), "väärennettäneen" )
        ensure_gives(("alkaa",      "kaivaa",     "av5" ), "alettaneen"      )
        ensure_gives(("laskea",     "laskea",           ), "laskettaneen"    )
        ensure_gives(("tuntea",     "tuntea",     "av1" ), "tunnettaneen"    )
        ensure_gives(("lähteä",     "lähteä",     "av1" ), "lähdettäneen"    )
        ensure_gives(("pyrkiä",     "sallia",     "av5" ), "pyrittäneen"     )
        ensure_gives(("voida",      "voida",      "av2" ), "voitaneen"       )
        ensure_gives(("käydä",      "käydä",            ), "käytäneen"       )
        ensure_gives(("editoida",   "kanavoida",  "av2" ), "editoitaneen"    )
        ensure_gives(("myydä",      "saada",            ), "myytäneen"       )
        ensure_gives(("lyödä",      "juoda",            ), "lyötäneen"       )
        ensure_gives(("rangaista",  "nuolaista",  "av2" ), "rangaistaneen"   )
        ensure_gives(("panna",      "mennä",            ), "pantaneen"       )
        ensure_gives(("pierrä",     "purra",            ), "piertäneen"      )
        ensure_gives(("aatella",    "katsella",   "av2" ), "aateltaneen"     )
        ensure_gives(("ikävöidä",   "haravoida",  "av2" ), "ikävöitäneen"    )
        ensure_gives(("tarvita",    "valita",           ), "tarvittaneen"    )
        ensure_gives(("sponssata",  "saneerata",        ), "sponssattaneen"  )
        ensure_gives(("aueta",      "aleta",      "av6" ), "auettaneen"      )
        ensure_gives(("hellitä",    "haluta",     "av2" ), "hellittäneen"    )
        ensure_gives(("luututa",    "juoruta",    "av2" ), "luututtaneen"    )
        ensure_gives(("aidata",     "salata",     "av2" ), "aidattaneen"     )
        ensure_gives(("kiivetä",    "katketa",    "av2" ), "kiivettäneen"    )
        ensure_gives(("kaikota",    "kohota",     "av2" ), "kaikottaneen"    )
        ensure_gives(("ulista",     "kihistä"           ), "ulistaneen"      )
        ensure_gives(("kitistä",    "kitistä"           ), "kitistäneen"     )
        ensure_gives(("tietää",     "taitaa"            ), "tiedettäneen"    )
        ensure_gives(("piestä",     "juosta"            ), "piestäneen"      )
        ensure_gives(("tehdä",      "nähdä"             ), "tehtäneen"       )
        ensure_gives(("kalveta",    "kevetä"            ), "kalvettaneen"    )
