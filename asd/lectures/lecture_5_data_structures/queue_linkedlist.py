class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def put(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

        self.size += 1

    def get(self):
        if not self.size:
            return None
        else:
            to_return = self.head.value
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            self.size -= 1
            return to_return


if __name__ == '__main__':
    Q = Queue()
    for n in [1, 7, 9, 4, 3, 5, 7]:
        Q.put(n)
    for n in range(3):
        print(Q.get())
    for n in [8, 4, 3, 2]:
        Q.put(n)
    pass