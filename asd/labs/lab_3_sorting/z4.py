"""
Implement a heap sort that sorts elements of k sorted linked lists.
Lists are not empty. Required time complexity: O(nlog(k)).
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def heapify(h, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    min_ind = i
    if l < n and h[l].value < h[min_ind].value:
        min_ind = l
    if r < n and h[r].value < h[min_ind].value:
        min_ind = r
    if min_ind != i:
        h[i], h[min_ind] = h[min_ind], h[i]
        heapify(h, n, min_ind)


def build_heap(h):
    n = len(h)
    p = (n - 1) // 2
    for i in range(p, -1, -1):
        heapify(h, n, i)


def heap_sort(h):
    n = len(h) - 1
    first = Node(None)
    curr = first
    build_heap(h)
    while h[0] is not None:
        curr.next = h[0]
        curr = curr.next
        h[0] = h[0].next
        if h[0] is None:
            h[0] = h[n]
            n -= 1
        heapify(h, n + 1, 0)

    return first.next


if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(5)
    l1.next.next = Node(9)
    l2 = Node(1)
    l2.next = Node(11)
    l3 = Node(2)
    l3.next = Node(5)
    l3.next.next = Node(10)

    result = heap_sort([l1, l2, l3])
