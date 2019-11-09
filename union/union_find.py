class UnionFind(object):
    def __init__(self, size):
        self._roots = list(range(0, size))
        self._depths = [1] * size

    def __str__(self):
        return str(self._roots) + str(self._depths)

    # O(1)
    def union(self, a, b):
        if a >= len(self._roots) or b >= len(self._roots):
            return
        i = self.get_root(a)
        j = self.get_root(b)
        if self._depths[i] > self._depths[j]:
            a_root = self._roots[i]
            self._roots[j] = a_root
            self._depths[j] += self._depths[i]
        else:
            b_root = self._roots[j]
            self._roots[i] = b_root
            self._depths[i] += self._depths[j]

    def get_root(self, id):
        current_root = self._roots[id]
        while current_root != self._roots[current_root]:
            self._roots[current_root] = self._roots[self._roots[current_root]]
            current_root = self._roots[current_root]
        return current_root

    # O(2logN)
    def connected(self, a, b):
        return self.get_root(a) == self.get_root(b)
