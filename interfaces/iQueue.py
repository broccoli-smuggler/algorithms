class IQueue(object):
    def enqueue(self, a):
        return NotImplementedError

    def dequeue(self):
        return NotImplementedError

    def is_empty(self):
        return NotImplementedError

    def size(self):
        return NotImplementedError