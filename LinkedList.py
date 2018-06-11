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
        new_node = NodeDouble(data)
        new_node.set_next(self.head)
        if self.head:
            self.head.set_previous(new_node)
        self.head = new_node

    def delete(self, data):
        """Delete data from the link list. Raise ValueError if data is not in the list"""
        current_node = self.head
        while current_node:
            if current_node.get_data() == data:
                break
            current_node = current_node.get_next()

        if current_node is None:
            raise ValueError("Data not in the list")
        else:
            if current_node.get_next():
                current_node.get_next().set_previous(current_node.get_previous())
            if current_node.get_previous():
                current_node.get_previous().set_next(current_node.get_next())

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


if __name__ == '__main__':

    print('---------- TEST SINGLY LINKED LIST ----------')

    print('Initializing a new linked list...')
    linkedlist = SinglyLinkedList()
    print('')

    print('Inserting 3 items into the initialized linked list...')
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    print('')

    print('3 items inserted... size of the linked list should be 3...')
    print('===> LinkedList size:', linkedlist.size())
    print('')

    print('Searching for an item that exist in the linked list... ')
    print('Search should return a NodeSingle object...')
    print('===> Search returned:', linkedlist.search(1))
    print('')

    print('Deleting two items from the list... size of the linked list should now be 1...')
    linkedlist.delete(1)
    linkedlist.delete(2)
    print('===> LinkedList size:', linkedlist.size())

    print('---------------------------------------------')

    print('')

    print('---------- TEST DOUBLY LINKED LIST ----------')

    print('Initializing a new linked list...')
    linkedlist = DoublyLinkedList()
    print('')

    print('Inserting 5 items into the initialized linked list...')
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    linkedlist.insert(4)
    linkedlist.insert(5)
    print('')

    print('5 items inserted... size of the linked list should be 5...')
    print('===> LinkedList size:', linkedlist.size())
    print('')

    print('Searching for an item that exist in the linked list... ')
    print('Search should return a NodeDouble object...')
    print('===> Search returned:', linkedlist.search(4))
    print('')

    print('Getting the data of the next and previous nodes pointed by the searched item...')
    print('===> Searched item: 4')
    print('===> Next data (should be 3):', linkedlist.search(4).get_next().get_data())
    print('===> Previous data (should be 5):', linkedlist.search(4).get_previous().get_data())
    print('')

    print('Deleting 1 item from the list... size of the linked list should now be 4...')
    print('===> Item to delete: 3')
    linkedlist.delete(3)
    print('===> LinkedList size:', linkedlist.size())
    print('')

    print('The previous node pointed by 2 should now be 4...')
    print('===> Previous node pointed by 2:', linkedlist.search(2).get_previous().get_data())
    print('The next node pointed by 4 should now be 2...')
    print('===> Next node pointed by 4:', linkedlist.search(4).get_next().get_data())

    print('---------------------------------------------')

