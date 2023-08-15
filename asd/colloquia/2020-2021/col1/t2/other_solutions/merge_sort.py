from zad1testy import Node, runtests

def merge(h1, h2):
    n1, n2 = h1, h2
    last = head = Node()
    while n1 is not None and n2 is not None:
        if n1.val <= n2.val:
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


def SortH(p, k):
    head = Node()
    head.next = p
    done = False
    while not done:
        h1 = t1 = head.next
        prev = head
        while True:
            if h1 is None:
                break
            while t1.next is not None and t1.val <= t1.next.val:
                t1 = t1.next
            if t1.next is None:
                if h1 == head.next:
                    done = True
                break
            h2 = t2 = t1.next
            while t2.next is not None and t2.val <= t2.next.val:
                t2 = t2.next

            t1.next = None
            tmp = t2.next
            t2.next = None
            h3, t3 = merge(h1, h2)
            prev.next = h3
            t3.next = tmp
            h1 = t1 = tmp
            prev = t3
    return head.next


runtests(SortH)