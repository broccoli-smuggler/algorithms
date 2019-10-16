import unittest
from test import test_stack_base
from StacksOfQueues import max_stack


class TestMaxStack(test_stack_base.TestStackBase):
    def setUp(self):
        self.stack = max_stack.MaxStack()

    def test_get_max(self):
        self.assertTrue(self.stack.is_empty)
        self.stack.push(1)
        self.assertEqual(self.stack.get_max(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.push(0)
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_max(), 1)


if __name__ == '__main__':
    unittest.main()
