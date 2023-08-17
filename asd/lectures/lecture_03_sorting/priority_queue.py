class PriorityQueue:
    def __init__(self, n):
        self.heap = [None for _ in range(n)]
        self.size = 0

    def heapify(self, n, i):
        l = self.left(i)
        r = self.right(i)
        max_ind = i
        if l < n and self.heap[l] > self.heap[max_ind]:
            max_ind = l
        if r < n and self.heap[r] > self.heap[max_ind]:
            max_ind = r
        if max_ind != i:
            self.heap[i], self.heap[max_ind] = self.heap[max_ind], self.heap[i]
            self.heapify(n, max_ind)

    def pop(self):
        if self.size > 0:
            top = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.heapify(self.size, 0)
            return top
        return -1

    def insert(self, value):
        self.heap[self.size] = value
        i, k = self.parent(self.size), self.size
        self.size += 1
        while i >= 0:
            if self.heap[i] < self.heap[k]:
                self.heap[i], self.heap[k] = self.heap[k], self.heap[i]
                i, k = self.parent(i), i
            else:
                break

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    @staticmethod
    def parent(i):
        return (i - 1) // 2


if __name__ == '__main__':
    prq = PriorityQueue(10)
    print(prq.pop())
    prq.insert(5)
    prq.insert(3)
    prq.insert(7)
    prq.insert(2)
    prq.insert(11)
    prq.insert(22)
    print(prq.pop())
    print(prq.pop())
    print(prq.heap, prq.size)
