import unittest
from implementations.Stack import ArrayStack, LinkedListStack


class TestArrayStack(unittest.TestCase):
    # Unit test cases for the implementation of ArrayStack (fixed sized stack)

    def setUp(self):
        self.stack = ArrayStack(3)
        self.stack.push(1)
        self.stack.push(2)

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

    def test_push_on_full_stack(self):
        self.stack.push(3)
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


class TestLinkedListStack(unittest.TestCase):
    # Unit test cases for the implementation of LinkedListStack (dynamic stack)

    def setUp(self):
        self.stack = LinkedListStack()
        self.stack.push(1)
        self.stack.push(2)

    def tearDown(self):
        self.stack = None

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

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

