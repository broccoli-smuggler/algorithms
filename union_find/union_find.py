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
