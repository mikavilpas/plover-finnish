import unittest
from ensure import ensure
from .gradation import *

class TestRootWordService(unittest.TestCase):
    def test_gradate_kotus_i_ilta_illan_sivellin_siveltimen(self):
        gradate = gradate_kotus_i_ilta_illan_sivellin_siveltimen

        ensure(gradate("ilta")).equals("illa")
        ensure(gradate("sivellin")).equals("siveltin")
