import iStack


class ArrayStack(iStack.IStack):
    def __init__(self):
        self.stack_size = 10
        self.values_array = [None] * self.stack_size
        self.index = 0

    def push(self, value):
        if len(self.values_array) > self.index:
            self.values_array[self.index] = value
            self.index += 1
            return True
        else:
            return False

    def pop(self):
        if self.index == 0:
            return None
        self.index -= 1
        popped = self.values_array[self.index]
        self.values_array[self.index] = None
        return popped

    def size(self):
        return self.index

    def isEmpty(self):
        return self.index == 0

