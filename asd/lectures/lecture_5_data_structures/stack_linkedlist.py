class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node(None)

    def push(self, value):
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = Node(value)

    def pop(self):
        if self.is_empty():
            return None

        prev_n, n = self.head, self.head.next
        while n.next is not None:
            prev_n, n = n, n.next

        prev_n.next = None

        return n.value

    def is_empty(self):
        return self.head.next is None


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(7)
    s.push(1)
    print(s.pop())
