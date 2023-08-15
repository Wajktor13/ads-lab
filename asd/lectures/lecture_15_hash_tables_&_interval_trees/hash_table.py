class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]

    def to_integer(self, key):
        if isinstance(key, int):
            return key
        
        else:
            n = len(key)
            bytes = bytearray(key, 'ascii')
            tmp = [0 for _ in range(8)]

            for i in range(min(n, 8)):
                tmp[i] = bytes[i]

            if n > 1:
                tmp[0] ^= bytes[-1]
            for i in range(6, -1, -1):
                tmp[i] ^= tmp[i + 1]
            
            for i in range(8, n):
                tmp[i % 8] ^= bytes[i]
            
            bits = bin(tmp[0])
            for byte in tmp:
                bits += bin(byte)[2:]
            
            return int(bits, 2)
    
    def hash(self, key):
        integer = self.to_integer(key)
        A, B = 256, (5**0.5 - 1) / 2

        return int(A * ((integer * B) // 1))
    
    def index(self, key):
        return self.hash(key) % self.size
    
    def insert(self, key, value):
        new_node = HashNode(key, value)
        ind = self.index(key)

        if self.table[ind] is None:
            self.table[ind] = new_node

        else:
            node = self.table[ind]
            while node.next is not None:
                node = node.next
            node.next = new_node
            new_node.parent = node
    
    def get_value(self, key):
        node = self.table[self.index(key)]

        while node.key != key:
            node = node.next

        return node.value
    
    def remove(self, key):
        ind = self.index(key)
        node = self.table[ind]

        if node is not None:
            while node is not None and node.key != key:
                node = node.next
            
            if node is not None:
                if node.parent is not None:
                    node.parent.next = node.next
                else:
                    self.table[ind] = None

    def visualize(self):
        visualization = [[] for _ in range(self.size)]

        for i in range(self.size):
            node = self.table[i]
            while node is not None:
                visualization[i].append(node.value)
                node = node.next
        
        return visualization


if __name__ == "__main__":
    ht = HashTable(10)
    for k, v in [(1, 'e'), ('py', '20'), ('node', 'n'), ('ksu', 'www'),
                 ('ultra', '5'), (11, 'python'), ('qwerty', '111'), (121, 'qwerty')]:
        ht.insert(k, v)
    
    print(ht.visualize())
    ht.remove(11)
    ht.remove('node')
    print(ht.visualize())
