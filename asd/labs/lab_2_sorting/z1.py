"""
1.Write a program that merges two sorted one-way lists.
2.Merge sort of the natural series
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def merge(h1, h2):
    n1, n2 = h1, h2
    last = head = Node()
    while n1 is not None and n2 is not None:
        if n1.value <= n2.value:
            last.next = n1
            n1 = n1.next
        else:
            last.next = n2
            n2 = n2.next
        last = last.next
    if n1 is not None:
        last.next = n1
    elif n2 is not None:
        last.next = n2
    while last.next is not None:
        last = last.next

    return head.next, last


def merge_sort(first):
    head = Node()
    head.next = first
    done = False
    while not done:
        h1 = t1 = head.next
        prev = head
        while True:
            if h1 is None:
                break
            while t1.next is not None and t1.value <= t1.next.value:
                t1 = t1.next
            if t1.next is None:
                if h1 == head.next:
                    done = True
                break
            h2 = t2 = t1.next
            while t2.next is not None and t2.value <= t2.next.value:
                t2 = t2.next

            t1.next = None
            tmp = t2.next
            t2.next = None
            h3, t3 = merge(h1, h2)
            prev.next = h3
            t3.next = tmp
            h1 = t1 = tmp
            prev = t3
            
    return head


if __name__ == '__main__':
    llist = Node(1)
    x = llist
    for i in [3, 2, 2, 3, 1, 4, 2, 5, 7, 9]:
        x.next = Node(i)
        x = x.next

    llist = merge_sort(llist)
