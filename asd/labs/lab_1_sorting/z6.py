def min_ind(A, x):
    end = len(A) - 1
    result = -1

    while True:
        min_ind = binary_search(A, 0, end, x)
        end = min_ind - 1
        if min_ind < 0:
            return result
        else:
            result = min_ind
        

def binary_search(A, start, end, value):
    i, j = start, end

    while i <= j:
        m = (i + j) // 2
        print(end, m)
        if A[m] == value:
            return m
        if A[m] < value:
            i = m + 1
        else:
            j = m - 1

    return -1
