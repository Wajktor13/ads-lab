from zad1testy import Node, runtests


def SortH(p, k):
    if k > 2:
        return heap_sort(p, k)
    else:
        return bubble_sort(p)


def heap_sort(p, k):
    head = Node()
    heap = [None for _ in range(k + 1)]
    n = p

    for i in range(k + 1):
        heap[i] = n
        n = n.next
        if n is None:
            last = i
            break
    else:
        last = k

    buil_heap(heap, last)
    curr = head

    while heap[0] is not None and last >= 0:
        curr.next = heap[0]
        curr = curr.next
        if n is not None:
            heap[0] = n
            n = n.next
        else:
            heap[0] = heap[last]
            heap[last] = None
            last -= 1
        heapify(heap, last + 1, 0)

    curr.next = None
    return head.next


def heapify(h, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    min_ind = i
    if l < n and h[l].val < h[min_ind].val:
        min_ind = l
    if r < n and h[r].val < h[min_ind].val:
        min_ind = r
    if min_ind != i:
        h[i], h[min_ind] = h[min_ind], h[i]
        heapify(h, n, min_ind)


def buil_heap(h, last_ind):
    for i in range(last_ind // 2, -1, -1):
        heapify(h, last_ind + 1, i)


def bubble_sort(p):
    head = Node()
    head.next = p
    prev_n = head
    while prev_n.next.next is not None:
        if prev_n.next.val > prev_n.next.next.val:
            tmp = prev_n.next.next.next
            prev_n.next.next.next = prev_n.next
            prev_n.next = prev_n.next.next
            prev_n.next.next.next = tmp

        prev_n = prev_n.next

    return head.next


runtests(SortH)
