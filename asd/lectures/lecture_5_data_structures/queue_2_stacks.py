from stack_array import Stack


class Queue:
    def __init__(self, size):
        self.size = size
        self.stack_in = Stack(self.size)
        self.stack_out = Stack(self.size)

    def put(self, value):
        if self.stack_in.last >= self.size:
                return -1
        
        self.stack_in.push(value)
        return 1
    
    def get(self):
        if self.stack_out.is_empty():
            if self.stack_in.is_empty():
                return None
            self.transfer(self.stack_in.last)

        return self.stack_out.pop()

    def transfer(self, amount):
        for _ in range(amount):
            self.stack_out.push(self.stack_in.pop())

        return 1


if __name__ == '__main__':
    Q = Queue(4)
    for num in [1, 7, 8, 3]:
        Q.put(num)
    for i in range(3):
        print(Q.get())
    for num in [3, 9, 1]:
        Q.put(num)
    for i in range(4):
        print(Q.get())
