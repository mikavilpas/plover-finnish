import unittest
from ensure import ensure
from .double_consonant_frequencies import not_a_triple_consonant_cluster

class TestDoubleConsonantFrequencies(unittest.TestCase):
    def test_not_a_triple_consonant_cluster(self):
       ensure(not_a_triple_consonant_cluster(word = "a", chars = "b")).is_(False)
       ensure(not_a_triple_consonant_cluster("a", "bb")).is_(True)
       ensure(not_a_triple_consonant_cluster("abstraktio", "bb")).is_(True)

       # in the middle of a cluster
       ensure(not_a_triple_consonant_cluster("abstraktio", "st")).is_(False)

       # at the start
       ensure(not_a_triple_consonant_cluster("abstraktio", "bs")).is_(False)

       # at the end
       ensure(not_a_triple_consonant_cluster("abstraktio", "tr")).is_(False)
