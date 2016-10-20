import unittest

import eularian
from chinesepostman.network import Graph

class TestEularian(unittest.TestCase):

    def test_add_new_edges_simple_true(self):
        graph = Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        min_route = [[2, 3]]
        new_graph= eularian.add_new_edges(graph, min_route)
        expected = [(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)]
        self.assertEqual(expected, new_graph.all_edges)

    def test_make_eularian_simple_true(self):
        """ Test an obvious eularian circuit modification. """
        graph = Graph([(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4)])
        new_graph, cost = eularian.make_eularian(graph)
        expected = [(1,2,4), (1,3,4), (2,3,1), (2,4,4), (3,4,4), (2,3,1)]
        self.assertEqual((new_graph.all_edges, cost), (expected, 1))

    def test_find_dead_ends_simple_correct(self):
        """ Find dead ends in a graph. """
        # A triangle with an antenna
        graph = Graph([(1,2,1), (1,4,2), (2,3,1), (2,4,1)])
        self.assertEqual([(2,3,1)], eularian.find_dead_ends(graph))

    def test_find_dead_ends_double_correct(self):
        """ Find dead ends in a graph. """
        # Two adjacent triandles with tails on peak and belt
        graph = Graph([(1,2,1), (1,4,1), (1,6,1), (2,3,1), (2,4,1),
                       (4,5,1), (4,6,1),])
        self.assertEqual([(2,3,1), (4,5,1)], eularian.find_dead_ends(graph))

