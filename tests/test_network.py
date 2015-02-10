import unittest

import network

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = network.Graph([(1,2,4), (1,4,4), (2,4,1),
                                   (2,3,4), (3,4,4)])

    def test_node_keys(self):
        self.assertEqual([1, 2, 3, 4], self.graph.node_keys())

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

    def test_remove_edge_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        graph.remove_edge((1,4,4))
        expected = [(1,2,4), (2,4,1), (2,3,4), (3,4,4)]
        self.assertEqual(expected, graph.all_edges)

    def test_remove_edges_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        graph.remove_edges([(1,4,4), (2,3,4)])
        expected = [(1,2,4), (2,4,1), (3,4,4)]
        self.assertEqual(expected, graph.all_edges)

    def test_edge_options(self):
        expected = [(1,2,4), (1,4,4)]
        self.assertEqual(expected, self.graph.edge_options(1))

class TestNode(unittest.TestCase):

    def test_node_order_odd(self):
        node = network.Node(1, [(2,4), (4,4), (3,1)])
        self.assertEqual(3, node.order)

    def test_node_order_even(self):
        node = network.Node(1, [(2,4), (4,4)])
        self.assertEqual(2, node.order)

