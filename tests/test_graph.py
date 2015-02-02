import unittest

import graph as gr

class TestEularian(unittest.TestCase):

    def test_total_cost(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.total_cost(graph)
        expected = 14
        self.assertEqual(expected, result)

    def test_all_edges(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.all_edges(graph)
        expected = ['AB', 'AC', 'AD', 'AE']
        self.assertEqual(expected, result)

    def test_possible_paths(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.possible_paths('C', graph)
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

    def test_end_node_correct(self):
        result = gr.end_node('A', 'AE')
        self.assertEqual('E', result)

    def test_end_node_incorrect(self):
        result = gr.end_node('A', 'AE')
        self.assertNotEqual('A', result)

    def test_orders(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.orders(graph)
        expected = {'A': 3, 'B': 2, 'C': 2, 'E': 1}
        self.assertEqual(expected, result)

    def test_edge_cost_correct(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.edge_cost('AC', graph)
        self.assertEqual(3, result)

    def test_edge_cost_reversed(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.edge_cost('CA', graph)
        self.assertEqual(3, result)

    def test_edge_cost_not_found(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.edge_cost('AD', graph)
        self.assertIsNone(result)

