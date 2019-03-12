from . import joukahainen_kotus_mapping as mapping
from . import gradation as g

def lookup(word, nominal_or_verb, refword, joukahainen_gradation_class = None):
    def get_gradation(mapping_default_gradation):
        if joukahainen_gradation_class is not None:
            return g.gradation_function(word,
                                        refword,
                                        joukahainen_gradation_class)
        else:
            return mapping_default_gradation or g.identity

    if nominal_or_verb == "verb":
        verb_info = mapping.verbs[refword]
        verb      = verb_info.verb_class
        gradation = get_gradation(verb_info.gradation_fn)
        return verb(word, gradation)

    elif nominal_or_verb in ["noun", "adjective"]:
        nominal_info        = mapping.nominals[refword]
        inflection_function = nominal_info.inflection_fn
        gradation = get_gradation(nominal_info.gradation_fn)
        return nominal(word, gradation)

    else:
        raise Exception("Unknown word lookup: {}" % (word,
                                                     nominal_or_verb,
                                                     refword,
                                                     joukahainen_gradation_class))
