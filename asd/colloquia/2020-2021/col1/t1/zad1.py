from zad1testy import runtests


def Median(T):
    n = len(T)
    helper = [None] * (n**2)
    left = int((n**2 - n) / 2)
    right = left + n - 1
    left_value = quick_select(T, 0, n**2 - 1, left)
    right_value = quick_select(T, 0, n**2 - 1, right)
    unused = []
    
    done = False
    lower, mid, greater = 0, left, right + 1
    for row in range(n):
        for col in range(n):
            num = T[row][col]
            if left_value < num < right_value:
                helper[mid] = num
                mid += 1
                if mid > right:
                    done = True
                    break
            elif num < left_value:
                helper[lower] = num
                lower += 1
            elif num > right_value:
                helper[greater] = num
                greater += 1
            else:
                unused.append(num)
        if done:
            break
    
    for num in unused:
        if num <= left_value and lower < left:
            helper[lower] = num
            lower += 1
        elif num >= right_value and greater < n**2:
            helper[greater] = num
            greater += 1
        else:
            helper[mid] = num
            mid += 1

    l = 0
    m = left
    h = m + n
    for row in range(n):
        T[row][row] = helper[m]
        m += 1
        for col in range(row):
            T[row][col] = helper[l]
            l += 1
        for col in range(row + 1, n):
            T[row][col] = helper[h]
            h += 1


def quick_select(A, left, right, ind):
        n = len(A)

        if left == right:
            return A[left // n][left % n]

        mid = partition(A, left, right)
        if mid < ind:
            return quick_select(A, mid + 1, right, ind)
        elif mid == ind:
            return A[mid // n][mid % n]
        else:
            return quick_select(A, left, mid - 1, ind)


def partition(A, left, right):
    n = len(A)
    pivot = A[right // n][right % n]
    i = left - 1
    for j in range(left, right):
        if A[j // n][j % n] < pivot:
            i += 1
            A[j // n][j % n], A[i // n][i % n] = A[i // n][i % n], A[j // n][j % n]

    A[(i + 1) // n][(i + 1) % n], A[right // n][right % n] = A[right // n][right % n], A[(i + 1) // n][(i + 1) % n]

    return i + 1


# def Median(T):
#     n = len(T)
#     helper = [None for _ in range(n * n)]
#     for i in range(n * n):
#         helper[i] = T[i // n][i % n]

#     helper = merge_sort(helper)

#     l = 0
#     m = int((n * n - n) / 2)
#     h = m + n
#     for row in range(n):
#         T[row][row] = helper[m]
#         m += 1
#         for col in range(row):
#             T[row][col] = helper[l]
#             l += 1
#         for col in range(row + 1, n):
#             T[row][col] = helper[h]
#             h += 1


# def merge_sort(arr):
#     n = len(arr)
#     if n > 1:
#         p = n // 2
#         left = merge_sort(arr[:p])
#         right = merge_sort(arr[p:])
#         return merge(left, right)
#     return arr


# def merge(left, right):
#     result = []
#     l_len, r_len = len(left), len(right)
#     l_ind = r_ind = 0
#     while l_ind < l_len or r_ind < r_len:
#         if r_ind >= r_len or (l_ind < l_len and left[l_ind] < right[r_ind]):
#             result.append(left[l_ind])
#             l_ind += 1
#         else:
#             result.append(right[r_ind])
#             r_ind += 1
#     return result


runtests( Median )
