#! /bin/bash

set -x # show all commands when executing them

echo "Redoing the dictionary from scratch."

rm ../input_dictionaries/*autogenerated*.json -v

time python ./create_single_strokes.py | tee ./create_single_strokes.log
time python ./create_double_strokes.py | tee ./create_double_strokes.log
time python ./create_compound_noun_strokes.py | tee ./create_compound_noun_strokes.log

time python ./create_dictionary.py | tee ./create_dictionary.log
