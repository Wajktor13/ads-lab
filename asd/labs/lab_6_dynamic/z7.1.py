def contains_range(A, a, b):
    n = len(A) + 1
    m = b - a + 2
    F = [[[False if i == 0 else None for _ in range(m)] for _ in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            F[i][j][j] = True
    
    fill(A, a, b, F, n - 1, a, b)

    return F[n - 1][ind(a, a)][ind(b, a)]


def fill(A, a, b, F, i, x, y):
    ind_x, ind_y = ind(x, a), ind(y, a)

    if F[i][ind_x][ind_y] is not None:
        return F[i][ind_x][ind_y]

    F[i][ind_x][ind_y] = fill(A, a, b, F, i - 1, x, y)
    if F[i][ind_x][ind_y]:
        return True

    r = A[i - 1]

    if x <= r[0] and y >= r[1]:
        F[i][ind_x][ind_y] = fill(A, a, b, F, i - 1, x, r[0]) and fill(A, a, b, F, i - 1, r[1], y)
    
    return F[i][ind_x][ind_y]


def ind(v, a):
    return v - a + 1


if __name__ == '__main__':
    print(contains_range([[5, 6], [7, 9], [6, 7], [0, 4], [2, 3], [8, 12], [4, 6], [3, 4]], 2, 9))
    print(contains_range([[5, 6], [6, 7], [0, 4], [2, 3], [8, 12], [4, 6], [3, 4]], 2, 9))
    