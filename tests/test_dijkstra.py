import unittest

import dijkstra

class TestDijkstra(unittest.TestCase):

    def test_summarize_path(self):
        path = {1: None, 2:1, 3:None, 4:2}
        self.assertTrue([4, 2, 1], dijkstra.summarize_path(4, path))

    def test_find_cost(self):
        self.assertTrue(True)

