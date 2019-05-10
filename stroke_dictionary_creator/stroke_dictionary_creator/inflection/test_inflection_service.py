import unittest

from ensure import ensure

from .inflection_service import inflected_forms


def test_inflected_forms_noun():
    forms = inflected_forms("koe;noun-hame-av6")
    ensure(forms).contains("kokeen")

def test_inflected_forms_verbs():
    forms = inflected_forms("koettaa;verb-aavistaa-av1")
    ensure(forms).contains("koettamisitta")

class TestAdjectives(unittest.TestCase):
    def test_adjective_full(self):
        forms = inflected_forms("ehjä;adjective-koira")
        ensure(forms).contains("ehjimmille")

    def test_adjective_not_comparable(self):
        forms = inflected_forms("uloin;adjective-sisin")
        ensure(forms).contains("uloimmassa")
