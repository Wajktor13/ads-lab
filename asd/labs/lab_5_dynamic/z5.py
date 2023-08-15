def maximin(A, k):
    n = len(A)

    save = [[None for _ in range(n + 1)] for _ in range(k + 1)]
    save[1] = [(A[:i], -1) for i in range(n + 1)]

    F = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
    F[1][1] = A[0]
    for i in range(2, n + 1):
        F[1][i] = F[1][i-1] + A[i - 1]

    for row in range(2, k + 1):
        for col in range(row, n + 1):
            for i in range(col - 1, row - 2, -1):

                seq = A[i:col]
                if F[row][col] < min(sum(seq), F[row - 1][i]):
                    F[row][col] = min(sum(seq),  F[row - 1][i])

                    save[row][col] = (seq, i)

    return F[k][n], get_result(save)


def get_result(save):
    row, col = len(save) - 1, len(save[0]) - 1
    result = []

    while col > 0:
        result.append(save[row][col][0])
        col = save[row][col][1]
        row -= 1
        
    return result[::-1]
    

if __name__ == "__main__":
    print(maximin([1, 3, 7, 3, 2, 9, 1, 15, 12, 1, 1], 3))
