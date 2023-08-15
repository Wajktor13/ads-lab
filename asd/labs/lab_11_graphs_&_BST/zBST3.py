class TreeNode:
    def __init__(self):
        self.childs = [None for _ in range(4)]
        self.count = 0


def unique(DNA_array):
    key = {'G' : 0, 'A' : 1, 'T' : 2, 'C' : 3}
    root = TreeNode()

    for DNA in DNA_array:
        node = root
        for nucl in DNA:
            k = key[nucl]
            if node.childs[k] is None:
                node.childs[k] = TreeNode()
            node = node.childs[k] 
        node.count += 1

        if node.count > 1:
            return False

    return True


if __name__ == "__main__":
    print(unique(['TAAG', 'TA', 'TAAGA', 'TGAAAACAAAAGGG', 'TTTTTGGTGTCGTCA', 'TAAGA', 'CAGCTTA']))
    print(unique(['TAAG', 'TA', 'TAAGA', 'TGAAAACAAAAGGG', 'TTTTTGGTGTCGTCA', 'TAAGCA', 'CAGCTTA']))
