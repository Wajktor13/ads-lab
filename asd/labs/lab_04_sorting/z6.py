"""
n-el array
Write an algorith that finds pair of x, y (neighbours after sorting) that
have the maximum difference.
"""


def find(array):
    n = len(array)
    buckets = [[] for _ in range(n)]
    min_value = min(array)
    max_value = max(array)
    r = (max_value - min_value) / n

    for num in array:
        buckets[int((num // r) - min_value)].append(num)
        
    maximum = -float('inf')
    pair = [None, None]
    for i in range(n - 1):
        if not buckets[i]:
            continue
        j = i + 1
        while j < n and buckets[j] == []:
            j += 1
        if j < n:
            value = min(buckets[j]) - max(buckets[i])
            if value > maximum:
                maximum = value
                pair = (max(buckets[i]), min(buckets[j]))

    return pair


if __name__ == '__main__':
    print(find([6, 1, 2, 4, 5, 7, 10, 11, 4, 2, 0, 20, 12]))
