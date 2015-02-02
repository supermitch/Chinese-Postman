if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import eularian

import unittest

class Test(unittest.TestCase):
    def test_true(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

