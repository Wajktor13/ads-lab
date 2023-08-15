from zad2testy import runtests


class BinaryNode:
    def __init__(self):
        self.left = self.right = None
        self.postfixes = 1


def double_prefix( L ):
    L.sort(key=lambda string: len(string))
    root = BinaryNode()
    super_cools = []

    for string in L:
        node = root
        for char in string:
            if char == '0':
                if node.left is not None:
                    node = node.left
                    node.postfixes += 1
                else:
                    node.left = BinaryNode()
                    node = node.left
                    
            else:
                if node.right is not None:
                    node = node.right
                    node.postfixes += 1
                else:
                    node.right = BinaryNode()
                    node = node.right
    pass
    find_super_cools(root.left, '0', super_cools)
    find_super_cools(root.right, '1', super_cools)

    return super_cools


def find_super_cools(node, string, super_cools):
    if node is None or node.postfixes < 2 or (node.left is None and node.right is None):
        return
    
    if (node.right is None and node.left is not None and node.left.postfixes < 2) or\
       (node.left is None and node.right is not None and node.right.postfixes < 2) or\
       (node.left is not None and node.right is not None and node.left.postfixes < 2 and node.right.postfixes < 2):
        super_cools.append(string)
        return
    
    find_super_cools(node.left, string +'0', super_cools)
    find_super_cools(node.right, string + '1', super_cools)


double_prefix(['1000', '001000', '0011', '100010'])
runtests( double_prefix )
