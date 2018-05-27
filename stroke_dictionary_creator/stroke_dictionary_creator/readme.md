# Dictionary creator

The dictionary creator comes in two main scripts that can be used in steps in
order to create the main Finnish dictionary.

## `create_strokes_from_wordlist.py`

Reads in the Finnish word list, then goes through all the inflection forms of
each word, and creates strokes according to the Finnish steno theory.

## `create_dictionary.py`

Reads in all the dictionaries in the ../input_dictionaries/ directory, checks
that each stroke is valid, and finally writes the strokes to a JSON file that
Plover can read and use.
