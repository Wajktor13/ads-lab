import random


def find(A, k, left, right):
    if left <= right:
        p = randomized_partition(A, left, right)
        if p == k:
            return A[p]
        elif p < k:
            return find(A, k, p + 1, right)
        else:
            return find(A, k, left, p - 1)

    return - 1


def randomized_partition(A, left, right):
    pivot_ind = random.randint(left, right)
    pivot = A[pivot_ind]
    A[pivot_ind], A[right] = A[right], A[pivot_ind]
    
    j = left - 1
    for i in range(left, right):
        if A[i] < pivot:
            j += 1
            A[j], A[i] = A[i], A[j]

    A[right], A[j+1] = A[j+1], A[right] 

    return j+1
