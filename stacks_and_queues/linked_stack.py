from interfaces.iStack import IStack
from stacks_and_queues.node import Node


class LinkedStack(IStack):
    def __init__(self):
        self._stack_size = 0
        self._node = None

    def push(self, value):
        old_node = self._node
        self._node = Node(value, old_node)
        self._stack_size += 1
        return True

    def pop(self):
        if not self._node:
            return None
        value = self._node.value
        new_node = self._node.next
        self._node = new_node
        return value

    def size(self):
        return self._stack_size

    def is_empty(self):
        return self._node is None

