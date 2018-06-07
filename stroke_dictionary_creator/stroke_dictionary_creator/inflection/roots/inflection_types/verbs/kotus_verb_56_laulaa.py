from .moduses import *
from ...gradation import identity

class KotusVerb56Laulaa():
    def __init__(self, word, gradation_fn = identity):
        self.word = word
        self.gradation_fn = gradation_fn

    def moduses(self):
        roots = self._roots()
        return VerbModuses(roots)

    def participles(self):
        roots = self._roots()
        return VerbParticiples(self.word,
                               roots,
                               self.gradation_fn,
                               self.moduses())

    def _roots(self):
        word_alt = self.gradation_fn(self.word)
        [root, v]         = reverse_parse(self.word, root_and_double_end_vowel)
        [root_alt, v_alt] = reverse_parse(word_alt, root_and_double_end_vowel)

        roots = VerbRoots(present = root + v,
                          present_passive = root_alt + "e")
        return roots
