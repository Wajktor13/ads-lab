"""
2 tablice A i B
chcemy znalezc najdluzszy wspolny podciag, nie musi byc spojny
f(A, B, i , j) = f(A, B, i-1, j-1) + 1, A[i] == B[j]
                 max(f(A, B, i-1, j), f(A, B, i, j-1)), wpp
                 0, i < 0 or j < 0

wywolanie: f(A, B, len(A) - 1, len(B) - 1)

^ O(n^2)

modyfikacja: rosnacy, jedna tablica
wywolanie: f(A, sorted(A), len(A) - 1, len(A) - 1)
"""


def lcs(A, B):
    n = len(A)
    m = len(B)
    f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i-1][j], f[i][j-1])

    return f[n][m]


if __name__ == '__main__':
    print(lcs('ADEFEDCE', 'AEDCEZZZAZ'))

    """
    longest increasing subseq usig lcs
    """
    x = [1, 5, 4, 3, 7, 4, 3, 1, 2, 3, 5, 3, 1, 9]
    print(lcs(x, sorted(x)))
