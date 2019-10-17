from stacks_and_queues.linked_stack import LinkedStack
from interfaces.iStack import IStack


class MaxStack(IStack):
    def __init__(self):
        self.stack = LinkedStack()
        self.max_stack = LinkedStack()
        self.last_max = None

    def push(self, value):
        if self.stack.is_empty():
            self.stack.push(value)
            self.max_stack.push(value)
            self.last_max = value
        else:
            self.stack.push(value)
            if value > self.last_max:
                self.last_max = value
            self.max_stack.push(self.last_max)

    def pop(self):
        self.last_max = self.max_stack.pop()
        return self.stack.pop()

    def size(self):
        return self.stack.size()

    def get_max(self):
        return self.last_max

    def is_empty(self):
        return self.stack.is_empty()
