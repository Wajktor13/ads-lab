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
    
    def find(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
    
    def insert(self, key, value=None):
        new_node = BST_Node(key, value)

        if self.root is None:
            self.root = new_node
        
        else:
            prev_node, node = None, self.root
            while node is not None:
                if key < node.key:
                    prev_node, node = node, node.left
                elif key == node.key:
                    return
                else:
                    prev_node, node = node, node.right

            new_node.parent = prev_node
            if key < prev_node.key:
                prev_node.left = new_node
            else:
                prev_node.right = new_node
    
    def extract_min(self):
        if self.root is None:
            return None
        
        node = self.root
        while node.left is not None:
            node = node.left
        
        return node
    
    def extract_max(self):
        if self.root is None:
            return None
        
        node = self.root
        while node.right is not None:
            node = node.right
        
        return node

    def delete(self, key):
        to_delete = self.find(key)

        if to_delete is not None:
            if to_delete.right is None:
                if to_delete.parent.left == to_delete:
                    to_delete.parent.left = to_delete.left
                else:
                    to_delete.parent.right = to_delete.left
            
            elif to_delete.left is None:
                if to_delete.parent.left == to_delete:
                    to_delete.parent.left = to_delete.right
                else:
                    to_delete.parent.right = to_delete.right
            
            else:
                succ = self.successor(key)
                self.delete(succ.key)
                succ.left, succ.right = to_delete.left, to_delete.right
                if to_delete.parent.left == to_delete:
                    to_delete.parent.left = succ
                else:
                    to_delete.parent.right = succ

    def successor(self, key):
        node = self.find(key)

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
    
    def predecessor(self, key):
        node = self.find(key)

        if node is not None:

            if node.left is not None:
                node = node.left
                while node.right is not None:
                    node = node.right
                return node
            
            else:
                while node.parent is not None and node.parent.right != node:
                    node = node.parent
                node = node.parent
        
        return node
    
    def sort_nodes(self):
        sorted_nodes = []
        self.add_to_sorted_nodes(sorted_nodes, self.root)
        
        return sorted_nodes

    def add_to_sorted_nodes(self, sorted_nodes, node):
        if node is not None:
            self.add_to_sorted_nodes(sorted_nodes, node.left)
            sorted_nodes.append(node)
            self.add_to_sorted_nodes(sorted_nodes, node.right)


if __name__ == "__main__":
    tree = BST()

    for k in [10, 8, 15, 4, 9, 13, 20, 18, 21, 25, 19, 17]:
        tree.insert(k)
    
    print(tree.extract_max().key, tree.extract_min().key)
    print(tree.successor(10).key, tree.successor(9).key)
    print(tree.predecessor(20).key, tree.predecessor(18).key)
    tree.delete(19)
    print(tree.predecessor(20).key, tree.predecessor(18).key)
    print(list(map(lambda node: node.key, tree.sort_nodes())))
    