import random
from math import ceil


# pessimistic O(n)
def quick_select(arr, left, right, k):
    # print(arr, left, right, k)
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
    pivot_ind = left + select_pivot_magic_5(arr[left:right+1])
    arr[pivot_ind], arr[right] = arr[right], arr[pivot_ind]
    pivot = arr[right]

    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1


def select_pivot_magic_5(arr):
    n = len(arr)
    if n in (1, 2):
        return 0
    k = ceil(n / 5)
    groups = []
    medians = []
    i = 0
    for _ in range(k - 1):
        p = selection_sort(arr[i:i+5])
        groups.append(p)
        medians.append(p[2])
        i += 5
    p = selection_sort(arr[i:])
    groups.append(p)
    medians.append(p[int(((n % 5) - 1) // 2)])

    m = quick_select(medians, 0, k - 1, int((k - 1) // 2))

    for i in range(n):
        if arr[i] == m:
            return i


def selection_sort(a):
    for i in range(len(a)):
        min_index = i
        for k in range(i, len(a)):
            if a[k] < a[min_index]:
                min_index = k

        a[i], a[min_index] = a[min_index], a[i]

    return a


if __name__ == "__main__":
    while True:
        A = [random.randint(0, 10000) for _ in range(50)]
        ind = 10
        x = sorted(A.copy())[ind]
        y = quick_select(A, 0, len(A) - 1, ind)
        print(x, y)
        if y != x:
            print('err')
