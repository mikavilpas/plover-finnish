import sys
sys.path.append("../../word-analyser/")
import word_analyser.tools as tools

def strokeify(words):
    """Takes a list of words. Returns a list of lists that contains the strokes
    for that word.

    Example:
    "oi" -> [["OI"]]"""
    return [[]]

def main():
    words = tools.get_finnish_wordlist()
    print("Loaded {} Finnish language words and abbreviations.".format(len(words)))
    strokes = map(strokeify, words)
    # TODO write to yaml file
    return 0

if __name__ == '__main__':
    sys.exit(main())
