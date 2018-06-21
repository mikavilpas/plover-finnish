from .base import *

class KotusNoun3Valtio(Noun):
    def __init__(self, word: str, gradation_fn = identity):
        self.word = word

        # these examples use the word valtio (no gradation in this class)
        valtio = word
        (valti, o) = reverse_parse(valtio, root_and_end_vowel)

        super().__init__(
            NounStems(
                nominative         = valtio,
                genitive           = valtio,
                partitives         = [valtio],
                partitives_plural  = [valtio + self.s("it")],
                locationals_plural = [valtio + self.s("i")],
                essive             = valtio,
                plural             = valtio,
                illatives          = [valtio + o]),
            genitives_plural = [valtio + self.s("den"),
                                valtio + self.s("itten")],
            illatives_plural = [valtio + self.s("ihin")])
