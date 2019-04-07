from .adjective import inflect_as, Adjective
from .. import base

def joukahainen_adjective_arvelu(word, gradation_fn = base.identity) -> Adjective:

    # all words in this class end in "ttu" or "tty"
    (maini, t, u) = base.reverse_parse(gradation_fn(word),
                                       base.root_and_cv_ending)
    mainitumpi = maini + t + u + "mpi"
    mainituin  = maini + t + u + "in"

    return Adjective(positive    = inflect_as(word, "arvelu", gradation_fn),
                     comparative = inflect_as(mainitumpi, "suurempi", None),
                     superlative = inflect_as(mainituin, "sisin", None))
