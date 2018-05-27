import unittest
from ensure import ensure
from stroke_dictionary_creator.generators.generators import *
import itertools
import stroke_dictionary_creator.stroke_parser as stroke_parser

class TestGenerators(unittest.TestCase):
    def test_middle_vowel(self):
        ensure(middle_vowel.parse("a")).equals("A")
        ensure(middle_vowel.parse("e")).equals("E")
        ensure(middle_vowel.parse("i")).equals("I")
        ensure(middle_vowel.parse("o")).equals("O")
        ensure(middle_vowel.parse("u")).equals("AO")
        ensure(middle_vowel.parse("y")).equals("AO")
        ensure(middle_vowel.parse("ä")).equals("A")
        ensure(middle_vowel.parse("ö")).equals("O")

    def test_end_vowel(self):
        ensure(end_vowel.parse("e")).equals("e")
        ensure(end_vowel.parse("o")).equals("o")
        ensure(end_vowel.parse("ö")).equals("o")
        ensure(end_vowel.parse("i")).equals("i")
        ensure(end_vowel.parse("a")).equals("a")
        ensure(end_vowel.parse("ä")).equals("a")
        ensure(end_vowel.parse("u")).equals("eo")
        ensure(end_vowel.parse("y")).equals("eo")

    def test_initial_consonant(self):
        ensure(initial_consonant.parse("g")).equals("TKPV")
        ensure(initial_consonant.parse("j")).equals("SKVR")
        ensure(initial_consonant.parse("d")).equals("TK")
        ensure(initial_consonant.parse("b")).equals("PV")
        ensure(initial_consonant.parse("q")).equals("KV")
        ensure(initial_consonant.parse("m")).equals("PH")
        ensure(initial_consonant.parse("y")).equals("KVR")
        ensure(initial_consonant.parse("y")).equals("KVR")
        ensure(initial_consonant.parse("l")).equals("HR")

        ensure(initial_consonant.parse("s")).equals("S")
        ensure(initial_consonant.parse("t")).equals("T")
        ensure(initial_consonant.parse("k")).equals("K")
        ensure(initial_consonant.parse("p")).equals("P")
        ensure(initial_consonant.parse("v")).equals("V")
        ensure(initial_consonant.parse("h")).equals("H")
        ensure(initial_consonant.parse("r")).equals("R")

    def test_middle_diphtong(self):
        ensure(middle_diphtong.parse("ae")).equals("AE")
        ensure(middle_diphtong.parse("äe")).equals("AE")
        ensure(middle_diphtong.parse("ai")).equals("AI")
        ensure(middle_diphtong.parse("äi")).equals("AI")
        ensure(middle_diphtong.parse("ue")).equals("AOE")
        ensure(middle_diphtong.parse("ye")).equals("AOE")
        ensure(middle_diphtong.parse("ui")).equals("AOI")
        ensure(middle_diphtong.parse("yi")).equals("AOI")
        ensure(middle_diphtong.parse("ei")).equals("EI")

    def test_end_diphtong(self):
        ensure(end_diphtong.parse("ei")).equals("ei")
        ensure(end_diphtong.parse("eo")).equals("eo")
        ensure(end_diphtong.parse("eö")).equals("eo")
        ensure(end_diphtong.parse("ea")).equals("ea")
        ensure(end_diphtong.parse("eä")).equals("ea")
        ensure(end_diphtong.parse("ui")).equals("eoi")
        ensure(end_diphtong.parse("yi")).equals("eoi")
        ensure(end_diphtong.parse("ua")).equals("eoa")
        ensure(end_diphtong.parse("yä")).equals("eoa")
        ensure(end_diphtong.parse("oi")).equals("oi")
        ensure(end_diphtong.parse("öi")).equals("oi")
        ensure(end_diphtong.parse("oa")).equals("oa")
        ensure(end_diphtong.parse("öä")).equals("oa")

        # This is an exception to the rule.
        # The intention is to write words like "kulkija" (traveller) with a
        # single stroke.
        ensure(end_diphtong.parse("ja")).equals("ia")
        ensure(end_diphtong.parse("jä")).equals("ia")

    def test_end_triphtong(self):
        ensure(end_triphtong.parse("ija")).equals("eia")
        ensure(end_triphtong.parse("ijä")).equals("eia")
        ensure(end_triphtong.parse("uja")).equals("eoia")
        ensure(end_triphtong.parse("yjä")).equals("eoia")
        ensure(end_triphtong.parse("oja")).equals("oia")
        ensure(end_triphtong.parse("öjä")).equals("oia")

    def test_final_consonant(self):
        ensure(final_consonant.parse("l")).equals("NST")
        ensure(final_consonant.parse("m")).equals("SH")
        ensure(final_consonant.parse("p")).equals("HR")
        ensure(final_consonant.parse("v")).equals("SR")

        ensure(final_consonant.parse("n")).equals("N")
        ensure(final_consonant.parse("k")).equals("K")
        ensure(final_consonant.parse("s")).equals("S")
        ensure(final_consonant.parse("h")).equals("H")
        ensure(final_consonant.parse("t")).equals("T")
        ensure(final_consonant.parse("r")).equals("R")

    def test_long_vowel(self):
        ensure(long_vowel.parse("aa")).equals("A*")
        ensure(long_vowel.parse("ää")).equals("A*")
        ensure(long_vowel.parse("uu")).equals("AO*")
        ensure(long_vowel.parse("yy")).equals("AO*")
        ensure(long_vowel.parse("oo")).equals("O*")
        ensure(long_vowel.parse("öö")).equals("O*")
        ensure(long_vowel.parse("ee")).equals("*E")
        ensure(long_vowel.parse("ii")).equals("*I")

    def key_combinations(self, keys):
        combinations = itertools.combinations(keys, 2)
        return list(map(lambda c: "".join(c), combinations))

    def test_final_two_consonants(self):
        # try all combinations of 2 final consonants, and see that the stroke
        # parser is able to parse all combinations that final_two_consonants
        # reports as valid. stroke_parser is thus the reference implementation
        # that is presumed correct.
        consonants = "NKSHTR"
        combinations = self.key_combinations(consonants)

        for comb in combinations:
            stroke_parser_result = self.parse_or_none(stroke_parser.end_keys, comb)
            final_two_consonants_result = self.parse_or_none(final_two_consonants,
                                                             comb.lower())

            ensure(stroke_parser_result).equals(final_two_consonants_result)

    def parse_or_none(self, p, input_string):
        try:
            return p.parse(input_string)
        except Exception as e:
            return None

    def test_final_double_consonant(self):
        ensure(final_double_consonant.parse("nn")).equals("NKS")
        ensure(final_double_consonant.parse("kk")).equals("NKH")
        ensure(final_double_consonant.parse("mm")).equals("KSH")
        ensure(final_double_consonant.parse("ss")).equals("NSH")
        ensure(final_double_consonant.parse("rr")).equals("HTR")
        ensure(final_double_consonant.parse("pp")).equals("SHR")
