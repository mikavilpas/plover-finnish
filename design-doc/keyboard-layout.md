This page describes the design and layout of the Finnish steno keyboard.

```
---------------------------------------------------------------------------------
|                                  N U M B E R                                  |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
|       |   T   F   P   M   H   |       |   R   M   N   |   P   |   I   |   E   |
|       |       |       |       |       |       |       |       |       |       |
|   S   |---D---G---B---|---L---|   *   |-------|-------|---H---|-------|---U---|
|       |       |       |       |       |       |       |       |       |       |
|       |   K   Q   V   |   R   |       |   S   |   T   |   K   |   A   |   O   |
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
                    |       |       |       |       |
                    |   A   U   E   |   O   |   I   |
                    |       |       |       |       |
                    ---------------------------------
```

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [General design notes](#general-design-notes)
    - [Keys must be rearranged](#keys-must-be-rearranged)
- [Vowel system](#vowel-system)
    - [Initial vowel](#initial-vowel)
    - [A stroke to switch the vocal harmony group to the opposite one](#a-stroke-to-switch-the-vocal-harmony-group-to-the-opposite-one)
    - [Vowel doubling (a -> aa)](#vowel-doubling-a---aa)
    - [Final vowel](#final-vowel)
- [Consonant system](#consonant-system)
    - [Initial consonant](#initial-consonant)
    - [Final consonant](#final-consonant)
- [Suffix system](#suffix-system)

<!-- markdown-toc end -->


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
* in case of a stroke conflict, the more common word is chosen
* if a common word is not found, use the AOU variant if it exists
* if one doesn't exist, use the ÄÖY variant
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

Not all diphtongs are supported.
No long vowels are supported.

A special option `-IA` for the "-ia" and "-ija" endings is provided.

| Strokes | character | Notes |
| ----    | ----      | ----  |
| `-IA`   | ia,ija    |       |

# Consonant system

## Initial consonant

The initial consonant has almost the same layout as in English.

| Strokes | character | Notes                                           |
| ----    | ----      | ----                                            |
| `PV`    | b         |                                                 |
| `KR`    | c         |                                                 |
| `TK`    | d         |                                                 |
| `TP`    | f         |                                                 |
| `TKPV`  | g         |                                                 |
| `H`     | h         |                                                 |
| `SKVR`  | j         |                                                 |
| `K`     | k         |                                                 |
| `HR`    | l         |                                                 |
| `PH`    | m         |                                                 |
| `TPH`   | n         |                                                 |
| `P`     | p         |                                                 |
| `KV`    | q         |                                                 |
| `R`     | r         |                                                 |
| `S`     | s         |                                                 |
| `T`     | t         |                                                 |
| `V`     | v         | switched with w                                 |
| `SR`    | w         | very rare in Finnish                            |
|         | y         | missing because it's not a consonant in Finnish |
| `VR`    | z         | very rare. Is `S*` in the English layout.       |

## Final consonant

Some characters are bundled together because there are so few keys. These are
shown in the format (a,b,c,d), which means that this key is used for the four
characters, and in case of conflicts the keys are matched front to back.

| Strokes | character | Notes                      |
| ----    | ----      | ----                       |
| `-P`    | b         | (b,p)                      |
| `-S`    | c         | (s,v,f,c,z)                |
| `-T`    | d         | (t,d)                      |
| `-S`    | f         | (s,v,f,c,z)                |
| `-K`    | g         | (k,g,q)                    |
| `-PK`   | h         |                            |
|         | (j)       | handled as the vowel i     |
| `-K`    | k         | (k,g,q)                    |
| `-`     | l         |                            |
| `-RN`   | m         | (rn,m) because rn is rare  |
| `-N`    | n         |                            |
| `-P`    | p         | (b,p)                      |
| `-K`    | q         | (k,g,q)                    |
| `-R`    | r         |                            |
| `-S`    | s         | (s,v,f,c,z)                |
| `-T`    | t         | (t,d)                      |
| `-S`    | v         | (s,v,f,c,z)                |
|         | w         |                            |
|         | y         | not a consonant in Finnish |
| `-S`    | z         | (s,v,f,c,z)                |


# Suffix system

* **It should be possible to guess how to add a suffix**, based on the writer's
understanding of Finnish.

