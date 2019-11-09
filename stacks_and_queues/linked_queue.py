from interfaces.iQueue import IQueue
from stacks_and_queues.node import Node


class LinkedQueue(IQueue):
    def __init__(self):
        self._first_node = None
        self._end_node = None
        self._length = 0

    def enqueue(self, a):
        if not self._end_node:
            self._end_node = Node(a, None)
            self._first_node = self._end_node
        else:
            old_last = self._end_node
            self._end_node = Node(a, None)
            old_last.next = self._end_node
        self._length += 1

    def dequeue(self):
        first_value = None
        if self._first_node:
            first_value = self._first_node.value
            self._first_node = self._first_node.next
            self._length -= 1
        return first_value

    def is_empty(self):
        return not self._first_node

    def size(self):
        return self._length

