"""
Write a program that finds the maximum and the minimum of N-element
array in (3/2) * N steps.
"""


def find_max_and_min(arr):
    maximum = -float('inf')
    minimum = float('inf')
    for i in range(0, len(arr) - 1, 2):
        a, b = arr[i], arr[i+1]
        if a < b:
            a, b = b, a
        maximum = max(maximum, a)
        minimum = min(minimum, b)
    maximum, minimum = max(maximum, arr[-1]), min(minimum, arr[-1])
    return maximum, minimum
