import re


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


def check_palindrom(text):
    # clean data
    text = str(text).lower()
    text = re.sub('[^a-z0-9]+', '', text)
    mid = len(text) // 2
    is_even = True

    if len(text) % 2 != 0:
        is_even = False

    first_half = text[:mid]
    second_half = text[mid:]
    # put first half in stack first to last
    stack = Stack()
    for char in first_half:
        stack.push(char)

    # put other half in queue last to first
    queue = Queue()
    for char in second_half:
        queue.enqueue(char)

    # remove middle char
    if not is_even:
        queue.dequeue()

    # compare stack and queue
    for i in range(mid):
        if stack.pop() != queue.dequeue():
            return False
    return True


p = "Ni talar bra latin"
p = "Able was I ere I saw Elba!"
p = "A man, a plan, a canal – Panama"
p = 123321

print(check_palindrom(p))
