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
        self.nr_of_nodes = 0

    def enqueue(self, item):
        # Adding last in queue
        self.nr_of_nodes += 1
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
            self.nr_of_nodes -= 1
            return node.get_item()
        else:
            self.head = None
            self.tail = None
            return None

    def top(self):
        return self.head.get_item()

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.nr_of_nodes

    def __str__(self):
        nodes = ""
        node = self.head
        while node != None:
            nodes += str(node.get_item())
            node = node.get_next()
            if node != None:
                nodes += ", "
        return nodes


class Stack():
    # Last in last out
    def __init__(self):
        self.head = None
        self.nr_of_nodes = 0

    def push(self, item):
        node = Node(item)
        self.nr_of_nodes += 1
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
            self.nr_of_nodes -= 1
            return node.get_item()
        return None

    def top(self):
        return self.head.get_item()

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.nr_of_nodes

    def __str__(self):
        nodes = ""
        node = self.head
        while node != None:
            nodes += str(node.get_item())
            node = node.get_next()
            if node != None:
                nodes += ", "
        return nodes


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
    print("Test Queue-----------------")
    q = Queue()
    for i in range(1, 4):
        print("Enque:", i)
        q.enqueue(i)

    print("Dequeue:", q)
    print("Size:", q.size())

    while not q.isEmpty():
        print("Dequeue:", q.dequeue())

    print("Dequeue when empty:", q.dequeue())
    print("Queue:", q)
    print("Size:", q.size())

    print("Enque:", 5)
    q.enqueue(5)
    print("Size:", q.size())

    print("Top:", q.top())


def test_stack():
    print("Test Stack-----------------")
    s = Stack()
    for i in range(1, 4):
        print("Push:", i)
        s.push(i)

    print("Stack:", s)
    print("Size:", s.size())

    while not s.isEmpty():
        print("Pop:", s.pop())

    print("Pop when empty:", s.pop())
    print("Stack:", s)
    print("Size:", s.size())

    print("Push:", 5)
    s.push(5)
    print("Size:", s.size())

    print("Top:", s.top())


if __name__ == "__main__":
    test_queue()
    test_stack()

"""
The stack and the queue with linked list is both very efficient solutions for specific applications. 
In order to take advantage of the features with linked lists and keep the needed operations at O(1) the list was implemented 

"""
