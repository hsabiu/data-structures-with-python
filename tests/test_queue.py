import unittest
from Queue import Queue


class TestQueue(unittest.TestCase):
    # Unit test cases for the implementation of queue

    def setUp(self):
        self.queue = Queue(5)

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def tearDown(self):
        self.queue = None

    def test_normal_enqueue(self):
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.rear(), 5)

    def test_failed_enqueue(self):
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertRaises(OverflowError, self.queue.enqueue, 6)

    def test_normal_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_failed_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertRaises(OverflowError, self.queue.dequeue)

    def test_front(self):
        self.assertEqual(self.queue.front(), 1)

    def test_rear(self):
        self.assertEqual(self.queue.rear(), 3)

    def test_is_empty(self):
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()

        self.assertTrue(self.queue.is_empty())