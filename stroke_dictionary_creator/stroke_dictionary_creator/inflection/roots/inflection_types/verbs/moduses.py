from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts, root_and_double_end_vowel
from ...noun_inflection_info import InflectionInfo

class VerbRoots():
    def __init__(self, root_weak, root_strong, root_passive,
                 singular3, singular3_past, singular1_past,
                 conditional_strong, participle_root, plural3,
                 infinitive_root = None):
        self.root_weak          = root_weak
        self.root_strong        = root_strong
        self.root_passive       = root_passive
        self.singular3          = singular3
        self.singular3_past     = singular3_past
        self.singular1_past     = singular1_past
        self.conditional_strong = conditional_strong
        self.participle_root    = participle_root
        self.plural3            = plural3
        # many verbs don't have this separately
        self.infinitive_root    = infinitive_root or root_strong

VerbPersonalForms = namedtuple("VerbPersonalForms",
                               ["singular1", "singular1_negative",
                                "singular2", "singular2_negative",
                                "singular3", "singular3_negative",
                                "plural1", "plural1_negative",
                                "plural2", "plural2_negative",
                                "plural3", "plural3_negative",
                                "passive", "passive_negative",])

# This is like the other one, except it has many possible verb roots for some
# of the forms. Some require that in some cases.
VerbPersonalFormsMultipleRoots = namedtuple(
    "VerbPersonalFormsMultipleRoots",
    ["singular1s", "singular1_negative",
     "singular2s", "singular2_negative",
     "singular3s", "singular3_negative",
     "plural1s", "plural1_negative",
     "plural2s", "plural2_negative",
     "plural3s", "plural3_negative",
     "passive", "passive_negative",])

VerbPersonalFormsImperativePresent = namedtuple("VerbPersonalFormsImperativePresent",
                                                ["singular2", "singular2_negative",
                                                 "singular3", "singular3_negative",
                                                 "plural1", "plural1_negative",
                                                 "plural2", "plural2_negative",
                                                 "plural3", "plural3_negative",
                                                 "passive", "passive_negative",])

class VerbModuses():

    def __init__(self, roots: VerbRoots):
        self.roots = roots

    def indicative_present(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        # TODO allow verb bodies as a list

        return VerbPersonalForms(singular1          = r.root_weak + s("n"),
                                 singular2          = r.root_weak + s("t"),
                                 singular3          = r.singular3,
                                 singular1_negative = r.root_weak,
                                 singular2_negative = r.root_weak,
                                 singular3_negative = r.root_weak,
                                 plural1            = r.root_weak + s("mme"),
                                 plural2            = r.root_weak + s("tte"),
                                 plural3            = r.plural3 + s("vat"),
                                 plural1_negative   = r.root_weak,
                                 plural2_negative   = r.root_weak,
                                 plural3_negative   = r.root_weak,
                                 passive            = r.root_passive + s("taan"),
                                 passive_negative   = r.root_passive + s("ta"),)

    # Notice that this returns multiple roots!
    def indicative_past(self) -> VerbPersonalFormsMultipleRoots:
        r = self.roots
        s = self.s

        return VerbPersonalFormsMultipleRoots(
            singular1s         = self.many(r.singular1_past, s("in")),
            singular2s         = self.many(r.singular1_past, s("it")),
            singular3s         = self.many(r.singular3_past, s("i")),
            singular1_negative = r.root_strong + s("nut"),
            singular2_negative = r.root_strong + s("nut"),
            singular3_negative = r.root_strong + s("nut"),
            plural1s           = self.many(r.singular1_past, s("imme")),
            plural2s           = self.many(r.singular1_past, s("itte")),
            plural3s           = self.many(r.singular3_past, s("ivat")),
            plural1_negative   = r.root_strong + s("neet"),
            plural2_negative   = r.root_strong + s("neet"),
            plural3_negative   = r.root_strong + s("neet"),
            passive            = r.root_passive + s("ttiin"),
            passive_negative   = r.root_passive + s("ttu"),)

    def indicative_perfect(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        nut = r.root_strong + s("nut")
        neet = r.root_strong + s("neet")

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
                                 passive            = r.root_passive + s("ttu"),
                                 passive_negative   = r.root_passive + s("ttu"),)

    def conditional_present(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        isi = r.conditional_strong + s("isi")

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
                                 passive            = r.root_passive + s("ttaisiin"),
                                 passive_negative   = r.root_passive + s("ttaisi"),)

    def potential_present(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        ne = r.participle_root + s("ne")

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
                                 passive            = r.root_passive + s("ttaneen"),
                                 passive_negative   = r.root_passive + s("ttane"),)

    def imperative_present(self) -> VerbPersonalFormsImperativePresent:
        r = self.roots
        s = self.s

        ko = r.root_strong + s("ko")

        return VerbPersonalFormsImperativePresent(
            singular2          = r.root_weak,
            singular3          = ko + s("on"),
            singular2_negative = r.root_weak,
            singular3_negative = ko,
            plural1            = r.root_strong + s("kaamme"),
            plural2            = r.root_strong + s("kaa"),
            plural3            = r.root_strong + s("koot"),
            plural1_negative   = ko,
            plural2_negative   = ko,
            plural3_negative   = ko,
            passive            = r.root_passive + s("ttakoon"),
            passive_negative   = r.root_passive + s("ttako"),)

    def many(self, roots: [str], suffix: str) -> [str]:
        # some verb forms have multiple root forms, like yltää:ylti/ylsi
        return [r + suffix for r in roots]

    # suffix
    def s(self, text) -> str:
        return change_to_same_vowel_group_prefer_umlauts(self.roots.root_weak, text)
