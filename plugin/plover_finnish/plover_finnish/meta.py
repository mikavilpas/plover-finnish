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
