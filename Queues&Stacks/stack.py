import unittest


class Node(object):
    def __init__(self, value, next_node):
        self.next = next_node
        self.value = value


class IStack(object):
    def push(self, value):
        return NotImplementedError

    def pop(self):
        return NotImplementedError

    def size(self):
        return NotImplementedError

    def isEmpty(self):
        return NotImplementedError


class LinkedStack(IStack):
    def __init__(self):
        self.stack_size = 0
        self.node = None

    def push(self, value):
        old_node = self.node
        self.node = Node(value, old_node)
        self.stack_size += 1

    def pop(self):
        value = self.node.value
        new_node = self.node.next
        self.node = new_node
        return value

    def size(self):
        return self.stack_size

    def isEmpty(self):
        return self.node is None


class TestlinkedStack(unittest.TestCase):
    def test_init(self):
        ls = LinkedStack()
        self.assertTrue(ls.isEmpty())
        self.assertEqual(ls.size(), 0)

    def test_push(self):
        ls = LinkedStack()
        s = "Today"
        b = "power"
        ls.push(s)
        self.assertFalse(ls.isEmpty())
        self.assertEqual(ls.size(), 1)
        ls.push(b)
        self.assertFalse(ls.isEmpty())
        self.assertEqual(ls.size(), 2)

    def test_push_pop(self):
        ls = LinkedStack()
        s = "Today"
        b = "power"
        ls.push(s)
        ls.push(b)
        self.assertTrue(ls.pop() == "power")
        self.assertTrue(ls.pop() == "Today")


if __name__ == '__main__':
    unittest.main()
