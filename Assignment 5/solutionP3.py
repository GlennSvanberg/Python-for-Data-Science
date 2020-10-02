"""
Binary trees tree

Similar to linked list
Nodes below a node is children

binary tree has only 2 children
Child node to the right must contain a int larger than it's parent

Only one node that has no arrows pointing to it. This is the root node

nodes with no children is called leaf nodes

level 1 is where root is.

Full binary tree has all leafs on same level
Complete is same but the not always the last to the right
        avg
Space O(n)
Access O(log n )
Search O(log n )
Insertion O(log n)
Deletion O(log n)

worst for all these is normally O(n)
"""
import random


class Node():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)


class Tree():
    def __init__(self):
        self.root = None


class RandomTree():
    def __init__(self, numbers):
        self.root = None

        for n in numbers:
            if self.root == None:
                self.root = Node(n)
            else:
                self.set_node(self.root, Node(n))

    def set_node(self, tree_node, current_node):
        if random.choice([True, False]):
            if tree_node.right == None:
                tree_node.right = current_node
            else:
                self.set_node(tree_node.right, current_node)
        else:
            if tree_node.left == None:
                tree_node.left = current_node
            else:
                self.set_node(tree_node.left, current_node)

    def print_tree(self):
        if self.root != None:
            self.print_sub_tree(self.root)

    def print_sub_tree(self, tree):
        print(tree.value)
        if tree.left != None:
            self.print_sub_tree(tree.left)

        if tree.right != None:
            self.print_sub_tree(tree.right)


class BinarySearchTree():
    def __init__(self, one, two):
        self.root = None

        self.merge(one, two, self.root)
        self.sort()

    def sort(self):
        print("Sorting")

    def merge(self, one, two, node):

        if one == None and two == None:
            return None
        if one == None:
            one = Node(0)
        if two == None:
            two = Node(0)

        node = Node(one.value + two.value)
        if self.root == None:
            self.root = node

        node.left = self.merge(one.left, two.left, node.left)
        node.right = self.merge(one.right, two.right, node.right)
        return node

    def set_node(self, tree_node, current_node):
        if tree_node == None:
            tree_node = current_node
        else:
            # decide left or right tree Equal goes left
            if tree_node.value >= current_node.value:
                if tree_node.left == None:
                    tree_node.left = current_node
                else:
                    self.set_node(tree_node.left, current_node)
            else:
                if tree_node.right == None:
                    tree_node.right = current_node
                else:
                    self.set_node(tree_node.right, current_node)

    def merge_trees(self, trees):
        for tree in trees:
            for n in tree:
                if self.root == None:
                    self.root = Node(n)
                else:
                    self.set_node(self.root, Node(n))

    def __str_level(self, node, level=0, left=True, s=""):
        if node != None:
            s = s + self.__str_level(node.right, level + 1, True)
            if level == 0:
                parent = ""
            elif left:
                parent = "/¯"
            else:
                parent = "\\_"
            s += f"{' ' * 4 * level} {parent} {node.value} \n"
            s += self.__str_level(node.left, level + 1, False)
        return s

    def __str__(self):
        return self.__str_level(self.root)


def printTree(node, level=0, left=True):
    if node != None:
        printTree(node.left, level + 1, True)

        if level == 0:
            parent = ""
        elif left:
            parent = "/¯"
        else:
            parent = "\\_"
        print(' ' * 4 * level, parent, node.value)
        printTree(node.right, level + 1, False)


def test():

    one = [1, 2, 3, 4]
    random.shuffle(one)
    tree_one = RandomTree(one).root
    print("one-------------")
    printTree(tree_one)

    two = [4, 5, 6, 7, 8, 9]
    random.shuffle(two)
    tree_two = RandomTree(two).root
    print("two-------------")
    printTree(tree_two)

    print("binary search tree--------")

    tree = BinarySearchTree(tree_one, tree_two).root
    # tree.merge_trees(trees)

    print("test")
    printTree(tree)


# test()


def test2():

    one = [1, 2, 3, 4]
    random.shuffle(one)
    tree_one = RandomTree(one)
    print("one-------------")
    print(tree_one)


"""
    two = [4, 5, 6, 7, 8, 9]
    random.shuffle(two)
    tree_two = RandomTree(two).root
    print("two-------------")
    printTree(tree_two)

    print("binary search tree--------")

    tree = BinarySearchTree(tree_one, tree_two).root
    # tree.merge_trees(trees)

    print("test")
    printTree(tree)
    """
test2()
