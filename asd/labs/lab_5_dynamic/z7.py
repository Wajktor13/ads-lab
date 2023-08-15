def min_cost(A):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(1, n):
        C[0][i] = C[0][i - 1] + A[0][i]
        C[i][0] = C[i - 1][0] + A[i][0]
    
    for col in range(1, n):
        for row in range(1, n):
            C[row][col] = min(C[row - 1][col], C[row][col - 1]) + A[row][col]

    return C[n - 1][n - 1]


if __name__ == "__main__":
    print(min_cost([[1, 2, 3, 7, 8],
                    [9, 8, 2, 9, 9],
                    [1, 2, 1, 3, 7],
                    [1, 8, 8, 1, 9],
                    [9, 2, 0, 2, 1]]
                     ))
                     