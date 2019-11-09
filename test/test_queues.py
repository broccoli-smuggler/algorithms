import unittest
from stacks_and_queues.array_queue import ArrayQueue
from stacks_and_queues.linked_queue import LinkedQueue


class TestQueueBase(unittest.TestCase):
    queue = None

    def test_init(self):
        if self.queue:
            self.assertTrue(self.queue.is_empty(), msg=self.queue.__class__)
            self.assertEqual(self.queue.size(), 0, msg=self.queue.__class__)
            self.assertEqual(self.queue.dequeue(), None)

    def test_iter(self):
        if self.queue:
            a = 1
            b = 2
            c = 3
            self.queue.enqueue(a)
            self.queue.enqueue(b)
            self.queue.enqueue(c)
            result = []

            for item in self.queue:
                result.append(item)
            self.assertEqual([a, b, c], result)

    def test_enqueue_dequeue(self):
        if self.queue:
            a = "Hello"
            b = 45
            c = "poos"
            self.queue.enqueue(a)
            self.assertFalse(self.queue.is_empty())
            self.queue.enqueue(b)
            self.assertEqual(self.queue.dequeue(), a)
            self.queue.enqueue(c)
            self.assertEqual(self.queue.size(), 2)
            self.assertEqual(self.queue.dequeue(), b)
            self.queue.enqueue(a)
            self.assertEqual(self.queue.dequeue(), c)
            self.assertEqual(self.queue.dequeue(), a)
            self.assertEqual(self.queue.dequeue(), None)


class TestLinkedQueue(TestQueueBase):
    def setUp(self):
        self.queue = LinkedQueue()


class TestArrayQueue(TestQueueBase):
    def setUp(self):
        self.queue = ArrayQueue()


if __name__ == '__main__':
    unittest.main()
