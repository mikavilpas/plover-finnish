from ensure import ensure
from collections import namedtuple

# How to check if an object is an instance of a namedtuple?
# https://stackoverflow.com/a/2166841/1336788
def isnamedtupleinstance(x):
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple: return False
    f = getattr(t, '_fields', None)
    if not isinstance(f, tuple): return False
    return all(type(n)==str for n in f)

def ensure_inflections_equal(expected, actual):
    ensure(expected).is_a(type(actual))
    for k,expected_value in expected._asdict().items():
        actual_value = getattr(actual, k)

        # allow recursion for namedtuple only
        if isnamedtupleinstance(actual_value):
            ensure_inflections_equal(expected_value, actual_value)
        else:
            ensure((k, expected_value)).equals((k,actual_value))
