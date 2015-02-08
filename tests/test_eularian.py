import unittest

import eularian

class TestEularian(unittest.TestCase):

    def test_add_new_edges_simple_true(self):
        graph = [('AB', 4), ('AC', 4), ('BC', 1), ('BD', 4), ('CD', 4)]
        min_route = [['B', 'C']]
        expected = [('AB', 4), ('AC', 4), ('BC', 1), ('BD', 4), ('CD', 4), ('BC', 1)]
        self.assertEqual(eularian.add_new_edges(graph, min_route), expected)

    def test_make_eularian_simple_true(self):
        """ Test an obvious eularian circuit modification. """
        graph = [('AB', 4), ('AC', 4), ('BC', 1), ('BD', 4), ('CD', 4)]
        new, cost = eularian.make_eularian(graph)
        expected = [('AB', 4), ('AC', 4), ('BC', 1), ('BD', 4), ('CD', 4), ('BC', 1)]
        self.assertEqual((new, cost), (expected, 1))

