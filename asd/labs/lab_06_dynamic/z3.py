"""
"Prom"

dlugosci samochodu i promu sa w metrach (calkowite)
prom ma 2 poklady
2 opcje - samochod jedzie na dolny albo gorny
ile max samochodow mozna zmiescic bez zmiany kolejnosci samochodow

l1 - dl pasa 1
l2 - dl pasa 2
L - tablica dlugosci
i - ktory samochod

f(l1, l2, L, i) = 0, L[i] > l1 and L[i] > l1
                = f(l1 - L[i], l2, L, i - 1) + 1, L[i] > l2
                = f(l1, l2 - L[i], L, i - 1) + 1, L[i] > l1
                = max(f(l1 - L[i], l2, L, i - 1), f(l1, l2 - L[i], L, i - 1)) + 1, wpp


szacowanie zlozonosci rekurencyjnych przez wymiar tablicy pomoczniczej
tutaj tablica 3 wym (l1, l2 , i)  - n^3
"""


def ferry(len_upper, len_bottom, A):
    n = len(A)
    F = [[[0 for _ in range(len_upper + 1)] for _ in range(len_bottom + 1)] for _ in range(n)]

    for i in range(n):
        for lb in range(len_bottom + 1):
            for lu in range(len_upper + 1):
                if i == 0 and (A[i] <= lb or A[i] <= lu):
                    F[i][lb][lu] = 1

                elif lb < A[i] <= lu:
                    F[i][lb][lu] = F[i - 1][lb][lu - A[i]] + 1

                elif lu < A[i] <= lb:
                    F[i][lb][lu] = F[i - 1][lb - A[i]][lu] + 1

                elif A[i] <= lb and A[i] <= lu:
                    F[i][lb][lu] = max(F[i - 1][lb][lu - A[i]], F[i - 1][lb - A[i]][lu]) + 1
    
    return get_result(len_upper, len_bottom, A, F)


def get_result(len_upper, len_bottom, A, F):
    n = len(A)
    upper, bottom = [], []
    capacity = -float('inf')
    i, lb, lu = n, len_bottom, len_upper
    for p in range(n):
        if F[p][len_bottom][len_upper] > capacity:
            capacity = F[p][len_bottom][len_upper]
            i = p

    while True:
        if i == 0:
            length = 0
            for car in upper:
                length += A[car]
            if length + A[0] <= lu:
                upper.append(0)
            else:
                bottom.append(0)
            break

        elif lu - A[i] > 0 and F[i - 1][lb][lu - A[i]] == F[i][lb][lu] - 1:
            upper.append(i)
            lu -= A[i]
            i -= 1

        elif lb - A[i] > 0 and F[i - 1][lb - A[i]][lu] == F[i][lb][lu] - 1:
            bottom.append(i)
            lb -= A[i]
            i -= 1

    return capacity, sorted(upper), sorted(bottom)


###################################################


def ferry_recursive(len_upper, len_bottom, A):
    A = [0] + A
    n = len(A)
    F = [[[None for _ in range(len_upper + 1)] for _ in range(len_bottom + 1)] for _ in range(n)]
    for i in range(len_upper + 1):
        for j in range(len_bottom + 1):
            F[0][j][i] = (0, True)
    
    for i in range(len_upper + 1):
        for j in range(len_bottom + 1):
            fill(len_upper, len_bottom, A, F, n - 1, j, i)

    bottom, upper = [], []
    get_result_recursive(bottom, upper, A, F, n - 1, len_bottom, len_upper)

    return F[n - 1][len_bottom][len_upper][0], upper[::-1], bottom[::-1]


def fill(len_upper, len_bottom, A, F, i, lb, lu):
    if F[i][lb][lu] is not None:
        return F[i][lb][lu]
    
    F[i][lb][lu] = (fill(len_upper, len_bottom, A, F, i - 1, lb, lu)[0], False)

    if lb - A[i] >= 0 and fill(len_upper, len_bottom, A, F, i - 1, lb - A[i], lu)[1]:
        F[i][lb][lu] = (max(F[i][lb][lu][0], F[i-1][lb - A[i]][lu][0] + 1), True)

    if  lu - A[i] >= 0 and fill(len_upper, len_bottom, A, F, i - 1, lb, lu - A[i])[1]:
        F[i][lb][lu] = (max(F[i][lb][lu][0], F[i - 1][lb][lu - A[i]][0] + 1), True)
    
    return F[i][lb][lu]


def get_result_recursive(bottom, upper, A, F, i, lb, lu):
    if i == 0:
        return
    elif F[i][lb][lu][0] == F[i - 1][lb][lu][0]:
        get_result_recursive(bottom, upper, A, F, i - 1, lb, lu)
    elif lb - A[i] >= 0 and F[i - 1][lb - A[i]][lu][1] and F[i][lb][lu][0] == F[i - 1][lb - A[i]][lu][0] + 1:
        bottom.append(i - 1)
        get_result_recursive(bottom, upper, A, F, i - 1, lb - A[i], lu)
    else:
        upper.append(i - 1)
        get_result_recursive(bottom, upper, A, F, i - 1, lb, lu - A[i])


if __name__ == '__main__':
    print(ferry(10, 20, [3, 14, 3, 2, 6, 8, 9, 50, 1, 7]))
    print(ferry_recursive(10, 20, [3, 14, 3, 2, 6, 8, 9, 50, 1, 7]))
