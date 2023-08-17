def min_cost(A, a, b):
    n = len(A) + 1
    m = b - a + 2
    F = [[[float('inf') if i == 0 else None for _ in range(m)] for _ in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            F[i][j][j] = 0
    
    fill(A, a, b, F, n - 1, a, b)

    return F[n - 1][ind(a, a)][ind(b, a)]


def fill(A, a, b, F, i, x, y):
    ind_x, ind_y = ind(x, a), ind(y, a)

    if F[i][ind_x][ind_y] is not None:
        return F[i][ind_x][ind_y]

    F[i][ind_x][ind_y] = fill(A, a, b, F, i - 1, x, y)

    r = A[i - 1]

    if x <= r[0] and y >= r[1]:
        F[i][ind_x][ind_y] = min(F[i][ind_x][ind_y], fill(A, a, b, F, i - 1, x, r[0]) + r[2] + fill(A, a, b, F, i - 1, r[1], y))
    
    return F[i][ind_x][ind_y]


def ind(v, a):
    return v - a + 1


if __name__ == '__main__':
    print(min_cost([[3, 4, 40], [5, 6, 1], [7, 9, 3], [6, 7, 2], [0, 4, 5], [2, 3, 2], [8, 12, 1], [6, 7, 20], [4, 6, 7], [3, 4, 3],
                           [4, 6, 11]], 2, 9))
