"""
"Zaba"
zaba stoi na polu 0
nie cofa sie
ma poziom energii, na poczatku 0, brak max poziomu
zwieksza energie przez przekaski, ktore sa na nastepnych polach
moze skakac wiecej niz 1 pole

wynik - min liczba skokow potrzebna na dotarcie do pola n-1
T - tablica z przekaskami, n - jej dlugosc

funkcja - zwraca wynik, procedura - nie

f(i, e) - zwraca min ilosc skokow do pola n-1

f(i, e) = 0, i >= n-1
        = min( f(i + j, e - j + T[i+j])) + 1, i + j < n
       0 < j <= e

tablica 2 wym - n^2 chyba
"""


def frog(T):
    n = len(T)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    save = [[float('inf') for _ in range(n)] for _ in range(n)]

    save[T[0]][0] = (-1, -1)
    F[min(T[0], n - 2)][0] = 0

    for i in range(1, n):
        T[i] = min(T[i], n - 2)
        for e in range(T[i], n):
            for j in range(max(1, T[i] - e), min(i + 1, n + T[i] - e)):
                    if F[e - T[i] + j][i - j] + 1 < F[e][i]:
                        F[e][i] = F[e - T[i] + j][i - j] + 1
                        save[e][i] = (e - T[i] + j, i - j)

    return get_result(F, save)


def get_result(F, save):
    n = len(F)
    result = [0]
    best_energy = 0

    for i in range(n):
        if F[i][n - 1] <= F[best_energy][n - 1]:
            best_energy = i
    
    i, e = n - 1, best_energy
    while i > 0:
        result.append(i)
        e, i = save[e][i]

    return F[best_energy][n - 1], sorted(result)
    

if __name__ == '__main__':
    print(frog([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
