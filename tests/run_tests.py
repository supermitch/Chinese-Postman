if __name__ == '__main__' and __package__ is None:
    """ Add root path to sys.path for module discovery. """
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

if __name__ == '__main__':
    import unittest
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = unittest.runner.TextTestRunner(verbosity=1)
    testRunner.run(tests)

