def deepest(L):
    n = len(L)
    start = [i for i in range(n)]
    end = [i for i in range(n)]
    not_containing = [0 for _ in range(n)]

    quicksort(start, 0, n - 1, lambda interval: L[interval][0])
    quicksort(end, 0, n - 1, lambda interval: - L[interval][1])

    for i in range(n):
        not_containing[start[i]] += i
        not_containing[end[i]] += i
    
    min_ind = 0
    for i in range(1, n):
        if not_containing[i] < not_containing[min_ind]:
            min_ind = i
    
    return L[min_ind]


def quicksort(A, left, right, key):
    if left < right:
        p = partition(A, left, right, key)
        quicksort(A, left, p - 1, key)
        quicksort(A, p + 1, right, key)


def partition(A, left, right, key):
    pivot = key(A[right])
    A[right], A[right] = A[right], A[right]

    i = left - 1
    for j in range(left, right):
        if key(A[j]) < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[right] = A[right], A[i+1]

    return i + 1


if __name__ == '__main__':
    print(deepest([[1, 7], [3, 9], [2, 5], [3, 6], [9, 15], [5, 7]]))
    