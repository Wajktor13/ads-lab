def merge_sort(a):
    if len(a) > 1:
        p = len(a) // 2
        left = merge_sort(a[:p])
        right = merge_sort(a[p:])
        return merge(left, right)
    return a

def merge(left, right):
    l_len, r_len = len(left), len(right)
    l_ind = r_ind = i = 0
    result = [None for _ in range(l_len + r_len)]
    while l_ind < l_len or r_ind < r_len:
        if l_ind < l_len and (r_ind >= r_len or left[l_ind] <= right[r_ind]):
            result[i] = left[l_ind]
            l_ind += 1
        else:
            result[i] = right[r_ind]
            r_ind += 1
        i += 1
    return result


if __name__ == "__main__":
    print(merge_sort([2, 5, 2, 6, 5, 3, 8, 1, 4, 6]))
