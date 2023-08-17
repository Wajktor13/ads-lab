"""
Implement quicksort without recursion.
Pop and append are allowed.
"""


def quicksort(a, left, right):
    stack = [(left, right)]  # (start_index, end_index)
    while stack != []:
        left, right = stack.pop()
        p = partition(a, left, right)
        if left < p - 1:
            stack.append((left, p - 1))
        if right > p + 1:
            stack.append((p + 1, right))


def partition(a, left, right):
    pivot_ind = select_pivot(a, left, right)
    pivot = a[pivot_ind]
    a[pivot_ind], a[right] = a[right], a[pivot_ind]
    i = left - 1
    for j in range(left, right):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[right], a[i+1] = a[i+1], a[right]
    return i + 1


def select_pivot(a, left, right):
    if left - right <= 2:
        return right
    x = (left + right) // 2
    if min(a[left], a[right]) <= a[x] <= max(a[left], a[right]):
        return x
    elif min(a[x], a[right]) <= a[left] <= max(a[x], a[right]):
        return left
    else:
        return right
        


if __name__ == "__main__":
    x = [2, 4, 5, 3, 2, 5, 3, 6, 9, 5, 4, 3, 2, 5, 4, 3, 5, 5, 6, 7, 4, 1]
    quicksort(x, 0, len(x) - 1)
    print(x)