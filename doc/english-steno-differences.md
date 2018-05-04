# Differences to the English language and the English steno system

The system inspiring the Finnish steno system is the English one. However,
Finnish and English are very different languages, and hence it makes sense to
have the two systems diverge. This document describes the design choices that
account for the differences present in the two languages.

## No need for phonetic writing

> When writing Finnish, the foundational principle is that each letter stands for
> one sound and each sound is always represented by the same letter, within the
> bounds of a single morpheme.
[Wikipedia: Finnish language orthographic principles](https://en.wikipedia.org/wiki/Finnish_orthography#Orthographic_principles)

## Heavy use of affixes (prefixes, infixes and postfixes)

Finnish language, contrary to English, does not use many words to convey
meaning. Instead it combines endings to words, creating long words that have a
lot of packed meaning.

In Finnish, words are most often based on a root word, with many affixes added
to it, in order to give it additional meaning. This is very much in contrast to
English, which uses multiple words instead of affixes.

| istua            | "to sit down" (istun "I sit down")          |
|                  |                                             |
| istahtaa         | "to sit down for a while"                   |
| istahdan         | "I'll sit down for a while"                 |
| istahtaisin      | "I would sit down for a while"              |
| istahtaisinko    | "should I sit down for a while?"            |
| istahtaisinkohan | "I wonder if I should sit down for a while" |

[wikipedia: Finnish language lexicon](https://en.wikipedia.org/wiki/Finnish_language#Lexicon)

*The Finnish steno system should give special focus to writing affixes.*

## More distinct vowels, but harmony in the use of them

There are 8 vowels, split into two groups:

![vowel harmony](https://upload.wikimedia.org/wikipedia/commons/e/e3/Finnish_vowel_harmony_Venn_diagram.svg)

Words with the vowels in the left and right groups do not occur in the same
word. 

*It should be possible to avoid having vowel keys for `ÄÖY`.*

## More vowel sounds

The following sounds are used.

* Single character (8 sounds, 5 with vowel harmony): `a,e,i,o,u,y,ä,ö` 
* Double character (8 sounds, 5 with vowel harmony): `aa,ee,ii,oo,uu,yy,ää,öö` 
* Diphtongs (28 sounds, 10 with vowel harmony):
** `ei,öi,äi,oi,ai`
** `ey,öy,äy`	
** `eu,ou,au`	
** `yi,ui,iu,iy`	
** `ie,yö,uo`	

Grand total: 44 sounds. The minimum number of keys that can express all
different possibilities is 6 (2^6=64).

If vowel harmony is taken to account, this number drops to 20, possible to
express with 5 keys (2^5=32).

*It is required to have extra keys to account for the larger number of vowel
sounds.*
