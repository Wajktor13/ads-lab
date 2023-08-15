def min_x(A):
    n = len(A)
    i = int(n / 2)
    return A[i] if n % 2 != 0 else (A[i - 1] + A[i]) / 2
