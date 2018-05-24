# here are meta plugins that enhance the default dictionary based typing in Plover

import plover_finnish.vowel_group_service as vowel_group_service

def change_vowel_harmony_group(context, meta_args: str):
    '''Changes the vocal harmony group of the previous word. For example, paasto
    (fasting) will be changed to päästö (emission) by converting ao -> äö.

    :param context: The context of actions in Plover.
    :type context: plover.formatting._Context

    :param meta_args: Reserved for future use.
    :type meta_args: str

    :return: The next action for Plover to perform.
    :rtype: plover.formatting._Action
    '''

    last_word = context.last_action.word or ''
    action = context.last_action.copy_state()
    action.prev_replace = last_word
    action.prev_attach = True

    new_word = vowel_group_service.switch_vowel_group(last_word)
    action.text = action.word = new_word
    action.trailing_space = ''

    return action

def suffix_in_same_vowel_harmony_group(context, suffix: str):
    """Adds a suffix to the current word that has the matching vocal harmony group
    as the word. For example, paasto+ssa -> paastossa, but päästö+ssa ->
    päästössä (notice the ending a and ä are matched to the word).
    """
    last_word = context.last_action.word or ''
    action = context.new_action()
    action.prev_attach = True

    new_suffix = vowel_group_service.change_to_same_vowel_group(last_word, suffix)
    new_word = last_word + new_suffix

    action.word = action.text = new_word

    return action
