import unittest
from stacks_and_queues.linked_stack import LinkedStack
from stacks_and_queues.max_stack import MaxStack
from stacks_and_queues.array_stack import ArrayStack


class TestStackBase(unittest.TestCase):
    stack = None

    def test_init(self):
        if self.stack:
            self.assertTrue(self.stack.is_empty(), msg=self.stack.__class__)
            self.assertEqual(self.stack.size(), 0, msg=self.stack.__class__)
            self.assertEqual(self.stack.pop(), None)

    def test_push(self):
        if self.stack:
            s = "Today"
            b = "power"
            self.stack.push(s)
            self.assertFalse(self.stack.is_empty())
            self.assertEqual(self.stack.size(), 1)
            self.stack.push(b)
            self.assertFalse(self.stack.is_empty(), msg=self.stack.__class__)
            self.assertEqual(self.stack.size(), 2, msg=self.stack.__class__)

    def test_push_pop(self):
        if self.stack:
            s = "Today"
            b = "power"
            self.stack.push(s)
            self.stack.push(b)
            self.assertTrue(self.stack.pop() == "power", msg=self.stack.__class__)
            self.assertTrue(self.stack.pop() == "Today", msg=self.stack.__class__)

    def test_push_pop_many(self):
        if self.stack:
            amount = 90000
            for i in range(0, amount):
                self.stack.push(i)

            for i in range(1, amount+1):
                a = self.stack.pop()
                self.assertTrue(a == amount - i, msg=str(self.stack.__class__) + str(amount - i) + str(a))


class TestLinkedStack(TestStackBase):
    def setUp(self):
        self.stack = LinkedStack()


class TestArrayStack(TestStackBase):
    def setUp(self):
        self.stack = ArrayStack()


class TestMaxStack(TestStackBase):
    def setUp(self):
        self.stack = MaxStack()

    def test_get_max(self):
        self.assertTrue(self.stack.is_empty)
        self.stack.push(-1)
        self.assertEqual(self.stack.get_max(), -1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.push(0)
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.get_max(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_max(), -1)


if __name__ == '__main__':
    unittest.main()
