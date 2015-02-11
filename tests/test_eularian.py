import unittest

import eularian
import network

class TestEularian(unittest.TestCase):

    def test_add_new_edges_simple_true(self):
        graph = network.Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        min_route = [[2, 3]]
        expected = [(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)]
        self.assertEqual(eularian.add_new_edges(graph, min_route), expected)

    def test_make_eularian_simple_true(self):
        """ Test an obvious eularian circuit modification. """
        graph = network.Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        new, cost = eularian.make_eularian(graph)
        expected = network.Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)])
        self.assertEqual((new, cost), (expected, 1))

