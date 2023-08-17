def quick_sort(A, left, right):
    if left < right:
        i, j = hoare_partition(A, left, right)
        quick_sort(A, left, j)
        quick_sort(A, i, right)


def hoare_partition(A, left, right):
    pivot = A[left]
    i, j = left, right

    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    return i, j
