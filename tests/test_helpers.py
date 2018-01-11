import unittest

from chinesepostman import my_iter, my_math


class TestMyMath(unittest.TestCase):

    def test_is_even_true_correct(self):
        self.assertTrue(my_math.is_even(2))

    def test_is_even_false_correct(self):
        self.assertFalse(my_math.is_even(1))


class TestMyIter(unittest.TestCase):

    def test_flatten_tuples(self):
        data = [(1,2), (3,4), (5,6)]
        result = (1, 2, 3, 4, 5, 6)
        self.assertEqual(result, my_iter.flatten_tuples(data))

    def test_all_unique_true(self):
        data = [1, 2, 3, 4, 5, 6]
        self.assertTrue(my_iter.all_unique(data))

    def test_all_unique_false(self):
        data = [1, 2, 3, 3, 5, 6]
        self.assertFalse(my_iter.all_unique(data))
