from interfaces.iQueue import IQueue


class ArrayQueue(IQueue):
    def __init__(self):
        self._values_array = [None] * 2
        self._first_index = 0
        self._last_index = 0

    def _array_size(self):
        return len(self._values_array)

    def _new_values_array(self, new_size):
        new_size = int(new_size)
        if new_size > len(self._values_array):
            new_array = [None] * new_size
            new_array[0:len(self._values_array)] = self._values_array.copy()
        else:
            new_array = self._values_array[0:new_size]
        self._values_array = new_array

    def enqueue(self, item):
        self._values_array[self._last_index] = item
        self._last_index += 1

        # First see if we should be growing the array
        if self._last_index == self._array_size():
            self._values_array.extend([None] * self._array_size())

    def dequeue(self):
        if self.is_empty():
            return None
        item = self._values_array[self._first_index]
        self._values_array[self._first_index] = None
        self._first_index += 1

        # Check if we can chop the front off
        half = int(self._array_size() / 2)
        if self._first_index >= half:
            self._values_array = self._values_array[half:]
            self._first_index -= half
            self._last_index -= half
        return item

    def is_empty(self):
        return self._last_index == self._first_index

    def size(self):
        return self._last_index - self._first_index

