import re
from solutionP1 import Queue, Stack


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


def test():
    cases = []
    cases.append("Ni talar bra latin")
    cases.append("Able was I ere I saw Elba!")
    cases.append("A man, a plan, a canal – Panama")
    cases.append(123321)
    cases.append("Not a palindrom")

    for case in cases:
        print(case)
        if check_palindrom(case):
            print("Palindrom")
        else:
            print("NOT Palindrom")
        print("-------------------")


test()
