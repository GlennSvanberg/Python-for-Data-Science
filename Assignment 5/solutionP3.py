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
        self.parent = None

    def is_leaf(self):
        if self.right == None and self.left == None:
            return True
        return False

    def has_two_children(self):
        if self.right != None and self.left != None:
            return True
        return False

    def __str__(self):
        return str(self.value)


class Tree():
    def __init__(self):
        self.root = None

    def top(self):
        return self.root

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


class BinaryTree(Tree):
    def __init__(self, numbers):
        super().__init__()
        self.order = True
        for n in numbers:
            if self.root == None:
                self.root = Node(n)
            else:
                self.set_node(self.root, Node(n))

    def set_node(self, tree_node, current_node):
        # if random.choice([True, False]):
        # alternate left / right
        if self.order:
            if tree_node.right == None:
                tree_node.right = current_node
            else:
                self.set_node(tree_node.right, current_node)
        else:
            if tree_node.left == None:
                tree_node.left = current_node
            else:
                self.set_node(tree_node.left, current_node)
        self.order = not self.order


class BinarySearchTree(Tree):
    def __init__(self, one, two):
        super().__init__()

        self.merge(one, two, self.root)
        self.sort()

    def sort(self):
        values = []
        self.get_values(self.root, values)

        # set mid value as root to balance the tree
        values.sort()
        mid = len(values)//2
        mid_val = values.pop(mid)
        new_root = Node(mid_val)

        for val in values:
            self.set_node(new_root, Node(val))
        self.root = new_root

    def delete_node(self, node):
        if node == None:
            return
        print("deleting", node.value)

        if node.is_leaf():
            print("Node is leaf")
            if node.parent == None:
                print(
                    "This is both a node and a leaf, thus it is the whole tree and can't be deleted")
            else:
                parent = node.parent
                if parent.left != None and parent.left.value == node.value:
                    parent.left = None
                elif parent.right != None and parent.right.value == node.value:
                    parent.right = None

        elif node.has_two_children():
            print("Node has 2 children")

        else:
            print("Node has one child")

    def get_values(self, node, values):
        if node != None:
            values.append(node.value)
        else:
            return
        if node.left != None:
            self.get_values(node.left, values)
        if node.right != None:
            self.get_values(node.right, values)

    def get_nodes(self):
        nodes = []
        self._get_nodes(self.root, nodes)
        return nodes

    def _get_nodes(self, node, nodes):
        if node != None:
            nodes.append(node)
        else:
            return
        if node.left != None:
            self._get_nodes(node.left, nodes)
        if node.right != None:
            self._get_nodes(node.right, nodes)

    def set_node(self, parent, current_node):
        # if root set current as parent
        if parent == None:
            parent = current_node
        else:
            # decide left or right tree Equal goes left
            if parent.value >= current_node.value:

                if parent.left == None:
                    parent.left = current_node
                    current_node.parent = parent
                else:
                    current_node.parent = parent
                    self.set_node(parent.left, current_node)
            else:
                if parent.right == None:
                    parent.right = current_node
                    current_node.parent = parent
                else:
                    current_node.parent = parent
                    self.set_node(parent.right, current_node)

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


def test_random_tree():

    one = random.sample(range(1, 15), 10)
    tree_one = BinaryTree(one)
    print("one-------------")
    print(tree_one)

    two = random.sample(range(1, 15), 10)
    tree_two = BinaryTree(two)
    print("two-------------")
    print(tree_two)

    print("binary search tree--------")

    tree = BinarySearchTree(tree_one.top(), tree_two.top())

    print(tree)


def test_same_tree():
    one = [5, 5, 5, 5, 1, 1]
    tree_one = BinaryTree(one)
    print("one-------------")
    print(tree_one)

    two = [1, 3, 7, 8, 1, 1]
    tree_two = BinaryTree(two)
    print("two-------------")
    print(tree_two)

    print("binary search tree--------")

    tree = BinarySearchTree(tree_one.top(), tree_two.top())
    print(tree)

    print("delete")
    leaf_node = tree.root.left.left
    tree.delete_node(leaf_node)
    print(tree)

    nodes = tree.get_nodes()
    """
    for node in nodes:
        print("val", node)
        if node.parent != None:
            print("parent", node.parent)

    """


test_same_tree()
