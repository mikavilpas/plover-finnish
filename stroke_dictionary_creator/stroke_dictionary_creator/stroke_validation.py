from ensure import check
import stroke_parser
import parsy

# can be found in the file /plugin/plover_finnish/plover_finnish/system.py
finnish_steno_order = "STKPVHRAO*EINKSHTReoia"

def assert_stroke_has_valid_characters(word, stroke):
    # consider - a valid character
    valid_characters = finnish_steno_order + "-"
    for c in stroke:
        if not check(c).is_in(valid_characters):
            error_msg = "The word {} and its stroke {} contains the unknown character {}".format(word, stroke, c)
            raise Exception(error_msg)

def assert_stroke_writable(word, stroke):
    assert_stroke_has_valid_characters(word, stroke)

def assert_no_duplicate_keys_used(word, stroke):
    try:
        stroke_parser.stroke.parse(stroke)
    except parsy.ParseError as e:
        msg = "Error with the word {} and its stroke {}".format(word, stroke)
        raise Exception(msg, e)

def assert_dictionary_valid(dictionary) -> dict:
    for word, strokes in dictionary.items():
        for stroke in strokes.split("/"):
            assert_stroke_writable(word, stroke)
        assert_no_duplicate_keys_used(word, stroke)
    return dictionary
