#
# The source for (the implementation of) these mappings can be found in
# https://github.com/sp3ctum/corevoikko/blob/feature%2Fexploration/voikko-fi/common/hfconv.py#L23


from parsy import *
from .parse_utils import reverse, reverse_parse
from .tokens import *

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
    def add_k_for_word_pyyhe():
        # For words like pyyhe
        e = yield string("e")
        h = yield string("h")
        yy = yield vowel.times(2).concat()
        start = yield character.many().concat()

        return e + "k" + h + yy + start

    @generate
    def split_double_vowel_with_k():
        end = yield ((vowel + consonant) | consonant).many().concat()
        vowel2 = yield vowel
        vowel1 = yield vowel
        start = yield character.many().concat()

        return end + vowel2 + "k" + vowel1 + start

    parser = add_k_at_cvc_ending \
             | add_k_for_word_pyyhe \
             | split_double_vowel_with_k \
             | add_k_at_cvcv_ending

    return reverse(parser.parse(reverse(word)))

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
