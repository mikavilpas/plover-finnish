import unittest
from ensure import ensure
from . import gradation as g

class TestGradation(unittest.TestCase):
    def test_gradate_joukahainen_av1(self):
        gradate = g.gradate_joukahainen

        # try each gradation
        ensure(gradate("lobata", "salata", "av2")).equals("lobbata")
        ensure(gradate("taata", "salata", "av6")).equals("takata")
    #     ensure(gradate("alppi")).equals("alpi")
    #     ensure(gradate("aavikko")).equals("aaviko")
    #     ensure(gradate("ampua")).equals("ammua")
    #     ensure(gradate("apu")).equals("avu")
    #     ensure(gradate("antaa")).equals("annaa")
    #     ensure(gradate("aalto")).equals("aallo")
    #     ensure(gradate("juurtaa")).equals("juurraa")
    #     ensure(gradate("ahtaa")).equals("ahdaa")
    #     ensure(gradate("hanki")).equals("hangi")
    #     ensure(gradate("suku")).equals("suvu")
    #     ensure(gradate("kyky")).equals("kyvy")

    # def test_gradate_joukahainen_av2(self):
    #     gradate = g.gradate_joukahainen_av2

    #     # ('b',  'bb'), # kind of like kotus B. (lobata -> lobbaan)
    #     ensure(gradate("lobata")).equals("lobbata")
    #     # ('g',  'gg'), # kind of like kotus B. (digata -> diggaan)
    #     ensure(gradate("digata")).equals("diggaan")
    #     # ('t',  'tt'), # kotus C
    #     ensure(gradate("aate")).equals("aatte")
    #     # ('p',  'pp'), # kotus B
    #     ensure(gradate("lape")).equals("lappe")
    #     # ('k',  'kk'), # kotus A
    #     ensure(gradate("aluke")).equals("alukke")
    #     # ('mm', 'mp'), # kotus H
    #     # ('v',  'p'),  # kotus E
    #     # ('nn', 'nt'), # kotus J
    #     # ('ll', 'lt'), # kotus I
    #     # ('rr', 'rt'), # kotus K
    #     # ('d',  't'),  # kotus F
    #     # ('ng', 'nk'), # kotus G
    #     pass
