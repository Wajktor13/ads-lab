class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.last = 0

    def push(self, value):
        if self.last >= self.size:
            data = self.arr.copy()
            self.arr = [0] * (self.size * 2)

            for i in range(self.size):
                self.arr[i] = data[i]
            self.size *= 2

        self.arr[self.last] = value
        self.last += 1

    def pop(self):
        if self.is_empty():
            return None

        self.last -= 1
        return self.arr[self.last]

    def is_empty(self):
        return not self.last


if __name__ == '__main__':
    s = Stack(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(1)
    print(s.arr)
    print(s.pop())
