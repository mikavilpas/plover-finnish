from .. import base
from .adjective import Adjective, inflect_as, inflect_with

def joukahainen_adjective_valo(word, gradation_fn = base.identity) -> Adjective:

    # The example word is "aito;adjective-valo-av1"
    aido = gradation_fn(word)

    # The example word is "halju;adjective-valo"
    haljumpi = aido + "mpi"
    haljuin  = aido + "in"

    return Adjective(positive    = inflect_with(word, "valo", gradation_fn),
                     comparative = inflect_as(haljumpi, "suurempi"),
                     superlative = inflect_as(haljuin, "sisin"))
