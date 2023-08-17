"""
zachlanne
stacje benz
czolg miesci L litrow paliwa
na kazdym polu mozemy tankowac do pelna
chcemy dojechac do n-1 pola

#1 koszt nas nie interesuje, min ilosc przystankow
tankujemy na maks i dojezdamy najdlaej jak sie da

#2 modyfikacja - paliwo kosztuje, chcemy jak najtaniej
P - ceny
szukamy najtanszego paliwa w obrebie zasiegu
jesli sie znajduje, to tankujemy tylko tyle, aby do niej dojechac

#3 modyfikacja - mozemy tankowac tylko do pelna, min koszt - nie da sie zachlannie, tylko dynamicznie

zwracamy ile tankowalismy na danej stacji - plant trasy

zachlanne nie powinny byc rekurencyjne
"""


import random


def tank1(L, P):
    n = len(P)
    route = [0 for _ in range(n)]
    for i in range(0, n - 1, L):
        route[i] = L
    return route, summary(route, P)


def tank2(L, P):
    n = len(P)
    i = 0
    route = [0 for _ in range(n)]
    petrol = 0
    while i < n - 1:
        best = i + 1
        if P[best] >= P[i]:
            for j in range(i + 2, min(i+L+1, n)):
                if P[j] == P[best]:
                    best = j
                if P[j] < P[best]:
                    best = j
                    break

        if P[i] <= P[best]:
            if L >= n - 1 - i:
                route[i] = (n - 1) - i - petrol
                break

            route[i] = L - petrol
            petrol = L - (best - i)
            i = best

        else:
            route[i] = max(0, best - i - petrol)
            petrol = 0
            i = best

    return route, summary(route, P)


def tank3(L, P):
    n = len(P)
    F = [[float('inf') for _ in range(L + 1)] for _ in range(n)]
    F[0][0] = 0

    for field in range(1, n):
        for fuel in range(L):
            prev_field = field - (L - fuel)
            for fuel_on_prev in range(L):
                F[field][fuel] = min((F[field][fuel], F[prev_field][fuel_on_prev] +
                                      P[prev_field] * (L - fuel_on_prev)))

    route = [0 for _ in range(n)]
    field, fuel = n - 1, 0
    for i in range(L):
        if F[field][i] < F[field][fuel]:
            fuel = i

    while field > 0:
        value = F[field][fuel]
        field -= L - fuel
        for i in range(L):
            if F[field][i] + P[field] * (L - i) == value:
                route[field] = (L - i)
                fuel = i

    return route, summary(route, P)


def summary(route, P):
    n = len(P)
    return (f'Cost: {sum([route[i] * P[i] for i in range(n)])}',
            f'Breaks: {sum([1 if route[i] > 0 else 0 for i in range(n)])}')


if __name__ == '__main__':
    prices = [random.randint(1, 9) for _ in range(18)]
    capacity = 3
    tank3(capacity, prices)
    print(f'Prices:{prices}', f'#1:   {tank1(capacity, prices)}', f'#2:   {tank2(capacity, prices)}',
          f'#3:   {tank3(capacity, prices)}', sep='\n')
