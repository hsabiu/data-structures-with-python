class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def set_data(self, data):
        """Set data of this node"""
        self.data = data

    def set_next(self, next_node):
        """Set a pointer to the next node in the chain of nodes"""
        self.next = next_node

    def get_data(self):
        """Return the data contained in this node"""
        return self.data

    def get_next(self):
        """Return the pointer to the next node in the chain of nodes"""
        return self.next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """Insert data into the head of the link list"""
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def delete(self, data):
        """Delete data from the link list. Raise ValueError if data is not in the list"""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.get_data() == data:
                break
            previous_node = current_node
            current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data not in the list")
        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())

    def size(self):
        """Return the number of items in the link list"""
        counter = 0
        current_node = self.head
        while current_node:
            counter = counter + 1
            current_node = current_node.get_next()
        return counter

    def search(self, data):
        """Search the link list for data. If found, return the node, otherwise raise ValueError"""
        current_node = self.head
        while current_node:
            if current_node.get_data() == data:
                return current_node
            current_node = current_node.get_next()

        raise ValueError("Data not in the list")


class DoublyLinkedList:
    def __init__(self):
        pass


if __name__ == '__main__':

    test_list = SinglyLinkedList()

    test_list.insert(1)
    test_list.insert(2)
    test_list.insert(3)
    test_list.insert(4)
    test_list.insert(5)

    print(test_list.size())

    print(test_list.search(1))
    # print(test_list.search(10))

    test_list.delete(1)
    test_list.delete(5)

    print(test_list.size())
