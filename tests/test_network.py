import unittest

import network

class TestGraph(unittest.TestCase):

    def test_all_nodes(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        expected = [1, 2, 3, 4]
        self.assertEqual(expected, graph.all_nodes())

    def test_node_options_correct(self):
        graph = network.Graph([(1,2,4), (1,4,4), (2,4,1), (2,3,4), (3,4,4)])
        self.assertEqual([2, 4], graph.node_options(1))

