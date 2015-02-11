import unittest

import graph as gr

class TestGraph(unittest.TestCase):

    def test_edge_cost_not_found(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        self.assertIsNone(gr.edge_cost('AD', graph))

    def test_remove_edges_easy(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['AB', 'AC'])
        expected = [('AD', 4), ('AE', 5)]
        self.assertEqual(expected, result)

    def test_remove_edges_reversed(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['AB', 'CA'])
        expected = [('AD', 4), ('AE', 5)]
        self.assertEqual(expected, result)

    def test_remove_edges_none(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['XY'])
        expected = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        self.assertEqual(expected, result)

    def test_remove_edges_duplicates_true(self):
        graph = [('AB', 2), ('BC', 3), ('BC', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['BC'])
        expected = [('AB', 2), ('BC', 4), ('AE', 5)]
        self.assertEqual(expected, result)

    def test_remove_edges_duplicates_false(self):
        graph = [('AB', 2), ('BC', 3), ('BC', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['BC'])
        expected = [('AB', 2), ('BC', 3), ('AE', 5)]
        self.assertNotEqual(expected, result)

    def test_remove_edges_duplicates_false_all(self):
        graph = [('AB', 2), ('BC', 3), ('BC', 4), ('AE', 5)]
        result = gr.remove_edges(graph, ['BC'])
        expected = [('AB', 2), ('AE', 5)]
        self.assertNotEqual(expected, result)

    def test_edge_options(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.edge_options('C', graph)
        expected = ['AC', 'BC']
        self.assertEqual(expected, result)

    def test_all_nodes(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.all_nodes(graph)
        expected = set(['A', 'B', 'C', 'E'])
        self.assertEqual(expected, result)

    def test_odd_nodes(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.odd_nodes(graph)
        expected = ['A', 'E']
        self.assertEqual(expected, result)

    def test_node_options_correct(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.node_options('C', graph)
        self.assertEqual(['A', 'B'], result)

    def test_end_node_correct(self):
        self.assertEqual('E', gr.end_node('A', 'AE'))

    def test_end_node_incorrect(self):
        self.assertNotEqual('A', gr.end_node('A', 'AE'))

    def test_orders(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.orders(graph)
        expected = {'A': 3, 'B': 2, 'C': 2, 'E': 1}
        self.assertEqual(expected, result)

    def test_is_bridge_true(self):
        #  Two triangles joined by 'CD'
        graph = [('AB', 1), ('AC', 1), ('BC', 1), ('CD', 1), ('DE', 1),
                 ('DF', 1), ('EF', 1)]
        self.assertTrue(gr.is_bridge('CD', graph))

    def test_is_bridge_false(self):
        #  Two triangles joined by 'CD'
        graph = [('AB', 1), ('AC', 1), ('BC', 1), ('CD', 1), ('DE', 1),
                 ('DF', 1), ('EF', 1)]
        self.assertFalse(gr.is_bridge('BC', graph))

