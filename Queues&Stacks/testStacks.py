import unittest
import linkedStack
import arrayStack


class TestStacks(unittest.TestCase):
    def setUp(self):
        self.stacks = []
        self.stacks.append(arrayStack.ArrayStack())
        self.stacks.append(linkedStack.LinkedStack())

    def test_init(self):
        for stack in self.stacks:
            self.assertTrue(stack.isEmpty(), msg=stack.__class__)
            self.assertEqual(stack.size(), 0, msg=stack.__class__)

    def test_push(self):
        for stack in self.stacks:
            s = "Today"
            b = "power"
            stack.push(s)
            self.assertFalse(stack.isEmpty())
            self.assertEqual(stack.size(), 1)
            stack.push(b)
            self.assertFalse(stack.isEmpty(), msg=stack.__class__)
            self.assertEqual(stack.size(), 2, msg=stack.__class__)

    def test_push_pop(self):
        for stack in self.stacks:
            s = "Today"
            b = "power"
            stack.push(s)
            stack.push(b)
            self.assertTrue(stack.pop() == "power", msg=stack.__class__)
            self.assertTrue(stack.pop() == "Today", msg=stack.__class__)

    def test_push_pop_many(self):
        amount = 900000
        for stack in self.stacks:
            for i in range(0, amount):
                stack.push(i)

            for i in range(1, amount+1):
                a = stack.pop()
                self.assertTrue(a == amount - i, msg=str(stack.__class__) + str(amount - i) + str(a))


if __name__ == '__main__':
    unittest.main()
