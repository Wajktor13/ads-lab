"""
Write a program that finds two elements in a sorted array
with the given difference. Required time complexity: O(n)
"""


def find(arr, value):
    i, j = 0, 1
    while i < j < len(arr):
        difference = arr[j] - arr[i]
        if difference == value:
            return True
        elif difference < value:
            j += 1
        else:
            i += 1
    return False
