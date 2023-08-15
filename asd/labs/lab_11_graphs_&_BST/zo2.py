class BST_Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None


def find(tree, key):
    node = tree.root
    while node is not None:
        if key == node.key:
            return node
        elif key < node.key:
            node = node.left
        else:
            node = node.right


def successor(tree, key):
        node = tree.find(tree, key)

        if node is not None:

            if node.right is not None:
                node = node.right
                while node.left is not None:
                    node = node.left
                return node
            
            else:
                while node.parent is not None and node.parent.left != node:
                    node = node.parent
                node = node.parent
        
        return node


"""
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def next(self):
        if self.right is not None:
            n = self.right
            while n.left is not None:
                n = n.left
            return n
        
        else:
            n = self
            prev = None
            while n.parent is not None:
                prev = n
                n = n.parent
                if prev == n.left:
                    return n
        
        return None
"""
        