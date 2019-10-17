import unittest


if __name__ == '__main__':
    loader = unittest.defaultTestLoader
    suite = loader.discover('.')
    result = unittest.TestResult()
    runner = unittest.TextTestRunner(verbosity=2)
    print(runner.run(suite))
