from parsy import *
from .parse_utils import reverse, reverse_parse
from .tokens import *
from collections import OrderedDict

# Definitions for the more machine readable Joukahainen mappings into the
# (could be argued) more understandable Kotus system for gradation classes.
#
# The source for (the implementation of) these mappings can be found in
# https://github.com/sp3ctum/corevoikko/blob/feature%2Fexploration/voikko-fi/common/hfconv.py#L23

def gradate(word, a, b):
    word = reverse(word)
    target = reverse(a)
    replacement = reverse(b) if b else ''

    word = word.replace(target, replacement, 1)
    return reverse(word)

def gradator(from_, to):
    def do_gradate(word):
        result = gradate(word, from_, to)
        if result is None:
            raise Exception("cannot gradate {} from {} to {}."
                            .format(word, from_, to))
        return result

    return do_gradate

def find(word, substring):
    if substring is None:
        return None
    index = word.find(substring)
    return index if index >= 0 else None

def compile_voikko_gradation_regexp(pattern: str):
    import re
    # copied from hfconv
    pattern = pattern.replace('V', '(?:a|á|e|i|o|u|y|ä|ö|é)')
    pattern = pattern.replace('C', '(?:b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z|š|ž)')
    pattern = pattern.replace('A', '(?:a|ä)')
    pattern = pattern.replace('O', '(?:o|ö)')
    pattern = pattern.replace('U', '(?:u|y)')
    regExp = re.compile('^' + pattern + '$', re.IGNORECASE)
    return regExp

def compile_gradation_regex(gradclass):
    # gradclass:
    # ('valo', 'sw', [gradations])
    (refword, grade, gradations) = gradclass

    # gradations:
    # [('nt','(.*n)tU','lintu')]
    new_gradations = [(gradtype,
                       compile_voikko_gradation_regexp(pattern),
                       *rest)
                      for (gradtype, pattern, *rest)
                      in gradations]

    return (refword, grade, new_gradations)

# Inflection class map
from .voikko_hacks import hfconv
CLASSMAP = list(map(compile_gradation_regex, hfconv.modern_classmap))

def gradate_joukahainen(word, refword, gradation_class):
    gradations = reference_options(word, refword)
    matching = matching_gradations(word, gradation_class, gradations)

    if len(matching) == 0:
        raise ValueError("The gradation class {} is unknown/invalid for the word {}."
                         .format(gradation_class, word))
    gradtype = matching[0]

    gradator_fn = gradation_dispatch[gradation_class][gradtype]
    gradated_word = gradator_fn(word)

    return gradated_word

def matching_gradations(word, gradation_class: str, gradations):
    # Gradations are allowed based on the gradation_class, for example for the
    # words "lobata" (av2) and "taata" (av6), there could be false positives if
    # this weren't taken into account.
    allowed = allowed_gradations(gradation_class, gradations)
    matching = (grad_type
                for (grad_type, grad_regex, *_) in gradations
                if grad_regex.match(word)
                and grad_type in allowed)

    def _gradation_length(gradation_type):
        # eg. k>, kk, uku, lt, nt, tt, nk, ...
        return 0 if gradation_type is None else len(gradation_type)

    return sorted(matching, key = _gradation_length, reverse=True)

def gradate_kotus_d_joukahainen_av6_aie_aikeen(word) -> str:
    @generate
    def add_k_at_cvcv_ending():
        # For words like keritä,selitä,hylätä,juleta,keretä,virota
        end            = yield (vowel + consonant + vowel).concat()
        last_consonant = yield consonant
        start          = yield character.many().concat()

        return end + "k" + last_consonant + start

    @generate
    def add_k_at_cvc_ending():
        # For words like pyyhin
        end            = yield (consonant + vowel).concat()
        last_consonant = yield consonant
        start          = yield character.many().concat()

        return end + "k" + last_consonant + start

    @generate
    def split_double_vowel_with_k():
        end = yield ((vowel + consonant) | consonant).many().concat()
        vowel2 = yield vowel
        vowel1 = yield vowel
        start = yield character.many().concat()

        return end + vowel2 + "k" + vowel1 + start

    parser = add_k_at_cvc_ending | split_double_vowel_with_k | add_k_at_cvcv_ending

    return reverse(parser.parse(reverse(word)))

