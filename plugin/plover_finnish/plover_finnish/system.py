# STKPVHRAO*EINKSHTReoia

KEYS = (
    '#',
    'S-', 'T-', 'K-', 'P-', 'V-', 'H-', 'R-',
    'A-', 'O-',
    '*',
    '-E', '-I',
    '-N', '-K', '-S', '-H', '-T', '-R', '-e', '-o', '-i', '-a',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '5-', '0-', '-E', '-I', '*')

SUFFIX_KEYS = ["-e", "-o", "-i", "-a"]

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
        'T-'        : 'T-',
        'K-'        : 'K-',
        'P-'        : 'P-',
        'V-'        : 'W-',
        'H-'        : 'H-',
        'R-'        : 'R-',
        'A-'        : 'A-',
        'O-'        : 'O-',
        '*'         : ('*1', '*2', '*3', '*4'),
        '-E'        : '-E',
        '-I'        : '-U',
        '-N'        : '-F',
        '-K'        : '-R',
        '-S'        : '-P',
        '-H'        : '-B',
        '-T'        : '-L',
        '-R'        : '-G',
        '-e'        : '-T',
        '-o'        : '-S',
        '-i'        : '-D',
        '-a'        : '-Z',
        'no-op'     : ('Fn', 'pwr', 'res1', 'res2'),
    },
    'Keyboard': {
        '#'         : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'S-'        : ('a', 'q'),
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'V-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('t', 'g', 'y', 'h'),
        '-E'        : 'n',
        '-I'        : 'm',
        '-N'        : 'u',
        '-K'        : 'j',
        '-S'        : 'i',
        '-H'        : 'k',
        '-T'        : 'o',
        '-R'        : 'l',
        '-e'        : 'p',
        '-o'        : ';',
        '-i'        : '[',
        '-a'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
    'Passport': {
        '#'    : '#',
        'S-'   : ('S', 'C'),
        'T-'   : 'T',
        'K-'   : 'K',
        'P-'   : 'P',
        'V-'   : 'W',
        'H-'   : 'H',
        'R-'   : 'R',
        'A-'   : 'A',
        'O-'   : 'O',
        '*'    : ('~', '*'),
        '-E'   : 'E',
        '-I'   : 'U',
        '-N'   : 'F',
        '-K'   : 'Q',
        '-S'   : 'N',
        '-H'   : 'B',
        '-T'   : 'L',
        '-R'   : 'G',
        '-e'   : 'Y',
        '-o'   : 'X',
        '-i'   : 'D',
        '-a'   : 'Z',
        'no-op': ('!', '^', '+'),
    },
    'Stentura': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-I'   : '-U',
        '-N'   : '-F',
        '-K'   : '-R',
        '-S'   : '-P',
        '-H'   : '-B',
        '-T'   : '-L',
        '-R'   : '-G',
        '-e'   : '-T',
        '-o'   : '-S',
        '-i'   : '-D',
        '-a'   : '-Z',
        'no-op': '^',
    },
    'TX Bolt': {
        '#'    : '#',
        'S-'   : 'S-',
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : '*',
        '-E'   : '-E',
        '-I'   : '-U',
        '-N'   : '-F',
        '-K'   : '-R',
        '-S'   : '-P',
        '-H'   : '-B',
        '-T'   : '-L',
        '-R'   : '-G',
        '-e'   : '-T',
        '-o'   : '-S',
        '-i'   : '-D',
        '-a'   : '-Z',
    },
    'Treal': {
        '#'    : ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B'),
        'S-'   : ('S1-', 'S2-'),
        'T-'   : 'T-',
        'K-'   : 'K-',
        'P-'   : 'P-',
        'V-'   : 'W-',
        'H-'   : 'H-',
        'R-'   : 'R-',
        'A-'   : 'A-',
        'O-'   : 'O-',
        '*'    : ('*1', '*2'),
        '-E'   : '-E',
        '-I'   : '-U',
        '-N'   : '-F',
        '-K'   : '-R',
        '-S'   : '-P',
        '-H'   : '-B',
        '-T'   : '-L',
        '-R'   : '-G',
        '-e'   : '-T',
        '-o'   : '-S',
        '-i'   : '-D',
        '-a'   : '-Z',
        'no-op': ('X1-', 'X2-', 'X3'),
    },
}

# DICTIONARIES_ROOT and DEFAULT_DICTIONARIES define the location of
# the dictionaries included to be used with this system by default.
# The dictionaries listed earlier have priority when used.
DICTIONARIES_ROOT = 'asset:plover_finnish:dictionaries'
DEFAULT_DICTIONARIES = [ 'user_finnish.json', 'plover_finnish.json' ]
