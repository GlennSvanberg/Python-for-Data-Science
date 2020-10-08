class HashTable():
    def __init__(self):
        self.arr = [None] * 7

    def insert(self, value):
        if type(value) == list:
            for val in value:
                self.insert(val)
        else:
            hashed_value = value % len(self.arr)

            if self.arr[hashed_value] == None:
                self.arr[hashed_value] = Node(value)
            else:
                node = self.arr[hashed_value]
                while node.child != None:
                    node = node.child
                node.child = Node(value)

    def search(self, value):
        node = self.arr[value % len(self.arr)]
        while node.value != value and node != None:
            node = node.child

        return node.value

    def __str__(self):
        out = ""
        for root in self.arr:
            node = root
            if root == None:
                out += "None"
            while node != None:
                out += str(node.value) + ", "
                node = node.child
            else:
                out += "\n"

        return out


class Node():
    def __init__(self, value):
        self.value = value
        self.child = None

    def __str__(self):
        return str(self.value)


def test1():
    print("Insert and search single values:")
    ht = HashTable()
    ht.insert(16)
    ht.insert(8)
    ht.insert(15)
    ht.insert(0)
    print(ht)
    res = ht.search(16)
    print("res", res)


def test2():
    print("Insert list")
    ht = HashTable()
    l = [700, 21, 50, 85, 92, 101, 22, 23, 24, 25, 26, 28, 29, 30, 76]
    ht.insert(l)
    print(ht)


test1()
test2()
