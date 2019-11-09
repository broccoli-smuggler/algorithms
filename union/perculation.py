from union.union_find import UnionFind


class Percolation(object):
    def __init__(self, grid_size):
        self._grid_size = grid_size
        self._open_grid = [[False] * grid_size for i in range(grid_size)]
        self._number_open = 0
        self._union_size = grid_size * grid_size + 2

        # Make a unionfind object which can hold the full grid
        self._union_find = UnionFind(self._union_size)

        # connect the first row (1-grid_size) to the 0th element
        for c in range(1, grid_size + 1):
            self._union_find.union(0, c)

        # connect the last element with the end row
        for c in range(self._union_size - grid_size - 1, self._union_size - 1):
            self._union_find.union(c, self._union_size - 1)

    def _union_index(self, r, c):
        return self._grid_size * (r - 1) + (c - 1) + 1

    def number_open_sites(self):
        return self._number_open

    def open(self, r, c):
        if r < 1 or c < 1 or r > self._grid_size or c > self._grid_size:
            return

        if self.isFull(r, c):
            self._open_grid[r - 1][c - 1] = True
            self._number_open += 1

            if r == self._grid_size:
                self._union_find.union(self._union_size - 1, self._union_index(r, c))
            if r == 1:
                self._union_find.union(self._union_index(r, c), 0)
            if self.isOpen(r - 1, c):
                self._union_find.union(self._union_index(r, c), self._union_index(r - 1, c))
            if self.isOpen(r + 1, c):
                self._union_find.union(self._union_index(r, c), self._union_index(r + 1, c))
            if self.isOpen(r, c - 1):
                self._union_find.union(self._union_index(r, c), self._union_index(r, c - 1))
            if self.isOpen(r, c + 1):
                self._union_find.union(self._union_index(r, c), self._union_index(r, c + 1))

    def isFull(self, r, c):
        return not self.isOpen(r, c)

    def isOpen(self, r, c):
        if r > self._grid_size or c > self._grid_size or r < 1 or c < 1:
            return False
        return self._open_grid[r - 1][c - 1]

    def perculates(self):
        return self._union_find.connected(0, self._union_size - 1)

