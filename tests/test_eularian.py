import unittest

import eularian
import network

class TestEularian(unittest.TestCase):

    def test_add_new_edges_simple_true(self):
        graph = network.Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        min_route = [[2, 3]]
        new_graph= eularian.add_new_edges(graph, min_route)
        expected = [(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)]
        self.assertEqual(expected, new_graph.all_edges)

    def test_make_eularian_simple_true(self):
        """ Test an obvious eularian circuit modification. """
        graph = network.Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        new_graph, cost = eularian.make_eularian(graph)
        expected = [(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)]
        self.assertEqual((new_graph.all_edges, cost), (expected, 1))

