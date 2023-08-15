def solve(cities):  # city - (x, y)
    cities.sort(key=lambda c: c[0])
    n = len(cities)
    D = [[distance(cities[i], cities[j]) for i in range(n)] for j in range(n)]
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    F[0][1] = D[0][1]

    result = float('inf')
    for i in range(n - 1):
        result = min(result, tsp(F, D, i, n - 1) + D[i][n-1])
    return result


def distance(c1, c2):
    return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5


def tsp(F, D, i, j):
    if F[i][j] != float('inf'):
        return F[i][j]
    
    if i == j - 1:
        for k in range(i):
            F[i][j] = min(F[i][j], tsp(F, D, k, i) + D[k][j])
    else:
        F[i][j] = tsp(F, D, i, j-1) + D[j-1][j]
    return F[i][j]


if __name__ == '__main__':
    print(solve([(1, 3), (4, 5), (7, 1), (9, 3), (3, 8)]))
