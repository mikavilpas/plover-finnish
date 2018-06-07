from .moduses import *
from ...gradation import identity

class KotusVerb56Laulaa():
    def moduses(self, word, gradation_fn = identity):
        roots = self._roots(word, gradation_fn)
        return VerbModuses(roots)

    def participles(self, word, gradation_fn = identity):
        roots = self._roots(word, gradation_fn)
        return VerbParticiples(word, roots, gradation_fn)

    def _roots(self, word, gradation_fn):
        word_alt = gradation_fn(word)
        [root, v]         = reverse_parse(word, root_and_double_end_vowel)
        [root_alt, v_alt] = reverse_parse(word_alt, root_and_double_end_vowel)

        roots = VerbRoots(present = root + v,
                          present_passive = root_alt + "e")
        return roots
