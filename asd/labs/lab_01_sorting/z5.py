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
    