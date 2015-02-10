import unittest

import network

class TestGraph(unittest.TestCase):

    def test_all_nodes(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, graph.all_nodes())

    def test_node_options_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        self.assertEqual([(2, 4), (4, 4)], graph.node_options(1))

    def test_all_edges_correct(self):
        edges = [(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)]
        graph = network.Graph(edges)
        self.assertEqual(edges, graph.all_edges)

    def test_edge_cost_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        self.assertEqual(4, graph.edge_cost(1, 4))

    def test_edge_cost_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        self.assertNotEqual(1, graph.edge_cost(1, 2))

