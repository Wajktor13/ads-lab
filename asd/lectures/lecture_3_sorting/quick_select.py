# O(n)
def quick_select(arr, left, right, k):
    if left == right:
        return arr[left]
    if left < right:
        p = partition(arr, left, right)
        if p == k:
            return arr[p]
        elif p < k:
            return quick_select(arr, p + 1, right, k)
        else:
            return quick_select(arr, left, p - 1, k)


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1
