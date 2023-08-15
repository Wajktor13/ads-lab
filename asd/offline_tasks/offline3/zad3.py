"""Wiktor Wilkusz 411605
Sortowanie jest oparte na algorytmie bucket sort. Minimalna i maksymalna wartosc
jest pobierana z P. Buckety sa sortowane poprzez selection sort.
Zlozonosc miedzy O(n) a O(n^2), zalezna od rozkladu danych.
"""


from zad3testy import runtests


def SortTab(T,P):
    min_value = float('inf')
    max_value = -float('inf')
    for interval in P:
        if interval[2] > 0:
            min_value = min(min_value, interval[0])
            max_value = max(max_value, interval[1])

    n = (len(T) // 6) + 1
    buckets = [[] for _ in range(n)]
    r = (max_value - min_value) / n
    for num in T:
        buckets[int(num // r)].append(num)

    for bucket in buckets:
        selection_sort(bucket)

    return [num for bucket in buckets for num in bucket]


def selection_sort(a):
    n = len(a)
    for i in range(n - 1):
        tmp_min = i
        for j in range(i + 1, n):
            if a[j] < a[tmp_min]:
                tmp_min = j
        # if a[tmp_min] != a[i]:
        a[i], a[tmp_min] = a[tmp_min], a[i]


"""
def SortTab(T, P):
    n = len(T)
    min_value, max_value = int(min(T)), int(max(T)) + 1
    no_outher_buckets = max_value - min_value + 1
    outher_buckets = [[] for _ in range(no_outher_buckets)]

    for num in T:
        outher_buckets[int(num) - min_value].append(num)
    
    for i in range(no_outher_buckets):
        outher_buckets[i] = bucket_sort(outher_buckets[i])

    return [num for bucket in outher_buckets for num in bucket]


def bucket_sort(A):
    if A != []:
        n = len(A)
        min_val, max_val = int(min(A)), int(max(A)) + 1
        r = (max_val - min_val) / n
        buckets = [[] for _ in range(n + 3)]

        for num in A:
            buckets[int((num - min_val) // r)].append(num)
        
        for bucket in buckets:
            selection_sort(bucket)
        
        return [num for bucket in buckets for num in bucket]
    
    return []
"""


runtests( SortTab )
