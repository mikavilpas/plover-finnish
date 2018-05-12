import tools

def not_a_name(word, chars):
    first_character = word[0]
    return not first_character.isupper() and chars in word

def compactify(permutation):
    # a readable view of the entire data set for this permutation
    name = permutation["character_pair"]

    words = permutation["matched_words"]
    properties = dict(matched_words_preview = words[:4],
                      count = len(words))
    return {name: properties}

def count_of_words(a):
    (char_pair, properties) = list(a.iteritems())[0]
    return properties["count"]

def has_matches(consonant_group):
    return count_of_words(consonant_group) > 0

def frequency_analysis(character_permutations, word_filter):
    words = tools.get_finnish_wordlist()

    results = map(
        lambda c: compactify(
            tools.permutations_present_in_words(c, words, word_filter)),
        character_permutations)

    results = filter(has_matches, results)
    results = sorted(results, key = count_of_words, reverse = True)
    return results
