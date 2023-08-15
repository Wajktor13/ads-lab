"""
Implement (for linked list purposes):
    1.Node object definition
    2.Inserting to sorted ll
    3.Deleting node with the given value from unsorted ll
    4.Selection and insertion sort
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def insert_to_sorted_llist(first, to_insert):
    to_insert.next = None
    if first.value is None:
        return to_insert

    head = Node(None, first)  # guardian
    prev, curr = head, head.next
    while curr is not None and curr.value < to_insert.value:
        prev, curr = curr, curr.next

    prev.next = to_insert
    prev.next.next = curr

    return head.next


def delete_max_from_unsorted_llist(first):
    head = Node(None, first)  # guardian
    prev_max = max_node = None
    prev, curr = head, head.next
    while curr is not None:
        if prev_max is None or curr.value > prev_max.next.value:
            prev_max = prev
        prev, curr = curr, curr.next

    if prev_max is not None:
        max_node = prev_max.next
        prev_max.next = prev_max.next.next
        max_node.next = None

    return head.next, max_node



def insertion_sort(first):
    sfirst = Node(None)
    curr = first
    while curr is not None:
        tmp = curr.next
        sfirst = insert_to_sorted_llist(sfirst, curr)
        curr = tmp
    return sfirst


def selection_sort(first):
    first, sfirst = delete_max_from_unsorted_llist(first)
    curr = sfirst

    while first != None:
        first, curr.next = delete_max_from_unsorted_llist(first)
        curr = curr.next
    
    return reverse_llist(sfirst)


def reverse_llist(head):
    if head is None or head.next is None:
        return head

    prev, curr = head, head.next
    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev, curr = curr, tmp
    
    head.next = None

    return prev

"""
def selection_sort(first):
    if first is None or first.next is None:
        return first
    first = Node(None, first)
    prev_n1 = first
    while prev_n1.next.next is not None:
        prev_min = prev_n1
        prev_n2 = prev_n1.next
        while prev_n2.next is not None:
            if prev_n2.next.value < prev_min.next.value:
                prev_min = prev_n2
            prev_n2 = prev_n2.next

        curr_n = prev_n1.next
        min_n = prev_min.next
        if curr_n.next == min_n:
            prev_n1.next, min_n.next, curr_n.next = min_n, curr_n, min_n.next
        else:
            prev_n1.next = min_n
            tmp = min_n.next
            min_n.next = curr_n.next
            prev_min.next = curr_n
            curr_n.next = tmp

        prev_n1 = prev_n1.next
    return first.next
"""


if __name__ == '__main__':
    head = Node(7)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    n = selection_sort(head)

    while n is not None:
        print(n.value)
        n = n.next
