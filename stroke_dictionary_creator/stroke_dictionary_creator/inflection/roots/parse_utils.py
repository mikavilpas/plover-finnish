from parsy import *

# root words are simpler to parse in reverse order
def reverse(s): return s[::-1]

def reverse_parse(word, p):
    return_value = p.parse(reverse(word))
    if len(return_value) == 2:
        (root, data) = return_value
        return (reverse(root), data)
    return reverse(return_value)
