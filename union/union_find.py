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
        i = self.get_root(a)
        j = self.get_root(b)
        if self.depths[i] > self.depths[j]:
            a_root = self.roots[i]
            self.roots[j] = a_root
            self.depths[j] += self.depths[i]
        else:
            b_root = self.roots[j]
            self.roots[i] = b_root
            self.depths[i] += self.depths[j]

    def get_root(self, id):
        current_root = self.roots[id]
        while current_root != self.roots[current_root]:
            self.roots[current_root] = self.roots[self.roots[current_root]]
            current_root = self.roots[current_root]
        return current_root

    # O(2logN)
    def connected(self, a, b):
        return self.get_root(a) == self.get_root(b)
