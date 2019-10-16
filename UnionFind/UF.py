import unittest
import random


class UnionFind(object):
    def __init__(self, size):
        self.roots = list(range(0, size))
        self.depths = [1] * size

    def __str__(self):
        return str(self.roots) + str(self.depths)

    # O(1)
    def union(self, a, b):
        if a >= len(self.roots) or b >= len(self.roots):
            return
        if self.depths[a] > self.depths[b]:
            a_root = self.roots[a]
            self.roots[b] = a_root
            self.depths[b] += self.depths[a]
        else:
            b_root = self.roots[b]
            self.roots[a] = b_root
            self.depths[a] += self.depths[b]

    def get_root(self, id):
        current_root = self.roots[id]
        while current_root != self.roots[current_root]:
            current_root = self.roots[current_root]
            self.roots[current_root] = current_root
        return current_root

    # O(2logN)
    def connected(self, a, b):
        return self.get_root(self.roots[a]) == self.get_root(self.roots[b])


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

