import unittest

from ensure import ensure

from .. import gradation as g
from ..noun_inflection_info import InflectionInfo
from .kotus_noun_2_palvelu import kotus_noun_2_palvelu
from .test_utils import ensure_inflections_equal


class TestInflectionType2(unittest.TestCase):
    def test_kotus_noun_2_palvelu_full_cases(self):
        data = kotus_noun_2_palvelu("palvelu")
        expected = InflectionInfo(nominative          = 'palvelu',
                                  nominative_plural   = 'palvelut',
                                  genitive            = 'palvelun',
                                  genitives_plural    = ['palvelujen',
                                                         'palveluiden',
                                                         'palveluitten'],
                                  partitives          = ['palvelua'],
                                  partitives_plural   = ['palveluita',
                                                         'palveluja'],
                                  accusatives         = ['palvelu',
                                                         'palvelun'],
                                  accusative_plural   = 'palvelut',
                                  inessive            = 'palvelussa',
                                  inessives_plural    = ['palveluissa'],
                                  elative             = 'palvelusta',
                                  elatives_plural     = ['palveluista'],
                                  illatives           = ['palveluun'],
                                  illatives_plural    = ['palveluihin'],
                                  adessive            = 'palvelulla',
                                  adessives_plural    = ['palveluilla'],
                                  ablative            = 'palvelulta',
                                  ablatives_plural    = ['palveluilta'],
                                  allative            = 'palvelulle',
                                  allatives_plural    = ['palveluille'],
                                  essives             = ['palveluna'],
                                  essives_plural      = ['palveluina'],
                                  translative         = 'palveluksi',
                                  translatives_plural = ['palveluiksi'],
                                  abessive            = 'palvelutta',
                                  abessives_plural    = ['palveluitta'],
                                  instructives_plural = ['palveluin'],
                                  comitatives_plural  = ['palveluine'])

        ensure_inflections_equal(expected, data)

    def test_kotus_noun_2_palvelu_umlauts(self):
        data = kotus_noun_2_palvelu("epäily")
        ensure(data.comitatives_plural).equals(["epäilyine"])

    def test_gradation(self):
        data = kotus_noun_2_palvelu("mainittu", g.gradate_kotus_c_tyttö_tytön)

        expected = InflectionInfo(nominative          = 'mainittu',
                                  nominative_plural   = 'mainitut',
                                  genitive            = 'mainitun',
                                  genitives_plural    = ['mainittujen',
                                                         'mainituiden',
                                                         'mainituitten'],
                                  partitives          = ['mainittua'],
                                  partitives_plural   = ['mainituita',
                                                         'mainittuja'],
                                  accusatives         = ['mainittu',
                                                         'mainitun'],
                                  accusative_plural   = 'mainitut',
                                  inessive            = 'mainitussa',
                                  inessives_plural    = ['mainituissa'],
                                  elative             = 'mainitusta',
                                  elatives_plural     = ['mainituista'],
                                  illatives           = ['mainittuun'],
                                  illatives_plural    = ['mainittuihin'],
                                  adessive            = 'mainitulla',
                                  adessives_plural    = ['mainituilla'],
                                  ablative            = 'mainitulta',
                                  ablatives_plural    = ['mainituilta'],
                                  allative            = 'mainitulle',
                                  allatives_plural    = ['mainituille'],
                                  essives             = ['mainittuna'],
                                  essives_plural      = ['mainittuina'],
                                  translative         = 'mainituksi',
                                  translatives_plural = ['mainituiksi'],
                                  abessive            = 'mainitutta',
                                  abessives_plural    = ['mainituitta'],
                                  instructives_plural = ['mainituin'],
                                  comitatives_plural  = ['mainittuine'])

        ensure_inflections_equal(expected, data)
