class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [0 for _ in range(size)]
        self.first = self.last = 0
        self.elements = 0

    def put(self, value):
        if self.elements >= self.size:
            return -1
        else:
            self.arr[self.last] = value
            self.last = (self.last + 1) % self.size
            self.elements += 1
            return 1

    def get(self):
        if self.elements == 0:
            return None
        else:
            value = self.arr[self.first]
            self.first = (self.first + 1) % self.size
            self.elements -= 1
            return value


if __name__ == '__main__':
    Q = Queue(10)
    for n in [1, 7, 9, 4, 3, 5, 7]:
        Q.put(n)
    print(Q.arr)
    for n in range(3):
        print(Q.get())
    print(Q.first)
    for n in [8, 4, 3, 2]:
        Q.put(n)
    print(Q.arr)
    