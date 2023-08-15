class BST_Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def sum_tree(root):
    s = root.value

    if root.left is not None:
        s += sum_tree(root.left)

    if root.right is not None:
        s += sum_tree(root.right)
    
    return s


if __name__ == "__main__":
    r = BST_Node(10)
    r.left = BST_Node(7)
    r.right = BST_Node(15)
    r.left.left = BST_Node(5)
    r.left.right = BST_Node(8)
    r.left.right.right = BST_Node(9)
    print(sum_tree(r))
