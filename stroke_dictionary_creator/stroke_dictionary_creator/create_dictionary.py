# -*- coding: utf-8 -*-
import glob
import json
import os
import sys
from typing import Any, List

from ruamel.yaml import YAML
from toolz import functoolz

import manually_resolved_conflicts_service as conflicts
import stroke_validation as validation


def write_as_json_stroke_dictionary(destination, flat_stroke_dictionary):
    print("Writing output to: %s" % destination)
    with open(destination, "w") as f:
        json.dump(flat_stroke_dictionary,
                  f,
                  ensure_ascii = False,
                  indent = 2,
                  sort_keys = False)

def reverse_keys_and_values(d) -> dict:
    return {v: k for k, v in d.items()}

def warn_about_conflicts(new_dict, target_dict):
    new_strokes    = set(new_dict.values())
    target_strokes = set(target_dict.values())

    conflicting_strokes         = new_strokes.intersection(target_strokes)
    conflict_resolution_strokes = conflicts.conflict_strokes(load_file_as_yaml)

    for stroke in conflicting_strokes:
        new_words = [w for w, s in new_dict.items() if s == stroke]
        target_words = [w for w, s in target_dict.items() if s == stroke]
        words = list(set(new_words + target_words))

        if len(words) > 1 and stroke not in conflict_resolution_strokes:
            # ^ don't warn in case the strokes are exactly the same

            # Print the output in a format that can be easily pasted to the
            # conflicts file.
            print("{}: {}".format(stroke, words))

def combine(dictionaries) -> dict:
    # in case of conflicting_strokes, keeps the values specified earlier in the order of
    # dicts
    combined = {}
    for d in dictionaries:
        warn_about_conflicts(d, combined)
        combined.update(d)
    return combined

def load_file_as_yaml(filepath):
    with open(filepath) as f:
        d = YAML(typ="safe", pure=True).load(f)
        name = os.path.basename(filepath)
        print("Loaded %s with %s entries." % (name, len(d)))
        return d

def load_file_as_json(filepath):
    with open(filepath) as f:
        d = YAML(typ="safe", pure=True).load(f)
        name = os.path.basename(filepath)
        print("Loaded %s with %s entries." % (name, len(d)))
        return d

def load_dictionaries_from_path(path):
    yaml_dictionaries = list(map(load_file_as_yaml,
                                 glob.glob("../input_dictionaries/*.yaml")))

    json_dictionaries = list(map(load_file_as_json,
                                 glob.glob("../input_dictionaries/*.json")))
    return list(yaml_dictionaries + json_dictionaries)

def apply_conflict_resolution(strokes) -> dict:
    conflict_resolution_strokes = conflicts.conflict_strokes(load_file_as_yaml)
    print("Applying {} conflict resolution strokes."
          .format(len(conflict_resolution_strokes)))
    strokes.update(conflict_resolution_strokes)
    return strokes

def main():
    input_path = "../input_dictionaries/"
    print()
    print("Reading input yaml dictionaries from: %s" % input_path)

    flat_dictionary = functoolz.thread_first(
        load_dictionaries_from_path(input_path),
        combine,
        validation.assert_dictionary_valid,
        reverse_keys_and_values,
        apply_conflict_resolution)

    output_path = "../../plugin/plover_finnish/plover_finnish/dictionaries/plover_finnish.json"
    print("")
    print("Input dictionaries read. All strokes valid.")
    write_as_json_stroke_dictionary(output_path, flat_dictionary)
    print("")
    print("%s strokes total." % len(flat_dictionary))
    return 0 # no error_msg

if __name__ == '__main__':
    sys.exit(main())
