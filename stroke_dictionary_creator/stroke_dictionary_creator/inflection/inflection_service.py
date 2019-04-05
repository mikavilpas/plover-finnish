from .roots.lookup import lookup_verb, lookup_nominal
from .parsing import word_and_class
from .roots.noun_inflection_info import InflectionInfo
from .roots.inflection_types.verbs.verb import VerbBase
from functools import reduce
from typing import List

def inflected_forms(word_info):
    (word, klass, reference_word, gradation) = word_and_class.parse(word_info)

    if klass == "verb":
        results = lookup_verb(word, reference_word, gradation)
        return _all_conjugations(results)

    elif klass in ["noun", "adjective", "pnoun_place"]:
        results = lookup_nominal(word, reference_word, gradation)
        return _flatten([], results)

    else:
        # print("Warning: cannot inflect %s" % word_info)
        return [word]

def _flatten(results, named_tuple) -> List[str]:
    def _add(l: list, word_or_list) -> List[str]:
        if type(word_or_list) is str:
            l.append(word_or_list)
        elif type(word_or_list) is list:
            l.extend(word_or_list)
        return l

    for word_or_list in named_tuple._asdict().values():
        _add(results, word_or_list)
    return results

def _all_conjugations(verb: VerbBase) -> List[str]:
    moduses     = verb.moduses()
    participles = verb.participles()
    infinitives = verb.infinitives()

    all_forms = [moduses.indicative_present(),
                 moduses.indicative_past(),
                 moduses.indicative_perfect(),
                 moduses.conditional_present(),
                 moduses.potential_present(),
                 moduses.imperative_present(),

                 participles.group_1_VA(),
                 participles.group_2_NUT(),
                 participles.group_3_MA_agent_participle(),
                 participles.group_4_VA_passive(),
                 participles.group_5_TU_passive(),
                 participles.group_6_negation(),

                 infinitives.group_1_A(),
                 infinitives.group_2_E(),
                 infinitives.group_3_MA(),
                 infinitives.group_4_MINEN(),
                 infinitives.group_5_MAINEN()]

    return reduce(_flatten, all_forms, [])
