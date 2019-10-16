import unittest
from test import test_stack_base
from StacksOfQueues.linked_stack import LinkedStack


class TestLinkedStack(test_stack_base.TestStackBase):
    def setUp(self):
        self.stack = LinkedStack()


if __name__ == '__main__':
    unittest.main()
