import random
import unittest
from union.perculation import Percolation


class TestPerculation(unittest.TestCase):
    def setUp(self):
        self.perculator = Percolation(3)

    def test_init(self):
        self.assertTrue(self.perculator.isFull(1, 1))
        self.assertFalse(self.perculator.isOpen(0, 0))
        self.assertEqual(0, self.perculator.number_open_sites())

    def test_indexer(self):
        self.assertEqual(1, self.perculator._union_index(1, 1))
        self.assertEqual(4, self.perculator._union_index(2, 1))
        self.assertEqual(3, self.perculator._union_index(1, 3))
        self.assertEqual(9, self.perculator._union_index(3, 3))

    def test_open(self):
        for i in range(1, 4):
            self.perculator.open(i, i)
            self.assertTrue(self.perculator.isOpen(i, i))

    def test_basic_perculate(self):
        self.perculator = Percolation(4)
        self.perculator.open(1, 1)
        self.assertEqual(self.perculator.number_open_sites(), 1)
        self.assertFalse(self.perculator.perculates())
        self.perculator.open(2, 3)
        self.assertEqual(self.perculator.number_open_sites(), 2)
        self.assertFalse(self.perculator.perculates())
        self.perculator.open(1, 3)
        self.assertEqual(self.perculator.number_open_sites(), 3)
        self.assertFalse(self.perculator.perculates())
        self.perculator.open(4, 3)
        self.assertEqual(self.perculator.number_open_sites(), 4)
        self.assertFalse(self.perculator.perculates())
        self.perculator.open(3, 3)
        self.assertEqual(self.perculator.number_open_sites(), 5)
        self.assertTrue(self.perculator.perculates())

    def test_theory(self):
        size = 300
        running_average = 0
        number_tests = 20
        for i in range(1, number_tests + 1):
            self.perculator = Percolation(size)
            while not self.perculator.perculates():
                r = random.randint(1, size)
                c = random.randint(1, size)
                self.perculator.open(r, c)
            average = self.perculator.number_open_sites()/(size*size)
            print(self.perculator.number_open_sites())
            print(average)
            running_average += average
        final_average = running_average / number_tests
        print("Final average %f" % final_average)
        self.assertAlmostEqual(0.59, final_average, 2)


if __name__ == '__main__':
    unittest.main()
