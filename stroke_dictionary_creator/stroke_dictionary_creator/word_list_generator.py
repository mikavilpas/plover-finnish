# generate the joukahainen.txt word list.
# Takes the joukahainen.xml file's path as an input. An up to date version can be obtained from:
# https://github.com/voikko/corevoikko/blob/master/voikko-fi/vocabulary/joukahainen.xml
# It is not included in this repository.

import sys
import io
from toolz import functoolz
from xml.etree import ElementTree as ET

def read_words(data):
    return data.findall("word")

def convert_word(word_datum):
    form = word_datum.findtext("forms/form")
    infclass = word_datum.findtext("inflection/infclass")
    data = "{};{}".format(form, infclass)
    return data

def write_to_file(filepath, lines):
    with io.open(filepath, "w") as f:
        for line in lines:
            f.write(line + "\n")

def remove_abbreviations(lines):
    return [l for l in lines if ";None" not in l]

def main(args):
    path = args[1]

    data      = ET.parse(path).getroot()
    word_data = read_words(data)
    word_ids  = functoolz.thread_first(map(convert_word, word_data),
                                       sorted,
                                       remove_abbreviations)

    filepath = "../../wordlists/joukahainen.txt"
    write_to_file(filepath, word_ids)
    print("Wrote {} words with inflection information to file {}".format(len(word_ids), filepath))

if __name__ == '__main__':
    sys.exit(main(args = sys.argv))
