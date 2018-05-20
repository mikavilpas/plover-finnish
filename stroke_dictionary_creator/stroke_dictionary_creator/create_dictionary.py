# -*- coding: utf-8 -*-
import sys
from ruamel.yaml import YAML
import glob
from toolz import functoolz
from functools import reduce

def merge_dictionaries(dictionaries):
    # in case of conflicts, keeps the values specified earlier in the order of
    # dicts

    # TODO report if there are any duplicates

    return reduce(lambda result, x: result.update(x), dictionaries)

def load_file_as_yaml(filepath):
    with open(filepath) as f:
        return YAML().load(f)

def load_dictionaries_from_path(path):
    yaml = YAML()
    yaml_file_paths = glob.glob("../input_dictionaries/*.yaml")

    return map(load_file_as_yaml, yaml_file_paths)

def main():
    dictionary = functoolz.pipe(load_dictionaries_from_path("../input_dictionaries/"),
                                merge_dictionaries)
    return 0 # no error

if __name__ == '__main__':
    sys.exit(main())
