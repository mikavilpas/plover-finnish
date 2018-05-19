# S T K P V H R A O * E I N K S H T R e o i a

# new Finnish keys
KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'V-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-I',
    '-N', '-K', '-S', '-H', '-T', '-R', '-e', '-o', '-i', '-a',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '5-', '0-', '-E', '-I', '*')

# TODO end vowels could be considered suffixes
# SUFFIX_KEYS = ('-S', '-G', '-Z', '-D')
SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '0-',
    '-N': '-6',
    '-S': '-7',
    '-T': '-8',
    '-e': '-9',
}

UNDO_STROKE_STENO = '*'

ORTHOGRAPHY_RULES = [
    # Collapse vowels in suffixes
    # como + endo = comendo
    # cai + iria = cairia
    # (r'^(.+)[aeouiáéíóúãõâêôàü] \^ ([aeouiáéíóúãõâêôàü]\w*)$', r'\1\2'),
]

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Gemini PR': {
        '#'         : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),
        'S-'        : ('S1-', 'S2-'),
        'K-'        : 'T-',
        'T-'        : 'K-',
        'F-'        : 'P-',
        'P-'        : 'W-',
        'L-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-U'        : '-U',
        '-R'        : '-F',
        '-W'        : '-R',
        '-B'        : '-P',
        '-P'        : '-B',
        '-G'        : '-L',
        '-H'        : '-G',
        '-T'        : '-T',
        '-S'        : '-S',
        '-D'        : '-D',
        '-Z'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'K-'        : 'w',
        'T-'        : 's',
        'F-'        : 'e',
        'P-'        : 'd',
        'L-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-R'        : 'u',
        '-W'        : 'j',
        '-B'        : 'i',
        '-P'        : 'k',
        '-G'        : 'o',
        '-H'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'K-'   : 'T',
        'T-'   : 'K',
        'F-'   : 'P',
        'P-'   : 'W',
        'L-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-U'   : 'U',
        '-R'   : 'F',
        '-W'   : 'Q',
        '-B'   : 'N',
        '-P'   : 'B',
        '-G'   : 'L',
        '-H'   : 'G',
        '-T'   : 'Y',
        '-S'   : 'X',
        '-D'   : 'D',
        '-Z'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'K-'   : 'T-',
        'T-'   : 'K-',
        'F-'   : 'P-',
        'P-'   : 'W-',
        'L-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-R'   : '-F',
        '-W'   : '-R',
        '-B'   : '-P',
        '-P'   : '-B',
        '-G'   : '-L',
        '-H'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'K-'   : 'T-',
        'T-'   : 'K-',
        'F-'   : 'P-',
        'P-'   : 'W-',
        'L-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-U'   : '-U',
        '-R'   : '-F',
        '-W'   : '-R',
        '-B'   : '-P',
        '-P'   : '-B',
        '-G'   : '-L',
        '-H'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'K-'   : 'T-',
        'T-'   : 'K-',
        'F-'   : 'P-',
        'P-'   : 'W-',
        'L-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-U'   : '-U',
        '-R'   : '-F',
        '-W'   : '-R',
        '-B'   : '-P',
        '-P'   : '-B',
        '-G'   : '-L',
        '-H'   : '-G',
        '-T'   : '-T',
        '-S'   : '-S',
        '-D'   : '-D',
        '-Z'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

DICTIONARIES_ROOT = 'asset:plover:assets'
DEFAULT_DICTIONARIES = ()
