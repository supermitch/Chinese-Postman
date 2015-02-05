import unittest

import graph as gr

class TestEularian(unittest.TestCase):

    def test_total_cost(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        self.assertEqual(14, gr.total_cost(graph))

    def test_all_edges(self):
        graph = [('AB', 2), ('AC', 3), ('AD', 4), ('AE', 5)]
        result = gr.all_edges(graph)
        expected = ['AB', 'AC', 'AD', 'AE']
        self.assertEqual(expected, result)

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
        self.assertEqual('E', gr.end_node('A', 'AE'))

    def test_end_node_incorrect(self):
        self.assertNotEqual('A', gr.end_node('A', 'AE'))

    def test_orders(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        result = gr.orders(graph)
        expected = {'A': 3, 'B': 2, 'C': 2, 'E': 1}
        self.assertEqual(expected, result)

    def test_edge_cost_correct(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        self.assertEqual(3, gr.edge_cost('AC', graph))

    def test_edge_cost_reversed(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        self.assertEqual(3, gr.edge_cost('CA', graph))

    def test_edge_cost_not_found(self):
        graph = [('AB', 2), ('AC', 3), ('BC', 4), ('AE', 5)]
        self.assertIsNone(gr.edge_cost('AD', graph))

    def test_is_eularian_true(self):
        # A simple Eularian diamond
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1)]
        self.assertTrue(gr.is_eularian(graph))

    def test_is_eularian_false_semi_eularian(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1), ('BD', 2)]
        self.assertFalse(gr.is_eularian(graph))

    def test_is_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1), ('BD', 2),
                 ('AC', 2)]
        self.assertFalse(gr.is_eularian(graph))

    def test_is_semi_eularian_false_eularian(self):
        # A simple Eularian diamond
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1)]
        self.assertFalse(gr.is_semi_eularian(graph))

    def test_is_semi_eularian_true(self):
        # Diamond w/ one crossing edge: semi-Eularian
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1), ('BD', 2)]
        self.assertTrue(gr.is_semi_eularian(graph))

    def test_is_semi_eularian_false_non_eularian(self):
        # Diamond w/ two crossing edges: non-Eularian
        graph = [('AB', 1), ('BC', 1), ('CD', 1), ('DA', 1), ('BD', 2),
                 ('AC', 2)]
        self.assertFalse(gr.is_semi_eularian(graph))

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

