class NodeSingle:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def set_data(self, data):
        """Set data of this node"""
        self.data = data

    def set_next(self, next_node):
        """Set the next node in the chain of nodes"""
        self.next = next_node

    def get_data(self):
        """Return the data contained in this node"""
        return self.data

    def get_next(self):
        """Return the next node in the chain of nodes"""
        return self.next


class NodeDouble:
    def __init__(self, data=None, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

    def set_data(self, data):
        """Set the data of this node"""
        self.data = data

    def set_previous(self, previous_node):
        """Set the previous node in the chain of nodes"""
        self.previous_node = previous_node

    def set_next(self, next_node):
        """Set the next node in the chain of nodes"""
        self.next_node = next_node

    def get_previous(self):
        """Return the previous node in the chain of nodes"""
        return self.previous_node

    def get_next(self):
        """Return the next node in the chain of nodes"""
        return self.next_node

    def get_data(self):
        """Return the data contained in this node"""
        return self.data


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """Insert data into the head of the link list"""
        new_node = NodeSingle(data)
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
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """Insert data into the head of the link list"""
        pass

    def delete(self, data):
        """Delete data from the link list. Raise ValueError if data is not in the list"""
        pass

    def size(self):
        """Return the number of items in the link list"""
        pass

    def search(self, data):
        """Search the link list for data. If found, return the node, otherwise raise ValueError"""


if __name__ == '__main__':

    print('---------- TEST SINGLY LINKED LIST ----------')

    print('Initializing a new linked list...')
    linkedlist = SinglyLinkedList()

    print('Inserting 3 element in the initialized linked list...')
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)

    print('Finished inserting 3 elements... size of the linked list should be 3...')
    print('===> LinkedList size:', linkedlist.size())

    print('Searching for an element that exist in the linked list... ')
    print('Search should return a NodeSinglePonter object...')
    print('===> Search returned:', linkedlist.search(1))

    print('Deleting two elements from the list... size of the linked list should now be 1...')
    linkedlist.delete(1)
    linkedlist.delete(2)
    print('===> LinkedList size:', linkedlist.size())

    print('---------------------------------------------')
