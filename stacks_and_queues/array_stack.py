from interfaces.iStack import IStack


class ArrayStack(IStack):
    def __init__(self):
        self._values_array = [None] * 2
        self._index = 0

    def _stack_size(self):
        return len(self._values_array)

    def _new_values_array(self, new_size):
        new_size = int(new_size)
        if new_size > len(self._values_array):
            new_array = [None] * new_size
            new_array[0:len(self._values_array)] = self._values_array.copy()
        else:
            new_array = self._values_array[0:new_size]
        self._values_array = new_array

    def push(self, value):
        if len(self._values_array) > self._index:
            self._values_array[self._index] = value
            self._index += 1
            return True
        else:
            # Expand array
            self._new_values_array(self._stack_size() * 2)
            return self.push(value)

    def pop(self):
        if self._index == 0:
            return None
        self._index -= 1
        popped = self._values_array[self._index]
        self._values_array[self._index] = None
        # Shrink array
        if self._index < self._stack_size() / 4:
            self._new_values_array(self._stack_size() / 2)
        return popped

    def size(self):
        return self._index

    def is_empty(self):
        return self._index == 0
