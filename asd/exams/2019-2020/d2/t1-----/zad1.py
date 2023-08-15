from zad1testy import runtests

def zbigniew(T):
    n = len(T)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]

    F[min(T[0], n - 2)][0] = 0

    for i in range(1, n):
        T[i] = min(T[i], n - 2)
        for e in range(T[i], n):
            for j in range(max(1, T[i] - e), min(i + 1, n + T[i] - e)):
                    if F[e - T[i] + j][i - j] + 1 < F[e][i]:
                        F[e][i] = F[e - T[i] + j][i - j] + 1

    return get_result(F)


def get_result(F):
    n = len(F)
    best_energy = 0

    for i in range(n):
        if F[i][n - 1] <= F[best_energy][n - 1]:
            best_energy = i
    
    return F[best_energy][n - 1]


runtests( zbigniew ) 
