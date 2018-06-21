from .base import *

class KotusNoun1Valo(Noun):
    def __init__(self, word: str, gradation_fn = identity):
        self.word = word

        # these examples use the word aalto (gradation i: aalto-aallon)
        (aalt, o) = reverse_parse(word, root_and_end_vowel)
        aallo = gradation_fn(word)
        aalto = word

        super().__init__(
            NounStems(
                nominative         = aalto,
                genitive           = aallo,
                partitives         = [aalto],
                partitives_plural  = [aalto + self.s("j")],
                locationals_plural = [aallo + self.s("i")],
                essive             = aalto,
                plural             = aallo,
                illatives          = [aalto + self.s("u")]),
            genitives_plural = [aalto + self.s("jen")],
            illatives_plural = [aalto + self.s("ihin")])
