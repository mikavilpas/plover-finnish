from .moduses import *

class KotusVerb56Laulaa():
    def moduses(self, word):
        [root, v] = reverse_parse(word, root_and_double_end_vowel)
        roots = VerbRoots(present = root + v,
                          present_passive = root + "e")

        return VerbModuses(roots)
