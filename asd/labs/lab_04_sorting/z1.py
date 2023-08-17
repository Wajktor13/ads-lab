"""
Write an algorith that sorts n-element array with numbers from range (0, n^2)

1.Change the base to n
2.Radix
"""


def counting_sort_by_key(arr, n, key):
    count = [0 for _ in range(n)]
    result = [0] * n

    for elem in arr:
        count[key(elem)] += 1
    
    for i in range(1, n):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        result[count[key(arr[i])] - 1] = arr[i]
        count[key(arr[i])] -= 1
    
    for i in range(n):
        arr[i] = result[i]


def radix_sort(arr):
    n = len(arr)
    counting_sort_by_key(arr, n, lambda x: x % n)
    counting_sort_by_key(arr, n, lambda x: x // n)
    

if __name__ == '__main__':
    a = [22, 27, 8, 60, 5, 50, 19, 13]
    radix_sort(a)
    print(a)
