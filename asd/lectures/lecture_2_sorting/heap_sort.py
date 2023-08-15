def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


# repairs heap
def heapify(heap, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and heap[l] > heap[max_ind]:
        max_ind = l
    if r < n and heap[r] > heap[max_ind]:
        max_ind = r
    if max_ind != i:
        heap[i], heap[max_ind] = heap[max_ind], heap[i]
        heapify(heap, n, max_ind)


def build_heap(heap):
    heap_size = len(heap)
    for i in range(parent(heap_size - 1), -1, -1):
        heapify(heap, heap_size, i)


def heap_sort(heap):
    heap_size = len(heap)
    build_heap(heap)
    for i in range(heap_size - 1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        heapify(heap, i, 0)


if __name__ == '__main__':
    t = [12, 34, 2, 4,6, 4, 3, 5, 6,4]
    heap_sort(t)
    print(t)