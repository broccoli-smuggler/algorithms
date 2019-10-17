import unittest
import random
from union_find.union_find import UnionFind


class TestUF(unittest.TestCase):
    def test_init(self):
        UF = UnionFind(4)
        self.assertEqual([0, 1, 2, 3], UF.roots)

    def test_union_1(self):
        UF = UnionFind(4)
        UF.union(2, 3)
        self.assertEqual(UF.roots[2], UF.roots[3])
        UF.union(2, 1)
        self.assertEqual(UF.roots[1], UF.roots[3])

    def test_union_100(self):
        UF = UnionFind(40)
        UF.union(2, 3)
        UF.union(3, 4)
        UF.union(3, 30)
        self.assertEqual(UF.roots[4], UF.roots[3])
        UF.union(2, 10)
        self.assertEqual(UF.depths[10], UF.depths[30])

    def test_connected(self):
        UF = UnionFind(400)
        UF.union(0, 1)
        self.assertTrue(UF.connected(0, 1))
        UF.union(2, 3)
        UF.union(3, 4)
        UF.union(3, 300)
        self.assertTrue(UF.connected(300, 2))
        self.assertFalse(UF.connected(303, 2))

    def test_large(self):
        size = 40000000
        UF = UnionFind(size)

        for i in range(1, 600000):
            a = random.randint(0, size - 1)
            b = random.randint(0, size - 1)

            UF.union(a, b)
            self.assertTrue(UF.connected(a, b))


if __name__ == '__main__':
    unittest.main()
