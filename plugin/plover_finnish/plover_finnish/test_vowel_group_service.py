import unittest
from ensure import ensure
from .vowel_group_service import *

class TestVowelGroupService(unittest.TestCase):
    def test_vowel_group_discovery(self):
        ensure(vowel_group("auto")).equals(aou)
        ensure(vowel_group("piimä")).equals(äöy)

        # neither group
        ensure(vowel_group("kiire")).equals(None)

    def test_switch_vowel_group(self):
        ensure(switch_vowel_group("tallautua")).equals("tälläytyä")
        ensure(switch_vowel_group("paasto")).equals("päästö")

        # switching twice should be reversible
        ensure(switch_vowel_group(
            switch_vowel_group("tallautua"))).equals("tallautua")

        # a word that belongs to neither group should be unchanged
        ensure(switch_vowel_group("kiire")).equals("kiire")

    def test_change_to_same_vowel_group(self):
        ensure(change_to_same_vowel_group("paasto", "ssa")).equals("ssa")
        ensure(change_to_same_vowel_group("päästö", "ssa")).equals("ssä")
        ensure(change_to_same_vowel_group("päästö", "ssa")).equals("ssä")
