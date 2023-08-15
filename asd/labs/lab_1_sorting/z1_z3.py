# stable; worst - O(n^2), best - O(n)
def bubble_sort(a):
    end = len(a)
    made_changes = True
    while made_changes:
        made_changes = False
        for i in range(end - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                made_changes = True
        end -= 1
    return a


# unstable; worst - O(n^2), best - O(n^2)
def selection_sort(a):
    a_len = len(a)
    for i in range(a_len - 1):
        tmp_min = i
        for j in range(i + 1, a_len):
            if a[j] < a[tmp_min]:
                tmp_min = j
        a[i], a[tmp_min] = a[tmp_min], a[i]
    return a


# stable; worst - O(n^2), best - O(n)
# might be improved by using binary search
def insertion_sort(a):
    a_len = len(a)
    for i in range(1, a_len):
        val = a[i]
        j = i - 1
        while j >= 0 and a[j] > val:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = val
    return a


# unstable; worst - O(n^2), best - O(nlogn)
def binary_search(a, start, end, value):
    if a[start] > value:
        return start
    if a[end] < value:
        return end
    
    i = start + 1
    j = end - 1
    m = (i + j) // 2

    while not (a[m] <= value <= a[m+1]):
        if a[m] > value:
            end = m
        else:
            start = m
        m = (start + end) // 2
    
    return m + 1


def binary_insertion_sort(a):
    a_len = len(a)
    for i in range(1, a_len):
        j = binary_search(a, 0, i, a[i])
        a = a[:j] + [a[i]] + a[j:i] + a[i+1:]
    return a
