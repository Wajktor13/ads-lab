from zad1testy import runtests


def chaos_index( T ):
    n = len(T) 
    T_ind = [i for i in range(n)]
    k = -1

    T_ind = merge_sort(T_ind, key=lambda i: T[i])

    for i in range(n):
        k = max(k, abs(T_ind[i] - i))
    
    return k


def merge_sort(T, key):
    n = len(T)

    if n > 1:
        mid = n // 2
        left = merge_sort(T[:mid], key)
        right = merge_sort(T[mid:], key)
        return merge(left, right, key)

    return T


def merge(left, right, key):
    left_len, right_len = len(left), len(right)
    left_ind = right_ind = 0
    merged = []

    while left_ind < left_len and right_ind < right_len:
        if key(left[left_ind]) <= key(right[right_ind]):
            merged.append(left[left_ind])
            left_ind += 1
        else:
            merged.append(right[right_ind])
            right_ind += 1
    
    while left_ind < left_len:
            merged.append(left[left_ind])
            left_ind += 1
    
    while right_ind < right_len:
            merged.append(right[right_ind])
            right_ind += 1

    return merged  


runtests( chaos_index )
