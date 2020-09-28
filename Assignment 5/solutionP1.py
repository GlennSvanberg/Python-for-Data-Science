"""
Implement the followings in Python: (6 points)

Queue implementation using a linked list, enqueue () and dequeue () methods.
Stack implementation using a linked list, push () and pop () methods.
Note: create a node, stack, and queue classes.

Describe some of the application scenarios with concrete examples in which it would be suitable to use 1) the stack and 2) the queue data structures.

"""


class Queue():
    # First in first out
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        # Adding last in queue
        node = Node(item)
        last = self.tail
        if last == None:
            self.head = node
            self.tail = node
        else:
            last.set_next(node)
            self.tail = node

    def dequeue(self):
        # take first element in queue
        node = self.head
        if node != None:
            self.head = node.get_next()
            return node.get_item()
        else:
            self.head = None
            self.tail = None
            return None


class Stack():
    # Last in last out
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

    def pop(self):
        node = self.head
        if self.head != None:
            self.head = self.head.get_next()
        if node != None:
            return node.get_item()
        return None


class Node():
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


def test_queue():

    q = Queue()
    print("adding 1-4")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print("adding 5")
    q.enqueue(5)

    print(q.dequeue())
    print(q.dequeue())


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push(4)
    print(s.pop())
    print(s.pop())


# test_queue()
# test_stack()

"""
The stack and the queue with linked list is both very efficient solutions for specific applications. 
In order to take advantage of the features with linked lists and keep the needed operations at O(1) the list was implemented 

"""