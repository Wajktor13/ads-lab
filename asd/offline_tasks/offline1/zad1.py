"""Wiktor Wilkusz
Algorytm jest oparty na selection sort, z ta roznica, ze
petla wewnetrzna szuka minimum do k-tej pozycji liczac
od miejsca docelowego. Jest to poprawna modyfikacja, poniewaz
nawet jesli element zostanie przesuniety z miejsca pierwotnego,
to nadal znajdzie sie maksymalnie na k-tej pozycji liczac
od miejsca docelowego.

Zlozonosc czasowa: O(n*k)
dla k=1: O(n)
dla k=logn: O(n*logn)
dla k=n: O(n^2)
"""


from zad1testy import Node, runtests


def SortH(p,k):
    if p is None or p.next is None:
        return p
    head = Node()  # wartownik
    head.next = p
    prev_n1 = head

    # wyszukiwanie minimum
    while prev_n1.next.next is not None:
        prev_min = prev_n1
        prev_n2 = prev_n1.next
        i = 1
        while prev_n2.next is not None and i <= k:
            if prev_n2.next.val < prev_min.next.val:
                prev_min = prev_n2
            prev_n2 = prev_n2.next
            i += 1

        if prev_min == prev_n1:  # node jest na swoim miejscu - nie przepinamy
            prev_n1 = prev_n1.next
            continue

        # przepinanie
        n1 = prev_n1.next
        min_ = prev_min.next
        tmp = min_.next
        if n1.next == min_:
            # sa obok siebie
            prev_n1.next = min_
            min_.next = n1
            n1.next = tmp
        else:
            prev_n1.next = min_
            min_.next = n1.next
            prev_min.next = n1
            n1.next = tmp

        prev_n1 = prev_n1.next

    return head.next


runtests( SortH )
