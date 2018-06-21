from .base import *

class KotusNoun2Palvelu(Noun):
    def __init__(self, word: str, gradation_fn = identity):
        self.word = word

        # these examples use the word palvelu (no gradation in this class)
        palvelu = word
        (palvel, u) = reverse_parse(palvelu, root_and_end_vowel)

        super().__init__(
            NounStems(
                nominative         = palvelu,
                genitive           = palvelu,
                partitives         = [palvelu],
                partitives_plural  = [palvelu + self.s("it"),
                                      palvelu + self.s("j")],
                locationals_plural = [palvelu + self.s("i")],
                essive             = palvelu,
                plural             = palvelu,
                illatives          = [palvelu + u]),
            genitives_plural = [palvelu + self.s("jen"),
                                palvelu + self.s("iden"),
                                palvelu + self.s("itten")],
            illatives_plural = [palvelu + self.s("ihin")])
