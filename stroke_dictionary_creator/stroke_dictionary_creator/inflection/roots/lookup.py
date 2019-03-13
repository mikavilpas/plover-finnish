from . import joukahainen_kotus_mapping as mapping
from . import gradation as g

def lookup_verb(word, refword, joukahainen_gradation_class = None):
    verb_info = mapping.verbs[refword]
    verb      = verb_info.verb_class
    gradation = _get_gradation(word,
                               refword,
                               joukahainen_gradation_class,
                               verb_info.gradation_fn)
    return verb(word, gradation)

def lookup_nominal(word, refword, joukahainen_gradation_class = None):
    nominal_info = mapping.nominals[refword]
    nominal      = nominal_info.inflection_fn
    gradation    = _get_gradation(word,
                                  refword,
                                  joukahainen_gradation_class,
                                  nominal_info.gradation_fn)
    return nominal(word, gradation)

def _get_gradation(word,
                   refword,
                   joukahainen_gradation_class,
                   mapping_default_gradation):

    if joukahainen_gradation_class is not None:
        return g.gradation_function(word,
                                    refword,
                                    joukahainen_gradation_class)
    else:
        return mapping_default_gradation or g.identity
