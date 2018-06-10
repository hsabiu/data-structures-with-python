import unittest
from Stack import ArrayStack


class TestArrayStack(unittest.TestCase):
    # Unit test for the Stack class

    def setUp(self):
        self.stack = ArrayStack(3)
        self.assertIsNone(self.stack.push(1))
        self.assertIsNone(self.stack.push(2))

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.assertIsNone(self.stack.push(3))

    def test_push_on_full_stack(self):
        self.assertIsNone(self.stack.push(3))
        self.assertRaises(OverflowError, self.stack.push, 4)

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 2)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_on_empty_stack(self):
        self.stack.pop()
        self.stack.pop()
        self.assertRaises(OverflowError, self.stack.pop)

    def test_is_empty(self):
        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
