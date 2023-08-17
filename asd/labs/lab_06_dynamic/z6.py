class Node:
    def __init__(self, left_edge = 0, right_edge = 0) -> None:
        self.save = self.left = self.right = None
        self.left_edge = left_edge
        self.right_edge = right_edge


def max_path(root):
    go_to(root)

    return find(root)


def go_to(root: Node):
    if root.save is not None:
        return root.save

    root.save = 0

    if root.left is not None:
        root.save = max(root.save, go_to(root.left) + root.left_edge)
    
    if root.right is not None:
        root.save = max(root.save, go_to(root.right) + root.right_edge)
    
    return root.save


def find(root):
    if root is None:
        return -float('inf')

    elif root.left is not None and root.right is not None:
        if root.save == root.left.save + root.left_edge:
            return max(root.save + root.right.save + root.right_edge,
                       find(root.left), find(root.right))
        
        else:
            return max(root.save + root.left.save + root.left_edge,
                       find(root.left), find(root.right))

    elif root.left is not None:
        return root.left_edge
    
    else:
        return root.right_edge


if __name__ == "__main__":
    r = Node(1, 3)
    r.left = Node(3, 5)
    r.right = Node(2, 1)
    r.left.left = Node()
    r.left.right = Node()
    r.right.left = Node()
    r.right.right = Node()
    print(max_path(r))
