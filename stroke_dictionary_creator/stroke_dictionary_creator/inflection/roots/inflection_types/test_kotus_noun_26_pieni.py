import unittest
from ensure import ensure
from ..noun_inflection_info import InflectionInfo
from .test_utils import ensure_inflections_equal
from .kotus_noun_26_pieni import kotus_noun_26_pieni

class TestInflectionType(unittest.TestCase):
    def test_basic_example(self):
        data = kotus_noun_26_pieni("vieri")

        expected = InflectionInfo(nominative='vieri',
                                  nominative_plural='vieret',
                                  genitive='vieren',
                                  genitives_plural=['vierten',
                                                    'vierien'],
                                  partitives=['viertä'],
                                  partitives_plural=['vieriä'],
                                  accusatives=['vieri',
                                               'vieren'],
                                  accusative_plural='vieret',
                                  inessive='vieressä',
                                  inessives_plural=['vierissä'],
                                  elative='vierestä',
                                  elatives_plural=['vieristä'],
                                  illatives=['viereen'],
                                  illatives_plural=['vieriin'],
                                  adessive='vierellä',
                                  adessives_plural=['vierillä'],
                                  ablative='viereltä',
                                  ablatives_plural=['vieriltä'],
                                  allative='vierelle',
                                  allatives_plural=['vierille'],
                                  essives=['vierenä'],
                                  essives_plural=['vierinä'],
                                  translative='viereksi',
                                  translatives_plural=['vieriksi'],
                                  abessive='vierettä',
                                  abessives_plural=['vierittä'],
                                  instructives_plural=['vierin'],
                                  comitatives_plural=['vierine'])

        ensure_inflections_equal(expected, data)

    def test_other_vowel_harmony_group(self):
        data = kotus_noun_26_pieni("pieni")

        expected = InflectionInfo(nominative='pieni',
                                  nominative_plural='pienet',
                                  genitive='pienen',
                                  genitives_plural=['pienten',
                                                    'pienien'],
                                  partitives=['pientä'],
                                  partitives_plural=['pieniä'],
                                  accusatives=['pieni',
                                               'pienen'],
                                  accusative_plural='pienet',
                                  inessive='pienessä',
                                  inessives_plural=['pienissä'],
                                  elative='pienestä',
                                  elatives_plural=['pienistä'],
                                  illatives=['pieneen'],
                                  illatives_plural=['pieniin'],
                                  adessive='pienellä',
                                  adessives_plural=['pienillä'],
                                  ablative='pieneltä',
                                  ablatives_plural=['pieniltä'],
                                  allative='pienelle',
                                  allatives_plural=['pienille'],
                                  essives=['pienenä'],
                                  essives_plural=['pieninä'],
                                  translative='pieneksi',
                                  translatives_plural=['pieniksi'],
                                  abessive='pienettä',
                                  abessives_plural=['pienittä'],
                                  instructives_plural=['pienin'],
                                  comitatives_plural=['pienine'])

        ensure_inflections_equal(expected, data)

    # no words with gradation
    # no words ending in a consonant.
