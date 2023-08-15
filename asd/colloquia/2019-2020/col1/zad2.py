def section(T,p,q):
    n = len(T)
    first = quick_select(T, 0, n - 1, p)
    last = quick_select(T, 0, n - 1, q)
    result = [first]
    for h in T:
        if first > h > last:
            result.append(h)
    result.append(last)

    bucket_sort(result, first, last)

    return result


def quick_select(arr, start, end, k):
    if start == end:
        return arr[start]
    if start < end:
        p = partition(arr, start, end)
        if p == k:
            return arr[k]
        elif p < k:
            return quick_select(arr, p + 1, end, k)
        else:
            return quick_select(arr, start, p - 1, k)


def partition(arr, start, end):
    pivot_ind = (start + end) // 2
    pivot = arr[pivot_ind]
    arr[pivot_ind], arr[end] = arr[end], arr[pivot_ind]
    i = start - 1
    for j in range(start, end):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def bucket_sort(arr, max_val, min_val):
    r = int(max_val - min_val) + 1
    buckets = [[] for _ in range(r + 1)]
    for num in arr:
        buckets[int(num - min_val)].append(num)

    i = 0
    for k in range(r, -1, -1):
        selection_sort(buckets[k])
        for num in buckets[k]:
            arr[i] = num
            i += 1


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        max_ind = i
        for j in range(i):
            if arr[max_ind] < arr[j]:
                max_ind = j
        if max_ind != i:
            arr[i], arr[max_ind] = arr[max_ind], arr[i]


if __name__ == '__main__':
    x = [160.1, 150.2, 190.2, 205, 180.9, 199, 210.8, 198, 189.8, 233, 202.2]
    a, b = 3, 8
    y = section(x, a, b)
    print(y)
    print(f'Test: {y == list(reversed(sorted(x)))[a:b+1]}')
