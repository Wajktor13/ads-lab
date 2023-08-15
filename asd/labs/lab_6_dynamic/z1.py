"""
"Las"
wycinamy drzewo -> dostajemy pieniadze
nie mozemy wycinac 2 obok siebie
mamy tablice kosztow C

f(i) - max zysk do ind i wlacznie

f(i) = max( f(i-2) + C[i], f(i-1) )
     = C[0], i == 0
     = max(f(0), C[1]), i == 1

nie uzywac nonlocal

mozna na 3 zmiennych / 3 el. tablicy (np z %)
"""


def forest(C):
    n = len(C)

    if n < 1:
        return 0
    if n == 1:
        return C[0]

    F = [0 for _ in range(n)]
    F[0] = C[0]
    if C[1] > C[0]:
        F[1] = C[1]
        f1 = True
    else:
        F[1] = C[0]
        f1 = False

    for i in range(2, n):
        F[i] = max(F[i-1], F[i-2] + C[i])

    
    return get_result(C, F, f1)


def get_result(C, F, f1):
    result = []
    i = len(C) - 1
    while i >= 2:
        if F[i] == F[i-2] + C[i]:
            result.append(i)
            i -= 2
        else:
            i -= 1

    if i == 1 and f1:
        result.append(i)
    else:
        result.append(0)
    
    return result[::-1]


if __name__ == '__main__':
    print(forest([5, 17, 1, 1, 19, 1]))
