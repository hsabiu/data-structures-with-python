# Python implementation of a Stack data structure
from implementations.LinkedList import SinglyLinkedList


class ArrayStack:
    """Array implementation of stack data structure"""

    def __init__(self, capacity=1):
        self.capacity = capacity
        self.array = []

    def push(self, item):
        """Add item to the top of the stack, raise OverflowError if the stack is full"""

        if len(self.array) >= self.capacity:
            raise OverflowError("Stack overflow")
        self.array.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack, raise OverflowError if
        the stack is empty"""

        if self.is_empty():
            raise OverflowError("Stack Underflow")
        return self.array.pop()

    def peek(self):
        """Return the item at the top of the stack without modifying the data, raise
        Exception if the stack is empty"""

        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.array[-1]

    def is_empty(self):
        return len(self.array) == 0


class LinkedListStack:
    """Singly link list implementation of Stack data structure"""

    def __init__(self, capacity=1):
        self.capacity = capacity
        self.linkedlist = SinglyLinkedList()

    def push(self, item):
        """Add item to the top of the stack"""

        self.linkedlist.insert(item)

    def pop(self):
        """Remove and return the item at the top of the stack, raise Exception if
        the stack is empty"""

        if self.is_empty():
            raise OverflowError("Stack Underflow")
        data = self.linkedlist.head.get_data()
        self.linkedlist.delete(data)
        return data

    def peek(self):
        """Return the item at the top of the stack without modifying the data, raise
        Exception if the stack is empty"""

        if self.is_empty():
            raise Exception("Stack Underflow")
        return self.linkedlist.head.get_data()

    def is_empty(self):
        return self.linkedlist.size() == 0


if __name__ == '__main__':

    print('---------- TEST ARRAY STACK ----------')
    # Use array stack data structure to reverse a word
    word = 'WORD'
    reversed_word = ''

    stack = ArrayStack(len(word))

    for ch in word:
        stack.push(ch)

    while not stack.is_empty():
        reversed_word = reversed_word + stack.pop()

    print(f'Original word: {word}')
    print(f'Reversed word: {reversed_word}')
    print('--------------------------------------')

    print('')

    print('------- TEST LINKED LIST STACK -------')
    # Use linked list stack data structure to reverse a word
    del reversed_word
    word = 'WORD'
    reversed_word = ''

    stack = LinkedListStack(len(word))

    for ch in word:
        stack.push(ch)

    while not stack.is_empty():
        reversed_word = reversed_word + stack.pop()

    print(f'Original word: {word}')
    print(f'Reversed word: {reversed_word}')
    print('--------------------------------------')