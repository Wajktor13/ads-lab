"""
n-el array
log(n) various values

Expected time complexity: O(log(logn) * n)
"""


# 0(logn)
# binary search
def index(arr, val):
    left = 0
    right = len(arr) - 1
    while left <= right:
        p = (left + right) // 2
        if arr[p] == val:
            return p
        elif arr[p] < val:
            left = p + 1
        else:
            right = p - 1

    return -1  # not found


# O(n)
def insert(arr, val):
    arr.append(val)
    i = len(arr) - 2
    while i >= 0 and arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i -= 1


# O(nlog(k)), where k is a number of uniqe values
def sort_arr(arr):
    n = len(arr)
    values = []
    result = [0] * n

    for num in arr:
        if index(values, num) == -1:
            insert(values, num)

    counter = [0 for _ in values]  # avoid range when possible
    for num in arr:
        counter[index(values, num)] += 1

    for i in range(1, len(counter)):
        counter[i] += counter[i - 1]

    for i in range(n - 1, -1, -1):
        result[counter[index(values, arr[i])] - 1] = arr[i]
        counter[index(values, arr[i])] -= 1

    for i in range(n):
        arr[i] = result[i]


if __name__ == '__main__':
    a = [2, 2, 3, 3, 1, 2, 3, 2, 2, 2, 1, 2, 1, 1, 2, 3, 1, 3, 2, 2, 2, 1, 2, 3, 2, 2, 1, 3]
    sort_arr(a)
    print(a)
