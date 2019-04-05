import unittest
from ensure import ensure
from .compound_words import strokefy_compound_word
# import ..inflection.inflection_service as i
from ..inflection import inflection_service as i

class TestCompoundWords(unittest.TestCase):
    def test_compound_word(self):
        ensure(strokefy_compound_word(
            i.inflected_forms, "möhö=maha;noun-kala")).contains_all_of(
                [('möhömaha', 'PHOHo/PHAH')])
