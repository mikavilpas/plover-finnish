from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts

VerbRoots = namedtuple("VerbRoots",
                       ["present", "present_passive"])

VerbPersonalForms = namedtuple("VerbPersonalForms",
                               ["singular1", "singular1_negative",
                                "singular2", "singular2_negative",
                                "singular3", "singular3_negative",
                                "plural1", "plural1_negative",
                                "plural2", "plural2_negative",
                                "plural3", "plural3_negative",
                                "passive", "passive_negative",])

VerbPersonalFormsImperativePresent = namedtuple("VerbPersonalFormsImperativePresent",
                                                ["singular2", "singular2_negative",
                                                 "singular3", "singular3_negative",
                                                 "plural1", "plural1_negative",
                                                 "plural2", "plural2_negative",
                                                 "plural3", "plural3_negative",
                                                 "passive", "passive_negative",])

class VerbConjugation():
    roots = VerbRoots(present = "laula",
                      present_passive = "laule")

    def moduses(self):
        return VerbModuses(self.roots)

class VerbModuses():

    def __init__(self, roots):
        self.roots = roots

    # suffix
    def s(self, text):
        return change_to_same_vowel_group_prefer_umlauts(self.roots.present, text)

    def indicative_present(self):
        r = self.roots

        [pres_root, pres_v] = reverse_parse(r.present, root_and_end_vowel)

        return VerbPersonalForms(singular1          = r.present + "n",
                                 singular2          = r.present + "t",
                                 singular3          = pres_root + pres_v + pres_v,
                                 singular1_negative = r.present,
                                 singular2_negative = r.present,
                                 singular3_negative = r.present,
                                 plural1            = r.present + "mme",
                                 plural2            = r.present + "tte",
                                 plural3            = r.present + "vat",
                                 plural1_negative   = r.present,
                                 plural2_negative   = r.present,
                                 plural3_negative   = r.present,
                                 passive            = r.present_passive + "taan",
                                 passive_negative   = r.present_passive + "ta",)

    def indicative_past(self):
        r = self.roots
        s = self.s

        [pres_root, pres_v] = reverse_parse(r.present, root_and_end_vowel)

        return VerbPersonalForms(singular1          = pres_root + s("oin"),
                                 singular2          = pres_root + s("oit"),
                                 singular3          = pres_root + s("oi"),
                                 singular1_negative = r.present + s("nut"),
                                 singular2_negative = r.present + s("nut"),
                                 singular3_negative = r.present + s("nut"),
                                 plural1            = pres_root + s("oimme"),
                                 plural2            = pres_root + s("oitte"),
                                 plural3            = pres_root + s("oivat"),
                                 plural1_negative   = r.present + s("neet"),
                                 plural2_negative   = r.present + s("neet"),
                                 plural3_negative   = r.present + s("neet"),
                                 passive            = r.present_passive + s("ttiin"),
                                 passive_negative   = r.present_passive + s("ttu"),)

    def indicative_perfect(self):
        r = self.roots
        s = self.s

        nut = r.present + s("nut")
        neet = r.present + s("neet")

        return VerbPersonalForms(singular1          = nut,
                                 singular2          = nut,
                                 singular3          = nut,
                                 singular1_negative = nut,
                                 singular2_negative = nut,
                                 singular3_negative = nut,
                                 plural1            = neet,
                                 plural2            = neet,
                                 plural3            = neet,
                                 plural1_negative   = neet,
                                 plural2_negative   = neet,
                                 plural3_negative   = neet,
                                 passive            = r.present_passive + s("ttu"),
                                 passive_negative   = r.present_passive + s("ttu"),)

    def conditional_present(self):
        r = self.roots
        s = self.s

        isi = r.present + s("isi")

        return VerbPersonalForms(singular1          = isi + s("n"),
                                 singular2          = isi + s("t"),
                                 singular3          = isi,
                                 singular1_negative = isi,
                                 singular2_negative = isi,
                                 singular3_negative = isi,
                                 plural1            = isi + s("mme"),
                                 plural2            = isi + s("tte"),
                                 plural3            = isi + s("vat"),
                                 plural1_negative   = isi,
                                 plural2_negative   = isi,
                                 plural3_negative   = isi,
                                 passive            = r.present_passive + s("ttaisiin"),
                                 passive_negative   = r.present_passive + s("ttaisi"),)

    def potential_present(self):
        r = self.roots
        s = self.s

        ne = r.present + s("ne")

        return VerbPersonalForms(singular1          = ne + s("n"),
                                 singular2          = ne + s("t"),
                                 singular3          = ne + s("e"),
                                 singular1_negative = ne,
                                 singular2_negative = ne,
                                 singular3_negative = ne,
                                 plural1            = ne + s("mme"),
                                 plural2            = ne + s("tte"),
                                 plural3            = ne + s("vat"),
                                 plural1_negative   = ne,
                                 plural2_negative   = ne,
                                 plural3_negative   = ne,
                                 passive            = r.present_passive + s("ttaneen"),
                                 passive_negative   = r.present_passive + s("ttane"),)

    def imperative_present(self):
        r = self.roots
        s = self.s

        ko = r.present + s("ko")

        return VerbPersonalFormsImperativePresent(
            singular2          = r.present,
            singular3          = ko + s("on"),
            singular2_negative = r.present,
            singular3_negative = ko,
            plural1            = r.present + s("kaamme"),
            plural2            = r.present + s("kaa"),
            plural3            = r.present + s("koot"),
            plural1_negative   = ko,
            plural2_negative   = ko,
            plural3_negative   = ko,
            passive            = r.present_passive + s("ttakoon"),
            passive_negative   = r.present_passive + s("ttako"),)
