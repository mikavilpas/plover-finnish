import unittest
from ensure import ensure
from stroke_dictionary_creator.inflection.inflection_service import *

class TestInflectionService(unittest.TestCase):

    def test_inflected_forms_noun(self):
        forms = inflected_forms("koe;noun-hame-av6")
        ensure(forms).contains("kokeen")

    def test_inflected_forms_adjective(self):
        forms = inflected_forms("ehjä;adjective-koira")
        ensure(forms).contains("ehjiksi")

    def test_inflected_forms_verbs(self):
        forms = inflected_forms("koettaa;verb-aavistaa-av1")
        ensure(forms).contains("koettamisitta")
