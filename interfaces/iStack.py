class IStack(object):
    def push(self, value):
        return NotImplementedError

    def pop(self):
        return NotImplementedError

    def size(self):
        return NotImplementedError

    def is_empty(self):
        return NotImplementedError

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration
        return self.pop()
