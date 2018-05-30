from ensure import ensure

def ensure_inflections_equal(expected, actual):
    for k,v in expected._asdict().items():
        ensure((k,v)).equals((k, getattr(actual, k)))
