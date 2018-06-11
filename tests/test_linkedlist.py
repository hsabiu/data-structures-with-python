import unittest
from LinkedList import SinglyLinkedList, DoublyLinkedList


class TestSinglyLinkList(unittest.TestCase):
    # Class to test the implementation of a singly link list

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
    # Class to test the implementation of a singly link list
    pass
