This page describes the design and layout of the Finnish steno keyboard.

```
---------------------------------------------------------------------------------
|                                  N U M B E R                                  |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
|       |   T   F   P   M   H   |       |   R   |   P   |   T   |   A   |   E   |
|       |       |       |       |       |       |       |       |       |       |
|   S   |---D---G---B---|---L---|   *   |-------|-------|-------|---U---|-------|
|       |       |       |       |       |       |       |       |       |       |
|       |   K   Q   V   |   R   |       |   S   |   N   |   K   |   O   |   I   |
|       |       |       |       |       |       |       |       |       |       |
------------------------|-------|-------|-------|-------|-------|-------|--------
                    |       |       |       |       |
                    |   A   U   E   |   O   |   I   |
                    |       |       |       |       |
                    ---------------------------------
```

# General design notes

## Keys must be rearranged

The layout of the keyboard must be such that it is well adapted to the Finnish
language.

Because of the nature of the language, **some keys will need to be rearranged**
from the English one. It makes no sense to build a system that isn't good for
writing in the language it's made for.

# Vowel system

There are several vowel sounds that are needed for the Finnish language:
 
* One sound per vowel
* Doubled vowels
* Combinations of two vowels (diphtongs)

## Initial vowel

| Strokes | Notes   |
| ----    | ----    |
| `A`     | a and ä |
| `E`     | e       |
| `O`     | o and ö |
| `I`     | i       |
| `AE`    | u and y |

The diphtong "ae" doesn't exist in Finnish, so it can be used for other things.

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
    * Hence the normal rules don't apply

## Vowel doubling (a -> aa)

Can be doubled with `*`.

| Strokes | Finnish | English              | Notes |
| ----    | ----    | ----                 | ----  |
| `PH*A`  | maa     | the ground           |       |
| `S*A`   | saa     | he/she gets/receives |       |

## Final vowel

Only a single vowel is supported. No diphtongs or long vowels.

# Consonant system

Initial consonant the same as in English.

Final consonant can be doubled by making a star shape.

# Suffix system

* **It should be possible to guess how to add a suffix**, based on the writer's
understanding of Finnish.

