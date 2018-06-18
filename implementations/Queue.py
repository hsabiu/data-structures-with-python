from collections import deque


class Queue:
    def __init__(self, capacity=1):
        self.queue = deque([])
        self.capacity = capacity

    def enqueue(self, item):
        """Add item to the back of the queue (rear), raise OverflowError if the queue is full"""
        if len(self.queue) >= self.capacity:
            raise OverflowError("Can not add a new item to a full queue")
        self.queue.appendleft(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue, raise OverflowError if the queue is empty"""
        if self.is_empty():
            raise OverflowError("Queue is empty")
        return self.queue.pop()

    def front(self):
        """Return the item at the front of the queue without removing it"""
        return self.queue[-1]

    def rear(self):
        """Return the item at the back (rear) of the queue"""
        return self.queue[0]

    def size(self):
        """Return the number of items in the queue"""
        return len(self.queue)

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0


if __name__ == '__main__':

    print('------------- TEST QUEUE -------------')
    print('Creating a new queue of 5 item...')
    queue = Queue(5)
    print('New queue created...')
    print('')

    print('Inserting 5 elements (1-5) into the newly created queue...')
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print('5 elements inserted...')
    print('')

    print('Printing the front and rear of the queue')
    print('===> Items in queue (should be 5):', queue.size())
    print('')

    print('Printing the number of items in the queue')
    print('===> Front (should be 1):', queue.front())
    print('===> Rear (should be 5):', queue.rear())
    print('')

    print('Removing 5 elements from the queue in FIFO order')
    print('===>', queue.dequeue())
    print('===>', queue.dequeue())
    print('===>', queue.dequeue())
    print('===>', queue.dequeue())
    print('===>', queue.dequeue())
    print('')

    print('Testing if queue is empty. Test should return True')
    print('===>', queue.is_empty())
    print('--------------------------------------')
