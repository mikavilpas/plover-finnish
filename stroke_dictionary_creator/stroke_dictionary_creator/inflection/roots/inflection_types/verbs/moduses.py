from collections import namedtuple
from ..base import reverse_parse, root_and_end_vowel, change_to_same_vowel_group_prefer_umlauts, root_and_double_end_vowel
from ...noun_inflection_info import InflectionInfo

class VerbRoots():
    def __init__(self, root_weak, root_strong, root_passive,
                 singular3, singular3_past, singular1_past,
                 conditional_strong, participle_root, plural3,
                 infinitive_root = None, passive_weak_root = None,
                 present_root = None, potential_root = None,
                 potential_s3_root = None, potential_p3_root = None,
                 imperative_root = None, suffix_ut = None,
                 suffix_eet = None):
        self.root_weak          = root_weak
        self.root_strong        = root_strong
        self.root_passive       = root_passive
        self.singular3          = singular3
        self.singular3_past     = singular3_past
        self.singular1_past     = singular1_past
        self.conditional_strong = conditional_strong
        self.participle_root    = participle_root
        self.plural3            = plural3

        # many verbs don't have these separately
        self.infinitive_root   = infinitive_root   or root_strong
        self.passive_weak_root = passive_weak_root or root_passive
        self.potential_root    = potential_root    or participle_root + "n"
        self.potential_s3_root = potential_s3_root or potential_root
        self.potential_p3_root = potential_p3_root or potential_root
        self.present_root      = present_root      or root_weak
        self.suffix_ut         = suffix_ut         or "nut"
        self.suffix_eet        = suffix_eet        or "neet"
        self.imperative_root   = imperative_root   or root_strong

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

        return VerbPersonalForms(singular1          = r.present_root + s("n"),
                                 singular2          = r.present_root + s("t"),
                                 singular3          = r.singular3,
                                 singular1_negative = r.present_root,
                                 singular2_negative = r.present_root,
                                 singular3_negative = r.present_root,
                                 plural1            = r.present_root + s("mme"),
                                 plural2            = r.present_root + s("tte"),
                                 plural3            = r.plural3 + s("vat"),
                                 plural1_negative   = r.present_root,
                                 plural2_negative   = r.present_root,
                                 plural3_negative   = r.present_root,
                                 passive            = r.passive_weak_root + s("aan"),
                                 passive_negative   = r.passive_weak_root + s("a"),)

    # Notice that this returns multiple roots!
    def indicative_past(self) -> VerbPersonalFormsMultipleRoots:
        r   = self.roots
        s   = self.s
        ut  = s(r.suffix_ut)
        eet = s(r.suffix_eet)

        return VerbPersonalFormsMultipleRoots(
            singular1s         = self.many(r.singular1_past, s("in")),
            singular2s         = self.many(r.singular1_past, s("it")),
            singular3s         = self.many(r.singular3_past, s("i")),
            singular1_negative = r.root_strong + ut,
            singular2_negative = r.root_strong + ut,
            singular3_negative = r.root_strong + ut,
            plural1s           = self.many(r.singular1_past, s("imme")),
            plural2s           = self.many(r.singular1_past, s("itte")),
            plural3s           = self.many(r.singular3_past, s("ivat")),
            plural1_negative   = r.root_strong + eet,
            plural2_negative   = r.root_strong + eet,
            plural3_negative   = r.root_strong + eet,
            passive            = r.root_passive + s("tiin"),
            passive_negative   = r.root_passive + s("tu"),)

    def indicative_perfect(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        ut = r.root_strong + s(r.suffix_ut)
        eet = r.root_strong + s(r.suffix_eet)

        return VerbPersonalForms(singular1          = ut,
                                 singular2          = ut,
                                 singular3          = ut,
                                 singular1_negative = ut,
                                 singular2_negative = ut,
                                 singular3_negative = ut,
                                 plural1            = eet,
                                 plural2            = eet,
                                 plural3            = eet,
                                 plural1_negative   = eet,
                                 plural2_negative   = eet,
                                 plural3_negative   = eet,
                                 passive            = r.root_passive + s("tu"),
                                 passive_negative   = r.root_passive + s("tu"),)

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
                                 passive            = r.root_passive + s("taisiin"),
                                 passive_negative   = r.root_passive + s("taisi"),)

    def potential_present(self) -> VerbPersonalForms:
        r = self.roots
        s = self.s

        ne = r.potential_root + s("e")

        return VerbPersonalForms(singular1          = ne + s("n"),
                                 singular2          = ne + s("t"),
                                 singular3          = r.potential_s3_root + s("e"),
                                 singular1_negative = ne,
                                 singular2_negative = ne,
                                 singular3_negative = ne,
                                 plural1            = ne + s("mme"),
                                 plural2            = ne + s("tte"),
                                 plural3            = r.potential_p3_root + s("vat"),
                                 plural1_negative   = ne,
                                 plural2_negative   = ne,
                                 plural3_negative   = ne,
                                 passive            = r.root_passive + s("taneen"),
                                 passive_negative   = r.root_passive + s("tane"),)

    def imperative_present(self) -> VerbPersonalFormsImperativePresent:
        r = self.roots
        s = self.s

        ko = r.imperative_root + s("ko")

        return VerbPersonalFormsImperativePresent(
            singular2          = r.root_weak,
            singular3          = ko + s("on"),
            singular2_negative = r.root_weak,
            singular3_negative = ko,
            plural1            = r.imperative_root + s("kaamme"),
            plural2            = r.imperative_root + s("kaa"),
            plural3            = r.imperative_root + s("koot"),
            plural1_negative   = ko,
            plural2_negative   = ko,
            plural3_negative   = ko,
            passive            = r.root_passive + s("takoon"),
            passive_negative   = r.root_passive + s("tako"),)

    def many(self, roots: [str], suffix: str) -> [str]:
        # some verb forms have multiple root forms, like yltää:ylti/ylsi
        return [r + suffix for r in roots]

    # suffix
    def s(self, text) -> str:
        return change_to_same_vowel_group_prefer_umlauts(self.roots.root_weak, text)
