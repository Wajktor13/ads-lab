"""
Implement a data structure that is able to insert and return its data median in O(log(n)).

My idea: two heaps and one mid value. Left heap - values < than mid, right heap - values
>= than heap.
"""


class DoubleHeap:
    def __init__(self, size):
        self.size = (size + 1) // 2
        self.left = [None for _ in range(self.size + 1)]  # heap - max
        self.l_ind = 0  # first free index
        self.mid = None
        self.right = [None for _ in range(self.size + 1)]  # heap - min
        self.r_ind = 0  # first free index
    
    def insert(self, value):
        if self.mid is None:
            self.mid = value
        else:
            if value < self.mid:
                if self.l_ind < self.size:
                    self.left[self.l_ind] = value
                    self.l_ind += 1
                    self.heapify_up_left(self.l_ind - 1)
                    if self.l_ind - self.r_ind == 2:
                        prev_median = self.mid
                        self.mid = self.left[0]
                        self.left[0] = self.left[self.l_ind - 1]
                        self.l_ind -= 1
                        self.heapify_down_left(0)
                        self.right[self.r_ind] = self.right[0]
                        self.r_ind += 1
                        self.right[0] = prev_median
                        self.heapify_up_right(self.r_ind - 1)
                else:
                    return -1  # heap overflow
            else:
                if self.r_ind < self.size:
                    self.right[self.r_ind] = value
                    self.r_ind += 1
                    self.heapify_up_right(self.r_ind - 1)
                    if self.r_ind - self.l_ind == 2:
                        prev_median = self.mid
                        self.mid = self.right[0]
                        self.right[0] = self.right[self.r_ind - 1]
                        self.r_ind -= 1
                        self.heapify_down_right(0)
                        self.left[self.l_ind] = self.left[0]
                        self.l_ind += 1
                        self.left[0] = prev_median
                        self.heapify_up_left(self.l_ind - 1)
                else:
                    return -1  # heap overflow


    def heapify_up_left(self, i):
        p = (i - 1) // 2
        if p >= 0 and self.left[i] > self.left[p]:
            self.left[i], self.left[p] = self.left[p], self.left[i]
            self.heapify_up_left(p)
    
    def heapify_down_left(self, i):
        x, y = 2 * i + 1, 2 * i + 2  # left and right son
        max_ind = i
        if x < self.l_ind and self.left[x] > self.left[max_ind]:
            max_ind = x
        if y < self.l_ind and self.left[y] > self.left[max_ind]:
            max_ind = y
        if max_ind != i:
            self.left[i], self.left[max_ind] = self.left[max_ind], self.left[i]
            self.heapify_down_left(max_ind)


    def heapify_up_right(self, i):
        p = (i - 1) // 2
        if p >= 0 and self.right[i] < self.right[p]:
            self.right[i], self.right[p] = self.right[p], self.right[i]
            self.heapify_up_right(p)


    def heapify_down_right(self, i):
        x, y = 2 * i + 1, 2 * i + 2  # left and right son
        min_ind = i
        if x < self.r_ind and self.right[x] < self.right[min_ind]:
            min_ind = x
        if y < self.r_ind and self.right[y] < self.right[min_ind]:
            min_ind = y
        if min_ind != i:
            self.right[i], self.right[min_ind] = self.right[min_ind], self.right[i]
            self.heapify_down_right(min_ind)

    def median(self):
        if self.l_ind == self.r_ind:
            return self.mid
        elif self.l_ind > self.r_ind:
            return (self.left[0] + self.mid) / 2
        elif self.l_ind < self.r_ind:
            return (self.right[0] + self.mid) / 2

if __name__ == "__main__":
    x = DoubleHeap(20)
    for v in [5, 4, 1, 3, 2, 6, 7, 8, 10, 12, 11]:
        x.insert(v)
    print(x.left, x.mid, x.right)
    print(f"{x.l_ind}, {x.r_ind}")
    print(x.median())