import unittest

from chinesepostman.network import Graph, Edge

class TestGraph(unittest.TestCase):

    def setUp(self):
        """ Set up a default graph. """
        # Two very wide, flat triangles, Semi-Eularian
        self.edges = [(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)]
        self.graph = Graph(self.edges)

    def test_node_keys(self):
        self.assertEqual([1, 2, 3, 4], self.graph.node_keys)

    def test_odd_nodes(self):
        self.assertEqual([2, 4], self.graph.odd_nodes)

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
        graph = Graph([(1,2,1)])  # One edge, two nodes
        graph.add_edge(2, 3, 2)  # Add an edge from 2 to 3 w/ cost 2
        self.assertEqual([(1,2,1), (2,3,2)], graph.all_edges)

    def test_add_edge_correct_duplicate(self):
        graph = Graph([(1,2,1)])  # One edge, two nodes
        graph.add_edge(1, 2, 1)  # Add a parallel edge
        self.assertEqual([Edge(1,2,1), Edge(1,2,1)], graph.all_edges)

    def test_remove_edge_correct(self):
        graph = Graph(self.edges)
        graph.remove_edge(1,4,4)
        expected = [Edge(*args) for args in [(1,2,4), (2,4,1), (2,3,4), (3,4,4)]]
        self.assertEqual(expected, graph.all_edges)

    def test_remove_edges_correct(self):
        graph = Graph(self.edges)
        graph.remove_edges([Edge(1,4,4), Edge(2,3,4)])
        expected = [Edge(*args) for args in [(1,2,4), (2,4,1), (3,4,4)]]
        self.assertEqual(expected, graph.all_edges)

    def test_remove_edge_duplicate_correct(self):
        graph = Graph([(1,2,1), (1,2,1), (1,2,2), (2,3,1), (3,1,1)])
        graph.remove_edge(1,2,1)
        expected = [Edge(*args) for args in [(1,2,1), (1,2,2), (2,3,1), (3,1,1)]]
        self.assertEqual(expected, graph.all_edges)

    def test_edge_options(self):
        expected = {0: Edge(1,2,4), 1: Edge(1,4,4)}
        self.assertEqual(expected, self.graph.edge_options(1))

    def test_is_eularian_true(self):
        # A simple Eularian diamond
        graph = Graph([(1,2,1), (2,3, 1), (3,4,1), (4,1,1)])
        self.assertTrue(graph.is_eularian)

    def test_is_eularian_false_semi_eularian(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2)])
        self.assertFalse(graph.is_eularian)

    def test_is_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2), (1,3,2)])
        self.assertFalse(graph.is_eularian)

    def test_is_semi_eularian_false_eularian(self):
        # A simple Eularian diamond
        graph = Graph([(1,2,1), (2,3, 1), (3,4,1), (4,1,1)])
        self.assertFalse(graph.is_semi_eularian)

    def test_is_semi_eularian_true(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2)])
        self.assertTrue(graph.is_semi_eularian)

    def test_is_semi_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = Graph([(1,2,1), (2,3,1), (3,4,1), (4,1,1), (2,4,2), (1,3,2)])
        self.assertFalse(graph.is_semi_eularian)

    def test_is_bridge_true(self):
        #  Two triangles 1-2-3 and 4-5-6 joined by '3-4' bridge
        graph = Graph([(1,2,1), (1,3,1), (2,3,1), (3,4,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertTrue(graph.is_bridge(3))  # Edge 3 aka '3-4 'is a bridge

    def test_is_bridge_false(self):
        #  Two triangles 1-2-3 and 4-5-6 joined by '3-4' bridge
        graph = Graph([(1,2,1), (1,3,1), (2,3,1), (3,4,1), (4,5,1), (4,6,1), (5,6,1)])
        self.assertFalse(graph.is_bridge(2))  # Edge 2 aka '2-3' is not a bridge


class TestEdge(unittest.TestCase):

    def setUp(self):
        self.edge = Edge(1, 2, 3, True)

    def test_edge_instance_equal(self):
        self.assertEqual((1, 2, 3, True), self.edge)

    def test_edge_instance_unequal(self):
        self.assertNotEqual((1, 2, 3, False), self.edge)

    def test_edge_instance_short(self):
        edge = Edge(1, 2)
        self.assertEqual((1, 2, 0, False), edge)
