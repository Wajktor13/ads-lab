# O(n^3)
def mcss1(A):
    n = len(A)
    max_sum = -float('inf')
    for i in range(n):
        for j in range(i, n):
            curr_sum = 0
            for k in range(i, j + 1):
                curr_sum += A[k]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


# O(n^2)
def mcss2(A):
    n = len(A)
    max_sum = -float('inf')
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += A[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum


# O(nlogn) - divide and conquer
def mcss3(A, i, j):
    if i == j:
        return max(0, A[i])

    sep = (i + j) // 2
    left = right = 0

    tmp = 0
    for k in range(sep - 1, i - 1, -1):
        tmp = tmp + A[k]
        if tmp > left:
            left = tmp

    tmp = 0
    for k in range(sep, j + 1):
        tmp = tmp + A[k]
        if tmp > right:
            right = tmp

    mid = left + right

    return max(mcss3(A, i, sep), mid, mcss3(A, sep + 1, j))


# O(n) - dynamic
def mcss4(A):
    n = len(A)
    F = [0 for _ in range(n)]
    F[0] = A[0]
    for i in range(1, n):
        F[i] = max(F[i-1] + A[i], A[i])
    return max(F)


if __name__ == '__main__':
    x = [-1, 5, 4, -3, 18, -1, 5, -70, 5, 1]
    print(mcss1(x), mcss2(x), mcss3(x, 0, len(x) - 1), mcss4(x), sep='\n')
