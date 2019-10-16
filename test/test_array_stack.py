import unittest
from test import test_stack_base
from StacksOfQueues.array_stack import ArrayStack


class TestArrayStack(test_stack_base.TestStackBase):
    def setUp(self):
        self.stack = ArrayStack()


if __name__ == '__main__':
    unittest.main()

