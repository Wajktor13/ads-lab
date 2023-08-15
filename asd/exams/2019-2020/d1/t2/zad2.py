from zad2testy import runtests


# def opt_sum(tab):
#     n = len(tab)
#     F = [[(tab[i], 0) if j == i else [float('inf'), float('inf')] for j in range(n)] for i in range(n)]
#     for i in range(n - 1, -1, -1):
#         for j in range(n):
#             for k in range(i, j):
#                 x, y, z = F[i][k], F[k + 1][j], F[i][j]
#                 if z[1] > max(abs(x[1]), abs(y[1])):
#                     F[i][j] = [x[0] + y[0], abs(max(abs(x[1]), abs(y[1]), abs(x[0] + y[0])))]

#     return F[0][n-1][1]


def opt_sum(A):
    n = len(A)
    F = [[None for _ in range(n)] for _ in range(n)]

    return fill(A, F, 0, n - 1)


def fill(A, F, row, col):
    if F[row][col] is not None:
        return F[row][col]
    if row + 1 == col:
        F[row][col] = abs(A[row] + A[col])
        return F[row][col]
    
    F[row][col] = max(abs(sum(A[row:col+1])), min(fill(A, F, row + 1, col), fill(A, F, row, col - 1)))
    return F[row][col]

runtests(opt_sum)
