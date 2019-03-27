# -*- coding: utf-8 -*-
import sys
import os
from ruamel.yaml import YAML
import glob
from toolz import functoolz
import json
import stroke_validation as validation
import manually_resolved_conflicts_service as conflicts

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
            # don't warn in case the strokes are exactly the same
            print("Warning: multiple words defined for the stroke {}. You'll need to resolve the conflict by hand.".format(stroke))
            print(words)

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
        print("Loaded %s with %s strokes." % (name, len(d)))
        return d

def load_dictionaries_from_path(path):
    yaml_file_paths = glob.glob("../input_dictionaries/*.yaml")

    return map(load_file_as_yaml, yaml_file_paths)

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
