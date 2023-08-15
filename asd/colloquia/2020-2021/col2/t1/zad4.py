"""Wiktor Wilkusz 411605
Algorytm bazuje na algorytmie problemu plecakowego (0-1) z ta różnicą, że
pod uwagę bierzemy 2 możliwości - przepisanie wyniku z poprzedniego wiersza
i tej samej kolumny (obecny budynek nie jest wybierany) lub wybieramy obecny
budynek i dodajemy jego pojemność do wyniku z wiersza odpowidającego pierwszemu
niekoliyzjnemu budynkowi, ktory był wczesniej rozważany, i kolumny pomniejszonej
względem obecnej o koszt obecnie rozważanego budynku.
Tablica z indeksami budynków jest posortowana względem 2. współrzędnej
odpowiadającego indeksom budynku. Dzięki temu mamy pewność, że poszukując
niekolizyjnych budynków 'wstecz', przed pierwszym znalezionym budynkiem wszystkie
pozostałe również nie kolidują z obecnym, co czyni pierwszy budynek najlepszym
wyborem.

złożoność obliczeniowa: O(n^2 + np)
"""


from zad4testy import runtests


def select_buildings(T, p):
    n = len(T)

    ind = [i for i in range(n)]
    ind.sort(key=lambda i: T[i][2])

    F = [[0 for _ in range(p + 1)] for _ in range(n + 1)]

    for building in range(1, n + 1):
        h, a, b, w = T[ind[building - 1]]
        capacity = (b - a) * h

        best_prev_building = 0
        for prev_building in range(building - 1, 0, -1):
            if a > T[ind[prev_building - 1]][2]:
                best_prev_building = prev_building
                break

        for price in range(1, p + 1):
            if price - w < 0:
                F[building][price] = F[building - 1][price]
            else:
                F[building][price] = max(F[building - 1][price], F[best_prev_building][price - w] + capacity)

    result = []
    building, price = n, p
    while building > 0 and price > 0:
        if F[building - 1][price] == F[building][price]:
            building -= 1
        else:
            result.append(ind[building - 1])
            h, a, b, w = T[ind[building - 1]]
            price = price - w

            best_prev_building = 0
            for prev_building in range(building - 1, 0, -1):
                if a > T[ind[prev_building - 1]][2]:
                    best_prev_building = prev_building
                    break

            building = best_prev_building

    return sorted(result)


runtests(select_buildings)
