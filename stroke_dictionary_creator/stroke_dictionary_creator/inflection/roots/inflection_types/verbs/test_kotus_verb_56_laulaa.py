import unittest
from ensure import ensure
from .kotus_verb_56_laulaa import VerbConjugation, VerbPersonalForms, VerbPersonalFormsImperativePresent
from ..test_utils import ensure_inflections_equal

class TestClass(unittest.TestCase):
    conjugation = VerbConjugation()
    moduses = conjugation.moduses()

    def test_indicative_present(self):
        conjugations = self.moduses.indicative_present()

        expected = VerbPersonalForms(singular1          = "laulan",
                                     singular2          = "laulat",
                                     singular3          = "laulaa",
                                     singular1_negative = "laula",
                                     singular2_negative = "laula",
                                     singular3_negative = "laula",
                                     plural1            = "laulamme",
                                     plural2            = "laulatte",
                                     plural3            = "laulavat",
                                     plural1_negative   = "laula",
                                     plural2_negative   = "laula",
                                     plural3_negative   = "laula",
                                     passive            = "lauletaan",
                                     passive_negative   = "lauleta",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_past(self):
        conjugations = self.moduses.indicative_past()

        expected = VerbPersonalForms(singular1          = "lauloin",
                                     singular2          = "lauloit",
                                     singular3          = "lauloi",
                                     singular1_negative = "laulanut",
                                     singular2_negative = "laulanut",
                                     singular3_negative = "laulanut",
                                     plural1            = "lauloimme",
                                     plural2            = "lauloitte",
                                     plural3            = "lauloivat",
                                     plural1_negative   = "laulaneet",
                                     plural2_negative   = "laulaneet",
                                     plural3_negative   = "laulaneet",
                                     passive            = "laulettiin",
                                     passive_negative   = "laulettu",)

        ensure_inflections_equal(expected, conjugations)

    def test_indicative_perfect(self):
        conjugations = self.moduses.indicative_perfect()

        expected = VerbPersonalForms(singular1          = "laulanut",
                                     singular2          = "laulanut",
                                     singular3          = "laulanut",
                                     singular1_negative = "laulanut",
                                     singular2_negative = "laulanut",
                                     singular3_negative = "laulanut",
                                     plural1            = "laulaneet",
                                     plural2            = "laulaneet",
                                     plural3            = "laulaneet",
                                     plural1_negative   = "laulaneet",
                                     plural2_negative   = "laulaneet",
                                     plural3_negative   = "laulaneet",
                                     passive            = "laulettu",
                                     passive_negative   = "laulettu",)

        ensure_inflections_equal(expected, conjugations)


    def test_conditional_present(self):
        conjugations = self.moduses.conditional_present()

        expected = VerbPersonalForms(singular1          = "laulaisin",
                                     singular2          = "laulaisit",
                                     singular3          = "laulaisi",
                                     singular1_negative = "laulaisi",
                                     singular2_negative = "laulaisi",
                                     singular3_negative = "laulaisi",
                                     plural1            = "laulaisimme",
                                     plural2            = "laulaisitte",
                                     plural3            = "laulaisivat",
                                     plural1_negative   = "laulaisi",
                                     plural2_negative   = "laulaisi",
                                     plural3_negative   = "laulaisi",
                                     passive            = "laulettaisiin",
                                     passive_negative   = "laulettaisi",)

        ensure_inflections_equal(expected, conjugations)


    def test_potential_present(self):
        conjugations = self.moduses.potential_present()

        expected = VerbPersonalForms(singular1          = "laulanen",
                                     singular2          = "laulanet",
                                     singular3          = "laulanee",
                                     singular1_negative = "laulane",
                                     singular2_negative = "laulane",
                                     singular3_negative = "laulane",
                                     plural1            = "laulanemme",
                                     plural2            = "laulanette",
                                     plural3            = "laulanevat",
                                     plural1_negative   = "laulane",
                                     plural2_negative   = "laulane",
                                     plural3_negative   = "laulane",
                                     passive            = "laulettaneen",
                                     passive_negative   = "laulettane",)

        ensure_inflections_equal(expected, conjugations)


    def test_imperative_present(self):
        conjugations = self.moduses.imperative_present()

        expected = VerbPersonalFormsImperativePresent(
            singular2          = "laula",
            singular3          = "laulakoon",
            singular2_negative = "laula",
            singular3_negative = "laulako",
            plural1            = "laulakaamme",
            plural2            = "laulakaa",
            plural3            = "laulakoot",
            plural1_negative   = "laulako",
            plural2_negative   = "laulako",
            plural3_negative   = "laulako",
            passive            = "laulettakoon",
            passive_negative   = "laulettako",)

        ensure_inflections_equal(expected, conjugations)
