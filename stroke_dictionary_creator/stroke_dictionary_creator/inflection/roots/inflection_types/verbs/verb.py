from .moduses import *
from ...gradation import identity
from .participles import VerbParticiples
from .infinitives import VerbInfinitives

class VerbBase():
    def __init__(self, word, gradation_fn = identity):
        self.word = word
        self.gradation_fn = gradation_fn

    def moduses(self) -> VerbModuses:
        roots = self._roots()
        return VerbModuses(roots)

    def participles(self) -> VerbParticiples:
        roots = self._roots()
        return VerbParticiples(self.word,
                               roots,
                               self.moduses())

    def infinitives(self) -> VerbInfinitives:
        roots = self._roots()
        return VerbInfinitives(self.word,
                               roots,
                               self.moduses())

    def _roots(self) -> VerbRoots:
        # override this in the subclass!
        raise Exception("_roots not implemented. This verb class cannot be used.")
