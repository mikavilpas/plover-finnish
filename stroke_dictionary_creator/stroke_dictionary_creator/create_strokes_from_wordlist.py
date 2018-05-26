import sys
import generators.short_words as sw
from toolz import functoolz
import inflection_service as infl

sys.path.append("../../word-analyser/")
import word_analyser.tools as tools

def strokeify(word):
    inflection_forms = infl.inflected_forms(word)
    print(inflection_forms)

    stroke = sw.safe_parse_short_word(word)
    if stroke != None:
        print(stroke)
    return stroke

def matched(stroke):
    return stroke is not None and not stroke.endswith("None")

def main():
    words_raw = tools.get_finnish_wordlist()
    print("Loaded {} Finnish language words and abbreviations.".format(len(words_raw)))
    strokes = functoolz.thread_last(words_raw,
                                    (map, strokeify),
                                    (filter, matched))
    print(list(strokes))
    # TODO write to yaml file
    return 0

if __name__ == '__main__':
    sys.exit(main())
