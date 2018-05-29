from parsy import *
from ..tokens import *
from ..noun_inflection_info import InflectionInfo
from ..gradation import identity
from ..parse_utils import reverse_parse

sys.path.append("../../../../plugin/plover_finnish/")
from plover_finnish.vowel_group_service import change_to_same_vowel_group

@generate
def root_and_end_vowel():
    end_vowel = yield vowel
    rest = yield character.at_least(1).concat()
    return [rest, end_vowel]