gradation_dispatch = dict(
    # the gradations have the same keys as defined in hfconv
    av1 = dict(
        # strong to weak
        uku = gradator("uku", "uvu"), # kotus M
        yky = gradator("yky", "yvy"), # kotus M (again)
        tt  = gradator("tt",  "t"),   # kotus C
        pp  = gradator("pp",  "p"),   # kotus B
        kk  = gradator("kk",  "k"),   # kotus A
        mp  = gradator("mp",  "mm"),  # kotus H
        nt  = gradator("nt",  "nn"),  # kotus J
        lt  = gradator("lt",  "ll"),  # kotus I
        rt  = gradator("rt",  "rr"),  # kotus K
        nk  = gradator("nk",  "ng"),  # kotus G
        p   = gradator("p",   "v"),   # kotus E
        t   = gradator("t",   "d"),   # kotus F
    ),
    av2 = dict(
        # weak to strong
        mm = gradator("mm", "mp"), # kotus H
        nn = gradator("nn", "nt"), # kotus J
        ll = gradator("ll", "lt"), # kotus I
        rr = gradator("rr", "rt"), # kotus K
        ng = gradator("ng", "nk"), # kotus G
        b = gradator("b",  "bb"),  # kind of like kotus B. (lobata -> lobbaan)
        g = gradator("g",  "gg"),  # kind of like kotus B. (digata -> diggaan)
        t = gradator("t",  "tt"),  # kotus C
        p = gradator("p",  "pp"),  # kotus B
        k = gradator("k",  "kk"),  # kotus A
        v = gradator("v",  "p"),   # kotus E
        d = gradator("d",  "t"),   # kotus F
    ),
    av3 = {"k>j": gradator("k", "j")}, # kotus L, strong to weak
    av4 = {"j>k": gradator("j", "k")}, # kotus L, weak to strong
    av5 = {"k>" : gradator("k", "")},  # kotus D, strong to weak

    # kotus D, weak (nonexisting) to strong
    av6 = {">k" : gradate_kotus_d_joukahainen_av6_aie_aikeen}
)

# some of the gradations have to be set in stone because they are needed for
# the creation of infinitives, and they are useful in tests as well.
gradate_kotus_a_takki_takin    = gradation_dispatch["av1"]["kk"]
gradate_kotus_b_kaappi_kaapin  = gradation_dispatch["av1"]["pp"]
gradate_kotus_c_tyttö_tytön    = gradation_dispatch["av1"]["tt"]
gradate_kotus_c_kate_katteen   = gradation_dispatch["av2"]["t"]
gradate_kotus_d_reikä_reiän    = gradation_dispatch["av5"]["k>"]
gradate_kotus_e_sopu_sovun     = gradation_dispatch["av1"]["p"]
gradate_kotus_f_satu_sadun     = gradation_dispatch["av1"]["t"]
gradate_kotus_f_keidas_keitaan = gradation_dispatch["av2"]["d"]
gradate_kotus_i_ilta_illan     = gradation_dispatch["av1"]["lt"]
gradate_kotus_j_hento_hennon   = gradation_dispatch["av1"]["nt"]
gradate_kotus_h_kumpi_kumman   = gradation_dispatch["av1"]["mp"]
gradate_kotus_i_ilta_illan     = gradation_dispatch["av1"]["lt"]
gradate_kotus_k_virta_virran   = gradation_dispatch["av1"]["rt"]
gradate_kotus_l_arki_arjen     = gradation_dispatch["av3"]["k>j"]

def allowed_gradations(gradation_class: str, gradations):
    return [grad_type
            for (grade, grad_type, grad_class) in hfconv.grads
            if grad_class == gradation_class]

def reference_options(word, refword):
    matches = [options
               for (classname, grade, options) in CLASSMAP
               if classname == refword]
    if len(matches) == 0:
        raise ValueError("gradation for (word '{}', refword '{}') not found"
                         .format(word, refword))
    else:
        return matches[0]

identity = lambda a: a
