from interfaces.iStack import IStack


class Node(object):
    def __init__(self, value, next_node):
        self.next = next_node
        self.value = value


class LinkedStack(IStack):
    def __init__(self):
        self.stack_size = 0
        self.node = None

    def push(self, value):
        old_node = self.node
        self.node = Node(value, old_node)
        self.stack_size += 1
        return True

    def pop(self):
        value = self.node.value
        new_node = self.node.next
        self.node = new_node
        return value

    def size(self):
        return self.stack_size

    def is_empty(self):
        return self.node is None

