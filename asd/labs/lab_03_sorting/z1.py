"""
Implement quicksort with O(logn) space complexity and improved pivot
selecting method.
"""


# No tail recursion and always sorting the smaller part of the array
def quick_sort(arr, left, right):
    while left < right:
        p = partition(arr, left, right)
        if p <= (left + right) // 2:
            quick_sort(arr, left, p - 1)
            left = p + 1
        else:
            quick_sort(arr, p + 1, right)
            right = p - 1


def partition(arr, left, right):
    pivot_ind = median3_ind(arr, left, right, (left + right) // 2)
    pivot = arr[pivot_ind]
    arr[pivot_ind], arr[right] = arr[right], arr[pivot_ind]
    i = left - 1
    for k in range(left, right):
        if arr[k] < pivot:
            i += 1
            arr[i], arr[k] = arr[k], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def median3_ind(arr, x, y, z):
    if arr[x] <= arr[y] <= arr[z]:
        return y
    elif arr[y] <= arr[x] <= arr[z]:
        return x
    else:
        return z


if __name__ == '__main__':
    a = [2, 4, 3, 2, 4, 6, 6, 5, 3, 7, 9, 11, 3]
    quick_sort(a, 0, len(a) - 1)
    print(a)