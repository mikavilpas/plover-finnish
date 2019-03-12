import unittest
from ensure import ensure
from . import gradation as g
from .gradation import gradation_function
from .lookup import lookup

def ensure_gives(args, result):
    # It's super hard to read the tests when they get too long. I made this to
    # make it a bit more bearable.
    ensure(lookup(*args)
           .moduses().potential_present().passive).equals(result)

class TestLookup(unittest.TestCase):
    def test_verbs(self):
        # go through each case and make sure gradation works
        ensure_gives(("sanoa",      "verb", "punoa"             ), "sanottaneen"     )
        ensure_gives(("aallottaa",  "verb", "aavistaa",   "av1" ), "aallotettaneen"  )
        ensure_gives(("uuttaa",     "verb", "heittää",    "av1" ), "uutettaneen"     )
        ensure_gives(("väistää",    "verb", "muistaa"           ), "väistettäneen"   )
        ensure_gives(("riittää",    "verb", "inttää",     "av1" ), "riitettäneen"    )
        ensure_gives(("hiostuttaa", "verb", "sulaa",      "av1" ), "hiostutettaneen" )
        ensure_gives(("hoitaa",     "verb", "hohtaa",     "av1" ), "hoidettaneen"    )
        ensure_gives(("heilahtaa",  "verb", "hujahtaa",   "av1" ), "heilahdettaneen" )
        ensure_gives(("ansoittaa",  "verb", "kirjoittaa", "av1" ), "ansoitettaneen"  )
        ensure_gives(("ostaa",      "verb", "loistaa"           ), "ostettaneen"     )
        ensure_gives(("huoltaa",    "verb", "vuotaa",     "av1" ), "huollettaneen"   )
