class BST_Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.below = 1
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value=None):
        new_node = BST_Node(key, value)

        if self.root is None:
            self.root = new_node
        
        else:
            prev_node, node = None, self.root
            while node is not None:
                if key < node.key:
                    prev_node, node = node, node.left
                    prev_node.below += 1
                elif key == node.key:
                    return
                else:
                    prev_node, node = node, node.right
                    prev_node.below += 1

            new_node.parent = prev_node
            if key < prev_node.key:
                prev_node.left = new_node
            else:
                prev_node.right = new_node
    
    def find_ith(self, i):
        if self.root is not None and i <= self.root.below:
            return self.recursive_find_ith(self.root, i)

    def recursive_find_ith(self, node, i):
        lower = 0
        if node.left is not None:
            lower = node.left.below
        
        if lower + 1 == i:
            return node
        elif lower >= i:
            return self.recursive_find_ith(node.left, i)
        else:
            return self.recursive_find_ith(node.right, i - lower - 1)


if __name__ == "__main__":
    tree = BST()

    for k in [10, 8, 15, 4, 9, 13, 20, 18, 21, 25, 19, 17]:
        tree.insert(k)
    
    print(tree.find_ith(9).key)
    print(tree.find_ith(12).key)
    print(tree.find_ith(3).key)
    print(tree.find_ith(8).key)
                  