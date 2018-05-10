This page describes the design and layout of the Finnish steno keyboard.

```
---------------------------------------------------------------------------------
|                                  N U M B E R                                  |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
|       |   T   |   R   |   K   |       |   R   |   R   |   T   |   A   |   E   |
|       |       |       |       |       |       |       |       |       |       |
|   S   |---D---|---B---|---L---|   *   |-------|-------|-------|---U---|-------|
|       |       |       |       |       |       |       |       |       |       |
|       |   K   Q   V   |   R   |       |   S   |   N   |   K   |   O   |   I   |
|       |       |       |       |       |       |       |       |       |       |
------------------------|-------|-------|-------|-------|-------|-------|--------
                    |       |       |       |       |
                    |   A   |   O   |   E   |   I   |
                    |       |       |       |       |
                    ---------------------------------
```

# General notes

## Keys must be rearranged

The layout of the keyboard must be such that it is well adapted to the Finnish
language.

Because of the nature of the language, **some keys will need to be rearranged**
from the English one. It makes no sense to build a system that isn't good for
writing in the language it's made for.

# Vowel system

## A stroke to switch the vocal harmony group to the opposite one

In the following, the Finnish vowel harmony is accounted for with the notation
`2(4)`, indicating 4 different vowel sounds (for example `a, u, ä, y`), but
which is possible to reduce down to 2 forms of writing.

This is based on the idea that:

* `A` and `Ä` both never occur in the same word
* in case of a conflict, the more common word is chosen
* in case the wrong word was guessed, the writer can change the vowel group to
  the opposite one. For example the word "paasto" (fast, as in the act of
  fasting) could be chosen, but can be changed afterward to be the word "päästö"
  (emission)

It must be possible to:
* write 5(8) double vowel sounds: `aa,ee,ii,oo,uu,yy,ää,öö`
* write diphtong sounds. Finnish has a limited number of diphtong sounds.
* write vocal sounds in the most common root words.
    * this is a special requirement because the common diphtongs are based on
      syllables, while the strokes for the root words span many syllables
    * Hence the normal rules don't apply.

# Suffix system

* **It should be possible to guess how to add a suffix**, based on the writer's
understanding of Finnish.

