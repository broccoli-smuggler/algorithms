from interfaces.iStack import IStack


class ArrayStack(IStack):
    def __init__(self):
        self.stack_size = 2
        self.values_array = [None] * self.stack_size
        self.index = 0

    def new_values_array(self, new_size):
        new_size = int(new_size)
        if new_size > len(self.values_array):
            new_array = [None] * new_size
            new_array[0:len(self.values_array)] = self.values_array.copy()
        else:
            new_array = self.values_array[0:new_size]
        self.values_array = new_array

    def push(self, value):
        if len(self.values_array) > self.index:
            self.values_array[self.index] = value
            self.index += 1
            return True
        else:
            # Expand array
            self.new_values_array(len(self.values_array)*2)
            return self.push(value)

    def pop(self):
        if self.index == 0:
            return None
        self.index -= 1
        popped = self.values_array[self.index]
        self.values_array[self.index] = None
        # Shrink array
        if self.index < len(self.values_array)/4:
            self.new_values_array(len(self.values_array)/2)
        return popped

    def size(self):
        return self.index

    def is_empty(self):
        return self.index == 0
