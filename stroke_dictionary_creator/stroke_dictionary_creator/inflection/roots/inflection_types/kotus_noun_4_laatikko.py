from .base import *

class KotusNoun4Laatikko(Noun):
    def __init__(self, word: str, gradation_fn = identity):
        self.word = word

        # these examples use the word laatikko (gradation a: laatikko-laatikon)
        laatikko = word
        (laatikk, o) = reverse_parse(laatikko, root_and_end_vowel)
        laatiko = gradation_fn(word)

        super().__init__(
            NounStems(
                nominative         = laatikko,
                genitive           = laatiko,
                partitives         = [laatikko],
                partitives_plural  = [laatikko + self.s("j"),
                                      laatiko + self.s("it")],
                locationals_plural = [laatiko + self.s("i")],
                essive             = laatikko,
                plural             = laatiko,
                illatives          = [laatikko + o]),
            genitives_plural = [laatiko + self.s("iden"),
                                laatiko + self.s("itten"),
                                laatikko + self.s("jen")],
            illatives_plural = [laatikko + self.s("ihin"),
                                laatiko + self.s("ihin")])
