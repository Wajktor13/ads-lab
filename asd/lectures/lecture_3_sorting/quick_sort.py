def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)

    """
    while left < right:
        p = partition(arr, left, right)
        quick_sort(arr, left, p - 1)
        left = p + 1
    """


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


if __name__ == '__main__':
    a = [2, 3, 5, 4, 3, 4, 5, 7, 6, 5, 2]
    quick_sort(a, 0 , len(a) - 1)
    print(a)