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

