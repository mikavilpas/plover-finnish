from voikko import inflect_word, voikkoinfl, voikkoutils

def is_custom_compound_noun(word):
    return "=" in word

def not_inflectable(word, infclass):
    no_inflectable_reference_word = infclass.endswith("None")

    # this could be allowed later, since they actually technically can be
    # inflected
    custom_compound_noun = is_custom_compound_noun(word)

    return no_inflectable_reference_word or custom_compound_noun

def inflected_forms(word, infclass):
    # The inflections for all words cannot be retrieved. Some words have very
    # irregular forms that the inflector can only parse, not produce.
    #
    # An example: yö (night) - yön (the night's), öin (with nights) - öiden
    # (nights')
    if not_inflectable(word, infclass):
        # this could be allowed later, since they actually technically can be
        # inflected
        if is_custom_compound_noun(word):
            # print("    skipping custom compound word {}".format(word))
            return set()
        return set([word])
    else:
        inflections = inflect_word.inflect_word(word, infclass).values()
        return set(inflections)

nouns = inflect_word.noun_types
verbs = inflect_word.verb_types
nouns_and_verbs = nouns + verbs

def joukahainen_gradation_to_kotus(word: str,
                                   joukahainen_refword: str,
                                   joukahainen_gradation: str) -> str:
    # Joukahainen (the Finnish word list) has its own gradation classes for an
    # unknown reason. To properly apply gradation, the more official (I guess)
    # class of the word is needed. The class can be converted with this
    # function for this purpose.

    # this algorithm is a bit stupid but seems to work in practice
    for kl in nouns_and_verbs:
        gradation: str = kl.kotusGradClass(word, joukahainen_gradation)
        if gradation not in ["", None]:
            return gradation
