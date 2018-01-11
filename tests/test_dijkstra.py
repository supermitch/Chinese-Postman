import unittest

import chinesepostman.dijkstra as di
from chinesepostman import network


class TestDijkstra(unittest.TestCase):

    def test_summarize_path(self):
        path = {1: None, 2:1, 3:None, 4:2}
        self.assertEqual([1, 2, 4], di.summarize_path(4, path))

    def test_find_cost_easy(self):
        graph = network.Graph([(1,2,1), (2,3,1), (3,4,5), (4,1,5)])
        path = (1, 3)
        cost, route = di.find_cost(path, graph)
        expected = (2, [1, 2, 3])
        self.assertEqual(expected, (cost, route))
