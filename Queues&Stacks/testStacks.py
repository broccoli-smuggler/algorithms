import unittest
import linkedStack


class TestStacks(unittest.TestCase):
    stack = None

    def test_init(self):
        if self.stack:
            self.assertTrue(self.stack.isEmpty())
            self.assertEqual(self.stack.size(), 0)

    def test_push(self):
        if self.stack:
            s = "Today"
            b = "power"
            self.stack.push(s)
            self.assertFalse(self.stack.isEmpty())
            self.assertEqual(self.stack.size(), 1)
            self.stack.push(b)
            self.assertFalse(self.stack.isEmpty())
            self.assertEqual(self.stack.size(), 2)

    def test_push_pop(self):
        if self.stack:
            s = "Today"
            b = "power"
            self.stack.push(s)
            self.stack.push(b)
            self.assertTrue(self.stack.pop() == "power")
            self.assertTrue(self.stack.pop() == "Today")


class TestlinkedStack(TestStacks):
    def setUp(self):
        self.stack = linkedStack.LinkedStack()

    def test_init(self):
        super().test_init()

    def test_push(self):
        super().test_push()

    def test_push_pop(self):
        super().test_push_pop()


if __name__ == '__main__':
    unittest.main()
