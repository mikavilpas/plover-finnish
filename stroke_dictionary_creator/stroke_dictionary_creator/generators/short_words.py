from parsy import *

from .generators import *

no_middle_key = success("-")
end_EN_ending = morpheme("en", "e")

no_end_vocal_sound = success("")

# Legend: (s)tart, (m)iddle, (e)nd consonant, end_vocal_part (v)owel
#
s = (initial_consonant)                                    .desc("start part")
m = (middle_vocal_sound | no_middle_key)                   .desc("middle part")
e = (final_two_consonants | final_consonant)               .desc("end consonant part")
v = (end_EN_ending | end_vocal_sound | no_end_vocal_sound) .desc("end vocal part")

def join(*items):
    return "".join([w for w in items if w])

short_word = seq(s.optional(),
                 m.optional(),
                 e.optional(),
                 v.optional()).combine(join)
