"""
Write a function that inserts element into a heap-max.
Append is allowed.
"""


def parent(i):
    return (i - 1) // 2


def heapify_up(h, i):
    p = parent(i)
    if i != 0 and h[p] < h[i]:
        h[p], h[i] = h[i], h[p]
        heapify_up(h, p)


def insert(h, val):
    h.append(val)
    heapify_up(h, len(h) - 1)


if __name__ == '__main__':
    heap = []
    insert(heap, 2)
    insert(heap, 4)
    insert(heap, 1)
    insert(heap, 7)
    insert(heap, 7)
    insert(heap, 11)
    print(heap)
