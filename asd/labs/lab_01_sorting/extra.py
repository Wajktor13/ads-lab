"""
Write a program that finds first missing number in
a sequence (1, 2, 3, 4, ...). Required time complexity: O(logN)
"""


# binary search
def find(arr):
    left, rigt = 0, len(arr) - 1
    if rigt == -1:
        return 1
    while left < rigt:
        mid = (left + rigt) // 2
        if arr[mid] > mid + 1:
            rigt = mid
        else:
            left = mid + 1
    result = arr[left-1] + 1
    return result if result != arr[-1] else result + 1
