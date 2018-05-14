This page describes the design and layout of the Finnish steno keyboard.

```
---------------------------------------------------------------------------------
|                                  N U M B E R                                  |
---------------------------------------------------------------------------------
|       |       |       |       |       |       |       |       |       |       |
|       |   T   F   P   M   H   |       |   N       S   |   T   |   E   |   I   |
|       |       |       |       |       |       |       |       |       |       |
|   S   |---D---G---B---|---L---|   *   |-------|---M---|--- ---|---U---|-------|
|       |       |       |       |       |       |       |       |       |       |
|       |   K   Q   V   |   R   |       |   K   |   H   P   R   |   O   |   A   |
|       |       |       |       |       |       |       |       |       |       |
---------------------------------------------------------------------------------
                    |       |       |       |       |
                    |   A   U   O   |   E   |   I   |
                    |       |       |       |       |
                    ---------------------------------
```

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [General design notes](#general-design-notes)
    - [Keys must be rearranged](#keys-must-be-rearranged)
- [Layout specific stroke notation](#layout-specific-stroke-notation)
- [Vowel system](#vowel-system)
    - [Initial vowel](#initial-vowel)
    - [A stroke to switch the vocal harmony group to the opposite one](#a-stroke-to-switch-the-vocal-harmony-group-to-the-opposite-one)
    - [Vowel doubling (a -> aa)](#vowel-doubling-a---aa)
    - [Diphtongs](#diphtongs)
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

# Layout specific stroke notation

The final vowels require an extra dash to avoid confusing it with the middle
vowels.

Examples:

| Stroke  | Notes                               |
| ----    | ----                                |
| `A-`    | middle A                            |
| `-A`    | final A                             |
| `AEOI-` | all initial vowels (in the middle)  |
| `AA`    | initial A and final A               |
| `S-`    | initial S                           |
| `SA-`   | S and A but no final vowel          |
| `-SA`   | Final consonant S and final vowel A |

# Vowel system

There are several vowel sounds that are needed for the Finnish language:
 
* One sound per vowel
* Doubled vowels
* Combinations of two vowels (diphtongs)

## Initial vowel

| Stroke | Notes                               |
| ----   | ----                                |
| `A-`   | a and ä                             |
| `E-`   | e                                   |
| `O-`   | o and ö                             |
| `I-`   | i                                   |
| `AE-`  | u and y                             |
| `OI-`  | u and y also. Helps with diphtongs. |

The diphtong "ae" doesn't exist in Finnish, so it can be used for other things.

## A stroke to switch the vocal harmony group to the opposite one

In the following, the Finnish vowel harmony is accounted for with the notation
`2(4)`, indicating 4 different vowel sounds (for example `a, u, ä, y`), but
which is possible to reduce down to 2 forms of writing.

| Strokes        | Finnish          | English                         | Notes |
| ----           | ----             | ----                            | ----  |
| `S*A- / AE-`   | saa -> sää       | he/she gets/receives -> weather |       |
| `P*ASTO / AE-` | paasto -> päästö | fasting -> emission             |       |

This is based on the idea that:

* `A` and `Ä` both never occur in the same word
* in case of a stroke conflict, the more common word is chosen
* if a common word is not found, use the AOU variant if it exists
* if one doesn't exist, use the ÄÖY variant
* in case the wrong word was guessed, the writer can change the vowel group to
  the opposite one. For example the word "paasto" (fast, as in the act of
  fasting) could be chosen, but can be changed afterward to be the word "päästö"
  (emission)

## Vowel doubling (a -> aa)

Can be doubled with `*`.

| Strokes | Finnish | English              | Notes |
| ----    | ----    | ----                 | ----  |
| `PH*A-` | maa     | the ground           |       |
| `S*A-`  | saa     | he/she gets/receives |       |

## Diphtongs

Vowel harmony rules apply, which means some diphtongs are only reachable by
changing the vowel group with an extra stroke.

Ones using only the middle vowels:

| Strokes | Finnish example | English        | Notes      |
| ----    | ----            | ----           | ----       |
| `AU`    | kaula, käy      | neck, running  |            |
| `EI-`   | ei              | no             |            |
| `OI-`   | koira, töin     | dog, with jobs | öi is rare |
| `AI-`   | kaivo, äiti     | well, mother   |            |
| `AOI-`  | ui, hyi         | swim, ew       |            |

Ones that are only possible to stroke using the final vowels:

| Strokes | Finnish example | English                | Notes      |
| ----    | ----            |                        | ----       |
| `IE`    | tie             | road                   |            |
| `OU`    | koulu, löyly    | school, hot steam      |            |
| `IU`    | hius, kääriytyä | hair, to wrap          |            |
| `EEO`   | keula, peseytyä | front, to wash oneself | ey is rare |
| `AOO`   | yö, vuo         | night, stream          |            |

## Final vowel

Not all diphtongs are supported.
No long vowels are supported.

A special option `-IA` for the "-ia" and "-ija" endings is provided.

| Strokes | character | Notes |
| ----    | ----      | ----  |
| `-IA`   | ia,ija    |       |

This precise layout was chosen because it can support the largest amount of
ending vowels. Included in this repository is the full analysis made to find
this out.


# Consonant system

## Initial consonant

The initial consonant has almost the same layout as in English.

| Strokes  | character | Notes                                           |
| ----     | ----      | ----                                            |
| `PV--`   | b         |                                                 |
| `KR--`   | c         |                                                 |
| `TK--`   | d         |                                                 |
| `TP--`   | f         |                                                 |
| `TKPV--` | g         |                                                 |
| `H--`    | h         |                                                 |
| `SKVR--` | j         |                                                 |
| `K--`    | k         |                                                 |
| `HR--`   | l         |                                                 |
| `PH--`   | m         |                                                 |
| `TPH--`  | n         |                                                 |
| `P--`    | p         |                                                 |
| `KV--`   | q         |                                                 |
| `R--`    | r         |                                                 |
| `S--`    | s         |                                                 |
| `T--`    | t         |                                                 |
| `V--`    | v         | switched with w                                 |
| `SR--`   | w         | very rare in Finnish                            |
|          | y         | missing because it's not a consonant in Finnish |
| `VR--`   | z         | very rare. Is `S*` in the English layout.       |

## Final consonant

Not all consonants are supported on this side.

| Strokes | character | Notes                                  |
| ----    | ----      | ----                                   |
| `-H`    | h         |                                        |
| `-K`    | k         | k                                      |
| `-NST`  | l         |                                        |
| `-SH`   | m         |                                        |
| `-N`    | n         |                                        |
| `-HR`   | p         |                                        |
| `-R`    | r         |                                        |
| `-S`    | s         |                                        |
| `-T`    | t         |                                        |
| `-SR`   | v         | same characters as on the initial side |

## Doubling of the final consonant

In Finnish it's very common to indicate the length of the consonant by having it
written as a doubled consonant. There is a shortcut for this, which can be used
to end a word.

| Strokes | characters | Examples |
| ----    | ----       | ----     |
| `-NKS`  | nn         | kannu    |
| `-NKH`  | kk         | akka     |
| `-KHS`  | mm         | kummi    |
| `-NSH`  | ss         | kassi    |
| `-STR`  | tt         | Matti    |
| `-HTR`  | rr         | kurre    |

# Suffix system

* **It should be possible to guess how to add a suffix**, based on the writer's
understanding of Finnish.

