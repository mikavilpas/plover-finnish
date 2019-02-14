import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from ..gradation import gradate_kotus_c_tyttö_tytön
from .kotus_noun_47_kuollut import kotus_noun_47_kuollut

class TestInflection(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_47_kuollut("kuollut")

        expected = InflectionInfo(nominative="kuollut",
                                  nominative_plural   = "kuolleet",
                                  genitive            = "kuolleen",
                                  genitives_plural    = ["kuolleiden",
                                                         "kuolleitten"],
                                  partitives          = ["kuollutta"],
                                  partitives_plural   = ["kuolleita"],
                                  accusatives         = ["kuollut", "kuolleen"],
                                  accusative_plural   = "kuolleet",
                                  inessive            = "kuolleessa",
                                  inessives_plural    = ["kuolleissa"],
                                  elative             = "kuolleesta",
                                  elatives_plural     = ["kuolleista"],
                                  illatives           = ["kuolleeseen"],
                                  illatives_plural    = ["kuolleisiin", "kuolleihin"],
                                  adessive            = "kuolleella",
                                  adessives_plural    = ["kuolleilla"],
                                  ablative            = "kuolleelta",
                                  ablatives_plural    = ["kuolleilta"],
                                  allative            = "kuolleelle",
                                  allatives_plural    = ["kuolleille"],
                                  essives             = ["kuolleena"],
                                  essives_plural      = ["kuolleina"],
                                  translative         = "kuolleeksi",
                                  translatives_plural = ["kuolleiksi"],
                                  abessive            = "kuolleetta",
                                  abessives_plural    = ["kuolleitta"],
                                  instructives_plural = ["kuollein"],
                                  comitatives_plural  = ["kuolleine"])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        # this doesn't exist in the word list, but it's a real and common word
        data = kotus_noun_47_kuollut("nähnyt")

        expected = InflectionInfo(nominative='nähnyt',
                                  nominative_plural='nähneet',
                                  genitive='nähneen',
                                  genitives_plural=['nähneiden',
                                                    'nähneitten'],
                                  partitives=['nähnyttä'],
                                  partitives_plural=['nähneitä'],
                                  accusatives=['nähnyt',
                                               'nähneen'],
                                  accusative_plural='nähneet',
                                  inessive='nähneessä',
                                  inessives_plural=['nähneissä'],
                                  elative='nähneestä',
                                  elatives_plural=['nähneistä'],
                                  illatives=['nähneeseen'],
                                  illatives_plural=['nähneisiin',
                                                    'nähneihin'],
                                  adessive='nähneellä',
                                  adessives_plural=['nähneillä'],
                                  ablative='nähneeltä',
                                  ablatives_plural=['nähneiltä'],
                                  allative='nähneelle',
                                  allatives_plural=['nähneille'],
                                  essives=['nähneenä'],
                                  essives_plural=['nähneinä'],
                                  translative='nähneeksi',
                                  translatives_plural=['nähneiksi'],
                                  abessive='nähneettä',
                                  abessives_plural=['nähneittä'],
                                  instructives_plural=['nähnein'],
                                  comitatives_plural=['nähneine'])

        ensure_inflections_equal(expected, data)

    # all words use no gradation
