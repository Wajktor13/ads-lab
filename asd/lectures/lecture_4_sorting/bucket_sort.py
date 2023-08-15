def bucket_sort(arr):
    min_val, max_val = min(arr), max(arr)
    n = int(max_val - min_val) + 2
    r = int(max_val - min_val) / (n - 1)
    buckets = [[] for _ in range(n)]
    for num in arr:
        buckets[int(int(num // r) - min_val)].append(num)

    i = 0
    for bucket in buckets:
        selection_sort(bucket)
        for num in bucket:
            arr[i] = num
            i += 1


def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for k in range(i, len(a)):
            if a[k] < a[min_index]:
                min_index = k

        a[i], a[min_index] = a[min_index], a[i]

    return a
    