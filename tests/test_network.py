import unittest

import network

class TestGraph(unittest.TestCase):

    def setUp(self):
        """ Set up a default graph. """
        self.edges = [(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)]
        self.graph = network.Graph(self.edges)

    def test_node_keys(self):
        self.assertEqual([1, 2, 3, 4], self.graph.node_keys)

    def test_node_options_correct(self):
        self.assertEqual([(2, 4), (4, 4)], self.graph.node_options(1))

    def test_all_edges_correct(self):
        self.assertEqual(self.edges, self.graph.all_edges)

    def test_edge_cost_correct(self):
        self.assertEqual(4, self.graph.edge_cost(1, 4))

    def test_edge_cost_correct(self):
        self.assertNotEqual(1, self.graph.edge_cost(1, 2))

    def test_edge_cost_reversed(self):
        self.assertEqual(4, self.graph.edge_cost(4, 1))

    def test_total_cost_correct(self):
        self.assertEqual(17, self.graph.total_cost)

    def test_add_edge_correct_easy(self):
        graph = network.Graph([(1,2,1)])  # One edge, two nodes
        graph.add_edge(2, 3, 2)  # Add an edge from 2 to 3 w/ cost 2
        self.assertEqual([(1,2,1), (2,3,2)], graph.all_edges)

    def test_add_edge_correct_duplicate(self):
        graph = network.Graph([(1,2,1)])  # One edge, two nodes
        graph.add_edge(1, 2, 1)  # Add a parallel edge
        self.assertEqual([(1,2,1), (1,2,1)], graph.all_edges)

    def test_remove_edge_correct(self):
        graph = network.Graph(self.edges)
        graph.remove_edge((1,4,4))
        expected = [(1,2,4), (2,4,1), (2,3,4), (3,4,4)]
        self.assertEqual(expected, graph.all_edges)

    def test_remove_edges_correct(self):
        graph = network.Graph(self.edges)
        graph.remove_edges([(1,4,4), (2,3,4)])
        expected = [(1,2,4), (2,4,1), (3,4,4)]
        self.assertEqual(expected, graph.all_edges)

    def test_edge_options(self):
        expected = [(1,2,4), (1,4,4)]
        self.assertEqual(expected, self.graph.edge_options(1))

    def test_is_eularian_true(self):
        # A simple Eularian diamond
        graph = network.Graph([(1,2,1), (2,3, 1), (3,4,1), (4,1,1)])
        self.assertTrue(graph.is_eularian)

    def test_is_eularian_false_semi_eularian(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = network.Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2)])
        self.assertFalse(graph.is_eularian)

    def test_is_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = network.Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2),
                 (1,3,2)])
        self.assertFalse(graph.is_eularian)

    def test_is_semi_eularian_false_eularian(self):
        # A simple Eularian diamond
        graph = network.Graph([(1,2,1), (2,3, 1), (3,4,1), (4,1,1)])
        self.assertFalse(graph.is_semi_eularian)

    def test_is_semi_eularian_true(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = network.Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2)])
        self.assertTrue(graph.is_semi_eularian)

    def test_is_semi_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = network.Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2),
                 (1,3,2)])
        self.assertFalse(graph.is_semi_eularian)


class TestNode(unittest.TestCase):

    def test_node_order_odd(self):
        node = network.Node(1, [(2,4), (4,4), (3,1)])
        self.assertEqual(3, node.order)

    def test_node_order_even(self):
        node = network.Node(1, [(2,4), (4,4)])
        self.assertEqual(2, node.order)

