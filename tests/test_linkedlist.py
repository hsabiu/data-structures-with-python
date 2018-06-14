import unittest
from implementations.LinkedList import SinglyLinkedList, DoublyLinkedList


class TestSinglyLinkList(unittest.TestCase):
    # Unit test cases for the implementation of singly linkedlist

    def setUp(self):
        self.link_list = SinglyLinkedList()
        self.link_list.insert(1)
        self.link_list.insert(2)
        self.link_list.insert(3)

    def tearDown(self):
        self.link_list = None

    def test_insert(self):
        self.link_list.insert(4)
        self.assertEqual(self.link_list.head.data, 4)

    def test_correct_delete(self):
        self.link_list.delete(3)
        self.assertEqual(self.link_list.head.data, 2)

    def test_wrong_delete(self):
        self.assertRaises(ValueError, self.link_list.delete, 4)

    def test_correct_search(self):
        try:
            self.link_list.search(1)
        except ValueError:
            self.fail("search raised ValueError")

    def test_wrong_search(self):
        self.assertRaises(ValueError, self.link_list.search, 4)

    def test_size(self):
        self.assertEqual(self.link_list.size(), 3)


class TestDoublyLinkList(unittest.TestCase):
    # Unit test cases for the implementation of doubly linkedlist

    def setUp(self):
        self.link_list = DoublyLinkedList()
        self.link_list.insert(1)
        self.link_list.insert(2)
        self.link_list.insert(3)
        self.link_list.insert(4)
        self.link_list.insert(5)

    def tearDown(self):
        self.link_list = None

    def test_insert(self):
        self.link_list.insert(6)
        self.assertEqual(self.link_list.head.data, 6)

    def test_correct_delete(self):
        self.link_list.delete(3)
        item = self.link_list.search(4)

        self.assertEqual(self.link_list.head.data, 5)
        self.assertEqual(item.get_next().get_data(), 2)
        self.assertEqual(item.get_previous().get_data(), 5)

    def test_wrong_delete(self):
        self.assertRaises(ValueError, self.link_list.delete, 6)

    def test_correct_search(self):
        try:
            self.link_list.search(1)
        except ValueError:
            self.fail("search raised ValueError")

    def test_wrong_search(self):
        self.assertRaises(ValueError, self.link_list.search, 6)

    def test_size(self):
        self.assertEqual(self.link_list.size(), 5)
