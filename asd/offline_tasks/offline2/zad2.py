from zad2testy import runtests


def depth(L):
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

    deepest = L[min_ind]
    print(deepest)
    counter = 0
    for interval in L:
        if interval[0] >= deepest[0] and interval[1] <= deepest[1]:
            counter += 1
    
    return counter - 1


def quicksort(A, left, right, key):
    if left < right:
        p = partition(A, left, right, key)
        quicksort(A, left, p - 1, key)
        quicksort(A, p + 1, right, key)


def partition(A, left, right, key):
    pivot_ind = select_pivot(A, left, right, key)
    pivot = key(A[pivot_ind])
    A[pivot_ind], A[right] = A[right], A[pivot_ind]

    i = left - 1
    for j in range(left, right):
        if key(A[j]) < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[right] = A[right], A[i+1]

    return i + 1


def select_pivot(A, left, right, key):
    mid = (left + right) // 2

    if right - left < 15:
        return mid
    
    if key(A[left]) <= key(A[mid]) <= key(A[right]) or key(A[right]) <= key(A[mid]) <= key(A[left]):
        return mid

    elif key(A[mid]) <= key(A[left]) <= key(A[right]) or key(A[right]) <= key(A[left]) <= key(A[mid]):
        return left
    
    return right


runtests(depth)
